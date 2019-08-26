import os
#Ищем название вхождение названия одного из талонов
def search_talon(path_to_folder):
    global current_dir
    print(current_dir)
    print('talon name: ')
    talon_name = str(input())
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
    print('selected cct:', cct_found[index_chosen - 1])
    current_dir = os.path.join(path_to_simiFolders, cct_found[index_chosen - 1])

def change_current_folder():
    global path_to_simiFolders
    print('print folder:')
    path_to_folder = str(input())
    path_to_simiFolders = path_to_folder



#замена всех файлов в выбранной папке
def change_all_occurrences(path_to_folder):
    all_cct_dirs = os.listdir(path_to_folder)
    for dir_first_level in all_cct_dirs:
        # сохраняем путь к папке с cct
        path_first_level = os.path.join(path_to_folder, dir_first_level)
        path_xslt = os.path.join(path_first_level, 'xslt')
        path_to_xs = os.path.join(path_first_level, 'xslt_screen')
        if os.path.exists(path_to_xs):
            for xslt_file in os.listdir(path_to_xs):
                print(xslt_file, '->', path_xslt)
                os.rename(os.path.join(path_to_xs, xslt_file), os.path.join(path_xslt, xslt_file))
                os.rmdir(path_to_xs)
                print('empty xslt_screen folder removed')
        for files in os.listdir(path_xslt):
            if str(files).endswith('.screen.xslt'):
                new_name = str(files).replace('openEHR-EHR-COMPOSITION.t_', '')
                new_name = new_name.replace('.screen.xslt', '')
                new_name = new_name + '-display_form_screen.xslt'
                print('**************************************')
                print('changing name of xslt_screen...')
                print('old name:', files)
                os.rename(os.path.join(path_xslt, files), os.path.join(path_xslt, new_name))
                print('new name:', new_name)
            elif str(files).endswith(').xslt') or str(files).endswith('examination.xslt'):
                new_name = str(files).replace('openEHR-EHR-COMPOSITION.t_', '')
                new_name = new_name.replace('.xslt', '')
                new_name = new_name + '-display_form.xslt'
                print('**************************************')
                print('changing name of xslt...')
                print('old name:', files)
                os.rename(os.path.join(path_xslt, files), os.path.join(path_xslt, new_name))
                print('new name:', new_name)

#Перемещение заданного xslt_screen
def change_one_occurrence(path_cct_dir):
    path_to_Simi, cct_directory = os.path.split(path_cct_dir)
    path_first_level = os.path.join(path_to_Simi, cct_directory)
    path_xslt_folder = os.path.join(path_first_level, 'xslt')
    path_to_xs = os.path.join(path_first_level, 'xslt_screen')
    #ловим папку xslt_screen
    if os.path.exists(path_to_xs):
        for xslt_file in os.listdir(path_to_xs):
            print(xslt_file, '->', path_xslt_folder)
            os.rename(os.path.join(path_to_xs, xslt_file), os.path.join(path_xslt_folder, xslt_file))
            os.rmdir(path_to_xs)
            print('empty xslt_screen folder removed')
    for files in os.listdir(path_xslt_folder):
        if str(files).endswith('.screen.xslt'):
            new_name = str(files).replace('openEHR-EHR-COMPOSITION.t_', '')
            new_name = new_name.replace('.screen.xslt', '')
            new_name = new_name + '-display_form_screen.xslt'
            print('changing name of xslt_screen')
            print('old name:', files)
            os.rename(os.path.join(path_xslt_folder, files), os.path.join(path_xslt_folder, new_name))
            print('new name:', new_name)
        elif str(files).endswith(').xslt') or str(files).endswith('examination.xslt'):
            new_name = str(files).replace('openEHR-EHR-COMPOSITION.t_', '')
            new_name = new_name.replace('.xslt', '')
            new_name = new_name + '-display_form.xslt'
            print('changing name of XSLT')
            print('old name:', files)
            os.rename(os.path.join(path_xslt_folder, files), os.path.join(path_xslt_folder, new_name))
            print('new name:', new_name)

def help():
    print(
        'e -fi - changes in one folder',
        'e -a - changes in all folders',
        's - search talon',
        'c -fl - change current folder',
        sep='\n'
    )

