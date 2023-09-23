from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QRadioButton
app = QApplication([])
win = QWidget()
win.setWindowTitle('Конкурс від Craze Peaple')
win.resize(400, 200)

text = QLabel(win)
text.setText('В якому році канал отримав  золоту кнопку" від YouTube?')
text.move(50,10)

button1 = QRadioButton(win)
button1.setText('2005')
button1.move(50,60)

button2 = QRadioButton(win)
button2.setText('2010')
button2.move(300,60)

button3 = QRadioButton(win)
button3.setText('2015')
button3.move(50,120)

button4 = QRadioButton(win)
button4.setText('2020')
button4.move(300,120)

def show_information1():
    box1 = QMessageBox(win)
    box1.setText('Правильно! Ви виграли гіроскутер')
    box1.exec_()
def show_information2():
    box2 = QMessageBox(win)
    box2.setText('Ні, в 2015 році. Ви виграли фірмовий плакат')
    box2.exec_()

button3.clicked.connect(show_information1)
button1.clicked.connect(show_information2)
button2.clicked.connect(show_information2)
button4.clicked.connect(show_information2)

win.show()
app.exec_()
