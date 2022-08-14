import sys
from tkinter import TRUE
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from numpy import False_
from assets import source
import json
from palette import PaletteGrid, PaletteHorizontal, PaletteVertical
from toggleButton import Switch
import random


class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainScreenDialog.ui", self)
        self.buttonGame1main.clicked.connect(self.gotoGame1)
        self.buttonExitApp.clicked.connect(QCoreApplication.instance().quit)

    def gotoGame1(self):
        widget.setCurrentWidget(game1window)
        # game1window = Game1Window()
        # widget.addWidget(game1window)
        # widget.setCurrentIndex(1)


class Game1Window(QDialog):

    NodeConfigDefault = {}
    Nodeconfig = {}
    StatusBuzzer = " "
    StatusVibration = " "
    SelectedEmotion = " "
    SelectedColor = " "

    def __init__(self):
        super(Game1Window, self).__init__()
        loadUi("mainGame1ScreenDialog.ui", self)
        self.buttonGame1ReturnMain.clicked.connect(self.gotoMain)
        self.buttonGame1Config.clicked.connect(self.gotoConfig)
        self.buttonGame1Play.clicked.connect(self.gotoPlay)
        self.InitDefaultValues()
        # self.configgame1window = ConfigGame1Window()
        # widget.addWidget(self.configgame1window)
        # self.playgame1window = PlayGame1Window()
        # widget.addWidget(self.playgame1window)


    def gotoPlay(self):
        widget.setCurrentWidget(playgame1window)
        # widget.setCurrentIndex(3)

    def gotoConfig(self):
        widget.setCurrentWidget(configgame1window)
       # widget.setCurrentIndex(2)

    def gotoMain(self):
        widget.setCurrentWidget(mainwindow)
        #widget.setCurrentIndex(0)

    def InitDefaultValues(self):

        try:
            with open('Game1Settings.json', 'r') as fp:
                self.NodeConfig = json.load(fp)
                # for i in range(6):
                #     print(self.NodeConfig['Node' + str(i)])
        except IOError:
            print('File not found, will create a new one.')
            # Default values
            for i in range(6):
                self.NodeConfigDefault['Node' + str(i)] = {
                    'Color': '#00FF00',
                    'Feed': 'ZANAHORIA',
                    'Feed_idx':'0',
                    'Buzzer': 'ON',
                    'Vibration': 'OFF',
                }
            with open('Game1Settings.json', 'w') as f:
                json.dump(self.NodeConfigDefault, f, indent=4)


