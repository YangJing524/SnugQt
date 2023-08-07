# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QToolButton, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(699, 782)
        self.gridLayout = QGridLayout(SettingsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.saveSettingsButton = QPushButton(SettingsDialog)
        self.saveSettingsButton.setObjectName(u"saveSettingsButton")

        self.gridLayout.addWidget(self.saveSettingsButton, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.settingsTab.setAutoFillBackground(True)
        self.gridLayout_4 = QGridLayout(self.settingsTab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.seedValue = QSpinBox(self.settingsTab)
        self.seedValue.setObjectName(u"seedValue")
        self.seedValue.setMinimum(-1)
        self.seedValue.setMaximum(999999999)
        self.seedValue.setValue(-1)

        self.gridLayout_4.addWidget(self.seedValue, 16, 1, 1, 2)

        self.sdxlRefinerStepsValue = QSpinBox(self.settingsTab)
        self.sdxlRefinerStepsValue.setObjectName(u"sdxlRefinerStepsValue")
        self.sdxlRefinerStepsValue.setMinimum(1)
        self.sdxlRefinerStepsValue.setMaximum(100)
        self.sdxlRefinerStepsValue.setValue(5)

        self.gridLayout_4.addWidget(self.sdxlRefinerStepsValue, 21, 1, 1, 2)

        self.cfgValue = QSpinBox(self.settingsTab)
        self.cfgValue.setObjectName(u"cfgValue")
        self.cfgValue.setMinimum(1)
        self.cfgValue.setMaximum(40)
        self.cfgValue.setValue(8)

        self.gridLayout_4.addWidget(self.cfgValue, 19, 1, 1, 2)

        self.label_2 = QLabel(self.settingsTab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 9, 0, 1, 1)

        self.stepsValue = QSpinBox(self.settingsTab)
        self.stepsValue.setObjectName(u"stepsValue")
        self.stepsValue.setMinimum(1)
        self.stepsValue.setMaximum(200)
        self.stepsValue.setValue(20)

        self.gridLayout_4.addWidget(self.stepsValue, 20, 1, 1, 2)

        self.label_16 = QLabel(self.settingsTab)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 21, 0, 1, 1)

        self.line_3 = QFrame(self.settingsTab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 7, 0, 1, 3)

        self.modeSelectCombo = QComboBox(self.settingsTab)
        self.modeSelectCombo.addItem("")
        self.modeSelectCombo.addItem("")
        self.modeSelectCombo.addItem("")
        self.modeSelectCombo.setObjectName(u"modeSelectCombo")

        self.gridLayout_4.addWidget(self.modeSelectCombo, 1, 1, 1, 2)

        self.hiresFixCheck = QCheckBox(self.settingsTab)
        self.hiresFixCheck.setObjectName(u"hiresFixCheck")

        self.gridLayout_4.addWidget(self.hiresFixCheck, 8, 0, 1, 1)

        self.label_4 = QLabel(self.settingsTab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 19, 0, 1, 1)

        self.label_6 = QLabel(self.settingsTab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 28, 0, 1, 1)

        self.label = QLabel(self.settingsTab)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 16, 0, 1, 1)

        self.schedulerValue = QComboBox(self.settingsTab)
        self.schedulerValue.addItem("")
        self.schedulerValue.addItem("")
        self.schedulerValue.addItem("")
        self.schedulerValue.addItem("")
        self.schedulerValue.addItem("")
        self.schedulerValue.setObjectName(u"schedulerValue")

        self.gridLayout_4.addWidget(self.schedulerValue, 28, 1, 1, 2)

        self.line_2 = QFrame(self.settingsTab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 26, 0, 1, 3)

        self.label_9 = QLabel(self.settingsTab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_14 = QLabel(self.settingsTab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)

        self.batchValue = QSpinBox(self.settingsTab)
        self.batchValue.setObjectName(u"batchValue")
        self.batchValue.setMinimum(1)
        self.batchValue.setMaximum(32)
        self.batchValue.setValue(2)

        self.gridLayout_4.addWidget(self.batchValue, 18, 1, 1, 2)

        self.samplerValue = QComboBox(self.settingsTab)
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.setObjectName(u"samplerValue")

        self.gridLayout_4.addWidget(self.samplerValue, 27, 1, 1, 2)

        self.label_20 = QLabel(self.settingsTab)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 17, 0, 1, 1)

        self.line = QFrame(self.settingsTab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 15, 0, 1, 3)

        self.hiresfixStepsValue = QSpinBox(self.settingsTab)
        self.hiresfixStepsValue.setObjectName(u"hiresfixStepsValue")
        self.hiresfixStepsValue.setMinimum(1)
        self.hiresfixStepsValue.setMaximum(200)
        self.hiresfixStepsValue.setValue(12)

        self.gridLayout_4.addWidget(self.hiresfixStepsValue, 13, 1, 1, 2)

        self.hiresfixScaleByValue = QDoubleSpinBox(self.settingsTab)
        self.hiresfixScaleByValue.setObjectName(u"hiresfixScaleByValue")
        self.hiresfixScaleByValue.setDecimals(2)
        self.hiresfixScaleByValue.setMinimum(1.000000000000000)
        self.hiresfixScaleByValue.setMaximum(3.000000000000000)
        self.hiresfixScaleByValue.setSingleStep(0.100000000000000)
        self.hiresfixScaleByValue.setValue(1.400000000000000)

        self.gridLayout_4.addWidget(self.hiresfixScaleByValue, 9, 1, 1, 2)

        self.label_7 = QLabel(self.settingsTab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 20, 0, 1, 1)

        self.imgWidthValue = QSpinBox(self.settingsTab)
        self.imgWidthValue.setObjectName(u"imgWidthValue")
        self.imgWidthValue.setMinimum(512)
        self.imgWidthValue.setMaximum(2048)
        self.imgWidthValue.setSingleStep(8)
        self.imgWidthValue.setValue(512)

        self.gridLayout_4.addWidget(self.imgWidthValue, 5, 1, 1, 2)

        self.useExternalVaeCheck = QCheckBox(self.settingsTab)
        self.useExternalVaeCheck.setObjectName(u"useExternalVaeCheck")

        self.gridLayout_4.addWidget(self.useExternalVaeCheck, 3, 0, 1, 1)

        self.label_3 = QLabel(self.settingsTab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 18, 0, 1, 1)

        self.label_5 = QLabel(self.settingsTab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 27, 0, 1, 1)

        self.label_13 = QLabel(self.settingsTab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 13, 0, 1, 1)

        self.imgHeightValue = QSpinBox(self.settingsTab)
        self.imgHeightValue.setObjectName(u"imgHeightValue")
        self.imgHeightValue.setMinimum(512)
        self.imgHeightValue.setMaximum(2048)
        self.imgHeightValue.setSingleStep(8)
        self.imgHeightValue.setValue(512)

        self.gridLayout_4.addWidget(self.imgHeightValue, 6, 1, 1, 2)

        self.line_4 = QFrame(self.settingsTab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 4, 0, 1, 3)

        self.label_10 = QLabel(self.settingsTab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 6, 0, 1, 1)

        self.iterationsValue = QSpinBox(self.settingsTab)
        self.iterationsValue.setObjectName(u"iterationsValue")
        self.iterationsValue.setMinimum(1)
        self.iterationsValue.setMaximum(100)

        self.gridLayout_4.addWidget(self.iterationsValue, 17, 1, 1, 2)

        self.tabWidget.addTab(self.settingsTab, "")
        self.modelsSettingsTab = QWidget()
        self.modelsSettingsTab.setObjectName(u"modelsSettingsTab")
        self.modelsSettingsTab.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.modelsSettingsTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_15 = QLabel(self.modelsSettingsTab)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)

        self.comfyuiModelFolderValue = QLineEdit(self.modelsSettingsTab)
        self.comfyuiModelFolderValue.setObjectName(u"comfyuiModelFolderValue")

        self.gridLayout_2.addWidget(self.comfyuiModelFolderValue, 0, 1, 1, 1)

        self.comfyuiModelFolderSelect = QToolButton(self.modelsSettingsTab)
        self.comfyuiModelFolderSelect.setObjectName(u"comfyuiModelFolderSelect")

        self.gridLayout_2.addWidget(self.comfyuiModelFolderSelect, 0, 2, 1, 1)

        self.label_19 = QLabel(self.modelsSettingsTab)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 1, 0, 1, 1)

        self.comfyuiVaeFolderValue = QLineEdit(self.modelsSettingsTab)
        self.comfyuiVaeFolderValue.setObjectName(u"comfyuiVaeFolderValue")

        self.gridLayout_2.addWidget(self.comfyuiVaeFolderValue, 1, 1, 1, 1)

        self.comfyuiVaeFolderSelect = QToolButton(self.modelsSettingsTab)
        self.comfyuiVaeFolderSelect.setObjectName(u"comfyuiVaeFolderSelect")

        self.gridLayout_2.addWidget(self.comfyuiVaeFolderSelect, 1, 2, 1, 1)

        self.line_5 = QFrame(self.modelsSettingsTab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 2, 0, 1, 2)

        self.label_8 = QLabel(self.modelsSettingsTab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_17 = QLabel(self.modelsSettingsTab)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 4, 0, 1, 1)

        self.line_6 = QFrame(self.modelsSettingsTab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_6, 5, 0, 1, 2)

        self.label_11 = QLabel(self.modelsSettingsTab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 6, 0, 1, 1)

        self.label_12 = QLabel(self.modelsSettingsTab)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 7, 0, 1, 1)

        self.label_18 = QLabel(self.modelsSettingsTab)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 8, 0, 1, 1)

        self.sd12CheckpointCombo = QComboBox(self.modelsSettingsTab)
        self.sd12CheckpointCombo.setObjectName(u"sd12CheckpointCombo")

        self.gridLayout_2.addWidget(self.sd12CheckpointCombo, 3, 1, 1, 2)

        self.sd12VaeCombo = QComboBox(self.modelsSettingsTab)
        self.sd12VaeCombo.setObjectName(u"sd12VaeCombo")

        self.gridLayout_2.addWidget(self.sd12VaeCombo, 4, 1, 1, 2)

        self.sdxlBaseCheckpointCombo = QComboBox(self.modelsSettingsTab)
        self.sdxlBaseCheckpointCombo.setObjectName(u"sdxlBaseCheckpointCombo")

        self.gridLayout_2.addWidget(self.sdxlBaseCheckpointCombo, 6, 1, 1, 2)

        self.sdxlRefinerCheckpointCombo = QComboBox(self.modelsSettingsTab)
        self.sdxlRefinerCheckpointCombo.setObjectName(u"sdxlRefinerCheckpointCombo")

        self.gridLayout_2.addWidget(self.sdxlRefinerCheckpointCombo, 7, 1, 1, 2)

        self.sdxlVaeCombo = QComboBox(self.modelsSettingsTab)
        self.sdxlVaeCombo.setObjectName(u"sdxlVaeCombo")

        self.gridLayout_2.addWidget(self.sdxlVaeCombo, 8, 1, 1, 2)

        self.tabWidget.addTab(self.modelsSettingsTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(SettingsDialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"SnugQT - Settings", None))
