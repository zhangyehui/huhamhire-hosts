# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qthostsui.ui'
#
# Created: Fri Aug 02 19:08:24 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HostsUtlMain(object):
    def setupUi(self, HostsUtlMain):
        HostsUtlMain.setObjectName(_fromUtf8("HostsUtlMain"))
        HostsUtlMain.setEnabled(True)
        HostsUtlMain.resize(640, 360)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HostsUtlMain.sizePolicy().hasHeightForWidth())
        HostsUtlMain.setSizePolicy(sizePolicy)
        HostsUtlMain.setMinimumSize(QtCore.QSize(640, 360))
        HostsUtlMain.setMaximumSize(QtCore.QSize(640, 360))
        HostsUtlMain.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/img/utl_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HostsUtlMain.setWindowIcon(icon)
        HostsUtlMain.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        HostsUtlMain.setSizeGripEnabled(False)
        HostsUtlMain.setModal(False)
        self.Prog = QtGui.QProgressBar(HostsUtlMain)
        self.Prog.setGeometry(QtCore.QRect(10, 320, 500, 25))
        self.Prog.setAlignment(QtCore.Qt.AlignCenter)
        self.Prog.setTextVisible(True)
        self.Prog.setInvertedAppearance(False)
        self.Prog.setObjectName(_fromUtf8("Prog"))
        self.ConfigBox = QtGui.QGroupBox(HostsUtlMain)
        self.ConfigBox.setGeometry(QtCore.QRect(10, 20, 240, 90))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConfigBox.sizePolicy().hasHeightForWidth())
        self.ConfigBox.setSizePolicy(sizePolicy)
        self.ConfigBox.setObjectName(_fromUtf8("ConfigBox"))
        self.layoutWidget = QtGui.QWidget(self.ConfigBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 221, 50))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.configLayout = QtGui.QGridLayout(self.layoutWidget)
        self.configLayout.setMargin(0)
        self.configLayout.setObjectName(_fromUtf8("configLayout"))
        self.labelIP = QtGui.QLabel(self.layoutWidget)
        self.labelIP.setObjectName(_fromUtf8("labelIP"))
        self.configLayout.addWidget(self.labelIP, 0, 0, 1, 1)
        self.SelectMirror = QtGui.QComboBox(self.layoutWidget)
        self.SelectMirror.setObjectName(_fromUtf8("SelectMirror"))
        self.configLayout.addWidget(self.SelectMirror, 0, 1, 1, 1)
        self.labelMirror = QtGui.QLabel(self.layoutWidget)
        self.labelMirror.setObjectName(_fromUtf8("labelMirror"))
        self.configLayout.addWidget(self.labelMirror, 1, 0, 1, 1)
        self.SelectIP = QtGui.QComboBox(self.layoutWidget)
        self.SelectIP.setObjectName(_fromUtf8("SelectIP"))
        self.SelectIP.addItem(_fromUtf8(""))
        self.SelectIP.setItemText(0, _fromUtf8("IPv4"))
        self.SelectIP.addItem(_fromUtf8(""))
        self.SelectIP.setItemText(1, _fromUtf8("IPv6"))
        self.configLayout.addWidget(self.SelectIP, 1, 1, 1, 1)
        self.StatusBox = QtGui.QGroupBox(HostsUtlMain)
        self.StatusBox.setGeometry(QtCore.QRect(10, 120, 240, 90))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StatusBox.sizePolicy().hasHeightForWidth())
        self.StatusBox.setSizePolicy(sizePolicy)
        self.StatusBox.setObjectName(_fromUtf8("StatusBox"))
        self.layoutWidget1 = QtGui.QWidget(self.StatusBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 221, 40))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.StatusLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.StatusLayout.setMargin(0)
        self.StatusLayout.setObjectName(_fromUtf8("StatusLayout"))
        self.labelConn = QtGui.QLabel(self.layoutWidget1)
        self.labelConn.setObjectName(_fromUtf8("labelConn"))
        self.StatusLayout.addWidget(self.labelConn, 0, 0, 1, 1)
        self.labelConnStat = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelConnStat.setFont(font)
        self.labelConnStat.setObjectName(_fromUtf8("labelConnStat"))
        self.StatusLayout.addWidget(self.labelConnStat, 0, 1, 1, 1)
        self.labelOS = QtGui.QLabel(self.layoutWidget1)
        self.labelOS.setObjectName(_fromUtf8("labelOS"))
        self.StatusLayout.addWidget(self.labelOS, 1, 0, 1, 1)
        self.labelOSStat = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelOSStat.setFont(font)
        self.labelOSStat.setObjectName(_fromUtf8("labelOSStat"))
        self.StatusLayout.addWidget(self.labelOSStat, 1, 1, 1, 1)
        self.FunctionsBox = QtGui.QGroupBox(HostsUtlMain)
        self.FunctionsBox.setGeometry(QtCore.QRect(260, 20, 250, 290))
        self.FunctionsBox.setObjectName(_fromUtf8("FunctionsBox"))
        self.Functionlist = QtGui.QListWidget(self.FunctionsBox)
        self.Functionlist.setGeometry(QtCore.QRect(10, 20, 230, 260))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Functionlist.sizePolicy().hasHeightForWidth())
        self.Functionlist.setSizePolicy(sizePolicy)
        self.Functionlist.setObjectName(_fromUtf8("Functionlist"))
        self.frame = QtGui.QFrame(HostsUtlMain)
        self.frame.setGeometry(QtCore.QRect(520, 30, 110, 280))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.ButtonBackup = QtGui.QPushButton(self.frame)
        self.ButtonBackup.setGeometry(QtCore.QRect(0, 10, 48, 48))
        self.ButtonBackup.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/img/icon_backup.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonBackup.setIcon(icon1)
        self.ButtonBackup.setIconSize(QtCore.QSize(32, 32))
        self.ButtonBackup.setObjectName(_fromUtf8("ButtonBackup"))
        self.ButtonUpdate = QtGui.QPushButton(self.frame)
        self.ButtonUpdate.setGeometry(QtCore.QRect(60, 70, 48, 48))
        self.ButtonUpdate.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/img/icon_fetch.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonUpdate.setIcon(icon2)
        self.ButtonUpdate.setIconSize(QtCore.QSize(32, 32))
        self.ButtonUpdate.setObjectName(_fromUtf8("ButtonUpdate"))
        self.ButtonRestore = QtGui.QPushButton(self.frame)
        self.ButtonRestore.setGeometry(QtCore.QRect(60, 10, 48, 48))
        self.ButtonRestore.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/img/icon_restore.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonRestore.setIcon(icon3)
        self.ButtonRestore.setIconSize(QtCore.QSize(32, 32))
        self.ButtonRestore.setObjectName(_fromUtf8("ButtonRestore"))
        self.ButtonApply = QtGui.QPushButton(self.frame)
        self.ButtonApply.setGeometry(QtCore.QRect(0, 220, 48, 48))
        self.ButtonApply.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/img/icon_apply.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonApply.setIcon(icon4)
        self.ButtonApply.setIconSize(QtCore.QSize(32, 32))
        self.ButtonApply.setObjectName(_fromUtf8("ButtonApply"))
        self.ButtonExit = QtGui.QPushButton(self.frame)
        self.ButtonExit.setGeometry(QtCore.QRect(60, 220, 48, 48))
        self.ButtonExit.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/img/icon_exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonExit.setIcon(icon5)
        self.ButtonExit.setIconSize(QtCore.QSize(32, 32))
        self.ButtonExit.setObjectName(_fromUtf8("ButtonExit"))
        self.ButtonCheck = QtGui.QPushButton(self.frame)
        self.ButtonCheck.setGeometry(QtCore.QRect(0, 70, 48, 48))
        self.ButtonCheck.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/img/icon_update.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonCheck.setIcon(icon6)
        self.ButtonCheck.setIconSize(QtCore.QSize(32, 32))
        self.ButtonCheck.setObjectName(_fromUtf8("ButtonCheck"))
        self.ButtonANSI = QtGui.QPushButton(self.frame)
        self.ButtonANSI.setGeometry(QtCore.QRect(0, 160, 48, 48))
        self.ButtonANSI.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/img/icon_ansi.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonANSI.setIcon(icon7)
        self.ButtonANSI.setIconSize(QtCore.QSize(32, 32))
        self.ButtonANSI.setObjectName(_fromUtf8("ButtonANSI"))
        self.ButtonUTF = QtGui.QPushButton(self.frame)
        self.ButtonUTF.setGeometry(QtCore.QRect(60, 160, 48, 48))
        self.ButtonUTF.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/img/icon_utf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonUTF.setIcon(icon8)
        self.ButtonUTF.setIconSize(QtCore.QSize(32, 32))
        self.ButtonUTF.setObjectName(_fromUtf8("ButtonUTF"))
        self.InfoBox = QtGui.QGroupBox(HostsUtlMain)
        self.InfoBox.setGeometry(QtCore.QRect(10, 220, 240, 90))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InfoBox.sizePolicy().hasHeightForWidth())
        self.InfoBox.setSizePolicy(sizePolicy)
        self.InfoBox.setObjectName(_fromUtf8("InfoBox"))
        self.layoutWidget2 = QtGui.QWidget(self.InfoBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 221, 59))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.InfoLayout = QtGui.QGridLayout(self.layoutWidget2)
        self.InfoLayout.setMargin(0)
        self.InfoLayout.setObjectName(_fromUtf8("InfoLayout"))
        self.labelVersion = QtGui.QLabel(self.layoutWidget2)
        self.labelVersion.setObjectName(_fromUtf8("labelVersion"))
        self.InfoLayout.addWidget(self.labelVersion, 0, 0, 1, 1)
        self.labelVersionData = QtGui.QLabel(self.layoutWidget2)
        self.labelVersionData.setObjectName(_fromUtf8("labelVersionData"))
        self.InfoLayout.addWidget(self.labelVersionData, 0, 1, 1, 1)
        self.labelRelease = QtGui.QLabel(self.layoutWidget2)
        self.labelRelease.setObjectName(_fromUtf8("labelRelease"))
        self.InfoLayout.addWidget(self.labelRelease, 1, 0, 1, 1)
        self.labelReleaseData = QtGui.QLabel(self.layoutWidget2)
        self.labelReleaseData.setObjectName(_fromUtf8("labelReleaseData"))
        self.InfoLayout.addWidget(self.labelReleaseData, 1, 1, 1, 1)
        self.labelLatest = QtGui.QLabel(self.layoutWidget2)
        self.labelLatest.setObjectName(_fromUtf8("labelLatest"))
        self.InfoLayout.addWidget(self.labelLatest, 2, 0, 1, 1)
        self.labelLatestData = QtGui.QLabel(self.layoutWidget2)
        self.labelLatestData.setObjectName(_fromUtf8("labelLatestData"))
        self.InfoLayout.addWidget(self.labelLatestData, 2, 1, 1, 1)
        self.SelectLang = QtGui.QComboBox(HostsUtlMain)
        self.SelectLang.setGeometry(QtCore.QRect(520, 320, 108, 25))
        self.SelectLang.setObjectName(_fromUtf8("SelectLang"))
        self.labelIP.setBuddy(self.SelectMirror)
        self.labelMirror.setBuddy(self.SelectIP)

        self.retranslateUi(HostsUtlMain)
        QtCore.QObject.connect(self.ButtonExit, QtCore.SIGNAL(_fromUtf8("clicked()")), HostsUtlMain.close)
        QtCore.QObject.connect(self.SelectIP, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), HostsUtlMain.on_IPVersion_changed)
        QtCore.QObject.connect(self.SelectMirror, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), HostsUtlMain.on_Mirror_changed)
        QtCore.QObject.connect(self.Functionlist, QtCore.SIGNAL(_fromUtf8("itemChanged(QListWidgetItem*)")), HostsUtlMain.on_Selection_changed)
        QtCore.QObject.connect(self.ButtonApply, QtCore.SIGNAL(_fromUtf8("clicked()")), HostsUtlMain.on_MakeHosts_clicked)
        QtCore.QObject.connect(self.ButtonBackup, QtCore.SIGNAL(_fromUtf8("clicked()")), HostsUtlMain.on_Backup_clicked)
        QtCore.QObject.connect(self.ButtonRestore, QtCore.SIGNAL(_fromUtf8("clicked()")), HostsUtlMain.on_Restore_clicked)
        QtCore.QObject.connect(self.ButtonCheck, QtCore.SIGNAL(_fromUtf8("clicked()")), HostsUtlMain.on_CheckUpdate_clicked)
        QtCore.QObject.connect(self.ButtonUpdate, QtCore.SIGNAL(_fromUtf8("clicked()")), HostsUtlMain.on_FetchUpdate_clicked)
        QtCore.QObject.connect(self.SelectLang, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), HostsUtlMain.on_Lang_changed)
        QtCore.QObject.connect(self.ButtonANSI, QtCore.SIGNAL(_fromUtf8("clicked()")), HostsUtlMain.on_MakeANSI_clicked)
        QtCore.QObject.connect(self.ButtonUTF, QtCore.SIGNAL(_fromUtf8("clicked()")), HostsUtlMain.on_MakeUTF8_clicked)
        QtCore.QMetaObject.connectSlotsByName(HostsUtlMain)
        HostsUtlMain.setTabOrder(self.SelectMirror, self.SelectIP)
        HostsUtlMain.setTabOrder(self.SelectIP, self.Functionlist)
        HostsUtlMain.setTabOrder(self.Functionlist, self.ButtonApply)
        HostsUtlMain.setTabOrder(self.ButtonApply, self.ButtonExit)
        HostsUtlMain.setTabOrder(self.ButtonExit, self.ButtonCheck)
        HostsUtlMain.setTabOrder(self.ButtonCheck, self.ButtonUpdate)
        HostsUtlMain.setTabOrder(self.ButtonUpdate, self.ButtonBackup)
        HostsUtlMain.setTabOrder(self.ButtonBackup, self.ButtonRestore)

    def retranslateUi(self, HostsUtlMain):
        HostsUtlMain.setWindowTitle(_translate("HostsUtlMain", "Hosts Setup Utility", None))
        self.ConfigBox.setTitle(_translate("HostsUtlMain", "Config", None))
        self.labelIP.setText(_translate("HostsUtlMain", "Server", None))
        self.labelMirror.setText(_translate("HostsUtlMain", "IP Version", None))
        self.StatusBox.setTitle(_translate("HostsUtlMain", "Status", None))
        self.labelConn.setText(_translate("HostsUtlMain", "Connection", None))
        self.labelConnStat.setText(_translate("HostsUtlMain", "N/A", None))
        self.labelOS.setText(_translate("HostsUtlMain", "OS", None))
        self.labelOSStat.setText(_translate("HostsUtlMain", "N/A", None))
        self.FunctionsBox.setTitle(_translate("HostsUtlMain", "Functions", None))
        self.ButtonBackup.setToolTip(_translate("HostsUtlMain", "Backup hosts", None))
        self.ButtonBackup.setWhatsThis(_translate("HostsUtlMain", "Backup the hosts file of current system.", None))
        self.ButtonUpdate.setToolTip(_translate("HostsUtlMain", "Download data file", None))
        self.ButtonUpdate.setWhatsThis(_translate("HostsUtlMain", "Download the latest data file.", None))
        self.ButtonRestore.setToolTip(_translate("HostsUtlMain", "Restore backup", None))
        self.ButtonRestore.setWhatsThis(_translate("HostsUtlMain", "Restore a previous backup of hosts file.", None))
        self.ButtonApply.setToolTip(_translate("HostsUtlMain", "Apply hosts", None))
        self.ButtonApply.setWhatsThis(_translate("HostsUtlMain", "Apply changes to the hosts file.", None))
        self.ButtonExit.setToolTip(_translate("HostsUtlMain", "Exit", None))
        self.ButtonExit.setWhatsThis(_translate("HostsUtlMain", "Close this tool.", None))
        self.ButtonCheck.setToolTip(_translate("HostsUtlMain", "Check update / Refresh", None))
        self.ButtonCheck.setWhatsThis(_translate("HostsUtlMain", "Check the latest version of hosts data file.", None))
        self.ButtonANSI.setToolTip(_translate("HostsUtlMain", "Save with ANSI", None))
        self.ButtonANSI.setWhatsThis(_translate("HostsUtlMain", "Export to hosts file encoding by ANSI.", None))
        self.ButtonUTF.setToolTip(_translate("HostsUtlMain", "Save with UTF-8", None))
        self.ButtonUTF.setWhatsThis(_translate("HostsUtlMain", "Export to hosts file encoding by UTF-8.", None))
        self.InfoBox.setTitle(_translate("HostsUtlMain", "Hosts Info", None))
        self.labelVersion.setText(_translate("HostsUtlMain", "Version", None))
        self.labelVersionData.setText(_translate("HostsUtlMain", "N/A", None))
        self.labelRelease.setText(_translate("HostsUtlMain", "Release", None))
        self.labelReleaseData.setText(_translate("HostsUtlMain", "N/A", None))
        self.labelLatest.setText(_translate("HostsUtlMain", "Latest", None))
        self.labelLatestData.setText(_translate("HostsUtlMain", "N/A", None))

import qthosts_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HostsUtlMain = QtGui.QDialog()
    ui = Ui_HostsUtlMain()
    ui.setupUi(HostsUtlMain)
    HostsUtlMain.show()
    sys.exit(app.exec_())

