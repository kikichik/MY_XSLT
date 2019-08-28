import os
import docx
import lxml

def spec_version_meta(path_to_doc):
    doc_file = r''
    for files in os.listdir(path_to_doc):
        if str(files).startswith('OpenEHR'):
            doc_file = str(files)
    doc = docx.Document(os.path.join(path_to_doc, doc_file))
    section = doc.sections[0]
    footer = section.first_page_footer.paragraphs[0].text
    if footer != '':
        footer = str(footer).replace(footer[:8], '')
        footer = str(footer).replace(footer[5:], '')
        return footer
    else:
        return '1.0.0'


def show_xslt(files, path_xslt, path_to_doc):
    print('\n')
    print('**************************************')
    print('metatags:', files)
    meta_show(os.path.join(path_xslt, files), path_to_doc)

def meta_show(path_to_file, path_to_doc):
    path_to_xslt = path_to_file
    file = open(path_to_xslt, "rb").read()
    data = file
    tree = lxml.etree.fromstring(data)
    # Берем head и читаем атрибуты
    head = tree.find(r".//{http://www.w3.org/1999/XSL/Transform}template/html/head")
    for child in head:
        if str(child.attrib.keys()).find('spec_version') != -1:
            print('spec_version in xslt:', child.attrib.values())
            print('spec version in doc:', spec_version_meta(path_to_doc))
        if str(child.attrib.keys()).find('xslt_version') != -1:
            print('---------------------')
            print('xslt_version:', str(child.attrib.values()))
            print('---------------------')


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

#меняем  исходную папку
def change_current_folder():
    global path_to_simiFolders
    print('print folder:')
    path_to_folder = str(input())
    path_to_simiFolders = path_to_folder



#замена всех файлов в выбранной папке
def show_versions(path_to_folder):
    all_cct_dirs = os.listdir(path_to_folder)
    for dir_first_level in all_cct_dirs:
        # сохраняем путь к папке с cct
        path_first_level = os.path.join(path_to_folder, dir_first_level)
        path_xslt = os.path.join(path_first_level, 'xslt')
        path_to_xs = os.path.join(path_first_level, 'xslt_screen')
        path_to_doc = os.path.join(path_first_level, 'doc')
        if os.path.exists(path_to_xs):
            for xslt_file in os.listdir(path_to_xs):
                print(xslt_file, '->', path_xslt)
                os.rename(os.path.join(path_to_xs, xslt_file), os.path.join(path_xslt, xslt_file))
                os.rmdir(path_to_xs)
                print('empty xslt_screen folder removed')
        #меняем файлы в папке xslt
        for files in os.listdir(path_xslt):
            show_xslt(files, path_xslt, path_to_doc)

#Перемещение заданного xslt_screen
def change_one_occurrence(path_cct_dir):
    path_to_Simi, cct_directory = os.path.split(path_cct_dir)
    path_first_level = os.path.join(path_to_Simi, cct_directory)
    path_xslt_folder = os.path.join(path_first_level, 'xslt')
    path_to_xs = os.path.join(path_first_level, 'xslt_screen')
    path_to_doc = os.path.join(path_first_level, 'doc')
    #ловим папку xslt_screen
    if os.path.exists(path_to_xs):
        for xslt_file in os.listdir(path_to_xs):
            print(xslt_file, '->', path_xslt_folder)
            os.rename(os.path.join(path_to_xs, xslt_file), os.path.join(path_xslt_folder, xslt_file))
            os.rmdir(path_to_xs)
            print('empty xslt_screen folder removed')
    for files in os.listdir(path_xslt_folder):
        show_xslt(files, path_xslt_folder, path_to_doc)

def help():
    print(
        'e -fi - changes in one folder',
        'e -a - changes in all folders',
        's - search talon',
        'c -fl - change current folder',
        sep='\n'
    )