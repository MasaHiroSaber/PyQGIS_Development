# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IsochronousCircleTool.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_isochronous_circle_dialog(object):
    def setupUi(self, isochronous_circle_dialog):
        isochronous_circle_dialog.setObjectName("isochronous_circle_dialog")
        isochronous_circle_dialog.resize(379, 291)
        self.verticalLayout = QtWidgets.QVBoxLayout(isochronous_circle_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(isochronous_circle_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.layer_facility_ComboBox_ictool = QgsMapLayerComboBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer_facility_ComboBox_ictool.sizePolicy().hasHeightForWidth())
        self.layer_facility_ComboBox_ictool.setSizePolicy(sizePolicy)
        self.layer_facility_ComboBox_ictool.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.layer_facility_ComboBox_ictool.setFont(font)
        self.layer_facility_ComboBox_ictool.setObjectName("layer_facility_ComboBox_ictool")
        self.horizontalLayout.addWidget(self.layer_facility_ComboBox_ictool)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(isochronous_circle_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.layer_area_ComboBox_ictool = QgsMapLayerComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layer_area_ComboBox_ictool.sizePolicy().hasHeightForWidth())
        self.layer_area_ComboBox_ictool.setSizePolicy(sizePolicy)
        self.layer_area_ComboBox_ictool.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.layer_area_ComboBox_ictool.setFont(font)
        self.layer_area_ComboBox_ictool.setObjectName("layer_area_ComboBox_ictool")
        self.horizontalLayout_2.addWidget(self.layer_area_ComboBox_ictool)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_6 = QtWidgets.QFrame(isochronous_circle_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.travel_mode_comboBox_ictool = QtWidgets.QComboBox(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.travel_mode_comboBox_ictool.sizePolicy().hasHeightForWidth())
        self.travel_mode_comboBox_ictool.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.travel_mode_comboBox_ictool.setFont(font)
        self.travel_mode_comboBox_ictool.setObjectName("travel_mode_comboBox_ictool")
        self.travel_mode_comboBox_ictool.addItem("")
        self.travel_mode_comboBox_ictool.addItem("")
        self.horizontalLayout_7.addWidget(self.travel_mode_comboBox_ictool)
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.precision_comboBox = QtWidgets.QComboBox(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.precision_comboBox.sizePolicy().hasHeightForWidth())
        self.precision_comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(10)
        self.precision_comboBox.setFont(font)
        self.precision_comboBox.setObjectName("precision_comboBox")
        self.precision_comboBox.addItem("")
        self.precision_comboBox.addItem("")
        self.precision_comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.precision_comboBox)
        self.horizontalLayout_7.addWidget(self.frame_8)
        self.horizontalLayout_6.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame = QtWidgets.QFrame(isochronous_circle_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_3.addWidget(self.frame_4, 0, QtCore.Qt.AlignLeft)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_ictool_ok = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ictool_ok.sizePolicy().hasHeightForWidth())
        self.button_ictool_ok.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MiSans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_ictool_ok.setFont(font)
        self.button_ictool_ok.setObjectName("button_ictool_ok")
        self.horizontalLayout_5.addWidget(self.button_ictool_ok)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(isochronous_circle_dialog)
        QtCore.QMetaObject.connectSlotsByName(isochronous_circle_dialog)

    def retranslateUi(self, isochronous_circle_dialog):
        _translate = QtCore.QCoreApplication.translate
        isochronous_circle_dialog.setWindowTitle(_translate("isochronous_circle_dialog", "构建区域等时圈"))
        self.label.setText(_translate("isochronous_circle_dialog", "设施点图层"))
        self.label_2.setText(_translate("isochronous_circle_dialog", "区域面图层"))
        self.label_3.setText(_translate("isochronous_circle_dialog", "出行方式"))
        self.travel_mode_comboBox_ictool.setItemText(0, _translate("isochronous_circle_dialog", "步行"))
        self.travel_mode_comboBox_ictool.setItemText(1, _translate("isochronous_circle_dialog", "驾车"))
        self.label_4.setText(_translate("isochronous_circle_dialog", "等时圈精度"))
        self.precision_comboBox.setItemText(0, _translate("isochronous_circle_dialog", "低"))
        self.precision_comboBox.setItemText(1, _translate("isochronous_circle_dialog", "中"))
        self.precision_comboBox.setItemText(2, _translate("isochronous_circle_dialog", "高"))
        self.label_5.setText(_translate("isochronous_circle_dialog", "PS：由于高德API限制，每秒最高并发为30次，所以数据量比较大时需要等待比较久"))
        self.button_ictool_ok.setText(_translate("isochronous_circle_dialog", "运行"))
from qgsmaplayercombobox import QgsMapLayerComboBox
import rc_rc
