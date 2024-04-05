import json
notes = {'Добро пожаловать!':
             {'текст':'Это самое лучшее приложение для заметок в мире.',
              'теги':['добро', 'пожаловать']}
         }

try:
    with open('notes_data.json', 'r+', encoding='utf-8') as file:
        data = file.read().strip()
        if data == '':
            json.dump(notes, file)

        file.seek(0)
        data = json.load(file)

    print(type(data), data)
except:
    print('Ошибка работы с json')

