from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_MainWindow
import sys
import random

app = QtWidgets.QApplication(sys.argv)


MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.paper.hide()
ui.scissors.hide()
ui.rock.hide()
ui.result.hide()
ui.time_left.hide()
ui.time_text.hide()
ui.robot_text.hide()
MainWindow.show()
user_time = QtCore.QTimer()
user_time.setInterval(1000)
robot_time = QtCore.QTimer()
robot_time.setInterval(1000)
user_time_left = 10
robot_time_left = 3
robot_checkbox = False
user_chekbox = False
ukr_chekbox = True
eng_chekbox = False
robot_choice = None
user_choice = None
rsp = ['камінь','ножиці','папір','камінь','ножиці','папір']
def start():
    global user_chekbox
    global robot_checkbox
    global user_time_left
    global robot_time_left
    global robot_choice
    global user_choice
    user_time_left = 10
    robot_time_left = 3
    user_chekbox = False
    robot_checkbox = False
    robot_choice = None
    user_choice = None
    ui.label_text.hide()
    ui.play_bt.hide()
    ui.paper.show()
    ui.scissors.show()
    ui.rock.show()
    ui.time_left.show()
    ui.time_text.show()
    ui.robot_text.show()
    user_time.start()
    robot_time.start()
    ui.eng.hide()
    ui.pushButton_3.hide()

    if eng_chekbox:
        ui.time_text.setText('Time left:')
        ui.time_left.setText(str(user_time_left))
        ui.robot_text.setText('Robot choice')
        ui.rock.setText('Rock')
        ui.scissors.setText('Scissors')
        ui.paper.setText('Paper')
    if ukr_chekbox:
        ui.time_text.setText('Часу залишилось:')
        ui.time_left.setText(str(user_time_left))
        ui.robot_text.setText('Робот обирає')
        ui.rock.setText('Каміння')
        ui.scissors.setText('Ножиці')
        ui.paper.setText('Папір')


def lose():
    ui.paper.hide()
    ui.scissors.hide()
    ui.rock.hide()
    ui.time_left.hide()
    ui.time_text.hide()
    ui.robot_text.hide()
    if eng_chekbox:
        ui.result.setText('Go home')
        ui.label_text.setText('Lose')
    if ukr_chekbox:
        ui.result.setText('У меню')
        ui.label_text.setText('Програш')
    ui.label_text.show()
    ui.result.show()


def update_user_time():
    global user_time_left

    if user_time_left >= 0:
        ui.time_left.setText(str(user_time_left))
        user_time_left -= 1
    
    else:
        user_time.stop()
        lose()

def update_robot_time():
    global robot_time_left
    global robot_checkbox
    global user_chekbox
    global robot_choice
    if robot_time_left >= 0:
        robot_time_left -= 1
    
    else:
        robot_time.stop()
        if eng_chekbox:
            ui.robot_text.setText('Robot chose')
        if ukr_chekbox:
            ui.robot_text.setText('Робот обрав')
        robot_choice = random.choice(rsp)
        robot_checkbox = True

        if robot_checkbox and user_chekbox:
            if eng_chekbox:
                ui.result.setText('Result')
                ui.result.show()
            if ukr_chekbox:
                ui.result.setText("Результат")
                ui.result.show()

def rock():
    global user_choice
    global user_chekbox
    user_choice = 'камінь'
    user_chekbox = True
    ui.rock.hide()
    ui.paper.hide()
    ui.scissors.hide()
    user_time.stop()
    ui.time_left.hide()
    if eng_chekbox:
        ui.time_text.setText('You chose')
    if ukr_chekbox:
        ui.time_text.setText('Ти обрав')
    if robot_checkbox and user_chekbox:
        if eng_chekbox:
            ui.result.setText('Result')
            ui.result.show()
        if ukr_chekbox:
            ui.result.setText("Результат")
            ui.result.show()

