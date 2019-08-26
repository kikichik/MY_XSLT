from functions import change_all_occurrences, change_one_occurrence, change_current_folder, search_talon, help

path_to_simiFolders = r''
current_dir = r''

#команды
def commands(cmd):
    if cmd == 'e -fi':
        change_one_occurrence(current_dir)
    if cmd == 'e -a':
        change_all_occurrences(path_to_simiFolders)
    if cmd == 's':
        search_talon(path_to_simiFolders)
    if cmd == 'c -fl':
        change_current_folder()
    if cmd == 'h':
        help()



if __name__ == '__main__':
    if path_to_simiFolders == '':
        change_current_folder()
    if current_dir == '':
        search_talon(path_to_simiFolders)
    while True:
        print('command:')
        current_command = str(input())
        try:
            commands(current_command)
        except KeyError as e:
            raise ValueError('Undefined unit: {}'.format(e.args[0]))

















# для всех файлов
# if dirs_in_simi !='':
#     for dir_first_level in dirs_in_simi:
#         #папки второго уровня: cct, doc, forms, xml, xslt, xslt_screen
#         for dir_second_level in os.listdir((os.path.join(path_to_simiFolders, dir_first_level))):
#             if dir_second_level == 'xslt_screen':
#                 # сохраняем путь к папке xslt_screen
#                 path_to_xs = os.path.join(path_to_simiFolders, dir_first_level, dir_second_level)
#                 path_first_level = os.path.join(path_to_simiFolders, dir_first_level)
#                 for files in os.listdir(path_to_xs):
#                     print(files)
