from ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import (
    QMainWindow, QFileDialog, QMessageBox, QLineEdit, QButtonGroup,
    QCheckBox, QComboBox, QTableWidgetItem, QDialog, QTableWidget, QHeaderView,
    QStyledItemDelegate)
from PySide6.QtCharts import (QChart, QLineSeries, QValueAxis)
from PySide6.QtGui import (QColor, Qt, QIntValidator, QDoubleValidator,
                           QMouseEvent, QStandardItemModel, QStandardItem,
                           QDesktopServices)
from PySide6.QtCore import (QTimer, Qt, QUrl, Slot, QObject, Signal,
                            QItemSelectionModel)
from PySide6.QtQuickWidgets import QQuickWidget

from edfoil.classes.airfoil import Airfoil
from edfoil.classes.station import Station
from edfoil.classes.section import Section
from edfoil.classes.session import session
from edfoil.utils.bladeparams import norm_olp
from edfoil.utils.abaqusExp import *
from edfoil.utils.dev import resource_path
from edfoil.utils.themeLoader import Theme
from edfoil.utils.sessionIO import save_session_to_edf, load_session_from_edf
from resources.uis.ui_settingsDialog import Ui_settingsDialog

import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import pandas as pd
from scipy.interpolate import splev
from datetime import datetime

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        print(f'{ctime()} Starting EdFoil...')
        self.app = app
        self.setupUi(self)
        self.setWindowTitle('EdFoil')
        self._configure_tables()
        
        # Messagebar
        self.timer_msg = QTimer(parent=self)
        self.timer_msg.setSingleShot(True)
        self.timer_msg.timeout.connect(self.show_def_msg)
        
        # Project start
        self.db = session() # Class db [not a dictionary]
        self.edits = {}
        
        # Settings dialog
        self.settings_dialog = SettingsDialog(self)
        self.settings_button.clicked.connect(self.open_settings)
        self.settings_dialog.themes_box.currentTextChanged.connect(self.apply_theme)
        self.load_themes()
        self.apply_theme()
        self.save_settings() # Save default settings
        self.handle_msgbar(message='New database created.')
        
        # Station QML Bridge
        self.graphBridge = GraphBridge()
        self.station_chartview.setResizeMode(QQuickWidget.SizeRootObjectToView)
        qml_path = resource_path('edfoil/qml/station.qml')
        ctx = self.station_chartview.rootContext()
        ctx.setContextProperty("graphBridge", self.graphBridge)
        self.station_chartview.setSource(QUrl.fromLocalFile(qml_path))
        root = self.station_chartview.rootObject()
        root.mouseMoved.connect(self.station_mouse_moved)
        root.mouseExited.connect(self.station_mouse_exited)
        
        # OLP STA QML Bridge
        self.olpstaBridge = OverlapBridge()
        self.blade_olpsta_chartview.setResizeMode(QQuickWidget.SizeRootObjectToView)
        sta_ctx = self.blade_olpsta_chartview.rootContext()
        sta_ctx.setContextProperty("olpstaBridge", self.olpstaBridge)
        olp_sta_qml_path = resource_path('edfoil/qml/olp_sta.qml')
        self.blade_olpsta_chartview.setSource(QUrl.fromLocalFile(olp_sta_qml_path))
        
        # OLP LEN QML Bridge
        self.olplenBridge = OlpLengthBridge()
        self.blade_olplen_chartview.setResizeMode(QQuickWidget.SizeRootObjectToView)
        len_ctx = self.blade_olplen_chartview.rootContext()
        len_ctx.setContextProperty("olplenBridge", self.olplenBridge)
        olp_len_qml_path = resource_path('edfoil/qml/olp_factors.qml')
        self.blade_olplen_chartview.setSource(QUrl.fromLocalFile(olp_len_qml_path))
        
        # Signals
        self.db.airfoils.airfoilsChanged.connect(self._sync_airfoil_widgets)
        self.db.stations.stationsChanged.connect(self._sync_station_widgets)
        
        # Tab switching
        self.home_page_button.clicked.connect(self.switch_to_homePage)
        self.airfoil_page_button.clicked.connect(self.switch_to_airfoilPage)
        self.station_page_button.clicked.connect(self.switch_to_stationPage)
        self.blade_page_button.clicked.connect(self.switch_to_bladePage)
        self.skin_page_button.clicked.connect(self.switch_to_skinPage)
        # self.spar_page_button.clicked.connect(self.switch_to_sparPage)
        self.export_page_button.clicked.connect(self.switch_to_exportPage)
        
        # Lower sidebar buttons
        self.doc_button.clicked.connect(self.open_doc)
        self.info_button.clicked.connect(self.info_message)
        self.quit_button.clicked.connect(self.quit_message_box)
        
        # Main path
        self.main_path = os.getcwd()
        self.workpath_lineedit.setText(self.main_path)
        self.changedir_button.clicked.connect(self.change_work_directory)
        
        # ---------------------------------------------------------------------
        # Page 0 (Home)
        
        self.loadproject_button.clicked.connect(self.load_db)
        self.newproject_button.clicked.connect(self.new_db)
        
        # ---------------------------------------------------------------------
        # Page 1 (Airfoil Creator)
        
        # Main chart
        # self.airfoil_chartview.mouseMoveEvent = self.airfoil_mousecoords
        self.airfoil_fig = Figure(figsize=(10, 3), tight_layout=True)
        self.airfoil_ax = self.airfoil_fig.add_subplot(111)
        self.airfoil_ax.set_xlabel('x/c [-]', fontsize='x-large')
        self.airfoil_ax.set_ylabel('y/c [-]', fontsize='x-large')
        self.airfoil_ax.minorticks_on()
        self.airfoil_ax.tick_params(axis='both', which='both', direction='in',
                            top=True, right=True, labelsize='medium')
        self.airfoil_ax.grid(visible=True, which='major', linestyle='--', linewidth=0.75)
        self.canvas = FigureCanvasQTAgg(self.airfoil_fig)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.verticalLayout_9.addWidget(self.toolbar)
        self.verticalLayout_9.addWidget(self.canvas)
        
        # List of airfoils
        self.load_default_airfoils()
        self.update_parameters()
        
        # Signals
        self.airfoil_nacaseries_input.currentTextChanged.connect(self.update_parameters)
        self.airfoil_calculateairfoil_button.clicked.connect(self.calculate_airfoil)
        self.airfoil_saveairfoil_button.clicked.connect(self.save_airfoil)
        self.airfoil_listairfoils_widget.currentRowChanged.connect(self.update_naca_chart)
        self.airfoil_delAirfoil_button.clicked.connect(self.delete_airfoil)
        
        # ---------------------------------------------------------------------
        # Page 2 (Station Generator)
        
        # Timer for debouncing text input changes
        self.timer_station = QTimer()
        self.timer_station.setSingleShot(True)
        self.timer_station.timeout.connect(self.update_station_chart)
        
        # Airfoil list
        # self.station_listairfoils_box.addItems(list(self.db.airfoils.keys()))
        self._sync_airfoil_widgets()
        
        # Upload additional airfoils
        self.station_uploadairfoil_button.clicked.connect(self.upload_airfoil_file)
        
        # Main chart
        # self.station_chart_empty = self.graph_template()
        # self.station_chartview.setChart(self.station_chart_empty)
        # self.station_chartview.mouseMoveEvent = self.station_mousecoords
        
        # Validators
        self.station_chordlength_input.setValidator(QDoubleValidator(1.,1e6,3))
        self.station_twistangle_input.setValidator(QDoubleValidator(-1e6,1e6,3))
        self.station_offsetx_input.setValidator(QDoubleValidator(-1e6,1e6,3))
        self.station_offsety_input.setValidator(QDoubleValidator(-1e6,1e6,3))
        self.station_offsetz_input.setValidator(QDoubleValidator(0,1e6,3))
        self.station_multx_input.setValidator(QDoubleValidator(0.1,1e6,3))
        self.station_multy_input.setValidator(QDoubleValidator(0.1,1e6,3))
        self.station_multz_input.setValidator(QDoubleValidator(0.1,1e6,3))
        
        # Signals
        self.station_listairfoils_box.currentTextChanged.connect(self.onTextChanged)
        self.station_chordlength_input.textChanged.connect(self.onTextChanged)
        self.station_twistangle_input.textChanged.connect(self.onTextChanged)
        self.station_offsetx_input.textChanged.connect(self.onTextChanged)
        self.station_offsety_input.textChanged.connect(self.onTextChanged)
        self.station_offsetz_input.textChanged.connect(self.onTextChanged)
        self.station_multx_input.textChanged.connect(self.onTextChanged)
        self.station_multy_input.textChanged.connect(self.onTextChanged)
        self.station_multz_input.textChanged.connect(self.onTextChanged)
        self.station_mirrorx_input.checkStateChanged.connect(self.onTextChanged)
        self.station_mirrory_input.checkStateChanged.connect(self.onTextChanged)
        
        self.station_savestation_button.clicked.connect(self.save_station)
        self.station_delstation_button.clicked.connect(self.del_station)
        
        self.station_liststation_box.currentTextChanged.connect(self.update_station_params)
        
        # Advanced tab
        # ------------
        self.stations_insert_row(None, def_row=True)
        self.station_tableStations_input.setColumnWidth(0, 130)
        self.station_tableStations_input.setColumnWidth(1, 100)
        self.station_tableStations_input.setSortingEnabled(True)
        
        # Signals
        self.station_nStationsAdv_input.valueChanged.connect(self.update_stations_table)
        self.station_impTable_button.clicked.connect(self.import_stations_to_table)
        self.station_sortTable_button.clicked.connect(self.sort_advanced_stations_table)
        self.station_saveTable_button.clicked.connect(self.save_multiple_stations)
        
        # ---------------------------------------------------------------------
        # Page 3 (Blade Parameters)
        
        # Charts
        # self.blade_olpsta_chart = self.graph_template()
        # self.blade_olpsta_chartview.setChart(self.blade_olpsta_chart)
        
        # self.blade_olplen_chart = self.graph_template()
        # self.blade_olplen_chartview.setChart(self.blade_olplen_chart)
        
        # Radio Buttons LOC
        self.skin_grp_loc = QButtonGroup(self)
        self.skin_grp_loc.addButton(self.skin_loc_radio1)
        self.skin_grp_loc.addButton(self.skin_loc_radio2)
        self.skin_grp_loc.setExclusive(True)
        self.loc_frame.hide()
        
        # Radio Buttons LEN
        self.skin_grp_len = QButtonGroup(self)
        self.skin_grp_len.addButton(self.skin_len_radio1)
        self.skin_grp_len.addButton(self.skin_len_radio2)
        self.skin_grp_len.setExclusive(True)
        self.len_frame.hide()
        self.update_skin_ui()
        
        # Valditors
        self.blade_skinolpsta_table.setItemDelegate(FloatDelegate(self.blade_skinolpsta_table))
        self.blade_skinolplen_table.setItemDelegate(FloatDelegate(self.blade_skinolplen_table))
        # TODO: Hardcoded top values
        self.skin_olp_loc_const.setValidator(QDoubleValidator(0.1,200,3))
        self.skin_olp_len_const.setValidator(QDoubleValidator(1,200,3))
        
        # Signals
        self.blade_skinolpsta_table.cellChanged.connect(lambda row, col:
            self.new_row_table(self.blade_skinolpsta_table, row, col))
        self.blade_skinolplen_table.cellChanged.connect(lambda row, col:
            self.new_row_table(self.blade_skinolplen_table, row, col))
        
        self.skin_grp_loc.buttonToggled.connect(self.update_skin_ui)
        self.skin_grp_len.buttonToggled.connect(self.update_skin_ui)
        self.blade_order_input.valueChanged.connect(self.resize_blade_table)
        self.blade_interpolate_button.clicked.connect(self.interpolate_overlap)
        self.blade_saveparams_button.clicked.connect(self.save_bladeparams)
        self.blade_skinolplen_selected.currentTextChanged.connect(self.table_interpolation_vals)
        self.blade_skinolpsta_selected.currentTextChanged.connect(self.table_interpolation_vals)
        
        # ---------------------------------------------------------------------
        # Page 4 (Skin)
        
        # Calculations
        self.timer_skin = QTimer()
        self.timer_skin.setSingleShot(True)
        self.timer_skin.timeout.connect(self.build_section)
        
        # Validators
        # TODO: Top values are hardcoded for now
        self.skin_nplies_input.setValidator(QIntValidator(1, 10))
        self.skin_plythickness_input.setValidator(QDoubleValidator(0.1,20,3))
        self.skin_tethickness_input.setValidator(QDoubleValidator(0.1,200,3))
        self.skin_bond_input.setValidator(QDoubleValidator(0.1,20,3))
        
        # Chart
        self.skin_fig = Figure(figsize=(10, 3), tight_layout=True)
        self.skin_ax = self.skin_fig.add_subplot(111)
        self.skin_ax.set_xlabel('x [d]', fontsize='x-large')
        self.skin_ax.set_ylabel('y [d]', fontsize='x-large')
        self.skin_ax.minorticks_on()
        self.skin_ax.tick_params(axis='both', which='both', direction='in',
                            top=True, right=True, labelsize='medium')
        self.skin_ax.grid(visible=True, which='major', linestyle='--', linewidth=0.75)
        self.canvas_4 = FigureCanvasQTAgg(self.skin_fig)
        self.toolbar_4 = NavigationToolbar2QT(self.canvas_4, self)
        self.verticalLayout_10.addWidget(self.toolbar_4)
        self.verticalLayout_10.addWidget(self.canvas_4)
        
        # Signals
        self.stackedWidget.currentChanged.connect(self.update_stabox)
        self.skin_liststations.currentTextChanged.connect(self.update_olptgt)
        
        self.skin_liststations.currentTextChanged.connect(self.secInputChanged)
        self.skin_nplies_input.textChanged.connect(self.secInputChanged)
        self.skin_plythickness_input.textChanged.connect(self.secInputChanged)
        self.skin_overlaptarget_input.textChanged.connect(self.secInputChanged)
        self.skin_tethickness_input.textChanged.connect(self.secInputChanged)
        self.skin_bond_input.textChanged.connect(self.secInputChanged)
        self.skin_jiggle_toggle.checkStateChanged.connect(self.secInputChanged)
        self.skin_savefig_input.checkStateChanged.connect(self.secInputChanged)
        
        self.skin_saveSection_button.clicked.connect(self.saveSection)
        self.skin_saveAll_button.clicked.connect(self.saveAllSections)
        
        # ---------------------------------------------------------------------
        # Page 6 (EXPORT)
        self.stackedWidget.currentChanged.connect(self.update_sectionList)
        self.export_export_button.clicked.connect(self.exportSections)
        
        # Export type
        self.export_toggles = QButtonGroup(self)
        self.export_toggles.addButton(self.export_json_toggle)
        self.export_toggles.addButton(self.export_csv_toggle)
        self.export_toggles.setExclusive(True)
        
        # Signals
        self.export_toggles.buttonToggled.connect(self.changeExportType)
    
    @Slot(float, float)
    def station_mouse_moved(self, x, y):
        # print(f"Mouse axis coords: {x:.5f}, {y:.5f}")
        if hasattr(self, "station_xy_current"):
            self.station_xy_current.setText(f"(x, y) = ({x:.3f}, {y:.3f})")

    @Slot()
    def station_mouse_exited(self):
        # print("Mouse left plot")
        if hasattr(self, "station_xy_current"):
            self.station_xy_current.clear()
    
    ### AIRFOIL METHODS (Page 1)
    def update_parameters(self):
        naca_series = self.airfoil_nacaseries_input.currentText()
        if naca_series == 'NACA 4-digit':
            self.label_10.setText('1st digit (max camber):')
            self.label_11.setText('2nd digit (pos max camber):')
            self.label_12.setText('Last two digits (thickness):')
        else:
            self.label_10.setText('2nd digit:')
            self.label_11.setText('3rd digit:')
            self.label_12.setText('Last two digits (thickness):')
    
    def calculate_airfoil(self):
        
        naca_series = self.airfoil_nacaseries_input.currentText()
        digits = self.airfoil_seconddigit_input.text() + \
            self.airfoil_thirddigit_input.text()
        
        last_two = int(self.airfoil_lasttwodigits_input.text())
        last_two = f'{last_two:02d}' # Ensure two digits
        
        digits += last_two
        
        if naca_series == 'NACA 4-digit':
            airfoil_name = digits
        elif naca_series == 'NACA 6-series':
            airfoil_name = '6' + digits
        else: # NACA 6A-series
            airfoil_name = '6' + digits[0] + 'A' + digits[1:]
        
        # Check if airfoil already exists
        if f'NACA{airfoil_name}' in self.db.airfoils.keys():
            self.handle_msgbar(f'Airfoil NACA {airfoil_name} already exists.', wcolor='yellow')
            return
        
        print(f'{ctime()} Creating airfoil: {airfoil_name}')
        
        airfoil = Airfoil(airfoil_name)
        name_input = Airfoil.nameinput(airfoil_name)
        airfoil.naca456(name_input)
        
        self.edits['__airfoil__'] = airfoil
        
        # Replace unsaved airfoil in the list (if exists)
        last_row = self.airfoil_listairfoils_widget.count() - 1      
        if '*' in self.airfoil_listairfoils_widget.item(last_row).text():
            self.airfoil_listairfoils_widget.takeItem(last_row)
        
        # Insert new unsaved airfoil in the list
        self.airfoil_listairfoils_widget.addItem(f'{airfoil.family} {airfoil.profile}*')
        last_row = self.airfoil_listairfoils_widget.count() - 1  
        self.airfoil_listairfoils_widget.setCurrentRow(last_row)
    
    def save_airfoil(self):
        
        # Save the airfoil in the session database
        try:
            airfoil = self.edits['__airfoil__']
        except KeyError:
            self.handle_msgbar('No airfoil to save.', wcolor='yellow')
            return
        
        # self.db.airfoils[airfoil.name] = airfoil
        self.db.airfoils.add(name=airfoil.name, airfoil=airfoil)
        del self.edits['__airfoil__']
        
        # Update airfoil list (remove asterisk)
        # items = [self.airfoil_listairfoils_widget.item(i).text() 
        #     for i in range(self.airfoil_listairfoils_widget.count())]
        # index = items.index(f'{airfoil.family} {airfoil.profile}*')
        # new_text = f'{airfoil.family} {airfoil.profile}'
        # self.airfoil_listairfoils_widget.item(index).setText(new_text)
        
        # Print message
        self.handle_msgbar(f'Airfoil {airfoil.name} saved.', wcolor='green')
        # print(self.db.airfoils.keys())
                
    def update_naca_chart(self):
        
        try:
            airfoil_name = self.airfoil_listairfoils_widget.currentItem().text()
            
        except AttributeError:
            empty_chart = self.graph_template()
            self.airfoil_chartview.setChart(empty_chart)
            return
        
        # Debug
        # print(f'Selected airfoil: {airfoil_name}')
        
        if '*' in airfoil_name:
            airfoil = self.edits['__airfoil__']
        else:
            airfoil = self.db.airfoils[airfoil_name.replace(' ','')]
        
        self.airfoil_ax.clear()
        x, y = zip(*airfoil.xy)
        n = len(x) // 2
        
        self.airfoil_ax.set_title(airfoil.name, fontsize='xx-large')
        self.airfoil_ax.plot(x[:n+1],y[:n+1], color = 'C0', label='lower')
        self.airfoil_ax.plot(x[n:],y[n:], color = 'C1', label='upper')
        self.airfoil_ax.plot([x[0],x[n]],[y[0],y[n]], color = 'black', ls='--',label='chord line', lw=1)
        self.airfoil_ax.set_xlabel('x/c [-]', fontsize='x-large')
        self.airfoil_ax.set_ylabel('y/c [-]', fontsize='x-large')
        self.airfoil_ax.minorticks_on()
        self.airfoil_ax.tick_params(axis='both', which='both', direction='in',
                            top=True, right=True, labelsize='medium')
        self.airfoil_ax.grid(visible=True, which='major', linestyle='--', linewidth=0.75)
        self.airfoil_ax.set_aspect('equal', adjustable='datalim')
        self.airfoil_ax.legend(loc = 'best')
        
        self.canvas.draw_idle()
    
    def delete_airfoil(self):
        airfoil_name = self.airfoil_listairfoils_widget.currentItem().text()
        airfoil_id = airfoil_name.replace(' ','')
        
        if '*' in airfoil_id:
            self.handle_msgbar('Airfoil not saved yet.', wcolor='yellow')
            return
        
        if airfoil_id in self.db.airfoils.keys():
            del self.db.airfoils[airfoil_id]
            self.handle_msgbar(f'Airfoil {airfoil_name} deleted.', wcolor='green')
            
            # Update airfoil list
            items = [self.airfoil_listairfoils_widget.item(i).text() 
                for i in range(self.airfoil_listairfoils_widget.count())]
            index = items.index(airfoil_name)
            self.airfoil_listairfoils_widget.takeItem(index)
            
            # Clear chart
            # empty_chart = self.graph_template()
            # self.airfoil_chartview.setChart(empty_chart)
        else:
            self.handle_msgbar('Airfoil not found in database.', wcolor='red')
    
    ### STATION METHODS (Page 2a)
    def update_station_params(self):
        name_station = self.station_liststation_box.currentText()
        station = self.db.stations.get(name_station)
        
        self.station_listairfoils_box.setCurrentText(station.airfoil)
        
        self.station_chordlength_input.setText(f'{station.parameters['chord']}')
        self.station_twistangle_input.setText(f'{np.degrees(station.parameters['twist_angle']):.2f}')
        
        offset = station.parameters['offset']
        self.station_offsetx_input.setText(f'{offset[0]}')
        self.station_offsety_input.setText(f'{offset[1]}')
        self.station_offsetz_input.setText(f'{offset[2]}')
        
        multip = station.parameters['multiplier']
        self.station_multx_input.setText(f'{multip[0]}')
        self.station_multy_input.setText(f'{multip[1]}')
        self.station_multz_input.setText(f'{multip[2]}')
        
        mirror = station.parameters['mirror']
        self.station_mirrorx_input.setChecked(mirror[0])
        self.station_mirrory_input.setChecked(mirror[1])
        
    
    def update_station_chart(self):
        
        try:
            chord_length = float(self.station_chordlength_input.text()) if \
                self.station_chordlength_input.text() else 1
            twist_angle = float(self.station_twistangle_input.text()) if \
                self.station_twistangle_input.text() else 0
            
            x_offset = float(self.station_offsetx_input.text()) if \
                self.station_offsetx_input.text() else 0
            y_offset = float(self.station_offsety_input.text()) if \
                self.station_offsety_input.text() else 0
            z_offset = float(self.station_offsetz_input.text()) if \
                self.station_offsetz_input.text() else 0
            
            x_multiplier = float(self.station_multx_input.text()) if \
                self.station_multx_input.text() else 0
            y_multiplier = float(self.station_multy_input.text()) if \
                self.station_multy_input.text() else 0
            z_multiplier = float(self.station_multz_input.text()) if \
                self.station_multz_input.text() else 0
                
            x_mirror = self.station_mirrorx_input.isChecked()
            y_mirror = self.station_mirrory_input.isChecked()
            
            # Calculate new values
            airfoil_selected:str = self.station_listairfoils_box.currentText()
            station = Station(
                airfoil=self.db.airfoils[airfoil_selected],
                chord=chord_length,
                twist_angle=twist_angle,
                x_offset=x_offset,
                y_offset=y_offset,
                z_offset=z_offset,
                x_multiplier=x_multiplier,
                y_multiplier=y_multiplier,
                z_multiplier=z_multiplier,
                x_mirror=x_mirror,
                y_mirror=y_mirror,
            )
            
            self.push_station_to_qml(station)
            
            # Store it as an unsaved station
            self.edits['__station__'] = station
            
        except ValueError:
            self.handle_msgbar('Station: Wrong input', wcolor='red')
    
    def push_station_to_qml(self, station):
        """
        station.xy expected as list[(x,y), ...] (combined).
        Splits automatically if you stored upper/lower separately you can adapt.
        """
        if not hasattr(self, "graphBridge"):
            return
        points = [{'x': float(x), 'y': float(y)} for x, y in station.xy]
        self.graphBridge.updateSeriesRequested.emit(points, station.airfoil)
        
        # Leading Edge
        idx = len(station.xy) // 2
        le = station.xy[idx]
        self.graphBridge.updateLE.emit(float(le[0]), float(le[1]))
        
        # Set axis ranges
        x_min, x_max = station.xyRange()[0]
        y_min, y_max = station.xyRange()[1]
        padding = 0.05
        
        # Aspect ratio
        dx = x_max - x_min
        dy = y_max - y_min
        
        # Protect zero spans
        if dx <= 0: dx = 1e-12
        if dy <= 0: dy = 1e-12

        # Viewport pixel ratio (width / height)
        w = max(1, self.station_chartview.width())
        h = max(1, self.station_chartview.height())
        ratio = w / h  # desired dx/dy

        # Current ratio
        cur_ratio = dx / dy

        cx = 0.5 * (x_min + x_max)
        cy = 0.5 * (y_min + y_max)

        if cur_ratio > ratio:
            # Too wide → enlarge y span
            dy_new = dx / ratio
            y_min = cy - dy_new / 2
            y_max = cy + dy_new / 2
        else:
            # Too tall → enlarge x span
            dx_new = dy * ratio
            x_min = cx - dx_new / 2
            x_max = cx + dx_new / 2

        # Padding
        dx_adj = x_max - x_min
        dy_adj = y_max - y_min
        x_min -= dx_adj * padding
        x_max += dx_adj * padding
        y_min -= dy_adj * padding
        y_max += dy_adj * padding
        
        # ticks
        x_span = x_max - x_min
        y_span = y_max - y_min
        x_tick = _nice_step(x_span / 5.)
        y_tick = _nice_step(y_span / 5.)
        
        print(f'{ctime()} Scale factor (station graph): x_tick = {x_tick}, y_tick = {y_tick}')
        
        self.graphBridge.updateAxesRequested.emit(
            x_min, x_max, x_tick,
            y_min, y_max, y_tick
        )
    
    def save_station(self):
        station = self.edits['__station__']
        station_name  = 'sta_' + str(int(station.parameters['offset'][2]))
        # self.db.stations[station_name] = station
        self.db.stations.add(station_name, station)
        self.handle_msgbar(f'Station {station_name} saved.', wcolor='green')
        # n_stations = len(self.db.stations.keys())
        # sorted_stations = sorted(list(self.db.stations.keys()), key=len)
        # self.handle_msgbar(f'Number of stations: {n_stations}')
        # self.station_liststation_box.clear()
        # self.station_liststation_box.insertItems(0,sorted_stations)
        self.station_liststation_box.setCurrentText(station_name)
        # print(self.station_liststation_box.currentIndex())
        
    def del_station(self):
        station_name = self.station_liststation_box.currentText()
        
        if not station_name:
            return self.handle_msgbar('No station to delete.', wcolor='yellow')
        
        self.db.stations.remove(station_name)
        self.update_station_params()
        # self.update_station_chart()
        
        print(f'{ctime()} Station "{station_name}" deleted.')
        return self.handle_msgbar(f'Station "{station_name}" deleted.', wcolor='green')
    
    ### ADVANCED TAB METHODS (Page 2b)
    
    def stations_insert_row(
        self,
        row: int | None = None,
        airfoil: str | None = None,
        def_row: bool = False,
        data_row: list | None = None,
        xmirror: bool = False,
        ymirror: bool = True,
        ):
        
        t = self.station_tableStations_input
        
        if def_row:
            insert_at = 0
        else:
            if row is None:
                insert_at = t.rowCount()
            else:
                insert_at = min(max(0, row), t.rowCount())
        
        t.insertRow(insert_at)
        
        # Column 0: Airfoil
        c0 = QComboBox()
        c0.addItems(self.db.airfoils.keys())
        if airfoil in self.db.airfoils.keys():
            c0.setCurrentText(airfoil)
        else: c0.setCurrentIndex(0)
        t.setCellWidget(insert_at, 0, c0)
        
        # Column 1-8: Numeric items
        num_default = data_row if data_row else [1., 0., 0., 0., 0., 1., 1., 1.]
        
        for col, val in enumerate(num_default, start=1):
            t.setItem(insert_at, col, NumericItem(f"{val:.6g}"))
            
        # Column 9-10: Checkboxes
        x_mir = QCheckBox(); x_mir.setChecked(bool(xmirror))
        y_mir = QCheckBox(); y_mir.setChecked(bool(ymirror))
        t.setCellWidget(insert_at, 9, x_mir)
        t.setCellWidget(insert_at, 10, y_mir)
    
    def sort_advanced_stations_table(self):
        self.station_tableStations_input.sortItems(5)
    
    def import_stations_to_table(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter(self.tr('Data files (*.csv *.txt);;All files (*)'))
        dialog.setViewMode(QFileDialog.Detail)
        
        if not dialog.exec():
                return  # user cancelled
        filepath = dialog.selectedFiles()[0]
        
        # Read file
        try:
            df = pd.read_csv(filepath, header=0)
        except Exception as e:
            self.handle_msgbar(f"Failed to read file: {e}", wcolor='red')
            return
        
        # Clean station table and stations in session
        t = self.station_tableStations_input
        t.setSortingEnabled(False)
        t.clearContents()
        t.setRowCount(0)
        self.db.stations.clear()
        
        # Populate station table
        rows, _ = df.shape
        for r in range(rows):
            self.stations_insert_row(
                row = None,
                airfoil = df.at[r, 'airfoil'],
                def_row = False,
                data_row = df.iloc[r].tolist()[1:-2],
                xmirror = df.iloc[r]['mirror_x'],
                ymirror = df.iloc[r]['mirror_y'],
            )
        
        t.setSortingEnabled(True)
        self.station_nStationsAdv_input.setValue(len(df))
        self.handle_msgbar(f'File imported succesfully: {filepath}.', wcolor='green')
    
    def update_stations_table(self, value):
        # n_rows = self.station_tableStations_input.rowCount()
        
        # if value > n_rows:
        #     self.stations_insert_row(row=value)
            
        # elif value < n_rows:
        #     self.station_tableStations_input.removeRow(value)
        
        t = self.station_tableStations_input
        if value < 0:
            value = 0

        current = t.rowCount()
        if value == current:
            return  # nothing to do

        # Prevent sorting side‑effects while restructuring
        sorting = t.isSortingEnabled()
        if sorting:
            t.setSortingEnabled(False)

        if value > current:
            # Add required number of rows
            to_add = value - current
            for _ in range(to_add):
                self.stations_insert_row(row=None)  # append at end
        else:
            # Remove surplus rows from bottom
            # (keep top rows stable)
            for r in range(current - 1, value - 1, -1):
                t.removeRow(r)

        if sorting:
            t.setSortingEnabled(True)
        
    def save_multiple_stations(self):
        t = self.station_tableStations_input
        
        if not hasattr(self, "_suspend_station_sync"):
            self._suspend_station_sync = False
        self._suspend_station_sync = True
        
        n_rows = t.rowCount()
        n_cols = t.columnCount()
        sta_data = {}
        for row in range(n_rows):
            for col in range(n_cols):
                if col < 1:
                    sta_data[col] = t.cellWidget(row, col).currentText()
                elif col > 0 and col < 9:
                    sta_data[col] = t.item(row, col).text()
                else:
                    sta_data[col] = t.cellWidget(row, col).isChecked()
            
            station = Station(
                airfoil=self.db.airfoils[sta_data[0]],
                chord=float(sta_data[1]),
                twist_angle=float(sta_data[2]),
                x_offset=float(sta_data[3]),
                y_offset=float(sta_data[4]),
                z_offset=float(sta_data[5]),
                x_multiplier=float(sta_data[6]),
                y_multiplier=float(sta_data[7]),
                z_multiplier=float(sta_data[8]),
                x_mirror=bool(sta_data[9]),
                y_mirror=bool(sta_data[10]),
                # path=self.paths_airfoils[sta_data[0]],
            )
            
            station_name = f'sta_{int(sta_data[5])}'
            
            # self.db.stations[station_name] = station
            self.db.stations.add(station_name, station)
            
        self.handle_msgbar(f'Total stations created: {n_rows}.')
        
        self._suspend_station_sync = False
        self._sync_station_widgets()
    
    ### PARAMETERS METHODS (Page 3)
    
    def update_skin_ui(self, *args):
        """Single source of truth for the LOC/LEN UI."""
        # LOC side
        loc_uses_table = self.skin_loc_radio1.isChecked()
        self.blade_skinolpsta_table.setVisible(loc_uses_table)
        self.loc_frame.setVisible(not loc_uses_table)
        self.blade_skinolpsta_selected.setVisible(loc_uses_table)
        self.label_38.setVisible(loc_uses_table)

        # LEN side
        len_uses_table = self.skin_len_radio1.isChecked()
        self.blade_skinolplen_table.setVisible(len_uses_table)
        self.len_frame.setVisible(not len_uses_table)
        self.blade_skinolplen_selected.setVisible(len_uses_table)
        self.label_39.setVisible(len_uses_table)

        # Shared controls: show if EITHER side uses a table
        show_order_controls = loc_uses_table or len_uses_table
        self.frame_16.setVisible(show_order_controls)
        self.frame_19.setVisible(show_order_controls)
        # self.blade_order_input.setVisible(show_order_controls)
        # self.label_41.setVisible(show_order_controls)
        self.label_40.setVisible(show_order_controls)
    
    
    def new_row_table(self, table, row, col):
        last_row = table.rowCount() - 1
        last_col = table.columnCount() - 1
        
        if row == last_row and col == last_col:
            self.handle_msgbar(f'New row created.')
            n_rows = table.rowCount()
            table.insertRow(n_rows)
            
    def resize_blade_table(self, order):
        tables = [self.blade_skinolpsta_table,self.blade_skinolplen_table]
        
        for i in tables:    
            last_row = i.rowCount() - 1
            if last_row > order:
                i.removeRow(last_row)
            elif last_row < order:
                i.insertRow(last_row+1)
    
    def interpolate_overlap(self):
        order = int(self.blade_order_input.text())
        
        # OLP_STA
        data = []
        y_axis_label = 'Overlap loc. from LE [c]' if self.skin_loc_radio1.isChecked() else 'Distance from LE [d]'
        
        if self.skin_loc_radio1.isChecked():
            
            for row in range(self.blade_skinolpsta_table.rowCount()-1):
                row_data = []
                for col in range(self.blade_skinolpsta_table.columnCount()):
                    item = self.blade_skinolpsta_table.item(row, col)
                    row_data.append(float(item.text()))
                data.append(tuple(row_data))
            coords = tuple(data)
            
            x_target = [float(x[4:]) for x in self.db.stations.keys()]
            # Handling error in case no stations have been created
            if len(x_target) < len(coords):
                x_target, _ = zip(*coords)   
            
            y_target, tck = norm_olp(coords=coords, x_target=x_target, order=order)
            
            x_line = np.linspace(x_target[0],x_target[-1],100)
            y_line = [splev(x_line, x) for x in tck]
            
            xy_line = [list(zip(x_line,y)) for y in y_line]
            xy_pts = [list(zip(x_target,y)) for y in y_target]
            
        else: # If location is constant
            distance = float(self.skin_olp_loc_const.text())
            x_target = [float(x[4:]) for x in self.db.stations.keys()]
            y_target = np.full_like(x_target, distance).tolist()
            xy_pts = [list(zip(x_target, y_target)),]
            xy_line = xy_pts
        
        # save in temporary database
        self.edits['__olp_sta__'] = xy_pts

        # series = []
        # for n in range(len(xy_line)):
        #     series.append([])
        #     for j in range(len(xy_line[n])):
        #         series[n].append([float(xy_line[n][j][0]), float(xy_line[n][j][1])])
        series = [
            [[float(x), float(y)] for x, y in line]
            for line in xy_line
        ]
        self.edits['__olp_sta_line__'] = series
        
        # points = [[] for _ in range(len(y_target))]
        # for i in range(len(xy_pts)):
        #     for j in xy_pts[i]:
        #         points[i].append([float(j[0]), float(j[1])])
        points = [
            [[float(x), float(y)] for x, y in line]
            for line in xy_pts
        ]
        self.edits['__olp_sta_pts__'] = points

        # OLP_LEN
        data = []
        
        if self.skin_len_radio1.isChecked():
            for row in range(self.blade_skinolplen_table.rowCount()-1):
                row_data = []
                for col in range(self.blade_skinolplen_table.columnCount()):
                    item = self.blade_skinolplen_table.item(row, col)
                    row_data.append(float(item.text()))
                data.append(tuple(row_data))
            coords = tuple(data)
            
            x_target = [float(x[4:]) for x in self.db.stations.keys()]
            # Handling error in case no stations have been created
            if len(x_target) < len(coords) :
                x_target, _ = zip(*coords)
            
            y_target, tck = norm_olp(coords=coords, x_target=x_target, order=order)
        
            x_plot = np.linspace(x_target[0],x_target[-1],100)
            y_plot = [splev(x_plot, x) for x in tck]
            
            xy_line = [list(zip(x_plot,y)) for y in y_plot]
            xy_pts = [list(zip(x_target,y)) for y in y_target]
        
        else: # If length is constant
            distance = float(self.skin_olp_len_const.text())
            x_target = [float(x[4:]) for x in self.db.stations.keys()]
            y_target = np.full_like(x_target, distance).tolist()
            xy_pts = [list(zip(x_target, y_target)),]
            xy_line = xy_pts
        
        # save in temporary database
        self.edits['__olp_len__'] = {key:pd.DataFrame(
            xy_pts[key],
            columns=['station','value'],
        )
        for key in range(len(xy_pts))}
        
        ## Line
        # series = [[] for _ in range(len(y_target))]
        # for i in range(len(xy_line)):
        #     for j in xy_line[i]:
        #         series[i].append([float(j[0]), float(j[1])])
        series = [
            [[float(x), float(y)] for x, y in line]
            for line in xy_line
        ]
        self.edits['__olp_len_line__'] = series
        
        ## Scatter 
        # points = [[] for _ in range(len(y_target))]
        # for i in range(len(xy_pts)):
        #     for j in xy_pts[i]:
        #         points[i].append([float(j[0]), float(j[1])])
        points = [
            [[float(x), float(y)] for x, y in line]
            for line in xy_pts
        ]
        self.edits['__olp_len_pts__'] = points
        
        # Update QComboBox with order selection
        self.blade_skinolpsta_selected.clear()
        self.blade_skinolpsta_selected.addItems([str(x+1) for x in range(order)])
        self.blade_skinolpsta_selected.setCurrentIndex(0)
        
        self.blade_skinolplen_selected.clear()
        self.blade_skinolplen_selected.addItems([str(x+1) for x in range(order)])
        self.blade_skinolplen_selected.setCurrentIndex(0)
        
    def table_interpolation_vals(self):
        n_stations = len(self.db.stations)
        z = [sta.parameters['offset'][2] for sta in self.db.stations.values()]
        
        # Interpolation order selected
        if self.skin_loc_radio1.isChecked():
            k1 = int(self.blade_skinolpsta_selected.currentText())
        else:
            k1 = 1
        
        if self.skin_len_radio1.isChecked():
            try:
                k2 = int(self.blade_skinolplen_selected.currentText())
            except ValueError: # Because the box is not populated at the same time.
                k2 = 1
                print(f'{ctime()} Interpolation selected: k1 = {k1}, k2 = {k2}')
        else:
            k2 = 1
        
        y1 = self.edits['__olp_sta__'][k1-1]
        y2 = self.edits['__olp_len__'][k2-1]
        
        # Interpolation array
        y1 = np.array([row[1] for row in y1])
        # y2 = np.array([row[1] for row in y2])
        y2 = y2['value'].to_numpy()
        blade_ilp = np.array(list(zip(z,y1,y2)))
        chord = [sta.parameters['chord'] for sta in self.db.stations.values()]
        
        if self.skin_loc_radio1.isChecked():
            blade_ilp[:,1] *= chord
            self.db.blade['ovp_text'] = pd.DataFrame(
                zip(blade_ilp[:,1],[f'{x:.2f}' for x in blade_ilp[:,1]]),
                columns = ['value', 'text'],
            )
        else:
            # print(y1[0])
            self.db.blade['ovp_text'] = pd.DataFrame([{
                'value': y1[0],'text': f'{y1[0]:.2f}'}])
            
        if self.skin_len_radio1.isChecked():
            blade_ilp[:,2] *= chord
        
        # else:
        #     self.db.blade['']
            
        self.db.blade['overlap'] = pd.DataFrame(
            blade_ilp,
            columns=['z','olp_sta','olp_len'],
        )
        
        # Show interpolation values
        # print(self.db.blade['ovp_text'])
        model = QStandardItemModel(n_stations,3)
        model.setHorizontalHeaderLabels(['Station', 'OLP Start', 'OLP Length'])
        
        for i in range(n_stations):
            model.setItem(i, 0, QStandardItem(f'{z[i]:.0f}'))
            model.setItem(i, 1, QStandardItem(f'{blade_ilp[i][1]:.2f}'))
            model.setItem(i, 2, QStandardItem(f'{blade_ilp[i][2]:.2f}'))
            
        self.tableView.setModel(model)
        self._configure_tables()
        
        # --- Top Graph
        # -------------
        
        # Send to QML
        # print(f'olp_sta_line: {self.edits["__olp_sta_line__"]}')
        self.olplenBridge.updateSeries.emit(
            self.edits['__olp_sta_line__'], k1-1,
            self.edits['__olp_len_line__'], k2-1,
        )
        
        # Joined scatter points (for both OLP_STA and OLP_LEN)
        pts_sta = self.edits['__olp_sta_pts__'][k1-1]
        pts_len = self.edits['__olp_len_pts__'][k2-1]
        print(f'{ctime()} OLP_points selected (first value): {pts_sta[0]}')
        self.olplenBridge.updateScatter.emit(pts_sta + pts_len)
        
        # --- Bot Graph
        # -------------
        # LE and TE lists
        le_list = [
            [sta.parameters['offset'][2], sta.xy[len(sta.xy)//2].tolist()[0]] 
            for sta in self.db.stations.values()
        ]
        te_list = [
            [sta.parameters['offset'][2], sta.xy[0].tolist()[0]]
            for sta in self.db.stations.values()
        ]
        
        if self.skin_loc_radio1.isChecked():
            chord_1 = [sta.parameters['chord'] for sta in self.db.stations.values()]
        else:
            chord_1 = [1.0 for _ in self.db.stations.values()]
        
        if self.skin_len_radio1.isChecked():
            chord_2 = [sta.parameters['chord'] for sta in self.db.stations.values()]
        else:
            chord_2 = [1.0 for _ in self.db.stations.values()]
        
        xy_pts = self.edits['__olp_sta__'][k1-1]
        xy_sta = [
            [float(n[0]), float((n[1] * chord_1[i]) + le_list[i][1])]
            for i, n in enumerate(xy_pts)
        ]
        xy_pts = self.edits['__olp_len__'][k2-1]
        xy_len = [
            [row.station, (row.value * chord_2[i]) + xy_sta[i][1]]
            for i, row in enumerate(xy_pts.itertuples(index=False))
        ]
        # xy_sta = [[list(t) for t in inner] for inner in xy_line]
        # print(f'LE points: {le_list}')
        # print(f'TE points: {te_list}')
        print(f'{ctime()} OLP_STA points first value: {xy_sta[0][0]}')
        
        # Send to QML
        self.olpstaBridge.updateSeries.emit(xy_sta, xy_len, le_list, te_list)
        # self.olpstaBridge.updateScatter.emit(xy_pts)
    
    def save_bladeparams(self):
        idx_olp_sta = self.blade_skinolpsta_selected.currentIndex()
        idx_olp_len = self.blade_skinolplen_selected.currentIndex()
        
        try:
            self.db.blade['olp_sta'] = self.edits['__olp_sta__'][idx_olp_sta]
            # print(self.db.blade['olp_sta'])
            self.db.blade['olp_len'] = self.edits['__olp_len__'][idx_olp_len]
        except KeyError:
            self.handle_msgbar('Error: Overlap interpolation was not performed.', wcolor='red')
            return
        
        if self.skin_len_radio1.isChecked():
            chord = [sta.parameters['chord'] for sta in self.db.stations.values()]
            self.db.blade['olp_len']['value'] *= chord
        # print(self.db.blade['olp_len'])
        
        self.handle_msgbar(f'Parameters saved.', wcolor='green')
    
    ### SKIN METHODS
    
    def update_stabox(self):
        if self.stackedWidget.currentIndex() == 4:
            names_stations = self.db.stations.keys()
            self.skin_liststations.clear()
            self.skin_liststations.addItems(names_stations)
        
    def update_olptgt(self):
        try:
            df = self.db.blade['overlap']
        except KeyError:
            self.handle_msgbar('Warning: Blade interpolation was not saved.', wcolor='yellow')
            return
            
        n_station = float(self.skin_liststations.currentText()[4:])
        # station = self.db.stations[self.skin_liststations.currentText()]
        
        try:
            olp_target = df.loc[df['z'] == n_station, 'olp_sta'].item()
            print(f'{ctime()} olp_target (new): {olp_target:.2f}')
            
            # olp_sta = np.array(self.db.blade['olp_sta'])
            # norm_olp_tgt = float(olp_sta[np.where(olp_sta[:,0]==n_station)[0],1][0])
            # olp_target = norm_olp_tgt*station.parameters['chord']
            # print(f'olp_target (old): {olp_target:.2f}')
            self.skin_overlaptarget_input.setText(f'{olp_target:.2f}')
            
        except ValueError:
            self.handle_msgbar('Error: Overlap target could not be interpolated.', wcolor='red')
    
    def build_section(self):
        if self.stackedWidget.currentIndex() == 4:
            try:
                station = self.db.stations[self.skin_liststations.currentText()] if self.skin_liststations.currentText() != '' else None
                n_plies = int(self.skin_nplies_input.text()) if self.skin_nplies_input.text() else 1
                ply_thk = float(self.skin_plythickness_input.text()) if self.skin_plythickness_input.text() else 1
                te_thkn = float(self.skin_tethickness_input.text()) if self.skin_tethickness_input.text() else n_plies*ply_thk
                bond_th = float(self.skin_bond_input.text()) if self.skin_bond_input.text() else 1
                saveFig = self.skin_savefig_input.isChecked()
                
                try:
                    df_olp = self.db.blade['ovp_text']
                except KeyError:
                    self.handle_msgbar('Error: Blade interpolation was not saved.', wcolor='red')
                    return
                
                olp_txt = df_olp.loc[df_olp['text'] == self.skin_overlaptarget_input.text(), 'value'].item()
                olp_tgt = float(olp_txt) if olp_txt else 10
                print(f'{ctime()} olp_tgt: {olp_tgt}')
                section = Section(
                    station = station,
                    n_plies = n_plies,
                    ply_thickness = ply_thk,
                    overlap_target = olp_tgt,
                    te_thickness = te_thkn,
                    bond_thickness= bond_th,
                    saveFig = saveFig,
                    tolerance = self.db.settings['sec_le_tolerance'],
                    ini_u0 = self.db.settings['sec_initial_i0'],
                )
                
                # Jiggle method
                if section.parameters['isCircle']:
                    self.handle_msgbar(f'Jiggle method is not implemented on circular shapes.', wcolor='yellow')
                
                if self.skin_jiggle_toggle.isChecked() and not section.parameters['isCircle']:
                    
                    # Retrieve overlap distance
                    try:
                        df_len = self.db.blade['olp_len']
                    except KeyError:
                        self.handle_msgbar('Error: Blade interpolation was not saved.', wcolor='red')
                        return
                    
                    z_sta = float(self.skin_liststations.currentText()[4:])
                    print(f'{ctime()} name_sta: {z_sta}')
                    print(df_len)
                    olp_len = df_len.loc[df_len['station'] == z_sta]['value'].item()
                    
                    
                    section.jiggle(
                        overlap_dist = olp_len,
                        bond_thickness = bond_th,
                    )
                    
                    # Plot
                    self.skin_ax.clear()
                    colours = section.parameters['colours']
                    p_bot1 = section.points['bot_1']
                    p_bot2 = section.points['bot_2']
                    p_bot3 = section.points['bot_3']
                    p_top  = section.points['top_1']
                    p_bond = section.points['bond']
                    
                    for i in range(1, n_plies+1):
                        # BOT_2 - JIGGLE
                        self.skin_ax.plot(p_bot2[i]['x'], p_bot2[i]['y'], label = f'Ply {i}', c = colours[i-1])
                        
                        for j in range(4):
                            
                            # BOT_1
                            self.skin_ax.plot(
                                p_bot1[i][j]['x'], p_bot1[i][j]['y'],
                                c = colours[i-1], label = None)            
                            
                            # BOT_3
                            self.skin_ax.plot(
                                p_bot3[i][j]['x'], p_bot3[i][j]['y'],
                                c = colours[i-1], label = None)
                            
                            # TOP_1 
                            self.skin_ax.plot(
                                p_top[i][j]['x'], p_top[i][j]['y'],
                                c = colours[i-1], label = None)
                            
                    # BOND
                    self.skin_ax.plot(p_bond[1]['x'], p_bond[1]['y'], label = f'Bond', c = 'black')
                    
                    for i in range(4):
                        self.skin_ax.plot(p_bond[0][i]['x'], p_bond[0][i]['y'],
                                c = 'black', label = None)
                
                else:
                    
                    self.skin_ax.clear()
                    n_plies = section.parameters['n_plies']
            
                    cmap = plt.get_cmap('rainbow')
                    colours = [cmap(x/n_plies) for x in range(n_plies)]
                    
                    for i in range(1,n_plies+1):    
                        self.skin_ax.plot(
                            section.points['bot_1'][i][0]['x'], 
                            section.points['bot_1'][i][0]['y'],
                            label = f'Ply {i}', c = colours[i-1]
                        )
                        
                        self.skin_ax.plot(
                            section.points['top_1'][i][0]['x'],
                            section.points['top_1'][i][0]['y'],
                            label = None, c = colours[i-1]
                        )
                        
                        for j in range(1,4):
                            self.skin_ax.plot(
                                section.points['bot_1'][i][j]['x'], 
                                section.points['bot_1'][i][j]['y'],
                                label = None, c = colours[i-1]
                            )
                            self.skin_ax.plot(
                                section.points['top_1'][i][j]['x'], 
                                section.points['top_1'][i][j]['y'],
                                label = None, c = colours[i-1]
                            )
                
                self.skin_ax.set_xlabel('x [d]', fontsize='x-large')
                self.skin_ax.set_ylabel('y [d]', fontsize='x-large')
                self.skin_ax.minorticks_on()
                self.skin_ax.tick_params(axis='both', which='both', direction='in',
                                    top=True, right=True, labelsize='medium')
                self.skin_ax.grid(visible=True, which='major', linestyle='--', linewidth=0.75)
                self.skin_ax.set_aspect('equal', adjustable='datalim')
                self.skin_ax.legend(loc = 'best')
                
                self.canvas_4.draw_idle()
                
                # Temporary save
                self.edits['__section__'] = section
                self.handle_msgbar(f'Number of curves: {len(section.splines.keys())}')
            
            except NameError:
                print(f'{ctime()} Skin section: Error - Wrong input.')
                
    def saveSection(self):
        section_name = f'sec_{int(self.edits['__section__'].parameters['z'])}'
        self.db.sections[section_name] = self.edits['__section__']
        self.handle_msgbar(f'Section "{section_name}" saved.', wcolor='green')
    
    def saveAllSections(self):
        n = self.skin_liststations.count()
        # Progress bar
        self.progressBar.setRange(0, 100)  # normalised 0–100%
        
        for i in range(n):
            station = self.db.stations[self.skin_liststations.itemText(i)]    
            n_plies = int(self.skin_nplies_input.text()) if self.skin_nplies_input.text() else 1
            ply_thk = float(self.skin_plythickness_input.text()) if self.skin_plythickness_input.text() else 1
            te_thkn = float(self.skin_tethickness_input.text()) if self.skin_tethickness_input.text() else n_plies*ply_thk
            bond_th = float(self.skin_bond_input.text()) if self.skin_bond_input.text() else 1
            gen_olp = self.skin_jiggle_toggle.isChecked()
            saveFig = self.skin_savefig_input.isChecked()
            
            try:
                df = self.db.blade['overlap']
            except KeyError:
                self.handle_msgbar('Error: Blade interpolation was not saved.', wcolor='red')
                return
            
            z = station.parameters['offset'][2]
            olp_target = df.loc[df['z'] == z, 'olp_sta'].item()
            olp_tgt = olp_target if olp_target else 10
            
            section = Section(
                    station = station,
                    n_plies = n_plies,
                    ply_thickness = ply_thk,
                    overlap_target = olp_tgt,
                    te_thickness = te_thkn,
                    bond_thickness= bond_th,
                    saveFig = saveFig,
                )
            
            if gen_olp:
                
                # Retrieve overlap distance
                try:
                    df_len = self.db.blade['olp_len']
                except KeyError:
                    self.handle_msgbar('Error: Blade interpolation was not saved.', wcolor='red')
                    return
                
                z_sta = float(self.skin_liststations.currentText()[4:])
                olp_len = df_len.loc[df_len['station'] == z_sta]['value'].item()
                
                section.jiggle(
                    overlap_dist = olp_len,
                    bond_thickness = bond_th,
                )
            
            # Save section
            self.db.sections[f'sec_{int(z)}'] = section
            
            # Update progress bar
            progress = int((i + 1) / n * 100)
            self.progressBar.setValue(progress)

        self.handle_msgbar(f'{i+1} stations saved.', wcolor='green')

    ### EXPORT METHODS
    
    def update_sectionList(self):
        if self.stackedWidget.currentIndex() == 5:
            self.export_sectionsList.clear()
            list_sections = list(self.db.sections.keys())
            self.export_sectionsList.insertItems(0,list_sections)
            
    def exportSections(self):
        
        if len(self.export_sectionsList.selectedItems()) > 0:
            items = self.export_sectionsList.selectedItems()
        else:
            self.handle_msgbar('No sections selected.', wcolor='red')
            return
            
        # JSON option
        if self.export_json_toggle.isChecked():
            dict_sections = {
                int(sec.text()[4:]):skinSection(self.db.sections[sec.text()]) 
                for sec in items
            }
            filename = f'{self.export_expFileName_input.text()}'
            skinPart(sections=dict_sections, path= self.main_path, filename=filename)
              
            self.handle_msgbar(f'File "{filename}.json" exported succesfully.', wcolor='green')
            if self.db.settings['exp_open_folder']:
                QDesktopServices.openUrl(QUrl.fromLocalFile(self.main_path))
        
        elif self.export_csv_toggle.isChecked():
            
            foldername = self.export_expFileName_input.text()
            
            # Base folder
            skin_dir = os.path.join(self.main_path,foldername,'Skin')
            os.makedirs(skin_dir, exist_ok=True)
            
            dict_sections = {
                int(sec.text()[4:]):self.db.sections[sec.text()]
                for sec in items
            }
            
            for key, sec in dict_sections.items():
                z = sec.parameters['z']
                n_plies = sec.parameters['n_plies']

                for side in ['top', 'bot']:
                    for ply in range(1, n_plies + 1):
                        # Create ply subfolder (zero-padded)
                        ply_dir = os.path.join(skin_dir, f'Ply_{ply:02d}')
                        os.makedirs(ply_dir, exist_ok=True)

                        for spline in [0, 1]:
                            x = sec.points[f'{side}_1'][ply][spline]['x']
                            y = sec.points[f'{side}_1'][ply][spline]['y']
                            z_col = [z] * len(x)

                            df = pd.DataFrame({'x': x, 'y': y, 'z': z_col})

                            # Include section id (or z) to avoid overwriting across sections
                            filename = f"{side}_sec{key}_{spline}.csv"
                            df.to_csv(
                                os.path.join(ply_dir, filename),
                                index=False,
                                header=False,
                            )

            self.handle_msgbar(f'Folder "{foldername}" exported succesfully.', wcolor='green')
            if self.db.settings['exp_open_folder']:
                QDesktopServices.openUrl(QUrl.fromLocalFile(self.main_path))

        else:
            return
            
    def changeExportType(self, button, checked):
        if not checked:
            return
        
        if button is self.export_json_toggle:
            self.label_46.setText('Export file name:')
            self.label_47.setText('.json')
            self.label_47.show()
        
        if button is self.export_csv_toggle:
            self.label_46.setText('Export folder name:')
            self.label_47.hide()
    
    ### GENERAL UI METHODS
    
    def _sync_airfoil_widgets(self):
        names = self.db.airfoils.keys()
        
        display_names = [f'{a.family} {a.profile}' for a in self.db.airfoils.values()]
        self.airfoil_listairfoils_widget.blockSignals(True)
        self.airfoil_listairfoils_widget.clear()
        self.airfoil_listairfoils_widget.addItems(display_names)
        self.airfoil_listairfoils_widget.blockSignals(False)
        
        self.station_listairfoils_box.blockSignals(True)
        self.station_listairfoils_box.clear()
        self.station_listairfoils_box.addItems(names)
        self.station_listairfoils_box.blockSignals(False)
    
    def _sync_station_widgets(self, stations:dict | None = None):
        if getattr(self, "_suspend_station_sync", False):
            return
    
        if stations is None:
            stations = self.db.stations.all()
        
        names = self.db.stations.keys()
        self.station_liststation_box.blockSignals(True)
        self.station_liststation_box.clear()
        self.station_liststation_box.addItems(names)
        self.station_liststation_box.blockSignals(False)
        self.update_station_params()
        
        # ---- Rebuild the Advanced table from the snapshot ----
        t = self.station_tableStations_input

        # preserve sort & scroll
        sort_enabled = t.isSortingEnabled()
        if sort_enabled:
            hdr = t.horizontalHeader()
            sort_col = hdr.sortIndicatorSection()
            sort_order = hdr.sortIndicatorOrder()
        vpos = t.verticalScrollBar().value()

        t.setUpdatesEnabled(False)
        t.setSortingEnabled(False)
        t.clearContents()
        t.setRowCount(0)

        for name, sta in stations.items():
            # airfoil name
            airfoil_name = getattr(sta, "airfoil", None)
            
            p = sta.parameters
            offset = p.get("offset", (0.0, 0.0, 0.0))
            multp  = p.get("multiplier", (1.0, 1.0, 1.0))
            mirror = p.get("mirror", (False, True))
            # numeric columns (8 numbers: cols 1–8)
            nums = [
                float(p.get("chord", 1.0)),
                np.degrees(p.get("twist_angle", 0.0)),
                float(offset[0]),
                float(offset[1]),
                float(offset[2]),  # col 5
                float(multp[0]),
                float(multp[1]),
                float(multp[2]),
            ]

            self.stations_insert_row(
                row=None,
                airfoil=airfoil_name,
                def_row=False,
                data_row=nums,
                xmirror=bool(mirror[0]),
                ymirror=bool(mirror[1]),
            )

        # restore sort & scroll
        t.setSortingEnabled(sort_enabled)
        if sort_enabled:
            t.sortItems(sort_col, sort_order)
        t.setUpdatesEnabled(True)
        t.verticalScrollBar().setValue(vpos)
        
    def _configure_tables(self):
        hdr = self.station_tableStations_input.horizontalHeader()
        hdr.setSectionResizeMode(0, QHeaderView.Stretch)  # Airfoil
        
        # Interpolation values table
        hh = self.tableView.horizontalHeader()
        hh.setSectionResizeMode(QHeaderView.Stretch)
        
        # Blade overlap table
        hsl = self.blade_skinolpsta_table.horizontalHeader()
        hsl.setSectionResizeMode(QHeaderView.Stretch)
        
        hsl2 = self.blade_skinolplen_table.horizontalHeader()
        hsl2.setSectionResizeMode(QHeaderView.Stretch)
    
    def load_default_airfoils(self):
        for i in [x for x in os.listdir(resource_path('edfoil/airfoils'))]:
            airfoil_path = resource_path(f'edfoil/airfoils/{i}')
            airfoil = Airfoil()
            airfoil.importCoords(airfoil_path)
            # self.db.airfoils[airfoil.name] = airfoil
            self.db.airfoils.add(airfoil.name, airfoil)
            
            # Debug
            # print(list(self.db.airfoils.keys()))
        
        # Select first by default
        print(f'{ctime()} Number of default airfoils uploaded: {len(self.db.airfoils)}.')
        if len(self.db.airfoils) > 0:
            self.airfoil_listairfoils_widget.setCurrentRow(0, QItemSelectionModel.ClearAndSelect)
            print(f'{ctime()} Current index selected in Airfoil Creator: {self.airfoil_listairfoils_widget.currentItem().text()}')
            self.update_naca_chart()
        # names = [f'{x.family} {x.profile}' for x in self.db.airfoils.values()]
        # self.airfoil_listairfoils_widget.clear()
        # self.airfoil_listairfoils_widget.addItems(names)
            
    def station_mousecoords(self, event: QMouseEvent) -> None:
        coords = event.position()
        x,y = coords.x(), coords.y()
        coord_lims = self.station_chartview.chart().plotArea().getCoords()
        
        if (x >= coord_lims[0] and x <= coord_lims[2] and
            y >= coord_lims[1] and y <= coord_lims[3]):
            
            coords_scaled = self.station_chartview.chart().mapToValue(coords)
            x_scaled = coords_scaled.x()
            y_scaled = coords_scaled.y()
            
            self.station_xy_current.setText(f'({x_scaled:.2f}, {y_scaled:.2f})')
    
    def graph_template(self) -> QChart:
        """Empty graph template.

        Returns:
            chart: Chart Object.
        """
        data = QLineSeries()
        chart = QChart()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.legend().hide()
        chart.addSeries(data)
        
        axisX = QValueAxis()
        axisY = QValueAxis()
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        data.attachAxis(axisX)
        data.attachAxis(axisY)
        
        return chart
    
    def generate_colours(self, num_curves:int, cmap_name:str='viridis') -> list[QColor]:
        """
        Generate a list of QColor objects for the given number of curves.

        :param num_curves: Number of colours (curves)
        :param cmap_name: Matplotlib colormap name (default is 'viridis')
        :return: List of QColor objects
        """
        
        cmap = plt.get_cmap(cmap_name)
        colours = [cmap(i / num_curves) for i in range(num_curves)]
        qcolours = [QColor(int(r * 255), int(g * 255), int(b * 255)) for r, g, b, _ in colours]
        
        return qcolours
    
    def equal_axes(self, chart: QChart, range_values: list[list[float, float]]) -> None:
        # Unpack min/max correctly
        x_min, x_max = range_values[0]
        y_min, y_max = range_values[1]

        # Determine aspect ratio of the plot area
        height = chart.plotArea().height()
        width = chart.plotArea().width()
        aspect_ratio = width / height if height > 0 else 1.

        x_mid = (x_max + x_min) / 2
        y_mid = (y_max + y_min) / 2

        x_span = x_max - x_min or 1e-12  # Prevent division by zero
        y_span = y_max - y_min or 1e-12  # Prevent division by zero

        # Adjust spans to make them visually equal
        if x_span / y_span > aspect_ratio:
            # x dominates → expand y range
            new_y_span = x_span / aspect_ratio
            y_min = y_mid - new_y_span / 2
            y_max = y_mid + new_y_span / 2
            x_min = x_mid - x_span / 2
            x_max = x_mid + x_span / 2
        else:
            # y dominates → expand x range
            new_x_span = y_span * aspect_ratio
            x_min = x_mid - new_x_span / 2
            x_max = x_mid + new_x_span / 2
            y_min = y_mid - y_span / 2
            y_max = y_mid + y_span / 2
            
        # Padding
        pad = 0.05  # 5% padding
        px = (x_max - x_min) * pad
        py = (y_max - y_min) * pad
        x_min -= px; x_max += px
        y_min -= py; y_max += py

        # Apply to axes
        for axis in chart.axes(Qt.Horizontal):
            axis.setRange(x_min, x_max)
        for axis in chart.axes(Qt.Vertical):
            axis.setRange(y_min, y_max)   
    
    def change_work_directory(self) -> None:
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setViewMode(QFileDialog.List)
        if dialog.exec():
            self.main_path = dialog.selectedFiles()[0]
            self.workpath_lineedit.setText(self.main_path)
        
    def load_db(self) -> None:
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter(self.tr('EdFoil (*.edf)'))
        dialog.setViewMode(QFileDialog.Detail)
        if not dialog.exec():
            return
        
        filepath = dialog.selectedFiles()[0]
        
        # try:
        new_db = load_session_from_edf(filepath)
        # except Exception as e:
        #     self.handle_msgbar(f'Error loading session: {e}', wcolor='red')
        #     return
        
        # Replace db and update UI
        self.db = new_db
        self._sync_airfoil_widgets()
        self._sync_station_widgets()
        self.update_sectionList()
        self.update_stabox()
        self.handle_msgbar(f'Session loaded from: {filepath}', wcolor='green')
        
        
            
    def new_db(self) -> None:
        self.db = session()
        self.load_default_airfoils()
        self.handle_msgbar('New session started.')
        
    def mouse_coords(self,label,event):
        label.setText(f'({event.x()},{event.y()})')
        
    def switch_to_homePage(self):
        self.stackedWidget.setCurrentIndex(0)
        self.page_title_label.setText(self.home_page_button.text())
    
    def switch_to_airfoilPage(self):
        self.stackedWidget.setCurrentIndex(1)
        self.page_title_label.setText(self.airfoil_page_button.text())
        
        # :TODO Update airfoil list
        
        
    def switch_to_stationPage(self):
        self.stackedWidget.setCurrentIndex(2)
        self.page_title_label.setText(self.station_page_button.text())
        
        # Update airfoil list in station page
        # names_airfoils = list(self.db.airfoils.keys())
        # self.station_listairfoils_box.clear()
        # self.station_listairfoils_box.addItems(names_airfoils)
        self.update_station_chart()
        # Update dropdown menu in advanced tab
        # n_rows = self.station_tableStations_input.rowCount()
        # for row in range(n_rows):
        #     list_airfoils = QComboBox()
        #     list_airfoils.addItems(list(self.db.airfoils.keys()))
        #     self.station_tableStations_input.setCellWidget(row,0,list_airfoils)
        
    def switch_to_bladePage(self):
        self.stackedWidget.setCurrentIndex(3)
        self.page_title_label.setText(self.blade_page_button.text())
        
    def switch_to_skinPage(self):
        self.stackedWidget.setCurrentIndex(4)
        self.page_title_label.setText(self.skin_page_button.text())
    
    def switch_to_sparPage(self):
        self.stackedWidget.setCurrentIndex(5)
        self.page_title_label.setText(self.spar_page_button.text())
    
    def switch_to_exportPage(self):
        self.stackedWidget.setCurrentIndex(5)
        self.page_title_label.setText(self.export_page_button.text())
    
    def upload_airfoil_file(self):
        # TODO: Update this to not clash with Airfoil Creator Tab
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setNameFilter(self.tr('Files (*.csv *.txt *.dat)'))
        dialog.setViewMode(QFileDialog.Detail)
        fileNames = []
        if dialog.exec():
            fileNames = dialog.selectedFiles()
        
        airfoil_files = [x.split('/')[-1][:-4] for x in fileNames]
        # airfoil_names = {}
        for i, file in enumerate(fileNames):
            try:
                temp = Airfoil()
                print(f'{ctime()} Importing: {file}')
                temp.importCoords(path = file)
                self.db.airfoils.add(temp.name, temp)
                # airfoil_names[temp.name] = temp.name
                
            except:
                self.handle_msgbar(f'File ({i} of {len(airfoil_files)}): {file} could not be imported.')
        
        self.handle_msgbar(f'Number of files imported: {i}.', wcolor='green')
        
        # Add new files to the QComboBox
        # n_items_current = self.station_listairfoils_box.count()
        # self.station_listairfoils_box.insertItems(n_items_current, list(airfoil_names.keys()))
        
    
    def onTextChanged(self):
        # Restart the timer whenever the text changes
        self.timer_station.start(500)
        
    def secInputChanged(self):
        # Restart the timer whenever the text changes
        self.timer_skin.start(500)
    
    def quit_message_box(self):
        msgBox = QMessageBox()
        msgBox.setMinimumSize(500,400)
        msgBox.setWindowTitle('Warning Message')
        msgBox.setText('The project has been modified.')
        msgBox.setInformativeText('Do you want to save your changes before leaving?')
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setStandardButtons(QMessageBox.Save| QMessageBox.No| QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec()
        
        if ret == QMessageBox.Save:
            self.save_project()
        elif ret == QMessageBox.No:
            self.app.quit()
    
    def database_file(self, file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            QMessageBox.information(self, 'Success', f'File saved successfully: {file_path}')
        
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {str(e)}')
    
    def save_project(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilter(self.tr('EdFoil (*.edf)'))
        dialog.setViewMode(QFileDialog.List)
        dialog.setDefaultSuffix('edf')

        file_path, _ = QFileDialog.getSaveFileName(
            self, self.tr('Save File'),
            self.main_path, 
            'EdFoil Files (*.edf);;All Files (*)', 
            options=QFileDialog.Options()
        )
        
        if not file_path:
            # self.database_file(file_path,'Hello')
            return self.handle_msgbar('Save cancelled.', wcolor='red')
        
        try:
            save_session_to_edf(self.db, file_path)
            self.handle_msgbar(f'Project saved successfully: {file_path}', wcolor='green')

        except Exception as e:
            self.handle_msgbar(f'Error saving project: {str(e)}', wcolor='red')

    def info_message(self):
        msgBox = QMessageBox()
        about_text = 'This open source software, has been developed in ' \
        'the School of Engineering, in the University of Edinburgh.\n\n' \
        'The current version is version 0.3.1.'
        
        msgBox.about(self, 'About EdFoil', about_text)
        
    def open_settings(self):
        # Store current theme
        current_theme = self.settings_dialog.themes_box.currentText()
        
        # Store current section parameters
        current_le_tol = self.settings_dialog.le_tolerance.text()
        current_i0 = self.settings_dialog.initial_i0.text()
        
        # Store export folder option
        current_exp_folder = self.settings_dialog.export_folder.isChecked()
        
        if self.settings_dialog.exec():
            self.settings_dialog.apply_settings()
            self.save_settings()
            # Apply theme
            # theme = self.settings_dialog.themes_box.currentText()
            # theme_qss = self.themes.get(theme, "")
            # self.stylesheet.setStyleSheet(theme_qss)
            # self.handle_msgbar(f"Theme \"{theme}\" applied.")
        else:
            # Revert to previous theme if cancelled
            self.settings_dialog.themes_box.setCurrentText(current_theme)
            self.settings_dialog.le_tolerance.setText(current_le_tol)
            self.settings_dialog.initial_i0.setText(current_i0)
            self.settings_dialog.export_folder.setChecked(current_exp_folder)
            self.handle_msgbar("Settings cancelled.", wcolor='red')
            
    def load_themes(self):
        themes = [
            file.stem for file in Path(resource_path('resources/themes')).glob('*.qss')
            if file.stem != 'template'
        ]
        self.themes = {}
        for theme in themes:
            t = Theme(theme)
            t.load_qss(Path(resource_path(f'resources/themes/{theme}.qss')), sout=False)
            self.themes[theme] = t

        self.settings_dialog.themes_box.blockSignals(True)
        self.settings_dialog.themes_box.addItems(themes)
        self.settings_dialog.themes_box.setCurrentText('edfoil-light')
        self.settings_dialog.themes_box.blockSignals(False)
        
        print(f'{ctime()} Themes loaded.')
        
    def apply_theme(self):
        theme_name = self.settings_dialog.themes_box.currentText()
        if theme_name in self.themes:
            self.stylesheet.setStyleSheet(self.themes[theme_name].qss)
            # self.settings_dialog.frame.setStyleSheet(self.themes[theme_name].qss)  
            self.handle_msgbar(f'Theme "{theme_name}" applied.', wcolor='green')
        else:
            self.handle_msgbar(f'Error: Theme "{theme_name}" not found.', wcolor='red')


    def save_settings(self):
        le_tolerance = int(self.settings_dialog.le_tolerance.text())
        spl_initial_guess = float(self.settings_dialog.initial_i0.text())
        exp_folder = self.settings_dialog.export_folder.isChecked()
        
        self.db.settings['sec_le_tolerance'] = le_tolerance
        self.db.settings['sec_initial_i0'] = spl_initial_guess
        self.db.settings['exp_open_folder'] = exp_folder

        print(f'{ctime()} Section parameters saved:')
        print(f'           Leading edge tolerance: {le_tolerance}')
        print(f'           Initial guess i0: {spl_initial_guess}')
        print(f'           Open export folder: {exp_folder}')

    ### MESSAGE BAR METHODS
    
    def warning_color(self, color:str='red'):
        current_theme = self.settings_dialog.themes_box.currentText()
        # print(f'{ctime()} Current theme: {current_theme}.')
        palette = self.themes[current_theme].palette
        # print(f'{ctime()} Palette: {palette}')
        if color == 'red':
            color_selected = palette['DANGER']
        elif color == 'yellow':
            color_selected = palette['WARNING']
        elif color == 'green':
            color_selected = palette['SUCCESS']
        else:
            return

        ss = f'#warning_light:indicator {{\n border-radius: 8px;\n background-color: {color_selected};\n margin-left: 5px;\n}}'
        self.warning_light.setStyleSheet(ss)

    def handle_msgbar(self, message:str, wcolor:str | None = None, time:int=4000):
        if message:
            self.timer_msg.start(time)
            self.def_msgbar.hide()
            self.msgbar.setText(message)
            self.warning_color(wcolor)
            self.warning_light.show()
            self.msgbar.show()
    
    def show_def_msg(self):
            self.def_msgbar.show()
            self.msgbar.hide()
            self.warning_light.hide()
            
    def open_doc(self):
        
        # Find pdf file in resources
        pdf_path = resource_path('resources/EdFoil User Guide.pdf')
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))

## CLASSES

# For turning string inputs to floats inside QTableWidget instances
class NumericItem(QTableWidgetItem):
    def __lt__(self, other):
        try:
            return float(self.text()) < float(other.text())
        except ValueError:
            return super().__lt__(other)

# For only allowing floats in certain QTableWidgets
class FloatDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        validator = QDoubleValidator(-1e9, 1e9, 3, editor)  # min, max, decimals
        validator.setNotation(QDoubleValidator.StandardNotation)
        editor.setValidator(validator)
        return editor

# Graph bridge
class GraphBridge(QObject):
    updateSeriesRequested = Signal(list, str)  # (points, name)
    clearRequested        = Signal()
    updateAxesRequested   = Signal(float, float, float, float, float, float)
    updateLE = Signal(float, float)

# OLP STA QML bridge
class OverlapBridge(QObject):
    updateSeries = Signal(list, list, list, list)
    updateScatter = Signal(list)
    clear        = Signal()
    
# OLP END QML bridge
class OlpLengthBridge(QObject):
    updateSeries = Signal(list, int, list, int)
    updateScatter = Signal(list)
    clear        = Signal()

# General table reader
def _coerce_float(text: str) -> float:
    # tolerate commas and whitespace
    return float(text.replace(',', '').strip())

def read_table_as_tuples(table: QTableWidget, *, skip_blank_rows: bool = True) -> tuple[tuple[float, ...], ...]:
    rows_out = []
    n_rows, n_cols = table.rowCount(), table.columnCount()

    for r in range(n_rows):
        vals_str = []
        all_blank = True
        for c in range(n_cols):
            it = table.item(r, c)
            s = it.text() if it is not None else ""
            s = s.strip()
            if s != "":
                all_blank = False
            vals_str.append(s)

        if skip_blank_rows and all_blank:
            continue

        try:
            vals = tuple(_coerce_float(s) for s in vals_str)
        except ValueError:
            # You can surface a friendly message, highlight the bad cell, etc.
            # For now, skip rows that aren't fully numeric.
            continue

        rows_out.append(vals)

    return tuple(rows_out)

# Helper for tick intervals in QML
def _nice_step(raw: float) -> float:
    if raw <= 0:
        return 1.0
    exp10 = 10 ** np.floor(np.log10(raw))
    frac  = raw / exp10
    if frac < 1.5: base = 1
    elif frac < 3: base = 2
    elif frac < 7: base = 5
    else: base = 10
    return base * exp10

# Settings Window
class SettingsDialog(QDialog, Ui_settingsDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Settings")
        # Connect dialog buttons if present (example object names)
        if hasattr(self, "buttonBox"):
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)
            
        self.le_tolerance.setValidator(QIntValidator(0, 14, self))
        self.initial_i0.setValidator(QDoubleValidator(0.0, 100.0, 2, self))

    def apply_settings(self):
        # TODO: read widgets and store in your session / config
        pass
    
# Time getter
def ctime() -> str:
    return f'[{datetime.now().strftime('%H:%M:%S')}] -'