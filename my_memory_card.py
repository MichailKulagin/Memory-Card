#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QRadioButton, QMessageBox, QHBoxLayout, QGroupBox, QButtonGroup
from random import randint, shuffle

#создание приложения и главного окна
app = QApplication([])

main_win = QWidget()

main_win.resize(500,300)
main_win.setWindowTitle('Вопросник')

text = QLabel('Какой национальности не сучествует?')

#групировка
RadioGroupBox = QGroupBox('Варианты ответов')
but1 = QRadioButton('Энцы')
but2 = QRadioButton('Чулымцы')
but3 = QRadioButton('Смурфы')
but4 = QRadioButton('Алеуты')


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(but1)
layout_ans2.addWidget(but2)
layout_ans3.addWidget(but3)
layout_ans3.addWidget(but4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
# правильный ответ 
TGroupBox = QGroupBox('Результаты теста')
otvet = QLabel('Правильный ответ')
layout_quest = QHBoxLayout()
layout_quest.addWidget(otvet)
TGroupBox.setLayout(layout_quest)
# не правильный ответ
FGroupBox = QGroupBox('Результаты теста')
otvet = QLabel('Неверный ответ')
layout_quest = QHBoxLayout()
layout_quest.addWidget(otvet)
FGroupBox.setLayout(layout_quest)

StatGroupBox = QGroupBox('Рейтинг')
otvet = QLabel('0')
layout_quest = QHBoxLayout()
layout_quest.addWidget(otvet)
StatGroupBox.setLayout(layout_quest)

botton = QPushButton('Ответить')
Sledbotton = QPushButton('Следующий вопрос')

#расположение виджетов по лэйаутам
loyouth1 = QHBoxLayout()
loyouth2 = QHBoxLayout()
loyouth5Bootton = QHBoxLayout()
loyouth2.addWidget(FGroupBox, alignment=Qt.AlignCenter)
loyouth2.addWidget(TGroupBox, alignment=Qt.AlignCenter)
loyouth2.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
loyouth2.addWidget(StatGroupBox, alignment=Qt.AlignCenter)
loyouth1.addWidget(text, alignment=Qt.AlignCenter)
loyouth5Bootton.addWidget(botton, alignment=Qt.AlignCenter)
loyouth5Bootton.addWidget(Sledbotton, alignment=Qt.AlignCenter)


loyout_main = QVBoxLayout()
loyout_main.addLayout(loyouth1)
loyout_main.addStretch(1)
loyout_main.addLayout(loyouth2)
loyout_main.addStretch(1)
loyout_main.addLayout(loyouth5Bootton)
main_win.setLayout(loyout_main)


#размер кнопки ответить и следующий
loyouth5Bootton.addStretch(1)
loyouth5Bootton.addWidget(botton, stretch=1)
loyouth5Bootton.addWidget(Sledbotton, stretch=1)
loyouth5Bootton.addStretch(1)

loyouth2.addStretch(1)
loyouth2.addWidget(RadioGroupBox, stretch=5)
loyouth2.addWidget(FGroupBox, stretch=5)
loyouth2.addWidget(TGroupBox, stretch=5)
loyouth2.addStretch(1)


#скрываем обекты
StatGroupBox.hide()
TGroupBox.hide()
FGroupBox.hide()
Sledbotton.hide()

#создание класа
class Question():
    def __init__(self,question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



#создаем списоккнопок
answers = [but1, but2,but3, but4]

#перемешиваем
def ask(question):
    shuffle(answers)
    text.setText(question.question)
    answers[0].setText(question.right_answer)
    answers[1].setText(question.wrong1)
    answers[2].setText(question.wrong2)
    answers[3].setText(question.wrong3)


#обработка нажатий на кнопки

def otvet_T():
    global t_otvet, chet, c
    t_otvet+=1
    c = t_otvet/chet * 100
    c = int(c)
    print('Всего вопросов: ', chet)
    print('Правильных ответов: ', t_otvet)
    print('Рейтинг: ', c,'%')
    RadioGroupBox.hide()
    botton.hide()
    Sledbotton.show()
    TGroupBox.show()

def otvet_F():
    global t_otvet, chet, c   
    c = t_otvet/chet * 100
    c = int(c)
    print('Всего вопросов: ', chet)
    print('Правильных ответов: ', t_otvet)
    print('Рейтинг: ', c,'%')
    RadioGroupBox.hide()
    botton.hide()
    Sledbotton.show()
    FGroupBox.show()

def check_answer():
    global t_otvet, chet, c
    if answers[0].isChecked():
        chet+=1
        otvet_T()

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            chet+=1
            otvet_F()
    return(chet)
def otvet():
    
    but1.setCheckable(True)
    but2.setCheckable(True)
    but3.setCheckable(True)
    but4.setCheckable(True)
    check_answer()
        
def sled_hide():
    RadioGroupBox.show()
    botton.show()
    Sledbotton.hide()
    FGroupBox.hide()
    TGroupBox.hide()

def sled():  
    but1.setCheckable(False)
    but2.setCheckable(False)
    but3.setCheckable(False)
    but4.setCheckable(False)
    but1.setCheckable(True)
    but2.setCheckable(True)
    but3.setCheckable(True)
    but4.setCheckable(True)
    sled_hide()
    next_question()
#подписка на событие
botton.clicked.connect(otvet)
Sledbotton.clicked.connect(sled)

#создаем вопрос
ask1 = Question('В каком году распался ссср?', '1991', '1981', '1979', '1989')

list_question = []
list_question.append(Question('В каком году распался ссср?', '1991', '1981', '1979', '1989'))
list_question.append(Question('На каком языке говарят в Индии?', 'Хинди', 'Индийском', 'Русском', 'Немецком'))
list_question.append(Question('В КАКОМ ГОДУ СОЗДАЛИ ИНТЕРНЕТ?', '1969', '1978', '1981', '1986'))
list_question.append(Question('В каком году создали python?', '1989', '1978', '1981', '1986'))
list_question.append(Question('В каком году создали ютуб?', '2005', '2000', '2007', '2004'))
list_question.append(Question('В каком году создали ВК?', '2006', '2005', '2007', '2004'))
list_question.append(Question('В каком году создали Google?', '1998', '2000', '1999', '1997'))
list_question.append(Question('Какой браузер популярней?', 'Брейв', 'Мозила', 'Хром', 'Яндекс'))

ask(ask1)

global curr_answer
global t_otvet
global chet
global c
t_otvet = 0
curr_answer = 0
c = 0
chet = 0

def next_question():
    global curr_answer, chet
    chett = len(list_question)
    curr_answer = randint(0, chett-1)
    q = list_question[curr_answer]
    ask(q) 

main_win.show()
app.exec_()

