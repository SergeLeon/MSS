# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_performance_dockwidget.ui'
#
# Created by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_PerformanceDockWidget(object):
    def setupUi(self, PerformanceDockWidget):
        PerformanceDockWidget.setObjectName(_fromUtf8("PerformanceDockWidget"))
        PerformanceDockWidget.resize(1032, 172)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PerformanceDockWidget.sizePolicy().hasHeightForWidth())
        PerformanceDockWidget.setSizePolicy(sizePolicy)
        PerformanceDockWidget.setMinimumSize(QtCore.QSize(1001, 0))
        PerformanceDockWidget.setMaximumSize(QtCore.QSize(16777215, 172))
        self.verticalLayout_3 = QtGui.QVBoxLayout(PerformanceDockWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_7 = QtGui.QLabel(PerformanceDockWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_9.addWidget(self.label_7)
        self.cbURL = QtGui.QComboBox(PerformanceDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbURL.sizePolicy().hasHeightForWidth())
        self.cbURL.setSizePolicy(sizePolicy)
        self.cbURL.setEditable(True)
        self.cbURL.setObjectName(_fromUtf8("cbURL"))
        self.cbURL.addItem(_fromUtf8(""))
        self.cbURL.addItem(_fromUtf8(""))
        self.horizontalLayout_9.addWidget(self.cbURL)
        self.btGetCapabilities = QtGui.QPushButton(PerformanceDockWidget)
        self.btGetCapabilities.setObjectName(_fromUtf8("btGetCapabilities"))
        self.horizontalLayout_9.addWidget(self.btGetCapabilities)
        self.tbViewCapabilities = QtGui.QToolButton(PerformanceDockWidget)
        self.tbViewCapabilities.setObjectName(_fromUtf8("tbViewCapabilities"))
        self.horizontalLayout_9.addWidget(self.tbViewCapabilities)
        self.line_4 = QtGui.QFrame(PerformanceDockWidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_9.addWidget(self.line_4)
        self.btComputePerformance = QtGui.QPushButton(PerformanceDockWidget)
        self.btComputePerformance.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btComputePerformance.setFont(font)
        self.btComputePerformance.setObjectName(_fromUtf8("btComputePerformance"))
        self.horizontalLayout_9.addWidget(self.btComputePerformance)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(PerformanceDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(40, 0))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.cbMode = QtGui.QComboBox(PerformanceDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbMode.sizePolicy().hasHeightForWidth())
        self.cbMode.setSizePolicy(sizePolicy)
        self.cbMode.setMinimumSize(QtCore.QSize(200, 0))
        self.cbMode.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbMode.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.cbMode.setMinimumContentsLength(0)
        self.cbMode.setObjectName(_fromUtf8("cbMode"))
        self.cbMode.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cbMode)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_11 = QtGui.QLabel(PerformanceDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(40, 0))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_2.addWidget(self.label_11)
        self.cbAircraft = QtGui.QComboBox(PerformanceDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbAircraft.sizePolicy().hasHeightForWidth())
        self.cbAircraft.setSizePolicy(sizePolicy)
        self.cbAircraft.setMinimumSize(QtCore.QSize(200, 0))
        self.cbAircraft.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbAircraft.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.cbAircraft.setFrame(True)
        self.cbAircraft.setObjectName(_fromUtf8("cbAircraft"))
        self.cbAircraft.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cbAircraft)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.teLayerAbstract = QtGui.QTextEdit(PerformanceDockWidget)
        self.teLayerAbstract.setMinimumSize(QtCore.QSize(242, 0))
        self.teLayerAbstract.setReadOnly(True)
        self.teLayerAbstract.setObjectName(_fromUtf8("teLayerAbstract"))
        self.verticalLayout.addWidget(self.teLayerAbstract)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.line_2 = QtGui.QFrame(PerformanceDockWidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_6.addWidget(self.line_2)
        self.stackedWidget = QtGui.QStackedWidget(PerformanceDockWidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(550, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.cbTimeOn = QtGui.QCheckBox(self.page)
        self.cbTimeOn.setEnabled(False)
        self.cbTimeOn.setMinimumSize(QtCore.QSize(95, 0))
        self.cbTimeOn.setMaximumSize(QtCore.QSize(120, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.cbTimeOn.setPalette(palette)
        self.cbTimeOn.setChecked(True)
        self.cbTimeOn.setObjectName(_fromUtf8("cbTimeOn"))
        self.horizontalLayout_8.addWidget(self.cbTimeOn)
        self.dteTime = QtGui.QDateTimeEdit(self.page)
        self.dteTime.setMinimumSize(QtCore.QSize(180, 0))
        self.dteTime.setMaximumSize(QtCore.QSize(250, 16777215))
        self.dteTime.setDate(QtCore.QDate(2010, 1, 18))
        self.dteTime.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(8, 0, 0)))
        self.dteTime.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dteTime.setMinimumTime(QtCore.QTime(8, 0, 0))
        self.dteTime.setCalendarPopup(False)
        self.dteTime.setTimeSpec(QtCore.Qt.UTC)
        self.dteTime.setObjectName(_fromUtf8("dteTime"))
        self.horizontalLayout_8.addWidget(self.dteTime)
        self.label = QtGui.QLabel(self.page)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_8.addWidget(self.label)
        self.sbWaypoint = QtGui.QSpinBox(self.page)
        self.sbWaypoint.setMaximum(999)
        self.sbWaypoint.setObjectName(_fromUtf8("sbWaypoint"))
        self.horizontalLayout_8.addWidget(self.sbWaypoint)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.tbMoreOptions = QtGui.QToolButton(self.page)
        self.tbMoreOptions.setObjectName(_fromUtf8("tbMoreOptions"))
        self.horizontalLayout_8.addWidget(self.tbMoreOptions)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.cbWeightOn = QtGui.QCheckBox(self.page)
        self.cbWeightOn.setEnabled(False)
        self.cbWeightOn.setMinimumSize(QtCore.QSize(95, 0))
        self.cbWeightOn.setMaximumSize(QtCore.QSize(120, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.cbWeightOn.setPalette(palette)
        self.cbWeightOn.setCheckable(True)
        self.cbWeightOn.setChecked(True)
        self.cbWeightOn.setObjectName(_fromUtf8("cbWeightOn"))
        self.horizontalLayout_4.addWidget(self.cbWeightOn)
        self.sbWeight = QtGui.QSpinBox(self.page)
        self.sbWeight.setMinimumSize(QtCore.QSize(180, 0))
        self.sbWeight.setMaximumSize(QtCore.QSize(250, 16777215))
        self.sbWeight.setMinimum(1)
        self.sbWeight.setMaximum(999999)
        self.sbWeight.setSingleStep(1000)
        self.sbWeight.setProperty("value", 60000)
        self.sbWeight.setObjectName(_fromUtf8("sbWeight"))
        self.horizontalLayout_4.addWidget(self.sbWeight)
        self.line_5 = QtGui.QFrame(self.page)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout_4.addWidget(self.line_5)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cbInitialisationOn = QtGui.QCheckBox(self.page)
        self.cbInitialisationOn.setEnabled(False)
        self.cbInitialisationOn.setMinimumSize(QtCore.QSize(95, 0))
        self.cbInitialisationOn.setMaximumSize(QtCore.QSize(120, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.cbInitialisationOn.setPalette(palette)
        self.cbInitialisationOn.setObjectName(_fromUtf8("cbInitialisationOn"))
        self.horizontalLayout_3.addWidget(self.cbInitialisationOn)
        self.cbInitTime = QtGui.QComboBox(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbInitTime.sizePolicy().hasHeightForWidth())
        self.cbInitTime.setSizePolicy(sizePolicy)
        self.cbInitTime.setMinimumSize(QtCore.QSize(180, 0))
        self.cbInitTime.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbInitTime.setObjectName(_fromUtf8("cbInitTime"))
        self.cbInitTime.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cbInitTime)
        self.tbInitTime_cbback = QtGui.QToolButton(self.page)
        self.tbInitTime_cbback.setObjectName(_fromUtf8("tbInitTime_cbback"))
        self.horizontalLayout_3.addWidget(self.tbInitTime_cbback)
        self.tbInitTime_cbfwd = QtGui.QToolButton(self.page)
        self.tbInitTime_cbfwd.setObjectName(_fromUtf8("tbInitTime_cbfwd"))
        self.horizontalLayout_3.addWidget(self.tbInitTime_cbfwd)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lblInterpolation = QtGui.QLabel(self.page_2)
        self.lblInterpolation.setObjectName(_fromUtf8("lblInterpolation"))
        self.horizontalLayout_7.addWidget(self.lblInterpolation)
        self.rbNWPnointerpolation = QtGui.QRadioButton(self.page_2)
        self.rbNWPnointerpolation.setChecked(True)
        self.rbNWPnointerpolation.setObjectName(_fromUtf8("rbNWPnointerpolation"))
        self.horizontalLayout_7.addWidget(self.rbNWPnointerpolation)
        self.rbNWPinterpolation = QtGui.QRadioButton(self.page_2)
        self.rbNWPinterpolation.setObjectName(_fromUtf8("rbNWPinterpolation"))
        self.horizontalLayout_7.addWidget(self.rbNWPinterpolation)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.lblAccuracy = QtGui.QLabel(self.page_2)
        self.lblAccuracy.setObjectName(_fromUtf8("lblAccuracy"))
        self.horizontalLayout_10.addWidget(self.lblAccuracy)
        self.sbAccuracy = QtGui.QSpinBox(self.page_2)
        self.sbAccuracy.setProperty("value", 5)
        self.sbAccuracy.setObjectName(_fromUtf8("sbAccuracy"))
        self.horizontalLayout_10.addWidget(self.sbAccuracy)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.tbOptionsBack = QtGui.QToolButton(self.page_2)
        self.tbOptionsBack.setObjectName(_fromUtf8("tbOptionsBack"))
        self.horizontalLayout_10.addWidget(self.tbOptionsBack)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.lblDecline = QtGui.QLabel(self.page_2)
        self.lblDecline.setObjectName(_fromUtf8("lblDecline"))
        self.horizontalLayout_11.addWidget(self.lblDecline)
        self.sbEngineDecline = QtGui.QSpinBox(self.page_2)
        self.sbEngineDecline.setObjectName(_fromUtf8("sbEngineDecline"))
        self.horizontalLayout_11.addWidget(self.sbEngineDecline)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        spacerItem6 = QtGui.QSpacerItem(20, 19, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_6.addWidget(self.stackedWidget)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.retranslateUi(PerformanceDockWidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PerformanceDockWidget)

    def retranslateUi(self, PerformanceDockWidget):
        PerformanceDockWidget.setWindowTitle(
            QtGui.QApplication.translate("PerformanceDockWidget", "Flight Performance Service Dock Widget", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("PerformanceDockWidget", "Flight Perf. Serv. URL:", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.cbURL.setToolTip(
            QtGui.QApplication.translate("PerformanceDockWidget", "Enter a valid flight performance service URL here.",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.cbURL.setItemText(0, QtGui.QApplication.translate("PerformanceDockWidget", "http://localhost:8002/fc_wms",
                                                               None, QtGui.QApplication.UnicodeUTF8))
        self.cbURL.setItemText(1, QtGui.QApplication.translate("PerformanceDockWidget",
                                                               "http://osm.omniscale.net/proxy/service", None,
                                                               QtGui.QApplication.UnicodeUTF8))
        self.btGetCapabilities.setToolTip(
            QtGui.QApplication.translate("PerformanceDockWidget", "Request the capabilities from the server.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btGetCapabilities.setText(QtGui.QApplication.translate("PerformanceDockWidget", "get capabilities", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.tbViewCapabilities.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", "view", None, QtGui.QApplication.UnicodeUTF8))
        self.btComputePerformance.setToolTip(QtGui.QApplication.translate("PerformanceDockWidget",
                                                                          "Request the computation of the flight "
                                                                          "performance with the specifed parameters.",
                                                                          None, QtGui.QApplication.UnicodeUTF8))
        self.btComputePerformance.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", "compute performance", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", "Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbMode.setItemText(0, QtGui.QApplication.translate("PerformanceDockWidget", "NO_NWP.TAKEOFF_WEIGHT", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("PerformanceDockWidget", "Aircraft configuration:", None,
                                                           QtGui.QApplication.UnicodeUTF8))
        self.cbAircraft.setToolTip(QtGui.QApplication.translate("PerformanceDockWidget",
                                                                "Choose an aircraft configuration you would like "
                                                                "to use.",
                                                                None, QtGui.QApplication.UnicodeUTF8))
        self.cbAircraft.setItemText(0, QtGui.QApplication.translate("PerformanceDockWidget", "HALO (+10 DC)", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.teLayerAbstract.setHtml(QtGui.QApplication.translate("PerformanceDockWidget", """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; \
-qt-block-indent:0; text-indent:0px; font-size:10pt;"><br /></p></body></html>""", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PerformanceDockWidget",
                                                          "Specify the time at an arbitrary waypoint and the "
                                                          "(takeoff or landing) weight of the aircraft:",
                                                          None, QtGui.QApplication.UnicodeUTF8))
        self.cbTimeOn.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", "Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.dteTime.setToolTip(QtGui.QApplication.translate("PerformanceDockWidget",
                                                             "The time at which you would like the aircraft to be at "
                                                             "the waypoint you specify in the edit field to the right.",
                                                             None, QtGui.QApplication.UnicodeUTF8))
        self.dteTime.setDisplayFormat(
            QtGui.QApplication.translate("PerformanceDockWidget", "yyyy/MM/dd hh:mm UTC", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PerformanceDockWidget", "at waypoint no.", None,
                                                        QtGui.QApplication.UnicodeUTF8))
        self.sbWaypoint.setToolTip(QtGui.QApplication.translate("PerformanceDockWidget",
                                                                "The number of the waypoint at which you would like "
                                                                "the aircraft to be at the time you have specified.",
                                                                None, QtGui.QApplication.UnicodeUTF8))
        self.tbMoreOptions.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", "(more)", None, QtGui.QApplication.UnicodeUTF8))
        self.cbWeightOn.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", "Weight:", None, QtGui.QApplication.UnicodeUTF8))
        self.sbWeight.setToolTip(QtGui.QApplication.translate("PerformanceDockWidget",
                                                              "Either the takeoff weight or the landing weight of "
                                                              "the aircraft, depending on the mode you have selected.",
                                                              None, QtGui.QApplication.UnicodeUTF8))
        self.sbWeight.setSuffix(
            QtGui.QApplication.translate("PerformanceDockWidget", " lbs", None, QtGui.QApplication.UnicodeUTF8))
        self.cbInitialisationOn.setText(QtGui.QApplication.translate("PerformanceDockWidget", "Initialisation:", None,
                                                                     QtGui.QApplication.UnicodeUTF8))
        self.cbInitTime.setToolTip(QtGui.QApplication.translate("PerformanceDockWidget",
                                                                "If the mode you have selected uses NWP data, "
                                                                "select a forecast initialisation time.",
                                                                None, QtGui.QApplication.UnicodeUTF8))
        self.cbInitTime.setItemText(0,
                                    QtGui.QApplication.translate("PerformanceDockWidget", "2010-12-12T00:00:00Z", None,
                                                                 QtGui.QApplication.UnicodeUTF8))
        self.tbInitTime_cbback.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.tbInitTime_cbfwd.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.lblInterpolation.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", "When using NWP data:", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.rbNWPnointerpolation.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", "use nearest grid point", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.rbNWPinterpolation.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", "interpolate linearly", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.lblAccuracy.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", "Computation points between waypoints:", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.tbOptionsBack.setText(
            QtGui.QApplication.translate("PerformanceDockWidget", "(back)", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDecline.setText(QtGui.QApplication.translate("PerformanceDockWidget", "Engine power decline:", None,
                                                             QtGui.QApplication.UnicodeUTF8))
        self.sbEngineDecline.setSuffix(
            QtGui.QApplication.translate("PerformanceDockWidget", " %", None, QtGui.QApplication.UnicodeUTF8))