#if QT_CONFIG(tooltip)
        self.saveSettingsButton.setToolTip(QCoreApplication.translate("SettingsDialog", u"Save the current settings", None))
#endif // QT_CONFIG(tooltip)
        self.saveSettingsButton.setText(QCoreApplication.translate("SettingsDialog", u"Save settings", None))
#if QT_CONFIG(tooltip)
        self.seedValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Seed to use. -1 for random", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sdxlRefinerStepsValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Number of steps to perform with SDXL refiner", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cfgValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"CFG scale value", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Scale by:", None))
#if QT_CONFIG(tooltip)
        self.stepsValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Number of steps to perform when generating iamge", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("SettingsDialog", u"SDXL refiner steps:", None))
        self.modeSelectCombo.setItemText(0, QCoreApplication.translate("SettingsDialog", u"Stable Diffusion 1/2", None))
        self.modeSelectCombo.setItemText(1, QCoreApplication.translate("SettingsDialog", u"SDXL", None))
        self.modeSelectCombo.setItemText(2, QCoreApplication.translate("SettingsDialog", u"SDXL + Refiner", None))

#if QT_CONFIG(tooltip)
        self.modeSelectCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select the model architecture", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.hiresFixCheck.setToolTip(QCoreApplication.translate("SettingsDialog", u"Enable hi-res fix (only for SD1/2 models)", None))
