import os
import re

path_to_simiFolders = r'C:\Nikita\stashes\from simi'
dirs_in_simi = os.listdir(path_to_simiFolders)

def output_files_inside(some_file):
    print('-', some_file)
# все папки по врачам

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
    for dir_first_level in dirs_in_simi:
        #папки второго уровня: cct, doc, forms, xml, xslt, xslt_screen
        for dir_second_level in os.listdir((os.path.join(path_to_simiFolders, dir_first_level))):
            if dir_second_level == 'xslt_screen':
                # сохраняем путь к папке xslt_screen
                path_to_xs = os.path.join(path_to_simiFolders, dir_first_level, dir_second_level)
                path_first_level = os.path.join(path_to_simiFolders, dir_first_level)
                for files in os.listdir(path_to_xs):
                    print(files)
