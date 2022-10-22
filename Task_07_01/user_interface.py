def first_menu():
    while True:
        key_in = input("Введите номер пункта:\n\
        1. Открыть или создать файл справочника \n\
        2. Выйти из программы\n\
        ---> ")
        if key_in in ['1', '2']:
            return int(key_in)

def file_name():
    return (input('Введите имя файла (расширение .csv не указывать) ---> ') + '.csv')

def second_menu():
    while True:
        key_in = input("Введите номер пункта:\n\
        1. Просмотреть справочник \n\
        2. Добавить запись в справочник\n\
        3. Выйти из программы\n\
        ---> ")
        if key_in in ['1', '2', '3']:
            return int(key_in)

def add_record():
    record = input('Введите "Фамилия, Имя, Телефон, Описание" ---> ').split(', ')
    return record