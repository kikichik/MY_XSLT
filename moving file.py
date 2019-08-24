import os

path_to_simiFolders = r'D:\work\stashes\test_simi'
dirs_in_simi = os.listdir(path_to_simiFolders)
current_dir = r'D:\work\stashes\test_simi\cct=22954 Ophthalmologist child'

#Ищем название вхождение названия одного из талонов
def search_talon(path_to_folder, talon_name):
    cct_found = []
    all_cct_dirs = os.listdir(path_to_folder)
    iter = 0
    for dir_first_level in all_cct_dirs:
        if str(dir_first_level).lower().find(str(talon_name.lower())) != -1:
            iter += 1
            cct_found.append(dir_first_level)
            print(iter, '-', cct_found[iter - 1])
            print('choose cct:')
            index_chosen = int(input())
            print('selected cct:', )


#замена всех файлов в выбранной папке
def change_all_occurrences(path_to_folder):
    all_cct_dirs = os.listdir(path_to_folder)
    for dir_first_level in all_cct_dirs:
        #папки второго уровня: cct, doc, forms, xml, xslt, xslt_screen
        for dir_second_level in os.listdir((os.path.join(path_to_simiFolders, dir_first_level))):
            #ловим папку xslt_screen
            if dir_second_level == 'xslt_screen':
                # сохраняем путь к папке xslt_screen
                path_to_xs = os.path.join(path_to_simiFolders, dir_first_level, dir_second_level)
                path_first_level = os.path.join(path_to_simiFolders, dir_first_level)
                path_xslt = os.path.join(path_first_level, 'xslt')
                for files in os.listdir(path_to_xs):
                    print(files, '->', path_xslt)
#Перемещение заданного xslt_screen
def change_one_occurrence(path_to_Simi, cct_dir):
    path_first_level = os.path.join(path_to_Simi, cct_dir)
    path_xslt_folder = os.path.join(path_first_level, 'xslt')
    #папки второго уровня: cct, doc, forms, xml, xslt, xslt_screen
    for dir_second_level in os.listdir((os.path.join(path_to_Simi, cct_dir))):
        #ловим папку xslt_screen
        if dir_second_level == 'xslt_screen':
            # сохраняем путь к папке xslt_screen
            path_to_xs = os.path.join(path_to_Simi, cct_dir, dir_second_level)
            for files in os.listdir(path_to_xs):
                print(files,'->',path_xslt_folder)
                print('removed')

search_talon(path_to_simiFolders, 'pediatrist')

















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
