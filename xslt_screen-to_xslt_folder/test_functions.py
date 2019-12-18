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
    print('xslt file:', files)
    meta_show(os.path.join(path_xslt, files), path_to_doc)

def meta_show(path_to_file, path_to_doc):
    path_to_xslt = path_to_file
    file = open(path_to_xslt, "rb").read()
    tree = lxml.etree.fromstring(file)
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

class Paths(object):
    def __init__(self, path_first_level):
        self.path_xslt = os.path.join(path_first_level, 'xslt')
        self.path_to_xs = os.path.join(path_first_level, 'xslt_screen')
        self.path_to_doc = os.path.join(path_first_level, 'doc')

#вывод версии xslt_version, spec_version в doc и в xslt
def show_versions(path_to_folder):
    all_cct_dirs = os.listdir(path_to_folder)
    for dir_first_level in all_cct_dirs:
        # сохраняем путь к папке с cct
        path_first_level = os.path.join(path_to_folder, dir_first_level)
        paths = Paths(path_first_level)
        #меняем файлы в папке xslt
        for files in os.listdir(paths.path_xslt):
            show_xslt(files, paths.path_xslt, paths.path_to_doc)