class ConfigGame1Window(QDialog):

    Nodeconfig = {}
    NodeSelected = 0
    FeedList = ["FELIZ", "TRISTE", "ENFADADO",
                   "SORPRENDIDO", "ASUSTADO", "AVERGONZADO", ]
    ColorSelected = "#000000"
    VibrationStatus = "OFF"
    BuzzerStatus = "OFF"
    EmotionSelected = "none"

    def __init__(self):
        super(ConfigGame1Window, self).__init__()
        loadUi("configGame1ScreenDialog.ui", self)
        self.buttonConfigGame1Exit.clicked.connect(self.gotoMain)
        self.buttonNode1.clicked.connect(self.onButton)
        self.buttonNode2.clicked.connect(self.onButton)
        self.buttonNode3.clicked.connect(self.onButton)
        self.buttonNode4.clicked.connect(self.onButton)
        self.buttonNode5.clicked.connect(self.onButton)
        self.buttonNode6.clicked.connect(self.onButton)
        self.labelColorNode.setText("Botón no selecionado")
        self.buttonSetColor1.clicked.connect(self.selectColor)
        self.buttonSetColor2.clicked.connect(self.selectColor)
        self.buttonSetColor3.clicked.connect(self.selectColor)
        self.buttonSetColor4.clicked.connect(self.selectColor)
        self.buttonSetColor5.clicked.connect(self.selectColor)
        self.buttonSetColor6.clicked.connect(self.selectColor)
        self.buttonSetColor7.clicked.connect(self.selectColor)
        self.buttonSetColor8.clicked.connect(self.selectColor)
        self.checkBoxBuzzer.stateChanged.connect(self.stateBuzzer)
        self.checkBoxVibration.stateChanged.connect(self.stateVibration)
        self.comboBoxEmotions.addItems(self.FeedList)
        self.comboBoxEmotions.currentIndexChanged.connect(self.selectedEmotion)
        self.buttonConfigGame1Save.clicked.connect(self.saveConfig)
        self.LoadNodesConfig()
        self.HideAllWidgets()

    def HideAllWidgets(self):
        self.labelColorNode.hide()
        self.buttonColorNode.hide()
        self.checkBoxBuzzer.hide()
        self.checkBoxVibration.hide()
        self.labelOptionColors.hide()
        self.buttonSetColor1.hide()
        self.buttonSetColor2.hide()
        self.buttonSetColor3.hide()
        self.buttonSetColor4.hide()
        self.buttonSetColor5.hide()
        self.buttonSetColor6.hide()
        self.buttonSetColor7.hide()
        self.buttonSetColor8.hide()
        self.labelBuzzer.hide()
        self.labelVibration.hide()
        self.labelEmotionActual.hide()
        self.buttonEmotionActual.hide()
        self.labelSelectEmotion.hide()
        self.comboBoxEmotions.hide()
        self.buttonConfigGame1Save.hide()
        self.buttonConfigGame1Exit.hide()

    def ShowAllWidgets(self):
        self.labelColorNode.show()
        self.buttonColorNode.show()
        self.checkBoxBuzzer.show()
        self.checkBoxVibration.show()
        self.labelOptionColors.show()
        self.buttonSetColor1.show()
        self.buttonSetColor2.show()
        self.buttonSetColor3.show()
        self.buttonSetColor4.show()
        self.buttonSetColor5.show()
        self.buttonSetColor6.show()
        self.buttonSetColor7.show()
        self.buttonSetColor8.show()
        self.labelBuzzer.show()
        self.labelVibration.show()
        self.labelEmotionActual.show()
        self.buttonEmotionActual.show()
        self.labelSelectEmotion.show()
        self.comboBoxEmotions.show()
        self.buttonConfigGame1Save.show()
        self.buttonConfigGame1Exit.show()

    def LoadNodesConfig(self):

        try:
            with open('Settings.json', 'r') as fp:
                self.NodeConfig = json.load(fp)
                # for i in range(6):
                #     print(self.NodeConfig['Node' + str(i)])
        except IOError:
            print('File not found, will create a new one.')

    def onButton(self):

        self.ShowAllWidgets()
        self.LoadNodesConfig()
        button = self.sender()
        self.labelColorNode.setText("COLOR %s:" % button.text())
        self.labelBuzzer.setText("ESTADO CHICHARRA %s:" % button.text())
        self.labelVibration.setText("ESTADO VIBRACIÓN %s:" % button.text())
        self.labelEmotionActual.setText("EMOCIÓN ACTUAL %s:" % button.text())
        if button.text() == 'BOTÓN 1':
            self.NodeSelected = 0
        elif button.text() == 'BOTÓN 2':
            self.NodeSelected = 1
        elif button.text() == 'BOTÓN 3':
            self.NodeSelected = 2
        elif button.text() == 'BOTÓN 4':
            self.NodeSelected = 3
        elif button.text() == 'BOTÓN 5':
            self.NodeSelected = 4
        elif button.text() == 'BOTÓN 6':
            self.NodeSelected = 5

        print('Node' + str(self.NodeSelected))
        print(self.NodeConfig['Node' + str(self.NodeSelected)]['Color'])
        print(self.NodeConfig['Node' + str(self.NodeSelected)]['Buzzer'])
        print(self.NodeConfig['Node' + str(self.NodeSelected)]['Vibration'])
        print(self.NodeConfig['Node' + str(self.NodeSelected)]['Emotion'])

        self.buttonColorNode.setStyleSheet(
            "background-color:%s" % self.NodeConfig['Node' + str(self.NodeSelected)]['Color'])
        self.ColorSelected = self.NodeConfig['Node' +
                                             str(self.NodeSelected)]['Color']

        if self.NodeConfig['Node' + str(self.NodeSelected)]['Buzzer'] == "OFF":
            self.checkBoxBuzzer.setChecked(False)
        elif self.NodeConfig['Node' + str(self.NodeSelected)]['Buzzer'] == "ON":
            self.checkBoxBuzzer.setChecked(True)
        if self.NodeConfig['Node' + str(self.NodeSelected)]['Vibration'] == "OFF":
            self.checkBoxVibration.setChecked(False)
        elif self.NodeConfig['Node' + str(self.NodeSelected)]['Vibration'] == "ON":
            self.checkBoxVibration.setChecked(True)

        self.buttonEmotionActual.setText(
            self.NodeConfig['Node' + str(self.NodeSelected)]['Emotion'])

        self.EmotionSelected = self.NodeConfig['Node' +
                                               str(self.NodeSelected)]['Emotion']
        self.VibrationStatus = self.NodeConfig['Node' +
                                               str(self.NodeSelected)]['Vibration']
        self.BuzzerStatus = self.NodeConfig['Node' +
                                            str(self.NodeSelected)]['Buzzer']

    def selectColor(self):
        button = self.sender()
        if button.objectName() == 'buttonSetColor1':
            self.buttonColorNode.setStyleSheet(
                "background-color:#FF0000")
            self.ColorSelected = "#FF0000"
        if button.objectName() == 'buttonSetColor2':
            self.buttonColorNode.setStyleSheet(
                "background-color:#4E9A06")
            self.ColorSelected = "#4E9A06"
        if button.objectName() == 'buttonSetColor3':
            self.buttonColorNode.setStyleSheet(
                "background-color:#FCE94F")
            self.ColorSelected = "#FCE94F"
        if button.objectName() == 'buttonSetColor4':
            self.buttonColorNode.setStyleSheet(
                "background-color:#204A87")
            self.ColorSelected = "#204A87"
        if button.objectName() == 'buttonSetColor5':
            self.buttonColorNode.setStyleSheet(
                "background-color:#8F5902")
            self.ColorSelected = "#8F5902"
        if button.objectName() == 'buttonSetColor6':
            self.buttonColorNode.setStyleSheet(
                "background-color:#F57900")
            self.ColorSelected = "#F57900"
        if button.objectName() == 'buttonSetColor7':
            self.buttonColorNode.setStyleSheet(
                "background-color:#5C3566")
            self.ColorSelected = "#5C3566"
        if button.objectName() == 'buttonSetColor8':
            self.buttonColorNode.setStyleSheet(
                "background-color:#FF00DD")
            self.ColorSelected = "#FF00DD"

    def stateBuzzer(self):
        if self.checkBoxBuzzer.isChecked():
            self.BuzzerStatus = "ON"
        else:
            self.BuzzerStatus = "OFF"

    def stateVibration(self):
        if self.checkBoxVibration.isChecked():
            self.VibrationStatus = "ON"
        else:
            self.VibrationStatus = "OFF"

    def selectedEmotion(self, value):
        self.buttonEmotionActual.setText(self.comboBoxEmotions.currentText())
        self.EmotionSelected = self.comboBoxEmotions.currentText()

    def saveConfig(self):
        try:
            with open('Settings.json',) as fp:
                json_data = json.load(fp)
                json_data['Node' + str(self.NodeSelected)
                          ]['Color'] = self.ColorSelected
                json_data['Node' + str(self.NodeSelected)
                          ]['Vibration'] = self.VibrationStatus
                json_data['Node' + str(self.NodeSelected)
                          ]['Buzzer'] = self.BuzzerStatus
                json_data['Node' + str(self.NodeSelected)
                          ]['Emotion'] = self.EmotionSelected
            with open('Settings.json', 'w') as fp:
                json.dump(json_data, fp, indent=4)
                fp.close()
        except IOError:
            print('File not found, error')

        self.HideAllWidgets()
        # widget.setCurrentIndex(1)
        widget.setCurrentWidget(game1window)

    def gotoMain(self):
        self.ColorSelected = "#000000"
        self.VibrationStatus = "OFF"
        self.BuzzerStatus = "OFF"
        self.EmotionSelected = "none"
        self.HideAllWidgets()
        #widget.setCurrentIndex(1)
        widget.setCurrentWidget(game1window)


