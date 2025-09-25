from ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import (QMainWindow, QFileDialog, QMessageBox, 
                               QCheckBox, QComboBox, QTableWidgetItem)
from PySide6.QtCharts import (QChart, QLineSeries, QChartView, QCategoryAxis,
                              QValueAxis, QScatterSeries, QAreaSeries)
from PySide6.QtGui import QPainter, QFont, QPen, QBrush, QColor, Qt, QMouseEvent
from PySide6.QtCore import QTimer, Qt, QPointF, QSizeF


from edfoil.classes.airfoil import Airfoil
from edfoil.classes.station import Station
from edfoil.classes.section import Section
from edfoil.utils.bladeparams import norm_olp
from edfoil.utils.abaqusExp import *
from edfoil.utils.dev import resource_path

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import pandas as pd

from scipy.interpolate import splev

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        
        # Set color palette
        # color_background = palette.property('background')
        # color_button = palette.property('color1')
        # color_text = palette.property('text')
        
        self.setupUi(self)
        self.setWindowTitle('EdFoil')
        
        # Messagebar
        self.timer_msg = QTimer(parent=self)
        self.timer_msg.setSingleShot(True)
        self.timer_msg.timeout.connect(self.show_def_msg)
        
        # Project start
        self.db = session() # Class db [not a dictionary]
        self.edits = {}
        self.handle_msgbar(message='New database created.')
        
        # Tab switching
        self.home_page_button.clicked.connect(self.switch_to_homePage)
        self.airfoil_page_button.clicked.connect(self.switch_to_airfoilPage)
        self.station_page_button.clicked.connect(self.switch_to_stationPage)
        self.blade_page_button.clicked.connect(self.switch_to_bladePage)
        self.skin_page_button.clicked.connect(self.switch_to_skinPage)
        self.spar_page_button.clicked.connect(self.switch_to_sparPage)
        self.export_page_button.clicked.connect(self.switch_to_exportPage)
        
        # Lower sidebar buttons
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
        
        # List of airfoils
        self.load_default_airfoils()
        
        # Main chart
        # self.airfoil_chart = self.graph_template()
        # self.airfoil_chartview.setChart(self.airfoil_chart)
        # self.airfoil_chartview.mouseMoveEvent = self.airfoil_mousecoords
        self.airfoil_fig = Figure(figsize=(10, 3), tight_layout=True)
        self.airfoil_ax = self.airfoil_fig.add_subplot(111)
        self.canvas = FigureCanvasQTAgg(self.airfoil_fig)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.verticalLayout_9.addWidget(self.toolbar)
        self.verticalLayout_9.addWidget(self.canvas)
        
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
        self.timer_station.timeout.connect(self.update_airfoil_chart)
        
        # Airfoil list
        self.station_listairfoils_box.addItems(list(self.db.airfoils.keys()))
        
        # Upload additional airfoils
        self.station_uploadairfoil_button.clicked.connect(self.upload_airfoil_file)
        
        # Main chart
        self.station_chart_empty = self.graph_template()
        self.station_chartview.setChart(self.station_chart_empty)
        self.station_chartview.mouseMoveEvent = self.station_mousecoords
        
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
        
        # Advanced tab
        # ------------
        self.stations_insert_row(def_row=True)
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
        self.blade_olpsta_chart = self.graph_template()
        self.blade_olpsta_chartview.setChart(self.blade_olpsta_chart)
        
        self.blade_olplen_chart = self.graph_template()
        self.blade_olplen_chartview.setChart(self.blade_olplen_chart)
        
        # Signals
        self.blade_skinolpsta_table.cellChanged.connect(lambda row, col:
            self.new_row_table(self.blade_skinolpsta_table, row, col))
        self.blade_skinolplen_table.cellChanged.connect(lambda row, col:
            self.new_row_table(self.blade_skinolplen_table, row, col))
        
        self.blade_order_input.valueChanged.connect(self.resize_blade_table)
        
        self.blade_interpolate_button.clicked.connect(self.interpolate_overlap)
        
        self.blade_saveparams_button.clicked.connect(self.save_bladeparams)
        
        # ---------------------------------------------------------------------
        # Page 4 (Skin)
        
        # Calculations
        self.timer_skin = QTimer()
        self.timer_skin.setSingleShot(True)
        self.timer_skin.timeout.connect(self.build_section)
        
        # Charts
        self.skin_zoom_chart = self.graph_template()
        self.skin_zoom_chartview.setChart(self.skin_zoom_chart)
        
        self.skin_full_chart = self.graph_template()
        self.skin_full_chartview.setChart(self.skin_full_chart)
        
        # Signals
        self.stackedWidget.currentChanged.connect(self.update_stabox)
        self.skin_liststations.currentTextChanged.connect(self.update_olptgt)
        
        self.skin_liststations.currentTextChanged.connect(self.secInputChanged)
        self.skin_nplies_input.textChanged.connect(self.secInputChanged)
        self.skin_plythickness_input.textChanged.connect(self.secInputChanged)
        self.skin_overlaptarget_input.textChanged.connect(self.secInputChanged)
        self.skin_tethickness_input.textChanged.connect(self.secInputChanged)
        self.skin_savefig_input.checkStateChanged.connect(self.secInputChanged)
        
        self.skin_saveSection_button.clicked.connect(self.saveSection)
        
        # ---------------------------------------------------------------------
        # Page 6 (EXPORT)
        self.stackedWidget.currentChanged.connect(self.update_sectionList)
        self.export_export_button.clicked.connect(self.exportSections)
        
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
            self.handle_msgbar(f'Airfoil NACA {airfoil_name} already exists.')
            raise ValueError('Airfoil already exists.')
        
        print(f'Creating airfoil: {airfoil_name}')
        
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
            self.handle_msgbar('No airfoil to save.')
            return
        
        self.db.airfoils[airfoil.name] = airfoil
        del self.edits['__airfoil__']
        
        # Update airfoil list (remove asterisk)
        items = [self.airfoil_listairfoils_widget.item(i).text() 
            for i in range(self.airfoil_listairfoils_widget.count())]
        index = items.index(f'{airfoil.family} {airfoil.profile}*')
        new_text = f'{airfoil.family} {airfoil.profile}'
        self.airfoil_listairfoils_widget.item(index).setText(new_text)
        
        # Print message
        self.handle_msgbar(f'Airfoil {airfoil.name} saved.')
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
        
        # # Clear the current series data and update with new values
        # series = QLineSeries()
        # for i in airfoil.xy:
        #     series.append(float(i[0]),float(i[1]))
        
        # # Create new chart
        # chart = QChart()
        # chart.setAnimationOptions(QChart.SeriesAnimations)
        # # chart.legend().hide()
        # chart.addSeries(series)
        
        # xy_range = np.array(airfoil.xy)
        
        # x_min = np.min(xy_range[:,0])
        # x_max = np.max(xy_range[:,0])
        # y_min = np.min(xy_range[:,1])
        # y_max = np.max(xy_range[:,1])
        
        # # Chord line
        # cl = QLineSeries()
        # cl.append(x_min, 0)
        # cl.append(x_max, 0)
        # chart.addSeries(cl)
        
        # # Legend
        # series.setName(airfoil_name)
        # cl.setName('Chord line')
        # cl.setColor(QColor(150,150,150))
        # cl.setPen(QPen(QBrush(QColor(150,150,150)), 2, Qt.DashLine))
        # chart.legend().setVisible(True)
        # chart.legend().setAlignment(Qt.AlignBottom)
        
        # chart.createDefaultAxes()
        # x_axis = chart.axes(Qt.Horizontal)[0]
        # y_axis = chart.axes(Qt.Vertical)[0]
        # x_axis.setTitleText('x/c [-]')
        # y_axis.setTitleText('y/c [-]')
        # x_axis.setTitleFont(QFont('Helvetica',14))
        # y_axis.setTitleFont(QFont('Helvetica',14))
        
        # self.airfoil_chartview.setChart(chart)
        # self.equal_axes(chart, [[x_min, x_max], [y_min, y_max]])
        
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
                            top=True, right=True, labelsize='x-large')
        self.airfoil_ax.grid(visible=True, which='major', linestyle='-', linewidth=0.75)
        self.airfoil_ax.set_aspect('equal', adjustable='datalim')
        self.airfoil_ax.legend(loc = 'best')
        
        self.canvas.draw_idle()
    
    def delete_airfoil(self):
        airfoil_name = self.airfoil_listairfoils_widget.currentItem().text()
        airfoil_id = airfoil_name.replace(' ','')
        
        if '*' in airfoil_id:
            self.handle_msgbar('Airfoil not saved yet.')
            return
        
        if airfoil_id in self.db.airfoils.keys():
            del self.db.airfoils[airfoil_id]
            self.handle_msgbar(f'Airfoil {airfoil_name} deleted.')
            
            # Update airfoil list
            items = [self.airfoil_listairfoils_widget.item(i).text() 
                for i in range(self.airfoil_listairfoils_widget.count())]
            index = items.index(airfoil_name)
            self.airfoil_listairfoils_widget.takeItem(index)
            
            # Clear chart
            # empty_chart = self.graph_template()
            # self.airfoil_chartview.setChart(empty_chart)
        else:
            self.handle_msgbar('Airfoil not found in database.')
    
    ### STATION METHODS (Page 2a)
    
    def update_airfoil_chart(self):
        
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
            data = Station(
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
                # path=self.paths_airfoils[airfoil_selected],
            )
            
            # Clear the current series data and update with new values
            airfoil_series = QLineSeries()
            for i in data.xy:
                airfoil_series.append(float(i[0]),float(i[1]))
            
            # Draw scatter points TE and LE
            scatter_series = QScatterSeries()
            if airfoil_selected == 'circle':
                scatter_series.append(float(data.xy[0][0]), float(data.xy[0][1]))
            idx_LE:int = int(len(data.xy)/2)
            scatter_series.append(float(data.xy[idx_LE][0]), float(data.xy[idx_LE][1]))
            scatter_series.setMarkerShape(QScatterSeries.MarkerShapeRectangle)
            scatter_series.setMarkerSize(10)
            
            # Create new chart
            chart = QChart()
            chart.setAnimationOptions(QChart.SeriesAnimations)
            chart.legend().hide()
            chart.addSeries(airfoil_series)
            chart.addSeries(scatter_series)
            
            x_axis = QValueAxis()
            y_axis = QValueAxis()
            aspect_ratio = QSizeF(16,9)
            
            xy_range = data.xyRange()
            # print(xy_range)
            x_min, x_max = xy_range[0]
            y_min, y_max = xy_range[1]
            
            dx = x_max - x_min
            dy = y_max - y_min
            # print(f'dx: {dx}, dy: {dy}')
            
            aspect_ratio.scale(dx,dy,Qt.KeepAspectRatioByExpanding)
            # print(f'Scaled aspect ratio: {aspect_ratio}')
            
            height = aspect_ratio.height()
            width = aspect_ratio.width()
            # print(f'height: {height}, width: {width}')
            
            x_mid = (x_min + x_max) / 2
            y_mid = (y_min + y_max) / 2
            
            new_x_min = x_mid - width * 0.5 * 1.1
            new_x_max = x_mid + width * 0.5 * 1.1
            
            new_y_min = y_mid - height * 0.5 * 1.1
            new_y_max = y_mid + height * 0.5 * 1.1
            
            x_axis.setRange(new_x_min, new_x_max)
            y_axis.setRange(new_y_min, new_y_max)
            
            chart.addAxis(x_axis, Qt.AlignBottom)
            chart.addAxis(y_axis, Qt.AlignLeft)
            airfoil_series.attachAxis(x_axis)
            airfoil_series.attachAxis(y_axis)
            scatter_series.attachAxis(x_axis)
            scatter_series.attachAxis(y_axis)

            self.station_chartview.setChart(chart)
            
            # Store it as an unsaved station
            self.edits['__station__'] = data
            
        except ValueError:
            self.handle_msgbar('Station: Wrong input')
    
    
    def save_station(self):
        station = self.edits['__station__']
        station_name  = 'sta_' + str(int(station.parameters['offset'][2]))
        self.db.stations[station_name] = station
        self.handle_msgbar(f'Station {station_name} saved.')
        n_stations = len(self.db.stations.keys())
        sorted_stations = sorted(list(self.db.stations.keys()), key=len)
        # self.handle_msgbar(f'Number of stations: {n_stations}')
        self.station_liststation_box.clear()
        self.station_liststation_box.insertItems(0,sorted_stations)
        self.station_liststation_box.setCurrentText(station_name)
        # print(self.station_liststation_box.currentIndex())
    
    ### ADVANCED TAB METHODS (Page 2b)
    
    def stations_insert_row(
        self,
        airfoil: str | None = None,
        def_row: bool = False,
        data_row: list | None = None,
        xmirror: bool = False,
        ymirror: bool = True,
        ):
        
        t = self.station_tableStations_input
        if def_row:
            n_rows = 0
        else:
            n_rows = t.rowCount()
            t.insertRow(n_rows)
        
        # Column 0: Airfoil
        c0 = QComboBox()
        c0.addItems(list(self.db.airfoils.keys()))
        if airfoil in list(self.db.airfoils.keys()):
            c0.setCurrentText(airfoil)
        else: c0.setCurrentIndex(0)
        t.setCellWidget(n_rows, 0, c0)
        
        # Column 1-8: Numeric items
        num_default = data_row if data_row else [1., 0., 0., 0., 0., 1., 1., 1.]
        for c, val in enumerate(num_default, start=1):
            t.setItem(n_rows, c, NumericItem(f"{val:.6g}"))
            
        # Column 9-10: Checkboxes
        x_mir = QCheckBox()
        x_mir.setChecked(xmirror)
        y_mir = QCheckBox()
        y_mir.setChecked(ymirror)
        t.setCellWidget(n_rows, 9, x_mir)
        t.setCellWidget(n_rows, 10, y_mir)
    
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
            self.handle_msgbar(f"Failed to read file: {e}")
            return
        
        # Clean station table and stations in session
        t = self.station_tableStations_input
        t.setSortingEnabled(False)
        t.clearContents()
        t.setRowCount(0)
        t.setSortingEnabled(True)
        self.db.cleanStations()
        
        # Populate station table
        rows, _ = df.shape
        for r in range(rows):
            self.stations_insert_row(
                airfoil=df.iloc[r]['airfoil'],
                def_row=False,
                data_row=df.iloc[r].tolist()[1:-2],
                xmirror=df.iloc[r]['mirror_x'],
                ymirror=df.iloc[r]['mirror_y'],
            )
        
        self.station_nStationsAdv_input.setValue(rows)
        self.handle_msgbar(f'File imported succesfully: {filepath}')
    
    def update_stations_table(self, value):
        n_rows = self.station_tableStations_input.rowCount()
        
        if value > n_rows:
            self.stations_insert_row()
            
        elif value < n_rows:
            self.station_tableStations_input.removeRow(value)
        
    def save_multiple_stations(self):
        n_rows = self.station_tableStations_input.rowCount()
        n_cols = self.station_tableStations_input.columnCount()
        sta_data = {}
        for row in range(n_rows):
            for col in range(n_cols):
                if col < 1:
                    sta_data[col] = self.station_tableStations_input.cellWidget(row, col).currentText()
                elif col > 0 and col < 9:
                    sta_data[col] = self.station_tableStations_input.item(row, col).text()
                else:
                    sta_data[col] = self.station_tableStations_input.cellWidget(row, col).isChecked()
            
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
            
            self.db.stations[station_name] = station
            
        self.handle_msgbar(f'Total stations created: {n_rows}.')
    
    ### PARAMETERS METHODS (Page 3)
    
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
        
        # OLP_STA
        data = []
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
            
        order = int(self.blade_order_input.text())
        
        y_target, tck = norm_olp(coords=coords, x_target=x_target, order=order)
        
        # Update graphs
        line_series = [QLineSeries() for x in range(len(y_target))]
        scatter_series = [QScatterSeries() for x in range(len(y_target))]
        x_line = np.linspace(x_target[0],x_target[-1],100)
        y_line = [splev(x_line, x) for x in tck]
        
        xy_line = [list(zip(x_line,y)) for y in y_line]
        xy_pts = [list(zip(x_target,y)) for y in y_target]
        
        # save in temporary database
        self.edits['__olp_sta__'] = np.array(xy_pts)
        
        # Add points to series
        for i in range(len(xy_line)):
            for j in xy_line[i]:
                line_series[i].append(float(j[0]), float(j[1]))
                
        for i in range(len(xy_pts)):
            for j in xy_pts[i]:
                scatter_series[i].append(float(j[0]), float(j[1]))
        
        # Add series to the chart
        self.blade_olpsta_chart.removeAllSeries()
        
        for i in line_series:
            self.blade_olpsta_chart.addSeries(i)
        
        for i in scatter_series:
            i.setMarkerShape(QScatterSeries.MarkerShapeRectangle)
            i.setMarkerSize(10)
            self.blade_olpsta_chart.addSeries(i)
            
        self.blade_olpsta_chart.createDefaultAxes()
        self.blade_olpsta_chart.zoom(0.9)
        
        # OLP_LEN
        data = []
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
        
        # Update graphs
        series = [QLineSeries() for x in range(len(y_target))]
        points = [QScatterSeries() for x in range(len(y_target))]
        
        x_plot = np.linspace(x_target[0],x_target[-1],100)
        y_plot = [splev(x_plot, x) for x in tck]
        
        xy = [list(zip(x_plot,y)) for y in y_plot]
        xy_pts = [list(zip(x_target,y)) for y in y_target]
        
        # save in temporary database
        self.edits['__olp_len__'] = xy
        
        for i in range(len(xy)):
            for j in xy[i]:
                series[i].append(float(j[0]), float(j[1]))
                
        for i in range(len(xy)):
            for j in xy_pts[i]:
                points[i].append(float(j[0]), float(j[1]))
        
        self.blade_olplen_chart.removeAllSeries()
        for i in series:
            self.blade_olplen_chart.addSeries(i)
            
        for i in points:
            i.setMarkerShape(QScatterSeries.MarkerShapeRectangle)
            i.setMarkerSize(10)
            self.blade_olplen_chart.addSeries(i)
            
        self.blade_olplen_chart.createDefaultAxes()
        self.blade_olplen_chart.zoom(0.9)
        
        # Update QComboBox with order selection
        self.blade_skinolpsta_selected.clear()
        self.blade_skinolpsta_selected.addItems([str(x+1) for x in range(order)])
        
        self.blade_skinolplen_selected.clear()
        self.blade_skinolplen_selected.addItems([str(x+1) for x in range(order)])
    
    def save_bladeparams(self):
        idx_olp_sta = self.blade_skinolpsta_selected.currentIndex()
        idx_olp_len = self.blade_skinolplen_selected.currentIndex()
        
        self.db.blade['olp_sta'] = self.edits['__olp_sta__'][idx_olp_sta]
        # print(self.db.blade['olp_sta'])
        self.db.blade['olp_len'] = self.edits['__olp_len__'][idx_olp_len]
        # print(self.db.blade['olp_len'])
        
        self.handle_msgbar(f'Parameters saved.')
    
    ### SKIN METHODS
    
    def update_stabox(self):
        if self.stackedWidget.currentIndex() == 4:
            names_stations = list(self.db.stations.keys())
            self.skin_liststations.clear()
            self.skin_liststations.addItems(names_stations)
        
    def update_olptgt(self):
        olp_sta = self.db.blade['olp_sta']
        n_station = float(self.skin_liststations.currentText()[4:])
        
        try:
            norm_olp_tgt = float(olp_sta[np.where(olp_sta[:,0]==n_station)[0],1][0])
            station = self.db.stations[self.skin_liststations.currentText()]
            olp_target = norm_olp_tgt*station.parameters['chord']
            self.skin_overlaptarget_input.setText(str(olp_target))
            
        except ValueError:
            self.handle_msgbar('Error: Overlap target could not be interpolated.')
    
    def build_section(self):
        if self.stackedWidget.currentIndex() == 4:
            try:
                station = self.db.stations[self.skin_liststations.currentText()] if self.skin_liststations.currentText() != '' else None
                n_plies = int(self.skin_nplies_input.text()) if self.skin_nplies_input.text() else 1
                ply_thk = float(self.skin_plythickness_input.text()) if self.skin_plythickness_input.text() else 1
                olp_tgt = float(self.skin_overlaptarget_input.text()) if self.skin_overlaptarget_input.text() else 10
                te_thkn = float(self.skin_tethickness_input.text()) if self.skin_tethickness_input.text() else n_plies*ply_thk
                saveFig = self.skin_savefig_input.isChecked()
                
                data = Section(station = station,
                            n_plies = n_plies,
                            ply_thickness = ply_thk,
                            overlap_target = olp_tgt,
                            te_thickness = te_thkn,
                            saveFig = saveFig,
                            )
                print('Section generated.')
                
                # Generate colours
                colours = self.generate_colours(num_curves=n_plies, cmap_name='viridis')
                
                # Plots
                plies = list(data.t['bot_plies'].keys())
                ply_series = {}
                for i in (plies):
                    ply = data.t['bot_plies'][i]
                    ply_series[i] = {x:QLineSeries() for x in list(ply.keys())}
                
                    for j in list(ply.keys()):
                        x = data.splines[j]['x'](ply[j]).tolist()
                        y = data.splines[j]['y'](ply[j]).tolist()
                        xy = list(zip(x,y))
                        points = [QPointF(float(x), float(y)) for x, y in xy]
                        ply_series[i][j].append(points)
                        # ply_series[i][j].setName(f'Curve {j}')
                        ply_series[i][j].setColor(colours[i-1])
                
                # Full graph
                chart = QChart()
                chart.setAnimationOptions(QChart.SeriesAnimations)
                for i in list(ply_series.keys()):
                    for j in list(ply_series[i].keys()):
                        chart.addSeries(ply_series[i][j])
                chart.createDefaultAxes()
                
                x_axis = chart.axes(Qt.Horizontal)[0]
                y_axis = chart.axes(Qt.Vertical)[0]
                x_axis.setTitleText('x [d]')
                y_axis.setTitleText('y [d]')
                x_axis.setTitleFont(QFont('Helvetica',14))
                y_axis.setTitleFont(QFont('Helvetica',14))
                self.skin_full_chartview.setChart(chart)
                self.equal_axes(chart, station.xyRange())
                
                # Zoomed graph     
                x = [
                    data.points['bot_1'][1][2]['x'][0],
                    data.points['top_1'][1][3]['x'][0],
                ]
                
                y = [
                    data.points['bot_1'][1][2]['y'][0],
                    data.points['top_1'][1][3]['y'][0],
                ]
                
                x.sort()
                y.sort()
                print(f'x: {x}\n y: {y}')
                
                # Temporary save
                self.edits['__section__'] = data
                self.handle_msgbar(f'Number of curves: {len(data.splines.keys())}')
            
            except NameError:
                print('Skin section: Error - Wrong input.')
                
    def saveSection(self):
        section_name = f'sec_{int(self.edits['__section__'].parameters['z'])}'
        self.db.sections[section_name] = self.edits['__section__']
        self.handle_msgbar(f'Section "{section_name}" saved.')
    
    ### ABAQUS EXPORT METHODS
    
    def update_sectionList(self):
        if self.stackedWidget.currentIndex() == 6:
            self.export_sectionsList.clear()
            list_sections = list(self.db.sections.keys())
            self.export_sectionsList.insertItems(0,list_sections)
            
    def exportSections(self):
        if len(self.export_sectionsList.selectedItems()) > 0:
            items = self.export_sectionsList.selectedItems()
            dict_sections = {int(sec.text()[4:]):skinSection(self.db.sections[sec.text()]) for sec in items}
            filename = f'{self.export_expFileName_input.text()}'
            skinPart(sections=dict_sections, filename=filename)
            
            self.handle_msgbar(f'File "{filename}.json" exported succesfully.')
        else:
            self.handle_msgbar('No sections selected.')
    
    ### GENERAL UI METHODS
    
    def load_default_airfoils(self):
        
        self.paths_airfoils = {}
        for i in [x for x in os.listdir(resource_path('edfoil/airfoils'))]:
            airfoil_path = resource_path(f'edfoil/airfoils/{i}')
            airfoil = Airfoil()
            airfoil.importCoords(airfoil_path)
            self.db.airfoils[airfoil.name] = airfoil
            # TODO: Get rid of path airfoils
            self.paths_airfoils[airfoil.name] = airfoil_path
            
            # Debug
            # print(list(self.db.airfoils.keys()))
        
        names = [f'{x.family} {x.profile}' for x in self.db.airfoils.values()]
        self.airfoil_listairfoils_widget.clear()
        self.airfoil_listairfoils_widget.addItems(names)
    
    # def airfoil_mousecoords(self, event: QMouseEvent) -> None:
    #     # coords = event.position()
    #     # x,y = coords.x(), coords.y()
    #     # coord_lims = self.airfoil_chart.plotArea().getCoords()
        
    #     # if (x >= coord_lims[0] and x <= coord_lims[2] and
    #     #     y >= coord_lims[1] and y <= coord_lims[3]):
            
    #     #     coords_scaled = self.airfoil_chart.mapToValue(coords)
    #     #     x_scaled = coords_scaled.x()
    #     #     y_scaled = coords_scaled.y()
            
    #     #     self.airfoil_xy_current.setText(f'({x_scaled:.2f}, {y_scaled:.2f})')
        
    #     chart = self.airfoil_chartview.chart()
    #     if chart is None or not chart.series():
    #         return
          
    #     series = chart.series()[0]  # or find the one you want
    #     pos = event.position()      # QChartView coords

    #     # Map to data using the series-aware overload
    #     value_pt = chart.mapToValue(pos, series)

    #     # Check that the mapped point is inside the plotArea by re-mapping back
    #     back = chart.mapToPosition(value_pt, series)  # chart coords
    #     if chart.plotArea().contains(back):
    #         self.airfoil_xy_current.setText(f'({value_pt.x():.2f}, {value_pt.y():.2f})')
    #     else:
    #         # Optional: clear or ignore when outside
    #         pass
            
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
        dialog.setNameFilter(self.tr('Tblade (*.tbd *.json)'))
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec():
            filepath = dialog.selectedFiles() # [0]
            # TODO: decode tbd or json file into db class dictionary.
            
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
        
    def switch_to_stationPage(self):
        self.stackedWidget.setCurrentIndex(2)
        self.page_title_label.setText(self.station_page_button.text())
        
        # Update airfoil list in station page
        names_airfoils = list(self.db.airfoils.keys())
        self.station_listairfoils_box.clear()
        self.station_listairfoils_box.addItems(names_airfoils)
        
        # Update dropwn menu in advanced tab
        n_rows = self.station_tableStations_input.rowCount()
        for row in range(n_rows):
            list_airfoils = QComboBox()
            list_airfoils.addItems(list(self.db.airfoils.keys()))
            self.station_tableStations_input.setCellWidget(row,0,list_airfoils)
        
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
        self.stackedWidget.setCurrentIndex(6)
        self.page_title_label.setText(self.export_page_button.text())
    
    def upload_airfoil_file(self):
        # TODO: Update this to not clash with Airfoil Creator Tab
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setNameFilter(self.tr('Files (*.csv *.txt)'))
        dialog.setViewMode(QFileDialog.Detail)
        fileNames = []
        if dialog.exec():
            fileNames = dialog.selectedFiles()
        
        # Add new files to the QComboBox
        airfoil_names = [x.split('/')[-1][:-4] for x in fileNames]
        n_items_current = self.station_listairfoils_box.count()
        self.station_listairfoils_box.insertItems(n_items_current, airfoil_names)
        
        for i in range(len(fileNames)):
            self.paths_airfoils[airfoil_names[i]] = fileNames[i]
    
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
        dialog.setNameFilter(self.tr('TBlade (*.tbd)'))
        dialog.setViewMode(QFileDialog.List)
        dialog.setDefaultSuffix('tbd')
        
        file_path, _ = QFileDialog.getSaveFileName(self, self.tr('Save File'),
            self.main_path, 'TBlade Files (*.tbd);;All Files (*)', 
            options=QFileDialog.Options())
        
        # TODO: encode db class dictionary into tbd file.
        if file_path:
            self.database_file(file_path,'Hello')
            
    def info_message(self):
        msgBox = QMessageBox()
        about_text = 'This open source software, has been developed in ' \
        'the School of Engineering, in the University of Edinburgh.\n\n' \
        'The current version is version 0.2'
        
        msgBox.about(self, 'About EdFoil', about_text)
    
    ### MESSAGE BAR METHODS
    
    def handle_msgbar(self, message:str, time:int=4000):
        if message:
            self.timer_msg.start(time)
            self.def_msgbar.hide()
            self.msgbar.setText(message)
            self.msgbar.show()
            
    def show_def_msg(self):
            self.def_msgbar.show()
            self.msgbar.hide()
        

# Main database in every session.       
class session():
    def __init__(self):
        self.airfoils = {}
        self.stations = {}
        self.sections = {}
        self.skin = {}
        self.blade = {}
    
    def cleanStations(self):
        self.stations = {}

# For turning string inputs to floats inside QTableWidget instances
class NumericItem(QTableWidgetItem):
    def __lt__(self, other):
        try:
            return float(self.text()) < float(other.text())
        except ValueError:
            return super().__lt__(other)