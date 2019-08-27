import os
import lxml.etree
import docx

path_to_simiFolders = r''
current_dir = r''

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
        print('spec version:', footer)
        return str(footer)
    else:
        print('spec version:', '1.0.0')
        return '1.0.0'


def change_xslt(files, path_xslt, path_to_doc):
    if str(files).endswith('screen.xslt'):
        if str(files).find('openEHR-EHR-COMPOSITION.t_') != -1:
            new_name = str(files).replace('openEHR-EHR-COMPOSITION.t_', '')
            new_name = new_name.replace('.screen.xslt', '')
            new_name = new_name + '-display_form_screen.xslt'
            print('\n')
            print('**************************************')
            print('changing name of xslt_screen...')
            print('old name:', files)
            os.rename(os.path.join(path_xslt, files), os.path.join(path_xslt, new_name))
            print('new name:', new_name)
            print('adding meta_tags:', files)
            meta_add(os.path.join(path_xslt, new_name), path_to_doc)
        if str(files).find('openEHR-EHR-COMPOSITION. t_') != -1:
            new_name = str(files).replace('openEHR-EHR-COMPOSITION. t_', '')
            new_name = new_name.replace('.screen.xslt', '')
            new_name = new_name + '-display_form_screen.xslt'
            print('**************************************')
            print('changing name of xslt_screen...')
            print('old name:', files)
            os.rename(os.path.join(path_xslt, files), os.path.join(path_xslt, new_name))
            print('new name:', new_name)
            print('adding meta_tags..')
            meta_add(os.path.join(path_xslt, new_name), path_to_doc)
        if str(files).find('display_form') != -1:
            print('\n')
            print('**************************************')
            print('adding meta_tags:', files)
            meta_add(os.path.join(path_xslt, files), path_to_doc)
    elif str(files).endswith(').xslt') or str(files).endswith('examination.xslt') or str(files).find('screen') == -1:
        if str(files).find('openEHR-EHR-COMPOSITION.t_') != -1:
            new_name = str(files).replace('openEHR-EHR-COMPOSITION.t_', '')
            new_name = new_name.replace('.xslt', '')
            new_name = new_name + '-display_form.xslt'
            print('\n')
            print('**************************************')
            print('changing name of xslt...')
            print('old name:', files)
            os.rename(os.path.join(path_xslt, files), os.path.join(path_xslt, new_name))
            print('new name:', new_name)
            print('adding meta_tags..')
            meta_add(os.path.join(path_xslt, new_name), path_to_doc)
        if str(files).find('openEHR-EHR-COMPOSITION. t_') != -1:
            new_name = str(files).replace('openEHR-EHR-COMPOSITION. t_', '')
            new_name = new_name.replace('.xslt', '')
            new_name = new_name + '-display_form.xslt'
            print('\n')
            print('**************************************')
            print('changing name of xslt...')
            print('old name:', files)
            os.rename(os.path.join(path_xslt, files), os.path.join(path_xslt, new_name))
            print('new name:', new_name)
            print('adding meta_tags..')
            meta_add(os.path.join(path_xslt, new_name), path_to_doc)
        if str(files).find('display_form') != -1:
            print('\n')
            print('**************************************')
            print('adding meta_tags:', files)
            meta_add(os.path.join(path_xslt, files), path_to_doc)

def meta_add(path_to_file, path_to_doc):
    path_to_xslt = path_to_file
    file = open(path_to_xslt, "rb").read()
    data = file
    # tree = lxml.etree.fromstring(data)
    for string in data:
        str(string).replace(r'\n', '')
    tree = lxml.etree.fromstring(data)
    for child in tree:
        if child.tag == r'{http://www.w3.org/1999/XSL/Transform}template':
            attributes = child.attrib
            if str(attributes.values()).find('/*') != -1:
                template = child
    # Берем head и читаем атрибуты
    head = tree.find(r".//{http://www.w3.org/1999/XSL/Transform}template/html/head")
    xslt_version = lxml.etree.Element("meta", {'xslt_version': '1.0.0'})
    spec_version = lxml.etree.Element("meta", {'spec_version': spec_version_meta(path_to_doc)})
    for child in head:
        if str(child.attrib.keys()).find('fork') != -1:
            print('---------------------')
            print('found wrong meta-tag!')
            print('---------------------')
            head.remove(child)
        head.insert(1, xslt_version)
        head.insert(1, spec_version)
    print('xslt version: 1.0.0')
    with open(path_to_file, "wb") as new_file:
        new_file.write(b'<?xml version="1.0" encoding="UTF-8"?>\n' + lxml.etree.tostring(tree, encoding="utf-8"))

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
def change_all_occurrences(path_to_folder):
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
            change_xslt(files, path_xslt, path_to_doc)

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
        change_xslt(files, path_xslt_folder, path_to_doc)

def help():
    print(
        'e -fi - changes in one folder',
        'e -a - changes in all folders',
        's - search talon',
        'c -fl - change current folder',
        sep='\n'
    )




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








