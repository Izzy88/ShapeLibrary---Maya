# -*- coding: utf-8 -*-
from PySide2 import QtWidgets, QtCore


class Ui_forma_main(object):
    def setupUi(self, forma_main):
        forma_main.setObjectName("forma_main")
        forma_main.resize(239, 98)
        self.verticalLayoutWidget = QtWidgets.QWidget(forma_main)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 241, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_main = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_main.setContentsMargins(5, 5, 5, 5)
        self.layout_main.setObjectName("layout_main")
        self.layout_shape_name = QtWidgets.QHBoxLayout()
        self.layout_shape_name.setObjectName("layout_shape_name")
        self.label_shape_name = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_shape_name.sizePolicy().hasHeightForWidth())
        self.label_shape_name.setSizePolicy(sizePolicy)
        self.label_shape_name.setObjectName("label_shape_name")
        self.layout_shape_name.addWidget(self.label_shape_name)
        self.text_edit_shape_name = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_edit_shape_name.sizePolicy().hasHeightForWidth())
        self.text_edit_shape_name.setSizePolicy(sizePolicy)
        self.text_edit_shape_name.setMaximumSize(QtCore.QSize(16777215, 30))
        self.text_edit_shape_name.setObjectName("text_edit_shape_name")
        self.layout_shape_name.addWidget(self.text_edit_shape_name)
        self.layout_main.addLayout(self.layout_shape_name)
        self.layout_shape_type = QtWidgets.QHBoxLayout()
        self.layout_shape_type.setObjectName("layout_shape_type")
        self.label_shape_type = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_shape_type.sizePolicy().hasHeightForWidth())
        self.label_shape_type.setSizePolicy(sizePolicy)
        self.label_shape_type.setObjectName("label_shape_type")
        self.layout_shape_type.addWidget(self.label_shape_type)
        self.radio_btn_2d = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_btn_2d.sizePolicy().hasHeightForWidth())
        self.radio_btn_2d.setSizePolicy(sizePolicy)
        self.radio_btn_2d.setChecked(True)
        self.radio_btn_2d.setObjectName("radio_btn_2d")
        self.layout_shape_type.addWidget(self.radio_btn_2d)
        self.radio_btn_3d = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_btn_3d.setObjectName("radio_btn_3d")
        self.layout_shape_type.addWidget(self.radio_btn_3d)
        self.layout_main.addLayout(self.layout_shape_type)
        self.layout_btn_save = QtWidgets.QHBoxLayout()
        self.layout_btn_save.setObjectName("layout_btn_save")
        self.btn_save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setObjectName("btn_save")
        self.layout_btn_save.addWidget(self.btn_save)
        self.layout_main.addLayout(self.layout_btn_save)

        self.retranslateUi(forma_main)
        QtCore.QMetaObject.connectSlotsByName(forma_main)

    def retranslateUi(self, forma_main):
        _translate = QtCore.QCoreApplication.translate
        forma_main.setWindowTitle(_translate("forma_main", "Save - Shape Library"))
        self.label_shape_name.setText(_translate("forma_main", "Shape Name"))
        self.label_shape_type.setText(_translate("forma_main", "Shape Type"))
        self.radio_btn_2d.setText(_translate("forma_main", "2D"))
        self.radio_btn_3d.setText(_translate("forma_main", "3D"))
        self.btn_save.setText(_translate("forma_main", "Save"))
