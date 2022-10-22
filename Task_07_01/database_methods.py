import user_interface as ui

def output_list(list_file_element):
    for string in list_file_element:
        print(string)
    return

def add_record(list_file_element):
    list_file_element.append(ui.add_record())
    return
