from random import choice, shuffle
from time import sleep
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QHBoxLayout, QMessageBox, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])

from card_window import *
from menu_window import *

class Question:
    current = None
    count_right = 0 #лічильник правильних відповідей
    count_ans = 0 #лічильник відповідей

    def __init__(self, question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

    def got_right(self):
        Question.count_ans += 1
        Question.count_right += 1
        print(Question.count_ans)
        print(Question.count_right)

    def got_wrong(self):
        Question.count_ans += 1
        print(Question.count_ans)

q1 = Question('УПА заснована...', '14 жовтня 1942', '18 серпня 1940', '24 серпня 1991', '1 грудня 1942')
q2 = Question('ІІ Світова Війна закінчилась...', '1 вересня 1945', '9 травня 1945', '2 вересня 1945', '16 серпня 1945')
q3 = Question('Тарас Шевченко помер...', '10 березня 1861', '10 березня 1863', '10 березня 1862', '10 березня 1859')
q4 = Question('Іван Франко народився...', '27 серпня 1856', '8 жовтня 1854', '3 серпня 1851', '11 грудня 1851')
q5 = Question('Леся Українка померла...', 'в Сумарі, Грузія', 'Тбілсі, Грузія', 'Франкфурт, Німеччина', 'Донецьк, Україна')
q6 = Question('Бій під Крутами відбувся...', '16 або 17 січня 1918', '21 або 22 грудня 1917', '11 або 12 лютого 1918', '18 або 19 січня 1918')
q7 = Question('Київ був збудований...', '430р.', '121р. до н.е.', '615р.', '412р.')
q8 = Question('І Світова Війна закінчилась...', '11 листопада 1918', '8 грудня 1918', '3 липня 1918', '1 серпня 1918')
q9 = Question('Під час голодомору померло...', '3млн. 941тис.', '4млн. 311тис.', '911тис.', '1млн. 110тис.')
q10 = Question('Перша столиця України -', 'Київ', 'Харків', 'Львів', 'Житомир')


questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
radio_buttons = [btn1, btn2, btn3, btn4]

main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(600, 500)
main_win.move(200,200)
main_win.setLayout(main_line)

def new_question():
    Question.current = choice(questions) #вибираємо випадкове питання
    question.setText(Question.current.question)
    right_lb.setText(Question.current.right_answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(Question.current.right_answer)

    radio_buttons[1].setText(Question.current.wrong_answer1)
    radio_buttons[2].setText(Question.current.wrong_answer2)
    radio_buttons[3].setText(Question.current.wrong_answer3)



new_question()


def check_result():
    radio_group.setExclusive(False)
    # перевіряємо правильність відповіді
    if radio_buttons[0].isChecked():
        Question.current.got_right()
        result_lb.setText("Правильно")
        radio_buttons[0].setChecked(False)
    else:
        Question.current.got_wrong()
        result_lb.setText("Неправильно")

    radio_group.setExclusive(True)


def click_btn():
    if answer_btn.text() == "Відповісти":
        check_result()
        group_box.hide()
        answer_box.show()
        answer_btn.setText("Наступне питання")
    else:
        answer_box.hide()
        group_box.show()
        answer_btn.setText("Відповісти")
        new_question()


def relax():
    pause_time = int(time_box.value()) * 60
    main_win.hide()
    sleep(pause_time)
    main_win.show()


def menu_show():
    main_win.hide()
    count_ans_lb.setText(f"Кількість відповідей: {Question.count_ans}")
    count_right_lb.setText(f"Кількість правильних відповідей: {Question.count_right}")
    success_lb.setText(f"Успішність: {2/4*100}%")
    menu_win.show()

def menu_hide():
    menu_win.hide()
    main_win.show()

def clear():
    le_quest.clear()
    le_right_ans.clear()
    le_wrong1.clear()
    le_wrong2.clear()
    le_wrong3.clear()

def add_question():
    new_q = Question(le_quest.text(),
                     le_right_ans.text(),
                     le_wrong1.text(),
                     le_wrong2.text(),
                     le_wrong3.text())
    questions.append(new_q)
    clear()

add_btn.clicked.connect(add_question)
clear_btn.clicked.connect(clear)

back_btn.clicked.connect(menu_hide)
answer_btn.clicked.connect(click_btn)
sleep_btn.clicked.connect(relax)
menu_btn.clicked.connect(menu_show)

main_win.show()
app.exec_()
