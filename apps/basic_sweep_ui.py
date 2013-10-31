# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/basic_sweep.ui'
#
# Created: Thu Oct 31 14:35:30 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SweepDialog(object):
    def setupUi(self, SweepDialog):
        SweepDialog.setObjectName(_fromUtf8("SweepDialog"))
        SweepDialog.resize(1020, 830)
        SweepDialog.setWindowTitle(QtGui.QApplication.translate("SweepDialog", "KIDleidoscope", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(SweepDialog)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.plot_group_box = QtGui.QGroupBox(SweepDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.plot_group_box.sizePolicy().hasHeightForWidth())
        self.plot_group_box.setSizePolicy(sizePolicy)
        self.plot_group_box.setAutoFillBackground(False)
        self.plot_group_box.setFlat(False)
        self.plot_group_box.setObjectName(_fromUtf8("plot_group_box"))
        self.horizontalLayout_14.addWidget(self.plot_group_box)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox = QtGui.QGroupBox(SweepDialog)
        self.groupBox.setTitle(QtGui.QApplication.translate("SweepDialog", "Coarse Sweep", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText(QtGui.QApplication.translate("SweepDialog", "Start:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.spin_start_freq = QtGui.QDoubleSpinBox(self.groupBox)
        self.spin_start_freq.setSuffix(QtGui.QApplication.translate("SweepDialog", " MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_start_freq.setDecimals(3)
        self.spin_start_freq.setMaximum(256.0)
        self.spin_start_freq.setProperty("value", 110.001)
        self.spin_start_freq.setObjectName(_fromUtf8("spin_start_freq"))
        self.horizontalLayout.addWidget(self.spin_start_freq)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("SweepDialog", "Stop:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spin_stop_freq = QtGui.QDoubleSpinBox(self.groupBox)
        self.spin_stop_freq.setFrame(True)
        self.spin_stop_freq.setSuffix(QtGui.QApplication.translate("SweepDialog", " MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_stop_freq.setDecimals(3)
        self.spin_stop_freq.setMaximum(256.0)
        self.spin_stop_freq.setProperty("value", 210.0)
        self.spin_stop_freq.setObjectName(_fromUtf8("spin_stop_freq"))
        self.horizontalLayout_2.addWidget(self.spin_stop_freq)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("SweepDialog", "Step:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.combo_step_size = QtGui.QComboBox(self.groupBox)
        self.combo_step_size.setObjectName(_fromUtf8("combo_step_size"))
        self.combo_step_size.addItem(_fromUtf8(""))
        self.combo_step_size.setItemText(0, QtGui.QApplication.translate("SweepDialog", " 62.5 kHz", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_step_size.addItem(_fromUtf8(""))
        self.combo_step_size.setItemText(1, QtGui.QApplication.translate("SweepDialog", "125 kHz", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_step_size.addItem(_fromUtf8(""))
        self.combo_step_size.setItemText(2, QtGui.QApplication.translate("SweepDialog", "250 kHz", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_step_size.addItem(_fromUtf8(""))
        self.combo_step_size.setItemText(3, QtGui.QApplication.translate("SweepDialog", "500 kHz", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_step_size.addItem(_fromUtf8(""))
        self.combo_step_size.setItemText(4, QtGui.QApplication.translate("SweepDialog", "1.00 MHz", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_3.addWidget(self.combo_step_size)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.push_start_sweep = QtGui.QPushButton(self.groupBox)
        self.push_start_sweep.setText(QtGui.QApplication.translate("SweepDialog", "Start Coarse Sweep", None, QtGui.QApplication.UnicodeUTF8))
        self.push_start_sweep.setAutoDefault(False)
        self.push_start_sweep.setObjectName(_fromUtf8("push_start_sweep"))
        self.verticalLayout_2.addWidget(self.push_start_sweep)
        self.push_abort = QtGui.QPushButton(self.groupBox)
        self.push_abort.setText(QtGui.QApplication.translate("SweepDialog", "Abort Sweep", None, QtGui.QApplication.UnicodeUTF8))
        self.push_abort.setAutoDefault(False)
        self.push_abort.setObjectName(_fromUtf8("push_abort"))
        self.verticalLayout_2.addWidget(self.push_abort)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setText(QtGui.QApplication.translate("SweepDialog", "Not working yet:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_13.addWidget(self.label_7)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setSuffix(QtGui.QApplication.translate("SweepDialog", " dBm/tone", None, QtGui.QApplication.UnicodeUTF8))
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(-50.0)
        self.doubleSpinBox.setMaximum(0.0)
        self.doubleSpinBox.setSingleStep(0.5)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.horizontalLayout_13.addWidget(self.doubleSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.label_coarse_info = QtGui.QLabel(self.groupBox)
        self.label_coarse_info.setText(QtGui.QApplication.translate("SweepDialog", "Spacing:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_coarse_info.setObjectName(_fromUtf8("label_coarse_info"))
        self.verticalLayout_2.addWidget(self.label_coarse_info)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setText(QtGui.QApplication.translate("SweepDialog", "Sub-sweeps:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_11.addWidget(self.label_5)
        self.spin_subsweeps = QtGui.QSpinBox(self.groupBox)
        self.spin_subsweeps.setMinimum(1)
        self.spin_subsweeps.setMaximum(200)
        self.spin_subsweeps.setObjectName(_fromUtf8("spin_subsweeps"))
        self.horizontalLayout_11.addWidget(self.spin_subsweeps)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(SweepDialog)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("SweepDialog", "Fine Sweep", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setText(QtGui.QApplication.translate("SweepDialog", "Span (Hz):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        self.line_span_hz = QtGui.QLineEdit(self.groupBox_2)
        self.line_span_hz.setText(QtGui.QApplication.translate("SweepDialog", "20000", None, QtGui.QApplication.UnicodeUTF8))
        self.line_span_hz.setObjectName(_fromUtf8("line_span_hz"))
        self.horizontalLayout_7.addWidget(self.line_span_hz)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setText(QtGui.QApplication.translate("SweepDialog", "Points:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.line_npoints = QtGui.QLineEdit(self.groupBox_2)
        self.line_npoints.setText(QtGui.QApplication.translate("SweepDialog", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.line_npoints.setObjectName(_fromUtf8("line_npoints"))
        self.horizontalLayout_8.addWidget(self.line_npoints)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.label_spacing = QtGui.QLabel(self.groupBox_2)
        self.label_spacing.setText(QtGui.QApplication.translate("SweepDialog", "Spacing:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_spacing.setObjectName(_fromUtf8("label_spacing"))
        self.verticalLayout_7.addWidget(self.label_spacing)
        self.push_start_fine_sweep = QtGui.QPushButton(self.groupBox_2)
        self.push_start_fine_sweep.setText(QtGui.QApplication.translate("SweepDialog", "Start Fine Sweep", None, QtGui.QApplication.UnicodeUTF8))
        self.push_start_fine_sweep.setAutoDefault(False)
        self.push_start_fine_sweep.setObjectName(_fromUtf8("push_start_fine_sweep"))
        self.verticalLayout_7.addWidget(self.push_start_fine_sweep)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout_12.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_status = QtGui.QLabel(SweepDialog)
        self.label_status.setText(QtGui.QApplication.translate("SweepDialog", "status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.verticalLayout_3.addWidget(self.label_status)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.push_add_resonator = QtGui.QPushButton(SweepDialog)
        self.push_add_resonator.setText(QtGui.QApplication.translate("SweepDialog", "Add Selected Point", None, QtGui.QApplication.UnicodeUTF8))
        self.push_add_resonator.setObjectName(_fromUtf8("push_add_resonator"))
        self.horizontalLayout_9.addWidget(self.push_add_resonator)
        self.push_clear_all = QtGui.QPushButton(SweepDialog)
        self.push_clear_all.setText(QtGui.QApplication.translate("SweepDialog", "Clear All", None, QtGui.QApplication.UnicodeUTF8))
        self.push_clear_all.setAutoDefault(False)
        self.push_clear_all.setObjectName(_fromUtf8("push_clear_all"))
        self.horizontalLayout_9.addWidget(self.push_clear_all)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.tableview_freqs = QtGui.QTableWidget(SweepDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableview_freqs.sizePolicy().hasHeightForWidth())
        self.tableview_freqs.setSizePolicy(sizePolicy)
        self.tableview_freqs.setObjectName(_fromUtf8("tableview_freqs"))
        self.tableview_freqs.setColumnCount(0)
        self.tableview_freqs.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableview_freqs)
        self.horizontalLayout_12.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.push_save = QtGui.QPushButton(SweepDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_save.sizePolicy().hasHeightForWidth())
        self.push_save.setSizePolicy(sizePolicy)
        self.push_save.setText(QtGui.QApplication.translate("SweepDialog", "Start Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.push_save.setAutoDefault(False)
        self.push_save.setObjectName(_fromUtf8("push_save"))
        self.horizontalLayout_4.addWidget(self.push_save)
        self.line_filename = QtGui.QLineEdit(SweepDialog)
        self.line_filename.setReadOnly(True)
        self.line_filename.setObjectName(_fromUtf8("line_filename"))
        self.horizontalLayout_4.addWidget(self.line_filename)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_14.addLayout(self.verticalLayout_6)

        self.retranslateUi(SweepDialog)
        self.combo_step_size.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SweepDialog)

    def retranslateUi(self, SweepDialog):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SweepDialog = QtGui.QDialog()
    ui = Ui_SweepDialog()
    ui.setupUi(SweepDialog)
    SweepDialog.show()
    sys.exit(app.exec_())

