# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(672, 636)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./source/icon/chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "版本信息与联系方式"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600; color:#ffaa00;\">VLPRVTL目标检测软件</span></h1><h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">开发者: </span><span style=\" font-size:x-large; font-weight:600; color:#55aaff;\">JoeyforJoy WHU222huan GanAHE</span></h2><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:600;\">1.当前版本 version 2.0.0. </span></h3><h3 style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:600;\">2.本软件遵循GPL v3.0 开源协议,如需使用请遵循开源协议,<br/>不可将此软件用于商业用途,不可将此软件申请为个人著作产品,<br/>不可将该软件用于违法犯罪行为,否则将依法追究法律责任. </span></h3><h3 style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:600;\">3.主页:</span><a href=\"https://www.ganahe.top/\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://www.ganahe.top/</span></a><span style=\" font-size:large; font-weight:600;\">.从主页获取更多详细信息.</span></h3><h3 style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:600;\">4.Github地址：[1]<span style=\" font-size:large; font-weight:600;\"> [3]</span><a href=\"https://www.github.com/ganah\"><span style=\" font-size:large; font-weight:600; text-decoration: underline; color:#0000ff;\">GanAHE</span></a></h3><p><img src=\"./source/about.jpg\" width=\"650\" height=\"350\"/></p></body></html>"))
