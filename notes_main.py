from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QListWidget, QHBoxLayout, QVBoxLayout, QLabel, \
QPushButton, QLineEdit, QInputDialog, QMessageBox

import json
def read_data():
    try:
        with open('f.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except:
        print('Error add dict!')

def write_data(new_data):
    try:
        with open('f.json', 'w', encoding='utf-8') as file:
            json.dump(new_data, file, ensure_ascii=False, sort_keys=True)
    except:
        print('Error add dict!')
def check_json():
    notes = {'Добро пожаловать!':
                 {'текст':'Это самое лучшее приложение для заметок в мире.',
                  'теги':['добро', 'пожаловать']}
             }
    try:
        with open('f.json', 'r+', encoding='utf-8') as file:
            data = file.read().strip()
            if data == '':
                json.dump(notes, file, ensure_ascii=False, sort_keys=True)

            file.seek(0)
            data = json.load(file)

        # print(type(data), data)
        return data
    except:
        print('Ошибка работы с json')

def show_results():
    key = list_text1.selectedItems()[0].text()
    data = read_data()

    text_field.setText(data[key]['текст'])
    list_text2.clear()
    for j in data[key]['теги']:
        list_text2.addItem(j)

#Creat notice
def add_note_json(d):
    data = read_data()
    new_d = {**data, **d}
    write_data(new_d)

def add_note():
    notes_name, ok = QInputDialog.getText(window, 'Добавить заметку', 'Название заметки:')
    notes = {}
    if ok and notes_name != '':
        notes[notes_name] = {'текст': '', 'теги': []}
        list_text1.addItem(notes_name)
        add_note_json(notes)

def delete_note():
    if list_text1.selectedItems():
        key = list_text1.selectedItems()[0].text()
        data = read_data()
        del data[key]
        write_data(data)
        list_text1.clear()
        list_text2.clear()
        text_field.clear()
        list_text1.addItems(data)
    else:
        print('Заметка для удаления не выбрана.')

def save_note():
    if list_text1.selectedItems():
        key = list_text1.selectedItems()[0].text()
        text = text_field.toPlainText()
        data = read_data()
        data[key]['текст'] = text
        write_data(data)

def add_teg():
    global key, data
    if list_text1.selectedItems():
        key = list_text1.selectedItems()[0].text()
        text = lineEdit.text()
        data = read_data()
        if text not in data[key]['теги']:
            data[key]['теги'].append(text)
            write_data(data)
    list_text2.clear()
    for j in data[key]['теги']:
        list_text2.addItem(j)
    else:
        print('Заметка для сохранения не выбрана.')

def del_teg():
    if list_text2.selectedItems():
        key = list_text1.selectedItems()[0].text()
        text = list_text2.selectedItems()[0].text()
        data = read_data()
        if text in data[key]['теги']:
            data[key]['теги'].remove(text)
            write_data(data)
        list_text2.clear()
        for j in data[key]['теги']:
            list_text2.addItem(j)
        else:
            print('Заметка для сохранения не выбрана.')
def find_btn():
    global data
    result  = {}
    searching = lineEdit.text().strip()
    if searching and bnt6.text() == 'Искать заметки по тегу':
        data = read_data()
        try:
            for i in data:
                print(i)
                if searching in data[i]['теги']:
                    result[i] = data[i]
            data = result
            bnt6.setText('Сбросить поиск')
        except:
            print('Error again')
        list_text1.clear()
        list_text2.clear()
        text_field.clear()
        list_text1.addItems(data)
    elif bnt6.text() == 'Сбросить поиск':
        try:
            data = read_data()
            bnt6.setText('Искать заметки по тегу')
        except:
            print('Error again')
        list_text1.clear()
        list_text2.clear()
        text_field.clear()
        list_text1.addItems(data)
    else:
        pass


app = QApplication([])
window = QWidget()
window.setWindowTitle('Умные заметки')
window.resize(800, 600)
window.show()

text_field = QTextEdit()
text_field.setText('')
list_text1 = QListWidget()
list_text1_label = QLabel('Список заметок')
list_text2 = QListWidget()
list_text2_label = QLabel('Список тегов')
lineEdit = QLineEdit()
lineEdit.setPlaceholderText('Введите тег...')

# выводим существующие заметки
data = check_json()

for i in data.keys():
    list_text1.addItem(i)
list_text1.itemClicked.connect(show_results)

# widgets buttons
bnt_add = QPushButton('Создать заметку')
bnt_delete = QPushButton('Удалить заметку')
bnt3 = QPushButton('Сохранить заметку')
bnt4 = QPushButton('Добавить к заметке')
bnt5 = QPushButton('Открепить от заметки')
bnt6 = QPushButton('Искать заметки по тегу')
bnt_addTeg = QPushButton('Добавить к заметки')
bnt_delTeg = QPushButton('Открепить от заметки')


h_main = QHBoxLayout()
v1_layout = QVBoxLayout()
v2_layout = QVBoxLayout()
h2_1 = QHBoxLayout()
h2_2 = QHBoxLayout()
h2_3 = QHBoxLayout()
h2_4 = QHBoxLayout()
h2_5 = QHBoxLayout()
h2_6 = QHBoxLayout()
h2_7 = QHBoxLayout()
h2_8 = QHBoxLayout()
h2_9 = QHBoxLayout()

# first big textarea
v1_layout.addWidget(text_field)

# second zone
h2_1.addWidget(list_text1_label)
h2_2.addWidget(list_text1)
h2_3.addWidget(bnt_add)
h2_3.addWidget(bnt_delete)
h2_4.addWidget(bnt3)
h2_5.addWidget(list_text2_label)
h2_6.addWidget(list_text2)
h2_7.addWidget(lineEdit)
h2_8.addWidget(bnt6)
h2_9.addWidget(bnt_addTeg)
h2_9.addWidget((bnt_delTeg))

v2_layout.addLayout(h2_1)
v2_layout.addLayout(h2_2)
v2_layout.addLayout(h2_3)
v2_layout.addLayout(h2_4)
v2_layout.addLayout(h2_5)
v2_layout.addLayout(h2_6)
v2_layout.addLayout(h2_7)
v2_layout.addLayout(h2_9)
v2_layout.addLayout(h2_8)

h_main.addLayout(v1_layout)
h_main.addLayout(v2_layout)

window.setLayout(h_main)

bnt_add.clicked.connect(add_note)
bnt_delete.clicked.connect(delete_note)
bnt3.clicked.connect(save_note)
bnt_addTeg.clicked.connect(add_teg)
bnt_delTeg.clicked.connect(del_teg)
bnt6.clicked.connect(find_btn)
app.exec_()