#endif // QT_CONFIG(tooltip)
        self.hiresFixCheck.setText(QCoreApplication.translate("SettingsDialog", u"Hi-res fix (SD1/2 only)", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDialog", u"CFG scale:", None))
        self.label_6.setText(QCoreApplication.translate("SettingsDialog", u"Scheduler:", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Seed:", None))
        self.schedulerValue.setItemText(0, QCoreApplication.translate("SettingsDialog", u"normal", None))
        self.schedulerValue.setItemText(1, QCoreApplication.translate("SettingsDialog", u"karras", None))
        self.schedulerValue.setItemText(2, QCoreApplication.translate("SettingsDialog", u"exponential", None))
        self.schedulerValue.setItemText(3, QCoreApplication.translate("SettingsDialog", u"simple", None))
        self.schedulerValue.setItemText(4, QCoreApplication.translate("SettingsDialog", u"ddim_uniform", None))

#if QT_CONFIG(tooltip)
        self.schedulerValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Noise scheduler to use", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("SettingsDialog", u"Width:", None))
        self.label_14.setText(QCoreApplication.translate("SettingsDialog", u"Mode:", None))
#if QT_CONFIG(tooltip)
        self.batchValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"How many images to generate at once. More VRAM", None))
#endif // QT_CONFIG(tooltip)
        self.samplerValue.setItemText(0, QCoreApplication.translate("SettingsDialog", u"euler", None))
        self.samplerValue.setItemText(1, QCoreApplication.translate("SettingsDialog", u"euler_ancestral", None))
        self.samplerValue.setItemText(2, QCoreApplication.translate("SettingsDialog", u"heun", None))
        self.samplerValue.setItemText(3, QCoreApplication.translate("SettingsDialog", u"dpm_2", None))
        self.samplerValue.setItemText(4, QCoreApplication.translate("SettingsDialog", u"dpm_2_ancestral", None))
        self.samplerValue.setItemText(5, QCoreApplication.translate("SettingsDialog", u"lms", None))
        self.samplerValue.setItemText(6, QCoreApplication.translate("SettingsDialog", u"dpmpp_2s_ancestral", None))
        self.samplerValue.setItemText(7, QCoreApplication.translate("SettingsDialog", u"dpmpp_sde", None))
        self.samplerValue.setItemText(8, QCoreApplication.translate("SettingsDialog", u"dpmpp_sde_gpu", None))
        self.samplerValue.setItemText(9, QCoreApplication.translate("SettingsDialog", u"dpmpp_2m", None))
        self.samplerValue.setItemText(10, QCoreApplication.translate("SettingsDialog", u"dpmpp_2m_sde", None))
        self.samplerValue.setItemText(11, QCoreApplication.translate("SettingsDialog", u"dpmpp_2m_sde_gpu", None))
        self.samplerValue.setItemText(12, QCoreApplication.translate("SettingsDialog", u"ddim", None))
        self.samplerValue.setItemText(13, QCoreApplication.translate("SettingsDialog", u"uni_pc", None))
        self.samplerValue.setItemText(14, QCoreApplication.translate("SettingsDialog", u"uni_pc_bh2", None))

#if QT_CONFIG(tooltip)
        self.samplerValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Noise sampler to use", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("SettingsDialog", u"Iterations:", None))
#if QT_CONFIG(tooltip)
        self.hiresfixScaleByValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Factor to scale hires-fix image by", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("SettingsDialog", u"Steps:", None))
#if QT_CONFIG(tooltip)
        self.imgWidthValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Width of the generated image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.useExternalVaeCheck.setToolTip(QCoreApplication.translate("SettingsDialog", u"Use an external VAE, or use model built-in VAE", None))
#endif // QT_CONFIG(tooltip)
        self.useExternalVaeCheck.setText(QCoreApplication.translate("SettingsDialog", u"Use external VAE", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Batch size:", None))
        self.label_5.setText(QCoreApplication.translate("SettingsDialog", u"Sampler:", None))
        self.label_13.setText(QCoreApplication.translate("SettingsDialog", u"Hi-res fix steps:", None))
#if QT_CONFIG(tooltip)
        self.imgHeightValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Height of the generated image", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("SettingsDialog", u"Height:", None))
#if QT_CONFIG(tooltip)
        self.iterationsValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Number of iterations to perform", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.label_15.setText(QCoreApplication.translate("SettingsDialog", u"ComfyUI models folder: ", None))
#if QT_CONFIG(tooltip)
        self.comfyuiModelFolderValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Path to a ComfyUI model folder", None))
#endif // QT_CONFIG(tooltip)
        self.comfyuiModelFolderValue.setText(QCoreApplication.translate("SettingsDialog", u"ComfyUI\\models\\checkpoints", None))
        self.comfyuiModelFolderSelect.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
        self.label_19.setText(QCoreApplication.translate("SettingsDialog", u"ComfyUI VAE folder:", None))
#if QT_CONFIG(tooltip)
        self.comfyuiVaeFolderValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Path to a ComfyUI VAE folder", None))
#endif // QT_CONFIG(tooltip)
        self.comfyuiVaeFolderValue.setText(QCoreApplication.translate("SettingsDialog", u"ComfyUI\\models\\vae", None))
        self.comfyuiVaeFolderSelect.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
        self.label_8.setText(QCoreApplication.translate("SettingsDialog", u"Stable Diffusion 1/2 model:", None))
        self.label_17.setText(QCoreApplication.translate("SettingsDialog", u"Stable Diffusion 1/2 VAE:", None))
        self.label_11.setText(QCoreApplication.translate("SettingsDialog", u"SDXL Base model:", None))
        self.label_12.setText(QCoreApplication.translate("SettingsDialog", u"SDXL Refiner model:", None))
        self.label_18.setText(QCoreApplication.translate("SettingsDialog", u"SDXL VAE:", None))
#if QT_CONFIG(tooltip)
        self.sd12CheckpointCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select SD1/2 checkpoint", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sd12VaeCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select SD1/2 external VAE", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sdxlBaseCheckpointCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select SDXL base model", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sdxlRefinerCheckpointCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select the SDXL refiner model", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sdxlVaeCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select the SDXL external VAE", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modelsSettingsTab), QCoreApplication.translate("SettingsDialog", u"Models", None))
    # retranslateUi

