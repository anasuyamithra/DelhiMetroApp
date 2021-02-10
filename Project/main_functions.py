## ==> GUI FILE
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.patches as mpatches
import pyqtgraph as pg 
import networkx as nx
from main import *
from back import *

import os
i = 0
class UIFunctions(MainWindow):
    def toggleMenu(self, maxWidth, enable):
        if enable:
            
            # Get Width
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # Set MaxWidth
            if width == 70:
                widthExtended = maxExtend
                self.ui.btn_toggle.clicked.connect(lambda: self.ui.Btn_page_1.setText(""))
                self.ui.btn_toggle.clicked.connect(lambda: self.ui.Btn_page_2.setText(""))
                self.ui.btn_toggle.clicked.connect(lambda: self.ui.Btn_page_3.setText(""))
            else:
                widthExtended = standard
                self.ui.btn_toggle.clicked.connect(lambda: self.ui.Btn_page_1.setText("Station Select"))
                self.ui.btn_toggle.clicked.connect(lambda: self.ui.Btn_page_2.setText("Metro Map"))
                self.ui.btn_toggle.clicked.connect(lambda: self.ui.Btn_page_3.setText("Comparing Djistra"))

            # Animation
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()
    
    def addTexttocomboBox(self):
        filename = "stationslist.txt"
        handle = open(os.path.join(os.path.dirname(__file__),filename))
        words=list()
        words = ['']

        for line in handle:
            line=line.rstrip()
            words.append(line)

        self.ui.comboBox_start.addItems(words)
        self.ui.comboBox_end.addItems(words)
    
    
    def printPathsLabels_staions(self,start_key,dest_key):
        ''' main function to dynamically allocate labels and assign colours to them '''
        global i
        
        key_to_line_changes = {}
        station_name = list()
        station_name, key_to_line_changes = print_route(g, start_key, dest_key)
        self.ui.scrollArea_2.setAlignment(Qt.AlignCenter)
    
        for i in range(len(station_name)):

        
            station = QtWidgets.QLabel(self.ui.scrollArea_2)
            self.ui.verticalLayout_15.addWidget(station)
            station.setMinimumSize(QtCore.QSize(230, 40))
            station.setMaximumSize(QtCore.QSize(230, 40))
            station.setAlignment(Qt.AlignCenter)
            
            #line_changes = {}
            
            
            try:  
                    station.setText(station_name[i])
                    if key_to_line_changes[i] == 1:
                            station.setStyleSheet("QLabel{ margin-left: 10px; border-radius: 20px; border: 1px solid rgb(217,11,52); background: rgb(35,35,35); color: rgb(217,11,52);} ")
                    if key_to_line_changes[i] == 2:
                            station.setStyleSheet("QLabel{margin-left: 10px; border-radius: 20px;border: 1px solid rgb(217,176,11); background: rgb(35,35,35);color: rgb(217,176,11);}")
                    if key_to_line_changes[i] == 3:
                            station.setStyleSheet("QLabel{margin-left: 10px; border-radius: 20px;border: 1px solid rgb(255,0,101); background: rgb(35,35,35);color: rgb(255,0,101);}}")
                    if key_to_line_changes[i] == 4:
                            station.setStyleSheet("QLabel{ margin-left: 10px; border-radius: 20px; border: 1px solid rgb(73,11,217); background: rgb(35,35,35); color: rgb(73,11,217);} ")
                    if key_to_line_changes[i] == 5:
                            station.setStyleSheet("QLabel{margin-left: 10px; border-radius: 20px;border: 1px solid rgb(217,73,11); background: rgb(35,35,35);color: rgb(217,73,11);}")
                    if key_to_line_changes[i] == 6:
                            station.setStyleSheet("QLabel{margin-left: 10px; border-radius: 20px;border: 1px solid rgb(52,217,11); background: rgb(35,35,35);color: rgb(52,217,11);}")
                    if key_to_line_changes[i] == 7:
                            station.setStyleSheet("QLabel{ margin-left: 10px; border-radius: 20px; border: 1px solid rgb(255,105,97); background: rgb(35,35,35); color: rgb(255,105,97);} ")
                    if key_to_line_changes[i] == 8:
                            station.setStyleSheet("QLabel{margin-left: 10px; border-radius: 20px;border: 1px solid rgb(176,11,217); background: rgb(35,35,35);color: rgb(176,11,217);}")
                    if key_to_line_changes[i] == 9:
                            station.setStyleSheet("QLabel{margin-left: 10px; border-radius: 20px;border: 1px solid rgb(217,11,155); background: rgb(35,35,35);color: rgb(217,11,155);}")
                    if key_to_line_changes[i] == 10:
                            station.setStyleSheet("QLabel{ margin-left: 10px; border-radius: 20px; border: 1px solid rgb(11,217,176); background: rgb(35,35,35); color: rgb(11,217,176);} ")
                    if key_to_line_changes[i] == 11:
                            station.setStyleSheet("QLabel{margin-left: 10px; border-radius: 20px;border: 1px solid rgb(166,166,166); background: rgb(35,35,35);color: rgb(166,166,166);}")
                        
            except:
                    print("key to line change dict error")

            

    def setInfo(self):
        ''' setting trip info '''
        paths_time = int(g.path_time)/2
        strTime = "<strong>{}</strong> mins to reach".format(int(paths_time))
        self.ui.label_time.setText(strTime)
        paths_line = int(g.path_len) - 1
        strLen = "<strong>{}</strong> stops".format(int(paths_line))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setWeight(75)
        self.ui.label_stops.setFont(font)
        self.ui.label_stops.setText(strLen)
        paths_changes = int(g.path_changes)/2
        strChanges = "<strong>{}</strong> changes".format(int(paths_changes))
        self.ui.label_changes.setText(strChanges)
        if paths_time >= 0 and paths_time < 5:
            self.ui.label_cost.setFont(font)
            self.ui.label_cost.setText("Rs. <strong>10</strong>")
        elif paths_time >=5 and paths_time < 11:
            self.ui.label_cost.setFont(font)
            self.ui.label_cost.setText("Rs. <strong>20</strong>")
        elif paths_time >=11 and paths_time < 25:
            self.ui.label_cost.setFont(font)
            self.ui.label_cost.setText("Rs. <strong>30</strong>")
        elif paths_time >=25 and paths_time <43:
            self.ui.label_cost.setFont(font)
            self.ui.label_cost.setText("Rs. <strong>40</strong>")
        elif paths_time >=43 and paths_time <64:
            self.ui.label_cost.setFont(font)
            self.ui.label_cost.setText("Rs. <strong>50</strong>")
        else:
            self.ui.label_cost.setFont(font)
            self.ui.label_cost.setText("Rs. <strong>60</strong>")
            

    def clearLayout(self,layout):
        g.path_changes = 0
        g.path_len = 0
        g.path_time = 0
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def plot(self,start_key,dest_key):
        ''' plot the route map '''
        #plt.style.use('Solarize_Light2')
        plt.style.use('fivethirtyeight')
        G = nx.read_graphml("coordinates.graphml")
        names, key_to_line_changes = print_route(g, start_key, dest_key)


        edge_x = []
        edge_y = []
        edge_path_x = []
        edge_path_y = []
        node_path_x = []
        node_path_y = []
        node_red_x = []
        node_red_y = []
        node_yellow_x = []
        node_yellow_y = []
        node_pink_x = []
        node_pink_y = []
        node_blue_x = []
        node_blue_y = []
        node_orange_x = []
        node_orange_y = []
        node_green_x = []
        node_green_y = []
        node_rapid_x = []
        node_rapid_y = []
        node_violet_x = []
        node_violet_y = []
        node_magenta_x = []
        node_magenta_y = []
        node_aqua_x = []
        node_aqua_y = []
        node_grey_x = []
        node_grey_y = []
        values = list()


        for name in names:
            values.append(g.key_to_name[name])

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        for edge in G.edges():
            if int(edge[0]) in values and int(edge[1]) in values:
                x0 = G.nodes[edge[0]]['x']
                y0 = G.nodes[edge[0]]['y']
                x1 = G.nodes[edge[1]]['x']
                y1 = G.nodes[edge[1]]['y']
                edge_path_x.append(x0)
                edge_path_x.append(x1)
                edge_path_x.append(None)
                edge_path_y.append(y0)
                edge_path_y.append(y1)
                edge_path_y.append(None)
                if int(edge[1]) >= 0 and int(edge[1]) <= 27:
                    ax.plot(edge_path_x,edge_path_y, "#ff0130", lw=2)
                    edge_path_x = []
                    edge_path_y = []
                elif int(edge[1]) >= 28 and int(edge[1]) <= 64:
                    ax.plot(edge_path_x,edge_path_y, "#f9c70c", lw=2)
                    edge_path_x = []
                    edge_path_y = []
                elif int(edge[1]) >= 65 and int(edge[1]) <= 102:
                    ax.plot(edge_path_x,edge_path_y, "#ff3ba7", lw=2)
                    edge_path_x = []
                    edge_path_y = []
                elif int(edge[1]) >= 103 and int(edge[1]) <= 153:
                    ax.plot(edge_path_x,edge_path_y, "#001fd7", lw=2)
                    edge_path_x = []
                    edge_path_y = []
                elif int(edge[1]) >= 154 and int(edge[1]) <= 161:
                    ax.plot(edge_path_x,edge_path_y, "#001fd7", lw=2)
                    edge_path_x = []
                    edge_path_y = []
                elif int(edge[1]) >= 162 and int(edge[1]) <= 167:
                    ax.plot(edge_path_x,edge_path_y, "#ff7e1c", lw=2)
                    edge_path_x = []
                    edge_path_y = []
                elif int(edge[1]) >= 168 and int(edge[1]) <= 188:
                    ax.plot(edge_path_x,edge_path_y, "#8fff2d", lw=2)
                    edge_path_x = []
                    edge_path_y = []
                elif int(edge[1]) >= 189 and int(edge[1]) <= 191:
                    ax.plot(edge_path_x,edge_path_y, "#8fff2d", lw=2)
                    edge_path_x = []
                    edge_path_y = []
                elif int(edge[1]) >= 192 and int(edge[1]) <= 202:
                    ax.plot(edge_path_x,edge_path_y, "black", lw=2)
                    edge_path_x = []
                    edge_path_y = []
                elif int(edge[1]) >= 203 and int(edge[1]) <= 236:
                    ax.plot(edge_path_x,edge_path_y, "#9c05d7", lw=2)
                    edge_path_x = []
                    edge_path_y = []
                elif int(edge[1]) >= 237 and int(edge[1]) <= 261:
                    ax.plot(edge_path_x,edge_path_y, "#cf1f6e", lw=2)
                    edge_path_x = []
                    edge_path_y = []
                elif int(edge[1]) >= 262 and int(edge[1]) <= 282:
                    ax.plot(edge_path_x,edge_path_y, "#17fffb", lw=2)
                    edge_path_x = []
                    edge_path_y = []
                elif int(edge[1]) >= 283 and int(edge[1]) <= 285:
                    ax.plot(edge_path_x,edge_path_y, "grey", lw=2)
                    edge_path_x = []
                    edge_path_y = []
            else:
                x0 = G.nodes[edge[0]]['x']
                y0 = G.nodes[edge[0]]['y']
                x1 = G.nodes[edge[1]]['x']
                y1 = G.nodes[edge[1]]['y']
                edge_x.append(x0)
                edge_x.append(x1)
                edge_x.append(None)
                edge_y.append(y0)
                edge_y.append(y1)
                edge_y.append(None)

        for node in G.nodes():
            if int(node) in values:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                if int(node) >= 0 and int(node) <= 27:
                    ax.scatter(x, y, s=30,c = "#ff0130")
                elif int(node) >= 28 and int(node) <= 64:
                    ax.scatter(x, y, s=30,c = "#f9c70c")
                elif int(node) >= 65 and int(node) <= 102:
                    ax.scatter(x, y, s=30,c = "#ff3ba7")
                elif int(node) >= 103 and int(node) <= 153:
                    ax.scatter(x, y, s=30,c = "#001fd7")
                elif int(node) >= 154 and int(node) <= 161:
                    ax.scatter(x, y, s=30,c = "#001fd7")
                elif int(node) >= 162 and int(node) <= 167:
                    ax.scatter(x, y, s=30,c = "#ff7e1c")
                elif int(node) >= 168 and int(node) <= 188:
                    ax.scatter(x, y, s=30,c = "#8fff2d")
                elif int(node) >= 189 and int(node) <= 191:
                    ax.scatter(x, y, s=30,c = "#8fff2d")
                elif int(node) >= 192 and int(node) <= 202:
                    ax.scatter(x, y, s=30,c = "black")
                elif int(node) >= 203 and int(node) <= 236:
                    ax.scatter(x, y, s=30,c = "#9c05d7")
                elif int(node) >= 237 and int(node) <= 261:
                    ax.scatter(x, y, s=30,c = "#cf1f6e")
                elif int(node) >= 262 and int(node) <= 282:
                    ax.scatter(x, y, s=30,c = "#17fffb")
                elif int(node) >= 283 and int(node) <= 285:
                    ax.scatter(x, y, s=30,c = "grey")
                else:
                    print("heh?")
                ax.text(x,y,G.nodes[node]['label'],fontsize=6)

            elif int(node) >= 0 and int(node) <= 27:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_red_x.append(x)
                node_red_y.append(y)
                
            elif int(node) >= 28 and int(node) <= 64:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_yellow_x.append(x)
                node_yellow_y.append(y)
            elif int(node) >= 65 and int(node) <= 102:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_pink_x.append(x)
                node_pink_y.append(y)
            elif int(node) >= 103 and int(node) <= 153:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_blue_x.append(x)
                node_blue_y.append(y)
            elif int(node) >= 154 and int(node) <= 161:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_blue_x.append(x)
                node_blue_y.append(y)
            elif int(node) >= 162 and int(node) <= 167:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_orange_x.append(x)
                node_orange_y.append(y)
            elif int(node) >= 168 and int(node) <= 188:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_green_x.append(x)
                node_green_y.append(y)
            elif int(node) >= 189 and int(node) <= 191:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_green_x.append(x)
                node_green_y.append(y)
            elif int(node) >= 192 and int(node) <= 202:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_rapid_x.append(x)
                node_rapid_y.append(y)
            elif int(node) >= 203 and int(node) <= 236:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_violet_x.append(x)
                node_violet_y.append(y)
            elif int(node) >= 237 and int(node) <= 261:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_magenta_x.append(x)
                node_magenta_y.append(y)
            elif int(node) >= 262 and int(node) <= 282:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_aqua_x.append(x)
                node_aqua_y.append(y)
            elif int(node) >= 283 and int(node) <= 285:
                x = G.nodes[node]['x']
                y = G.nodes[node]['y']
                node_grey_x.append(x)
                node_grey_y.append(y)
            else:
                print("")
        
        
        # plot data
        #ax.scatter(node_x, node_y,alpha=0.3)
        ax.scatter(node_red_x, node_red_y, s=10,c = "#ff0130", alpha=0.3)
        ax.scatter(node_yellow_x, node_yellow_y, s=10,c = "#f9c70c", alpha=0.6)
        ax.scatter(node_pink_x, node_pink_y, s=10,c = "#ff3ba7", alpha=0.6)
        ax.scatter(node_blue_x, node_blue_y, s=10,c = "#001fd7", alpha=0.3)
        ax.scatter(node_orange_x, node_orange_y, s=10,c = "#ff7e1c", alpha=0.6)
        ax.scatter(node_green_x, node_green_y, s=10,c = "#8fff2d", alpha=0.3)
        ax.scatter(node_rapid_x, node_rapid_y, s=10,c = "black", alpha=0.3)
        ax.scatter(node_violet_x, node_violet_y, s=10,c = "#9c05d7", alpha=0.3)
        ax.scatter(node_magenta_x, node_magenta_y, s=10,c = "#cf1f6e", alpha=0.3)
        ax.scatter(node_aqua_x, node_aqua_y, s=10,c = "#17fffb", alpha=0.3)
        ax.scatter(node_grey_x, node_grey_y, s=10,c = "grey", alpha=0.3)
        ax.plot(edge_x,edge_y,alpha=0.3)
        red_patch = mpatches.Patch(color='#ff0130', label='Red line')
        yellow_patch = mpatches.Patch(color='#f9c70c', label='Yellow line')
        pink_patch = mpatches.Patch(color='#ff3ba7', label='Pink line')
        blue_patch = mpatches.Patch(color='#001fd7', label='Blue line')
        orange_patch = mpatches.Patch(color='#ff7e1c', label='Orange line')
        green_patch = mpatches.Patch(color='#8fff2d', label='Green line')
        rapid_patch = mpatches.Patch(color='black', label='Rapid line')
        violet_patch = mpatches.Patch(color='#9c05d7', label='Violet line')
        magenta_patch = mpatches.Patch(color='#cf1f6e', label='Magenta line')
        cyan_patch = mpatches.Patch(color='#17fffb', label='Aqua line')
        grey_patch = mpatches.Patch(color='grey', label='Grey line')

        ax.legend(handles=[red_patch,yellow_patch,pink_patch,blue_patch,orange_patch,green_patch,rapid_patch,violet_patch,magenta_patch,cyan_patch,grey_patch],prop={'size': 7},loc='upper right', borderaxespad=0.)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.set_facecolor('#dfffff')

        # refresh canvas
        self.canvas.draw()
        
    def plot_main_graph(self):
            ''' plot the main graph on page 2 '''
            #plt.style.use('Solarize_Light2')
            plt.style.use('fivethirtyeight')
            G = nx.read_graphml("coordinates.graphml")
            
            
            edge_x = []
            edge_y = []
            node_red_x = []
            node_red_y = []
            node_yellow_x = []
            node_yellow_y = []
            node_pink_x = []
            node_pink_y = []
            node_blue_x = []
            node_blue_y = []
            node_orange_x = []
            node_orange_y = []
            node_green_x = []
            node_green_y = []
            node_rapid_x = []
            node_rapid_y = []
            node_violet_x = []
            node_violet_y = []
            node_magenta_x = []
            node_magenta_y = []
            node_aqua_x = []
            node_aqua_y = []
            node_grey_x = []
            node_grey_y = []

            for edge in G.edges():
                
                x0 = G.nodes[edge[0]]['x']
                y0 = G.nodes[edge[0]]['y']
                x1 = G.nodes[edge[1]]['x']
                y1 = G.nodes[edge[1]]['y']
                edge_x.append(x0)
                edge_x.append(x1)
                edge_x.append(None)
                edge_y.append(y0)
                edge_y.append(y1)
                edge_y.append(None)
            
            for node in G.nodes():
                if int(node) >= 0 and int(node) <= 27:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_red_x.append(x)
                    node_red_y.append(y)
                elif int(node) >= 28 and int(node) <= 64:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_yellow_x.append(x)
                    node_yellow_y.append(y)
                elif int(node) >= 65 and int(node) <= 102:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_pink_x.append(x)
                    node_pink_y.append(y)
                elif int(node) >= 103 and int(node) <= 153:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_blue_x.append(x)
                    node_blue_y.append(y)
                elif int(node) >= 154 and int(node) <= 161:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_blue_x.append(x)
                    node_blue_y.append(y)
                elif int(node) >= 162 and int(node) <= 167:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_orange_x.append(x)
                    node_orange_y.append(y)
                elif int(node) >= 168 and int(node) <= 188:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_green_x.append(x)
                    node_green_y.append(y)
                elif int(node) >= 189 and int(node) <= 191:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_green_x.append(x)
                    node_green_y.append(y)
                elif int(node) >= 192 and int(node) <= 202:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_rapid_x.append(x)
                    node_rapid_y.append(y)
                elif int(node) >= 203 and int(node) <= 236:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_violet_x.append(x)
                    node_violet_y.append(y)
                elif int(node) >= 237 and int(node) <= 261:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_magenta_x.append(x)
                    node_magenta_y.append(y)
                elif int(node) >= 262 and int(node) <= 282:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_aqua_x.append(x)
                    node_aqua_y.append(y)
                elif int(node) >= 283 and int(node) <= 285:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_grey_x.append(x)
                    node_grey_y.append(y)
                else:
                    print("Error in printing nodes graph")
                
            # instead of ax.hold(False)
            self.figure_main.clear()

            # create an axis
            ax_main = self.figure_main.add_subplot(111)

            # plot data
            ax_main.plot(edge_x,edge_y,alpha=0.2)
            ax_main.scatter(node_red_x, node_red_y,s=10,c = "#ff0130")
            ax_main.scatter(node_yellow_x, node_yellow_y,s=10,c = "#f9c70c")
            ax_main.scatter(node_pink_x, node_pink_y,s=10,c = "#ff3ba7")
            ax_main.scatter(node_blue_x, node_blue_y,s=10,c = "#001fd7")
            ax_main.scatter(node_orange_x, node_orange_y,s=10,c = "#ff7e1c")
            ax_main.scatter(node_green_x, node_green_y,s=10,c = "#8fff2d")
            ax_main.scatter(node_rapid_x, node_rapid_y,s=10,c = "black")
            ax_main.scatter(node_violet_x, node_violet_y,s=10,c = "#9c05d7")
            ax_main.scatter(node_magenta_x, node_magenta_y,s=10,c = "#cf1f6e")
            ax_main.scatter(node_aqua_x, node_aqua_y,s=10,c = "#17fffb")
            ax_main.scatter(node_grey_x, node_grey_y,s=10,c = "grey")
            
            red_patch = mpatches.Patch(color='#ff0130', label='Red line')
            yellow_patch = mpatches.Patch(color='#f9c70c', label='Yellow line')
            pink_patch = mpatches.Patch(color='#ff3ba7', label='Pink line')
            blue_patch = mpatches.Patch(color='#001fd7', label='Blue line')
            orange_patch = mpatches.Patch(color='#ff7e1c', label='Orange line')
            green_patch = mpatches.Patch(color='#8fff2d', label='Green line')
            rapid_patch = mpatches.Patch(color='black', label='Rapid line')
            violet_patch = mpatches.Patch(color='#9c05d7', label='Violet line')
            magenta_patch = mpatches.Patch(color='#cf1f6e', label='Magenta line')
            cyan_patch = mpatches.Patch(color='#17fffb', label='Aqua line')
            grey_patch = mpatches.Patch(color='grey', label='Grey line')

            ax_main.legend(handles=[red_patch,yellow_patch,pink_patch,blue_patch,orange_patch,green_patch,rapid_patch,violet_patch,magenta_patch,cyan_patch,grey_patch],prop={'size': 7},loc='upper right', borderaxespad=0.)
            ax_main.axes.get_xaxis().set_visible(False)
            ax_main.axes.get_yaxis().set_visible(False)
            ax_main.set_facecolor('#dfffff')
            ax_main.set_title('Map of Delhi Metro', color = '#dfffff')
            # refresh canvas
            self.canvas_main.draw()

    def plot_compare_graph(self,start_key,dest_key):
            ''' plot the compare graph on page 2 '''
            #plt.style.use('Solarize_Light2')
            plt.style.use('fivethirtyeight')
            G = nx.read_graphml("coordinates.graphml")
            names, key_to_line_changes = print_route(g, start_key, dest_key)
            
            edge_x = []
            edge_y = []
            edge_path_x = []
            edge_path_y = []
            edge_one_x = []
            edge_one_y = []
            edge_two_x = []
            edge_two_y = []
            edge_three_x = []
            edge_three_y = []
            edge_four_x = []
            edge_four_y = []
            edge_five_x = []
            edge_five_y = []
            node_red_x = []
            node_red_y = []
            node_yellow_x = []
            node_yellow_y = []
            node_pink_x = []
            node_pink_y = []
            node_blue_x = []
            node_blue_y = []
            node_orange_x = []
            node_orange_y = []
            node_green_x = []
            node_green_y = []
            node_rapid_x = []
            node_rapid_y = []
            node_violet_x = []
            node_violet_y = []
            node_magenta_x = []
            node_magenta_y = []
            node_aqua_x = []
            node_aqua_y = []
            node_grey_x = []
            node_grey_y = []
            values = list()
            ind = 0

            for name in names:
                values.append(g.key_to_name[name])
            x = extraFunctions()
            for path in nx.shortest_simple_paths(ntx_graph, source=start_key, target=dest_key, weight='weight'):
                if ind<7:
                    wts = x.all_path_length(ntx_graph,path,'weight')
                    g.all_paths[ind] = path
                    g.all_paths_wts[ind] = wts
                    ind = ind + 1
                else:
                    break

            for edge in G.edges():
                
                if int(edge[0]) in values and int(edge[1]) in values:
                    x0 = G.nodes[edge[0]]['x']
                    y0 = G.nodes[edge[0]]['y']
                    x1 = G.nodes[edge[1]]['x']
                    y1 = G.nodes[edge[1]]['y']
                    edge_path_x.append(x0)
                    edge_path_x.append(x1)
                    edge_path_x.append(None)
                    edge_path_y.append(y0)
                    edge_path_y.append(y1)
                    edge_path_y.append(None)
                elif int(edge[0]) in g.all_paths[1] and int(edge[1]) in g.all_paths[1]:
                    x0 = G.nodes[edge[0]]['x']
                    y0 = G.nodes[edge[0]]['y']
                    x1 = G.nodes[edge[1]]['x']
                    y1 = G.nodes[edge[1]]['y']
                    edge_one_x.append(x0)
                    edge_one_x.append(x1)
                    edge_one_x.append(None)
                    edge_one_y.append(y0)
                    edge_one_y.append(y1)
                    edge_one_y.append(None)
                elif int(edge[0]) in g.all_paths[2] and int(edge[1]) in g.all_paths[2]:
                    x0 = G.nodes[edge[0]]['x']
                    y0 = G.nodes[edge[0]]['y']
                    x1 = G.nodes[edge[1]]['x']
                    y1 = G.nodes[edge[1]]['y']
                    edge_two_x.append(x0)
                    edge_two_x.append(x1)
                    edge_two_x.append(None)
                    edge_two_y.append(y0)
                    edge_two_y.append(y1)
                    edge_two_y.append(None)
                elif int(edge[0]) in g.all_paths[3] and int(edge[1]) in g.all_paths[3]:
                    x0 = G.nodes[edge[0]]['x']
                    y0 = G.nodes[edge[0]]['y']
                    x1 = G.nodes[edge[1]]['x']
                    y1 = G.nodes[edge[1]]['y']
                    edge_three_x.append(x0)
                    edge_three_x.append(x1)
                    edge_three_x.append(None)
                    edge_three_y.append(y0)
                    edge_three_y.append(y1)
                    edge_three_y.append(None)
                elif int(edge[0]) in g.all_paths[4] and int(edge[1]) in g.all_paths[4]:
                    x0 = G.nodes[edge[0]]['x']
                    y0 = G.nodes[edge[0]]['y']
                    x1 = G.nodes[edge[1]]['x']
                    y1 = G.nodes[edge[1]]['y']
                    edge_four_x.append(x0)
                    edge_four_x.append(x1)
                    edge_four_x.append(None)
                    edge_four_y.append(y0)
                    edge_four_y.append(y1)
                    edge_four_y.append(None)
                elif int(edge[0]) in g.all_paths[5] and int(edge[1]) in g.all_paths[5]:
                    x0 = G.nodes[edge[0]]['x']
                    y0 = G.nodes[edge[0]]['y']
                    x1 = G.nodes[edge[1]]['x']
                    y1 = G.nodes[edge[1]]['y']
                    edge_five_x.append(x0)
                    edge_five_x.append(x1)
                    edge_five_x.append(None)
                    edge_five_y.append(y0)
                    edge_five_y.append(y1)
                    edge_five_y.append(None)
                else:
                    x0 = G.nodes[edge[0]]['x']
                    y0 = G.nodes[edge[0]]['y']
                    x1 = G.nodes[edge[1]]['x']
                    y1 = G.nodes[edge[1]]['y']
                    edge_x.append(x0)
                    edge_x.append(x1)
                    edge_x.append(None)
                    edge_y.append(y0)
                    edge_y.append(y1)
                    edge_y.append(None)
            
            for node in G.nodes():
                if int(node) >= 0 and int(node) <= 27:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_red_x.append(x)
                    node_red_y.append(y)
                elif int(node) >= 28 and int(node) <= 64:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_yellow_x.append(x)
                    node_yellow_y.append(y)
                elif int(node) >= 65 and int(node) <= 102:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_pink_x.append(x)
                    node_pink_y.append(y)
                elif int(node) >= 103 and int(node) <= 153:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_blue_x.append(x)
                    node_blue_y.append(y)
                elif int(node) >= 154 and int(node) <= 161:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_blue_x.append(x)
                    node_blue_y.append(y)
                elif int(node) >= 162 and int(node) <= 167:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_orange_x.append(x)
                    node_orange_y.append(y)
                elif int(node) >= 168 and int(node) <= 188:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_green_x.append(x)
                    node_green_y.append(y)
                elif int(node) >= 189 and int(node) <= 191:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_green_x.append(x)
                    node_green_y.append(y)
                elif int(node) >= 192 and int(node) <= 202:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_rapid_x.append(x)
                    node_rapid_y.append(y)
                elif int(node) >= 203 and int(node) <= 236:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_violet_x.append(x)
                    node_violet_y.append(y)
                elif int(node) >= 237 and int(node) <= 261:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_magenta_x.append(x)
                    node_magenta_y.append(y)
                elif int(node) >= 262 and int(node) <= 282:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_aqua_x.append(x)
                    node_aqua_y.append(y)
                elif int(node) >= 283 and int(node) <= 285:
                    x = G.nodes[node]['x']
                    y = G.nodes[node]['y']
                    node_grey_x.append(x)
                    node_grey_y.append(y)
                else:
                    print("Error in printing nodes graph")
                
            # instead of ax.hold(False)
            self.figure_compare.clear()

            # create an axis
            ax_compare = self.figure_compare.add_subplot(111)

            # plot data
            ax_compare.plot(edge_x,edge_y,alpha=0.3)
            ax_compare.plot(edge_path_x,edge_path_y,alpha=0.6, color = '#ff0130')
            ax_compare.plot(edge_one_x,edge_one_y,alpha=0.3, color = 'black')
            ax_compare.plot(edge_two_x,edge_two_y,alpha=0.3, color = 'yellow')
            ax_compare.plot(edge_three_x,edge_three_y,alpha=0.3, color = '#8fff2d')
            ax_compare.plot(edge_four_x,edge_four_y,alpha=0.3, color = '#ff7e1c')
            ax_compare.plot(edge_five_x,edge_five_y,alpha=0.3, color = '#9c05d7')
            ax_compare.scatter(node_red_x, node_red_y,s=10,c = "#ff0130")
            ax_compare.scatter(node_yellow_x, node_yellow_y,s=10,c = "#f9c70c")
            ax_compare.scatter(node_pink_x, node_pink_y,s=10,c = "#ff3ba7")
            ax_compare.scatter(node_blue_x, node_blue_y,s=10,c = "#001fd7")
            ax_compare.scatter(node_orange_x, node_orange_y,s=10,c = "#ff7e1c")
            ax_compare.scatter(node_green_x, node_green_y,s=10,c = "#8fff2d")
            ax_compare.scatter(node_rapid_x, node_rapid_y,s=10,c = "black")
            ax_compare.scatter(node_violet_x, node_violet_y,s=10,c = "#9c05d7")
            ax_compare.scatter(node_magenta_x, node_magenta_y,s=10,c = "#cf1f6e")
            ax_compare.scatter(node_aqua_x, node_aqua_y,s=10,c = "#17fffb")
            ax_compare.scatter(node_grey_x, node_grey_y,s=10,c = "grey")
            
            dijkstra_legend = "{} mins for Djikstra Path".format(g.all_paths_wts[0])
            path1_legend = "{} mins for Path 1".format(g.all_paths_wts[1])
            path2_legend = "{} mins for Path 2".format(g.all_paths_wts[2])
            path3_legend = "{} mins for Path 3".format(g.all_paths_wts[3])
            path4_legend = "{} mins for Path 4".format(g.all_paths_wts[4])
            path5_legend = "{} mins for Path 5".format(g.all_paths_wts[5])



            dijkstra_patch = mpatches.Patch(color='#ff0130', label=dijkstra_legend)
            path1_patch = mpatches.Patch(color='black', label=path1_legend)
            path2_patch = mpatches.Patch(color='yellow', label=path2_legend)
            path3_patch = mpatches.Patch(color='#8fff2d', label=path3_legend)
            path4_patch = mpatches.Patch(color='#ff7e1c', label=path4_legend)
            path5_patch = mpatches.Patch(color='#9c05d7', label=path5_legend)
            #pink_patch = mpatches.Patch(color='#ff3ba7', label='Pink line')
            #blue_patch = mpatches.Patch(color='#001fd7', label='Blue line')
            #orange_patch = mpatches.Patch(color='#ff7e1c', label='Orange line')

            ax_compare.legend(handles=[dijkstra_patch,path1_patch,path2_patch,path3_patch,path4_patch,path5_patch],prop={'size': 7},loc='upper right', borderaxespad=0.)
            ax_compare.axes.get_xaxis().set_visible(False)
            ax_compare.axes.get_yaxis().set_visible(False)
            ax_compare.set_facecolor('#dfffff')
            ax_compare.set_title('Comparing Djikstra Path with Top 5 Shortest Other Paths' , color = '#dfffff')
            # refresh canvas
            self.canvas_compare.draw()

    
    
class extraFunctions:    
    def all_path_length(self,G, nodes, weight):
        w = 0
        for ind,nd in enumerate(nodes[1:]):
            prev = nodes[ind]
            w += G[prev][nd][weight]
        return w

