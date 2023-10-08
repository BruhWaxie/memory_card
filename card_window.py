from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QRadioButton, QHBoxLayout, QMessageBox, QWidget, QLabel, QPushButton, QVBoxLayout, QSpinBox, QGroupBox, QButtonGroup

menu_btn = QPushButton('Меню')
sleep_btn = QPushButton('Відпочити')
time_box = QSpinBox()
time_lb = QLabel("хвилин")

time_box.setValue(30)


line1 = QHBoxLayout()


line1.addWidget(menu_btn)
line1.addStretch(1)
line1.addWidget(sleep_btn)
line1.addWidget(time_box)
line1.addWidget(time_lb)

question = QLabel('Яблуко')

btn1 = QRadioButton('Apple')
btn2 = QRadioButton('apply')
btn3 = QRadioButton('pear')
btn4 = QRadioButton('yabluko')

group_box = QGroupBox("Варіанти перекладу:")
radio_group = QButtonGroup()

radio_group.addButton(btn1)
radio_group.addButton(btn2)
radio_group.addButton(btn3)
radio_group.addButton(btn4)

col1 = QVBoxLayout()
col2 = QVBoxLayout()
line2 = QHBoxLayout()

col1.addWidget(btn1)
col1.addWidget(btn2)
col2.addWidget(btn3)
col2.addWidget(btn4)

line2.addLayout(col1)
line2.addLayout(col2)

answer_btn = QPushButton('Відповісти')

answer_box = QGroupBox('Результат тексту:')
result_lb = QLabel('Правильно')
right_lb = QLabel('Правильна відповідь:')

res_line = QVBoxLayout()
res_line.addWidget(result_lb, alignment=(Qt.AlignLeft | Qt.AlignTop))
res_line.addWidget(right_lb, alignment=Qt.AlignCenter, stretch= 2)

answer_box.setLayout(res_line)
answer_box.hide()

main_line = QVBoxLayout()
main_line.addLayout(line1)
main_line.addWidget(question, alignment=Qt.AlignCenter, stretch=1 )
group_box.setLayout(line2)
main_line.addWidget(group_box, stretch=8)
main_line.addWidget(answer_box, stretch=8)
main_line.addWidget(answer_btn, stretch=3)