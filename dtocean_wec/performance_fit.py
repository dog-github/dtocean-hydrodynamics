# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../designer/performance_fit.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(666, 567)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.rb_sd = QtGui.QRadioButton(self.groupBox)
        self.rb_sd.setObjectName(_fromUtf8("rb_sd"))
        self.verticalLayout.addWidget(self.rb_sd)
        self.rb_pm = QtGui.QRadioButton(self.groupBox)
        self.rb_pm.setObjectName(_fromUtf8("rb_pm"))
        self.verticalLayout.addWidget(self.rb_pm)
        self.rb_pto = QtGui.QRadioButton(self.groupBox)
        self.rb_pto.setObjectName(_fromUtf8("rb_pto"))
        self.verticalLayout.addWidget(self.rb_pto)
        self.rb_moo = QtGui.QRadioButton(self.groupBox)
        self.rb_moo.setObjectName(_fromUtf8("rb_moo"))
        self.verticalLayout.addWidget(self.rb_moo)
        self.rb_k_ext = QtGui.QRadioButton(self.groupBox)
        self.rb_k_ext.setObjectName(_fromUtf8("rb_k_ext"))
        self.verticalLayout.addWidget(self.rb_k_ext)
        self.rb_d_ext = QtGui.QRadioButton(self.groupBox)
        self.rb_d_ext.setObjectName(_fromUtf8("rb_d_ext"))
        self.verticalLayout.addWidget(self.rb_d_ext)
        self.gridLayout.addWidget(self.groupBox, 5, 0, 2, 2)
        self.mpl_window = QtGui.QWidget(Form)
        self.mpl_window.setObjectName(_fromUtf8("mpl_window"))
        self.mpl_vl = QtGui.QVBoxLayout(self.mpl_window)
        self.mpl_vl.setObjectName(_fromUtf8("mpl_vl"))
        self.gridLayout.addWidget(self.mpl_window, 6, 2, 2, 4)
        self.le_pfit_data = QtGui.QLineEdit(Form)
        self.le_pfit_data.setObjectName(_fromUtf8("le_pfit_data"))
        self.gridLayout.addWidget(self.le_pfit_data, 2, 0, 1, 4)
        self.btn_plot_pfit = QtGui.QPushButton(Form)
        self.btn_plot_pfit.setObjectName(_fromUtf8("btn_plot_pfit"))
        self.gridLayout.addWidget(self.btn_plot_pfit, 5, 2, 1, 4)
        self.cb_angle_index = QtGui.QComboBox(Form)
        self.cb_angle_index.setObjectName(_fromUtf8("cb_angle_index"))
        self.gridLayout.addWidget(self.cb_angle_index, 7, 0, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 7, 1, 1, 1)
        self.btn_load_pfit = QtGui.QPushButton(Form)
        self.btn_load_pfit.setObjectName(_fromUtf8("btn_load_pfit"))
        self.gridLayout.addWidget(self.btn_load_pfit, 2, 5, 1, 1)
        self.btn_browse_pfit = QtGui.QPushButton(Form)
        self.btn_browse_pfit.setObjectName(_fromUtf8("btn_browse_pfit"))
        self.gridLayout.addWidget(self.btn_browse_pfit, 2, 4, 1, 1)
        self.btn_fitting = QtGui.QPushButton(Form)
        self.btn_fitting.setObjectName(_fromUtf8("btn_fitting"))
        self.gridLayout.addWidget(self.btn_fitting, 3, 3, 1, 3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.wwAngle = QtGui.QDoubleSpinBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wwAngle.sizePolicy().hasHeightForWidth())
        self.wwAngle.setSizePolicy(sizePolicy)
        self.wwAngle.setMinimumSize(QtCore.QSize(0, 20))
        self.wwAngle.setMaximumSize(QtCore.QSize(200, 20))
        self.wwAngle.setMaximum(180.0)
        self.wwAngle.setObjectName(_fromUtf8("wwAngle"))
        self.gridLayout_2.addWidget(self.wwAngle, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.uiSpectrum = QtGui.QComboBox(Form)
        self.uiSpectrum.setObjectName(_fromUtf8("uiSpectrum"))
        self.uiSpectrum.addItem(_fromUtf8(""))
        self.uiSpectrum.addItem(_fromUtf8(""))
        self.uiSpectrum.addItem(_fromUtf8(""))
        self.uiSpectrum.addItem(_fromUtf8(""))
        self.uiSpectrum.addItem(_fromUtf8(""))
        self.uiSpectrum.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.uiSpectrum, 1, 1, 1, 1)
        self.uiGamma = QtGui.QDoubleSpinBox(Form)
        self.uiGamma.setMinimum(1.0)
        self.uiGamma.setMaximum(7.0)
        self.uiGamma.setObjectName(_fromUtf8("uiGamma"))
        self.gridLayout_2.addWidget(self.uiGamma, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.uiSpreading = QtGui.QDoubleSpinBox(Form)
        self.uiSpreading.setMinimum(-1.0)
        self.uiSpreading.setMaximum(50.0)
        self.uiSpreading.setObjectName(_fromUtf8("uiSpreading"))
        self.gridLayout_2.addWidget(self.uiSpreading, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 6)
        self.btn_skip_fit = QtGui.QPushButton(Form)
        self.btn_skip_fit.setObjectName(_fromUtf8("btn_skip_fit"))
        self.gridLayout.addWidget(self.btn_skip_fit, 3, 0, 1, 3)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Performance Fit - Module", None))
        self.groupBox.setTitle(_translate("Form", "Variable", None))
        self.rb_sd.setText(_translate("Form", "scatter diagram", None))
        self.rb_pm.setText(_translate("Form", "user provided power matrix", None))
        self.rb_pto.setText(_translate("Form", "pto damping", None))
        self.rb_moo.setText(_translate("Form", "mooring stiffness", None))
        self.rb_k_ext.setText(_translate("Form", "external damping", None))
        self.rb_d_ext.setText(_translate("Form", "external stiffness", None))
        self.le_pfit_data.setPlaceholderText(_translate("Form", "C:\\Users\\JohnDoe\\test_prj_inputs", None))
        self.btn_plot_pfit.setText(_translate("Form", "plot", None))
        self.label.setText(_translate("Form", "angle index", None))
        self.btn_load_pfit.setText(_translate("Form", "load data", None))
        self.btn_browse_pfit.setText(_translate("Form", "browse", None))
        self.btn_fitting.setText(_translate("Form", "Power Matrix Fitting", None))
        self.label_2.setText(_translate("Form", "Weatherwane angle semi-span [deg] \n"
" The full angle span i considered 2x the given value ", None))
        self.label_3.setText(_translate("Form", "Spectrum type", None))
        self.label_4.setText(_translate("Form", "Peak Enhancement Factor (only used in the Jonswap spectrum type)", None))
        self.uiSpectrum.setItemText(0, _translate("Form", "Jonswap", None))
        self.uiSpectrum.setItemText(1, _translate("Form", "Pierson_Moskowitz", None))
        self.uiSpectrum.setItemText(2, _translate("Form", "Bretschneider Mitsuyasu ", None))
        self.uiSpectrum.setItemText(3, _translate("Form", "Modified_Bretschneider Mitsuyasu", None))
        self.uiSpectrum.setItemText(4, _translate("Form", "Psc Swell", None))
        self.uiSpectrum.setItemText(5, _translate("Form", "Regular", None))
        self.label_5.setText(_translate("Form", "Spreading Paremeter", None))
        self.btn_skip_fit.setText(_translate("Form", "Skip Power Matrix Fitting", None))

