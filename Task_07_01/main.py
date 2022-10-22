# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.


import os
import user_interface as ui
import csv_model as cm
import database_methods as dm

key_in = ui.first_menu()
if key_in == 2:
    exit()
elif key_in == 1:
    file_name = ui.file_name()
    if not os.path.isfile(file_name):
        cm.write_file(file_name, [])
    list_file_element = cm.read_file(file_name)

while True:
    key_in = ui.second_menu()
    if key_in == 3:
        exit()
    elif key_in == 1:
        dm.output_list(list_file_element)
    elif key_in == 2:
        dm.add_record(list_file_element)
        cm.write_file(file_name, list_file_element)

