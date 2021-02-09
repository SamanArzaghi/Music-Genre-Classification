from PyQt5 import QtCore, QtGui, QtWidgets
from record import record
from browsForFile import browsForFile
from testing import testing

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MGC")
        MainWindow.resize(778, 345)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.line)
        self.genreLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.genreLabel.setFont(font)
        self.genreLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.genreLabel.setToolTipDuration(-1)
        self.genreLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.genreLabel.setAutoFillBackground(True)
        self.genreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.genreLabel.setObjectName("genreLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.genreLabel)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.line_2)
        self.liveButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.liveButton.setFont(font)
        self.liveButton.setObjectName("liveButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.liveButton)
        self.orLabel = QtWidgets.QLabel(self.centralwidget)
        self.orLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.orLabel.setObjectName("orLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.orLabel)
        self.mineButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mineButton.setFont(font)
        self.mineButton.setObjectName("mineButton")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.mineButton)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setObjectName("searchButton")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.searchButton)
        self.songLabel = QtWidgets.QLabel(self.centralwidget)
        self.songLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.songLabel.setObjectName("songLabel")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.songLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.liveButton.clicked.connect(self.liveCheck)
        self.mineButton.clicked.connect(self.manualCheck)
        self.searchButton.clicked.connect(self.browsFile)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MGC", "MGC"))
        self.genreLabel.setStatusTip(_translate("MGC", "ganere of the song"))
        self.genreLabel.setText(_translate("MGC", "GENRE"))
        self.liveButton.setStatusTip(_translate("MGC", "record current song playing"))
        self.liveButton.setText(_translate("MGC", "Live"))
        self.orLabel.setText(_translate("MGC", "OR"))
        self.mineButton.setStatusTip(_translate("MGC", "choosen song form device"))
        self.mineButton.setText(_translate("MGC", "Mine"))
        self.searchButton.setStatusTip(_translate("MGC", "search the device"))
        self.searchButton.setText(_translate("MGC", "..."))
        self.songLabel.setStatusTip(_translate("MGC", "songs name"))
        self.songLabel.setText(_translate("MGC", "---pick a song---"))

    def liveCheck(self):
        # record()
        # use convert(output.wav)
        record()
        self.genreLabel.setText(testing('output.wav'))

    def manualCheck(self):
        # self.songLabel.text()
        # use convert(self.songLabel.text())
        if self.songLabel.text() == "---pick a song---" :
            self.genreLabel.setText("FIRST CHOOSE A FILE")
        else :
            self.genreLabel.setText(testing(self.songLabel.text()))

    def browsFile(self):
        self.songLabel.setText(browsForFile())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