def scissors():
    global user_choice
    global user_chekbox
    user_choice = 'ножиці'
    user_chekbox = True
    ui.rock.hide()
    ui.paper.hide()
    ui.scissors.hide()
    user_time.stop()
    ui.time_left.hide()
    if eng_chekbox:
        ui.time_text.setText('You chose')
    if ukr_chekbox:
        ui.time_text.setText('Ти обрав')
    if robot_checkbox and user_chekbox:
        if eng_chekbox:
            ui.result.setText('Result')
            ui.result.show()
        if ukr_chekbox:
            ui.result.setText("Результат")
            ui.result.show()

def paper():
    global user_choice
    global user_chekbox
    user_choice = 'папір'
    user_chekbox = True
    ui.rock.hide()
    ui.paper.hide()
    ui.scissors.hide()
    user_time.stop()
    ui.time_left.hide()
    if eng_chekbox:
        ui.time_text.setText('You chose')
    if ukr_chekbox:
        ui.time_text.setText('Ти обрав')
    if robot_checkbox and user_chekbox:
        if eng_chekbox:
            ui.result.setText('Result')
            ui.result.show()
        if ukr_chekbox:
            ui.result.setText("Результат")
            ui.result.show()

def go_home():
    ui.paper.hide()
    ui.scissors.hide()
    ui.rock.hide()
    ui.result.hide()
    ui.time_left.hide()
    ui.time_text.hide()
    ui.robot_text.hide()
    ui.label_text.show()
    ui.play_bt.show()
    ui.eng.show()
    ui.pushButton_3.show()
def result_ukr():
    global user_choice
    global robot_choice

    if user_choice == robot_choice:
         ui.time_text.setText('Нічия')
        
    elif user_choice == 'ножиці' and robot_choice == 'папір':
         ui.time_text.setText('Перемога')
        
    elif user_choice == 'папір' and robot_choice == 'ножиці':
         ui.time_text.setText('Програш')

    elif user_choice == 'камінь' and robot_choice == 'ножиці':
         ui.time_text.setText('Перемога')

    elif user_choice == 'ножиці' and robot_choice == 'камінь':
         ui.time_text.setText('Програш')

    elif user_choice == 'папір' and robot_choice == 'камінь':
         ui.time_text.setText('Перемога')
        
    elif user_choice == 'камінь' and robot_choice == 'папір':
         ui.time_text.setText('Програш')
    
    ui.result.setText('У меню')

def result_eng():
    global user_choice
    global robot_choice

    if user_choice == robot_choice:
         ui.time_text.setText('Нічия')
        
    elif user_choice == 'ножиці' and robot_choice == 'папір':
         ui.time_text.setText('Win')
        
    elif user_choice == 'папір' and robot_choice == 'ножиці':
         ui.time_text.setText('Lose')

    elif user_choice == 'камінь' and robot_choice == 'ножиці':
         ui.time_text.setText('Win')

    elif user_choice == 'ножиці' and robot_choice == 'камінь':
         ui.time_text.setText('Lose')

    elif user_choice == 'папір' and robot_choice == 'камінь':
         ui.time_text.setText('Win')
        
    elif user_choice == 'камінь' and robot_choice == 'папір':
         ui.time_text.setText('Lose')
    
    ui.result.setText('Go home')

def result():
    if ui.result.text() == 'Go home' or ui.result.text() == 'У меню':
          go_home()

    elif ui.result.text() == 'Результат':
         result_ukr()

    elif ui.result.text() == 'Result':
         result_eng()
def eng():
    global eng_chekbox
    global ukr_chekbox
    ukr_chekbox = False
    eng_chekbox = True
    ui.play_bt.setText('Play')
    ui.label_text.setText('Rock    Scissors    Paper')
def ukr():
    global eng_chekbox
    global ukr_chekbox
    ukr_chekbox = True
    eng_chekbox = False
    ui.play_bt.setText('Грати')
    ui.label_text.setText('Камінь    Ножиці    Бумага')

ui.pushButton_3.clicked.connect(ukr)
ui.eng.clicked.connect(eng)
ui.result.clicked.connect(result)
ui.scissors.clicked.connect(scissors)
ui.paper.clicked.connect(paper)
ui.rock.clicked.connect(rock)
robot_time.timeout.connect(update_robot_time)
user_time.timeout.connect(update_user_time)
ui.play_bt.clicked.connect(start)
sys.exit(app.exec_())