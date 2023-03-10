from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import * 


class GUIEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LKMK Editor")
        self.resize(600, 600)
        mainLayout = QVBoxLayout()
        titleContainer = QHBoxLayout()
        contentContainer = QHBoxLayout()

        
        # Layout Settings:
        contentContainer.addWidget(self._createDropdown("hello", ["2x2", "2x3", "4x4"]))
        mainLayout.addLayout(titleContainer)
        mainLayout.addLayout(contentContainer)

        # View Init:
        self.setLayout(mainLayout)
        self.show()

    

    def _createDropdown(self, label, array):
        # Dropdown Menu Widget
        vbox = QVBoxLayout()
        groupBox = QGroupBox(label)
        dropDown = QComboBox()

        dropDown.addItems(array)
        vbox.addWidget(dropDown)

        groupBox.setLayout(vbox)
        return groupBox

    def _createLabel(self, label):
        # Label Widget:
        label = QLayout(label)

        # Label Widget Styling:


        # Label Return Value:
        return label
    
    def initGUI(self):
        pass
        #app Setup:
        # app = QApplication([])
        # app.setStyle('macos')
        # window = QMainWindow()
        # window.setWindowTitle("hello")

        # # layouts:
        # v_layout = QVBoxLayout()
        # h_layout = QHBoxLayout()
        
       
        
        # # groupbox layout:
        # groupBox = QGroupBox("Test Example")
        # testlayout = QHBoxLayout()
        # groupBox.setLayout(testlayout)

        # # Dropdown Menu Widget
        # dropDown = QComboBox()
        # dropDown.addItems(['One', 'Two', 'Three', 'Four'])
        # v_layout.addWidget(groupBox)
        # v_layout.addWidget(QLabel('hello world'))
        # v_layout.addWidget(dropDown)
        # # v_layout.addWidget(btn1)
        # # v_layout.addWidget(btn2)

        # # adding and setting up adn executing the layouts:
        # h_layout.addLayout(v_layout)
        # window.setLayout(h_layout)
        # window.show()
        # app.exec()

        #### Tray Icon Start ####
            # tray = QSystemTrayIcon()
            # tray.setVisible(True)

            # statusBarMenu = QMenu()
            # action = QAction("A menu item")
            # statusBarMenu.addAction(action)

            # quit = QAction("Quit")
            # quit.triggered.connect(app.quit)
            # statusBarMenu.addAction(quit)

            # tray.setContextMenu(statusBarMenu)
        #### Tray Icon End ###