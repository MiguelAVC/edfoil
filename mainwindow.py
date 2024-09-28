from ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import (QMainWindow, QFileDialog, QMessageBox, 
                               QCheckBox, QComboBox, QTableWidgetItem)
from PySide6.QtCharts import (QChart, QLineSeries, QChartView, QCategoryAxis,
                              QValueAxis, QScatterSeries, QAreaSeries)
from PySide6.QtGui import QPainter, QFont, QPen, QBrush, QColor, Qt, QMouseEvent
from PySide6.QtCore import QTimer, Qt, QDir, QPointF


from classes.station import Station
from classes.section import Section
from utils.bladeparams import norm_olp
from utils.abaqusExp import *

import os
import numpy as np
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
        self.setWindowTitle('TDesigner')
        
        # Messagebar
        self.timer_msg = QTimer(parent=self)
        self.timer_msg.setSingleShot(True)
        
        # Project start
        self.db = db()
        self.edits = {}
        self.handle_msgbar(message='New database created.')
        
        # Tab switching
        self.home_page_button.clicked.connect(self.switch_to_homePage)
        self.airfoil_page_button.clicked.connect(self.switch_to_airfoilPage)
        self.station_page_button.clicked.connect(self.switch_to_stationPage)
        self.blade_page_button.clicked.connect(self.switch_to_bladePage)
        self.skin_page_button.clicked.connect(self.switch_to_skinPage)
        self.spar_page_button.clicked.connect(self.switch_to_sparPage)
        self.abaqus_page_button.clicked.connect(self.switch_to_abaqusPage)
        
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
        
        self.airfoil_chart = self.graph_template('Airfoil Plot')
        self.airfoil_chartview.setChart(self.airfoil_chart)
        self.airfoil_chartview.mouseMoveEvent = self.airfoil_mousecoords
        
        # ---------------------------------------------------------------------
        # Page 2 (Station Generator)
        
        # Timer for debouncing text input changes
        self.timer_station = QTimer()
        self.timer_station.setSingleShot(True)
        self.timer_station.timeout.connect(self.update_airfoil_chart)
        
        # Initial airfoil list (from 'airfoils' folder)
        self.paths_airfoils = {}
        for i in [x for x in os.listdir('./airfoils')]:
            self.db.airfoils[i[:-4]] = np.genfromtxt(f'./airfoils/{i}')
            self.paths_airfoils[i[:-4]] = f'./airfoils/{i}'
        self.station_listairfoils_box.addItems(list(self.db.airfoils.keys()))
        
        # Upload additional airfoils
        self.station_uploadairfoil_button.clicked.connect(self.upload_airfoil_file)
        
        # Main chart
        self.station_chart = self.graph_template('Station Plot')
        self.station_chartview.setChart(self.station_chart)
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
        # Default values
        list_airfoils_advanced = QComboBox()
        list_airfoils_advanced.addItems(list(self.db.airfoils.keys()))
        self.station_tableStations_input.setCellWidget(0,0,list_airfoils_advanced)
        
        xmirror_airfoils_advanced = QCheckBox()
        xmirror_airfoils_advanced.setCheckable(True)
        self.station_tableStations_input.setCellWidget(0,9,xmirror_airfoils_advanced)
        
        ymirror_airfoils_advanced = QCheckBox()
        ymirror_airfoils_advanced.setCheckable(True)
        ymirror_airfoils_advanced.setChecked(True)
        self.station_tableStations_input.setCellWidget(0,10,ymirror_airfoils_advanced)
        
        self.list_airfoils_advanced_default = [1.,0.,0.,0.,0.,1.,1.,1.]
        self.station_tableStations_input.setSortingEnabled(False)
        for column in range(len(self.list_airfoils_advanced_default)):
            text_cell = QTableWidgetItem(str(self.list_airfoils_advanced_default[column]))
            self.station_tableStations_input.setItem(0,column+1,text_cell)
        self.station_tableStations_input.setSortingEnabled(True)
        
        # Signals
        self.station_nStationsAdv_input.valueChanged.connect(self.update_stations_table)
        self.station_sortTable_button.clicked.connect(self.sort_advanced_stations_table)
        self.station_saveTable_button.clicked.connect(self.save_multiple_stations)
        
        # ---------------------------------------------------------------------
        # Page 3 (Blade Parameters)
        
        # Charts
        self.blade_olpsta_chart = self.graph_template('Skin Overlap Start Interpolation')
        self.blade_olpsta_chartview.setChart(self.blade_olpsta_chart)
        
        self.blade_olplen_chart = self.graph_template('Skin Overlap Length Interpolation')
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
        self.skin_zoom_chart = self.graph_template('Trailing Edge')
        self.skin_zoom_chartview.setChart(self.skin_zoom_chart)
        
        self.skin_full_chart = self.graph_template('Skin Section')
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
        # Page 6 (ABAQUS EXPORT)
        self.stackedWidget.currentChanged.connect(self.update_sectionList)
        self.abaqus_export_button.clicked.connect(self.exportSections)
        
        
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
        if len(x_target) == 0:
            x_target, _ = zip(*coords)
            
        order = int(self.blade_order_input.text())
        
        y_target, tck = norm_olp(coords=coords, x_target=x_target, order=order)
        
        # Update graphs
        line_series = [QLineSeries() for x in range(len(y_target))]
        scatter_series = [QScatterSeries() for x in range(len(y_target))]
        x_line = np.linspace(coords[0][0],coords[-1][0],100)
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
        if len(x_target) == 0 :
            x_target, _ = zip(*coords)
        
        y_target, tck = norm_olp(coords=coords, x_target=x_target, order=order)
        
        # Update graphs
        series = [QLineSeries() for x in range(len(y_target))]
        x_plot = np.linspace(x_target[0],x_target[-1],100)
        y_plot = [splev(x_plot, x) for x in tck]
        
        xy = []
        for i in y_plot:
            xy.append(list(zip(x_plot,i)))
        # save in temporary database
        self.edits['__olp_len__'] = xy
        
        for i in range(len(xy)):
            for j in xy[i]:
                series[i].append(float(j[0]), float(j[1]))
        
        self.blade_olplen_chart.removeAllSeries()
        for i in series:
            self.blade_olplen_chart.addSeries(i)
        self.blade_olplen_chart.createDefaultAxes()
        self.blade_olplen_chart.zoom(0.9)
        
        # Update QComboBox with order selection
        self.blade_skinolpsta_selected.clear()
        self.blade_skinolpsta_selected.addItems([str(x+1) for x in range(order)])
        
        self.blade_skinolplen_selected.clear()
        self.blade_skinolplen_selected.addItems([str(x+1) for x in range(order)])
    
    ### ADVANCED TAB METHODS (Page 2b)
    def sort_advanced_stations_table(self):
        self.station_tableStations_input.sortItems(5)
    
    
    def update_stations_table(self, value):
        n_rows = self.station_tableStations_input.rowCount()
        # Make first column have a dropdown menu for airfoil
        list_airfoils = QComboBox()
        list_airfoils.addItems(list(self.db.airfoils.keys()))
        xmirror = QCheckBox()
        xmirror.setCheckable(True)
        ymirror = QCheckBox()
        ymirror.setCheckable(True)
        ymirror.setChecked(True)
        
        if value > n_rows:
            self.station_tableStations_input.insertRow(n_rows)
            self.station_tableStations_input.setCellWidget(n_rows,0,list_airfoils)
            self.station_tableStations_input.setCellWidget(n_rows,9,xmirror)
            self.station_tableStations_input.setCellWidget(n_rows,10,ymirror)
            
            for column in range(1,9):
                cell_item = self.station_tableStations_input.item(n_rows-1,column)
                new_cell = QTableWidgetItem(cell_item.text())
                self.station_tableStations_input.setItem(n_rows,column,new_cell)
            
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
            
            station = Station(chord=float(sta_data[1]),
                              twist_angle=float(sta_data[2]),
                              x_offset=float(sta_data[3]),
                              y_offset=float(sta_data[4]),
                              z_offset=float(sta_data[5]),
                              x_multiplier=float(sta_data[6]),
                              y_multiplier=float(sta_data[7]),
                              z_multiplier=float(sta_data[8]),
                              x_mirror=bool(sta_data[9]),
                              y_mirror=bool(sta_data[10]),
                              path=self.paths_airfoils[sta_data[0]])
            
            station_name = f'sta_{int(sta_data[5])}'
            
            self.db.stations[station_name] = station
            
        self.handle_msgbar(f'Total stations created: {n_rows}.')
    
    ### PARAMETERS METHODS (Page 3)
    
    def save_bladeparams(self):
        idx_olp_sta = self.blade_skinolpsta_selected.currentIndex()
        idx_olp_len = self.blade_skinolplen_selected.currentIndex()
        
        self.db.blade['olp_sta'] = self.edits['__olp_sta__'][idx_olp_sta]
        print(self.db.blade['olp_sta'])
        self.db.blade['olp_len'] = self.edits['__olp_len__'][idx_olp_len]
        
        self.handle_msgbar(f'Parameters saved.')
    
    def airfoil_mousecoords(self, event: QMouseEvent) -> str:
        coords = event.position()
        x,y = coords.x(), coords.y()
        coord_lims = self.airfoil_chart.plotArea().getCoords()
        
        if (x >= coord_lims[0] and x <= coord_lims[2] and
            y >= coord_lims[1] and y <= coord_lims[3]):
            
            coords_scaled = self.airfoil_chart.mapToValue(coords)
            x_scaled = coords_scaled.x()
            y_scaled = coords_scaled.y()
            
            self.airfoil_xy_current.setText(f'({x_scaled:.2f}, {y_scaled:.2f})')
            
    def station_mousecoords(self, event: QMouseEvent) -> str:
        coords = event.position()
        x,y = coords.x(), coords.y()
        coord_lims = self.station_chart.plotArea().getCoords()
        
        if (x >= coord_lims[0] and x <= coord_lims[2] and
            y >= coord_lims[1] and y <= coord_lims[3]):
            
            coords_scaled = self.station_chart.mapToValue(coords)
            x_scaled = coords_scaled.x()
            y_scaled = coords_scaled.y()
            
            self.station_xy_current.setText(f'({x_scaled:.2f}, {y_scaled:.2f})')
    
    def graph_template(self,title:str):
        """Empty graph template.

        Args:
            title (str): Plot title.

        Returns:
            chart: Chart Object.
        """
        data = QLineSeries()
        chart = QChart()
        chart.setAnimationOptions(QChart.AllAnimations)
        chart.legend().hide()
        chart.addSeries(data)
        chart.setTitle(title)
        
        # chart.createDefaultAxes()
        axisX = QValueAxis()
        axisY = QValueAxis()
        axisX.setTitleText('x [-]')
        axisY.setTitleText('y [-]')
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        # chart.setLocalizeNumbers(True)
        data.attachAxis(axisX)
        data.attachAxis(axisY)
        
        return chart
    
    def change_work_directory(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setViewMode(QFileDialog.List)
        if dialog.exec():
            self.main_path = dialog.selectedFiles()[0]
            self.workpath_lineedit.setText(self.main_path)
        
    def load_db(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter(self.tr('Tblade (*.tbd *.json)'))
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec():
            filepath = dialog.selectedFiles() # [0]
            # TODO: decode tbd or json file into db class dictionary.
            
    def new_db(self):
        self.db = db()
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
        
    def switch_to_bladePage(self):
        self.stackedWidget.setCurrentIndex(3)
        self.page_title_label.setText(self.blade_page_button.text())
        
    def switch_to_skinPage(self):
        self.stackedWidget.setCurrentIndex(4)
        self.page_title_label.setText(self.skin_page_button.text())
    
    def switch_to_sparPage(self):
        self.stackedWidget.setCurrentIndex(5)
        self.page_title_label.setText(self.spar_page_button.text())
    
    def switch_to_abaqusPage(self):
        self.stackedWidget.setCurrentIndex(6)
        self.page_title_label.setText(self.abaqus_page_button.text())
    
    def upload_airfoil_file(self):
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
            data = Station(chord=chord_length,
                           twist_angle=twist_angle,
                           x_offset=x_offset,
                           y_offset=y_offset,
                           z_offset=z_offset,
                           x_multiplier=x_multiplier,
                           y_multiplier=y_multiplier,
                           z_multiplier=z_multiplier,
                           path=self.paths_airfoils[airfoil_selected],
                           x_mirror=x_mirror,
                           y_mirror=y_mirror)
            
            # Clear the current series data and update with new values
            self.airfoil_series = QLineSeries()
            for i in data.xy:
                self.airfoil_series.append(float(i[0]),float(i[1]))
            
            # Draw scatter points TE and LE
            scatter_series = QScatterSeries()
            if airfoil_selected == 'circle':
                scatter_series.append(float(data.xy[0][0]), float(data.xy[0][1]))
            idx_LE:int = int(len(data.xy)/2)
            scatter_series.append(float(data.xy[idx_LE][0]), float(data.xy[idx_LE][1]))
            scatter_series.setMarkerShape(QScatterSeries.MarkerShapeRectangle)
            scatter_series.setMarkerSize(10)
            
            # Update axes to fit new data
            self.station_chart.removeAllSeries()
            self.station_chart.addSeries(self.airfoil_series)
            self.station_chart.addSeries(scatter_series)
            self.station_chart.createDefaultAxes()
            self.station_chart.zoom(0.9)
            
            # Store it as an unsaved station
            self.edits['__station__'] = data
            
        except ValueError:
            self.handle_msgbar('Station: Wrong input')
    
    
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
                print('section generated')
                # Plots
                plies = list(data.t['t_plies_bot'].keys())
                ply = data.t['t_plies_bot'][1]
                series = {x:QLineSeries() for x in list(ply.keys())}
                
                for j in list(ply.keys()):
                    x = data.splines[j]['x'](ply[j]).tolist()
                    y = data.splines[j]['y'](ply[j]).tolist()
                    xy = list(zip(x,y))
                    points = [QPointF(float(x), float(y)) for x, y in xy]
                    series[j].append(points)
                    series[j].setName(f'Curve {j}')
                
                # series = QAreaSeries(series_1,series_0)
                
                self.skin_full_chart.removeAllSeries()
                for j in series:
                    self.skin_full_chart.addSeries(series[j])
                self.skin_full_chart.createDefaultAxes()
                self.skin_full_chart.legend().show()
                self.skin_full_chart.zoom(0.9)
                
                self.handle_msgbar(f'Number of curves: {len(data.splines.keys())}')
                
                # Temporary save
                self.edits['__section__'] = data
                
            # except ValueError:
            #     self.handle_msgbar('Skin section: Wrong input')
            
            except NameError:
                print('Skin section: Error - Wrong input.')
                
    def saveSection(self):
        section_name = f'sec_{int(self.edits['__section__'].parameters['z'])}'
        self.db.sections[section_name] = self.edits['__section__']
        self.handle_msgbar(f'Section "{section_name}" saved.')
    
    ### ABAQUS EXPORT METHODS
    
    def update_sectionList(self):
        if self.stackedWidget.currentIndex() == 6:
            self.abaqus_sectionsList.clear()
            list_sections = list(self.db.sections.keys())
            self.abaqus_sectionsList.insertItems(0,list_sections)
            
    def exportSections(self):
        if len(self.abaqus_sectionsList.selectedItems()) > 0:
            items = self.abaqus_sectionsList.selectedItems()
            dict_sections = {int(sec.text()[4:]):skinSection(self.db.sections[sec.text()]) for sec in items}
            filename = f'{self.abaqus_expFileName_input.text()}'
            skinPart(sections=dict_sections, filename=filename)
            
            self.handle_msgbar(f'File "{filename}.json" exported succesfully.')
        else:
            self.handle_msgbar('No sections selected.')
    
    ### GENERAL UI METHODS
    
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
            QMessageBox.Information(self, 'Success', f'File saved successfully: {file_path}')
        
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
        
        if file_path:
            self.database_file(file_path,'Hello')
            
    def info_message(self):
        msgBox = QMessageBox()
        about_text = 'This open source software, has been developed in ' \
        'the School of Engineering, in the University of Edinburgh.\n\n' \
        'The current version is version 0.1'
        
        #TODO: Need to add Software Icon
        msgBox.about(self, 'About TBlade Designer', about_text)
    
    ### MESSAGE BAR METHODS
    
    def handle_msgbar(self, message:str, time:int=4000):
        if message:
            self.timer_msg.start(time)
            self.def_msgbar.hide()
            self.msgbar.setText(message)
            self.msgbar.show()
            self.timer_msg.timeout.connect(self.show_def_msg)
            
    def show_def_msg(self):
            self.def_msgbar.show()
            self.msgbar.hide()
        
        
class db():
    def __init__(self):
        self.airfoils = {}
        self.stations = {}
        self.sections = {}
        self.skin = {}
        self.blade = {}
        