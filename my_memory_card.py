from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup)
from random import shuffle

class Question:
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
window = QWidget()

window.resize(400,200)
window.setWindowTitle('Memory Card')

rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')

RadioGroupBox = QGroupBox('Варианты ответов')


LayoutAns1 = QHBoxLayout()
LayoutAns2 = QVBoxLayout()
LayoutAns3 = QVBoxLayout()
LayoutAns4 = QVBoxLayout()
LayoutAns2.addWidget(rbtn1)
LayoutAns2.addWidget(rbtn2)
LayoutAns3.addWidget(rbtn3)
LayoutAns3.addWidget(rbtn4)

LayoutAns1.addLayout(LayoutAns2)
LayoutAns1.addLayout(LayoutAns3)

RadioGroupBox.setLayout(LayoutAns1)

question = QLabel('Какой национальности не существует?')

ans_button = QPushButton('Ответить')

ans_group = QGroupBox('Результат теста')
lb_result = QLabel('Прав ты или нет?')
lb_correct = QLabel('Правильный ответ')

ans_layout = QVBoxLayout()
ans_layout.addWidget(lb_result, alignment=Qt.AlignHCenter)
ans_layout.addWidget(lb_correct, alignment=Qt.AlignHCenter)
ans_group.setLayout(ans_layout)

LayoutAns4.addWidget(question, alignment=Qt.AlignHCenter)
LayoutAns4.addWidget(RadioGroupBox, alignment=Qt.AlignHCenter)
LayoutAns4.addWidget(ans_group, alignment=Qt.AlignHCenter)
LayoutAns4.addWidget(ans_button, alignment=Qt.AlignHCenter)

ans_group.hide()
window.setLayout(LayoutAns4)

def show_result():
    RadioGroupBox.hide()
    ans_group.show()
    ans_button.setText('Следующий вопрос')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)


def show_question():
    RadioGroupBox.show()
    ans_group.hide()
    ans_button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)



def test():
    if 'Ответить' == ans_button.text():
        check_answer()
    else:
        next_question()

answers = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(quest):
    shuffle(answers)
    answers[0].setText(quest.right_ans)
    answers[1].setText(quest.wrong1)
    answers[2].setText(quest.wrong2)
    answers[3].setText(quest.wrong3)
    question.setText(quest.question)
    lb_correct.setText(quest.right_ans)
    show_question()


def show_correct(res):
    lb_result.setText(res)
    show_result()



def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    elif answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked():
        show_correct('Неправильно!')


ans_button.clicked.connect(test)

q = Question('На какой сигнал светофора можно ехать?', 'Зеленый', 'Красный', 'Желтый', 'Синий')
q2 = Question('Государственный язык в Эсватини?', 'Свати', 'Ток-писин', 'Квама', 'Сарси')
q3 = Question('Государственнй язык в Тунисе?', 'Арабский', 'Египетский', 'Французский', 'Латинский')

questions = [q, q2, q3]

window.question_num = -1
def next_question():
    window.question_num += 1
    if window.question_num >= len(questions):
        window.question_num = 0
    ask(questions[window.question_num])

next_question()
window.show()
app.exec_()

