def read_file(file_name):
    with open(file_name,'r+',encoding = 'utf-8') as f:
        list_file_string = f.read().splitlines()
        list_file_element = [list_file_string[i].split(';') for i in range(len(list_file_string))]
    return list_file_element

def write_file(file_name, list_file_element):
        list_file_string = [';'.join(list_file_element[i]) for i in range(len(list_file_element))]
        with open(file_name,'w',encoding = 'utf-8') as f:
            for line in list_file_string:
                f.write(line + '\n')
        return