class PlayGame1Window(QDialog):

    Food_images = ['Carrot.png', 'Cheese.png', 'Bone.png', 'Fish.png', 'Apple.png', 'Grain.png', 'Grass.png', 'Milk.png','Acorn.png','Worm.png']
    Index_images = 0

    def __init__(self):
        super(PlayGame1Window, self).__init__()
        loadUi("playGame1ScreenDialog.ui", self)
        self.buttonplayGame1ReturnMain.clicked.connect(self.gotoMain)
        self.buttonplayGame1Backward.clicked.connect(self.gotoPlay)
        self.buttonplayGame1Run.clicked.connect(self.gotoPlay)
        self.buttonplayGame1Forward.clicked.connect(self.gotoPlay)
        self.canvas.setText("VAMOS A DIVERTIRNOS")
        self.canvas.show()

    def gotoPlay(self):

        button = self.sender()

        if button.objectName() == 'buttonplayGame1Run':

            self.canvas.setText(" ")
            self.random_index = random.randint(0, len(self.Food_images)-1)
            self.Index_images = self.random_index
            self.canvas.setStyleSheet(
                "image : url("+":/prefijoNuevo/images/" + (self.Food_images[self.random_index]) + ")")

        if button.objectName() == 'buttonplayGame1Backward':

            if (self.Index_images == 0):
                self.canvas.setStyleSheet(
                "image : url("+":/prefijoNuevo/images/" + (self.Food_images[self.Index_images]) + ")")
            else :
                self.Index_images=self.Index_images-1
                self.canvas.setStyleSheet(
                "image : url("+":/prefijoNuevo/images/" + (self.Food_images[self.Index_images]) + ")")


        if button.objectName() == 'buttonplayGame1Forward':

            if (self.Index_images >= len(self.Food_images)-1):
                self.canvas.setStyleSheet(
                "image : url("+":/prefijoNuevo/images/" + (self.Food_images[self.Index_images]) + ")")
            else:
                self.Index_images=self.Index_images+1
                self.canvas.setStyleSheet(
                "image : url("+":/prefijoNuevo/images/" + (self.Food_images[self.Index_images]) + ")")

    def gotoMain(self):
        self.canvas.setStyleSheet(" background-color: rgb(qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0)), 53, 102);")
        widget.setCurrentIndex(1)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
widget.addWidget(mainwindow)
game1window = Game1Window()
widget.addWidget(game1window)
configgame1window = ConfigGame1Window()
widget.addWidget(configgame1window)
playgame1window = PlayGame1Window()
widget.addWidget(playgame1window)
widget.setFixedHeight(1024)
widget.setFixedWidth(1280)
widget.setCurrentWidget(mainwindow)
widget.show()
ColorNode = "none"
StatusBuzzerNode = "disable"
StatuVibration = "disable"
EmotioNode = "none"

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
