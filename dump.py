from base_utilites import (
    format_path as fp
)

import os 

from base_extractor import (
    get_text_from_doc , 
    get_text_from_pdf , 
    get_text_from_csv , 
    get_text_from_text , 
    get_text_from_docx 
)

def dump_doc_files() : 

    doc_file_paths = os.listdir(fp(
        '''
        DataBase/
            Docs
        '''))
    doc_file_paths = [
        fp(
            '''
            DataBase/
                Docs/
            '''
        ) + path
        for path 
        in doc_file_paths]

    text = ''
    for path in doc_file_paths : 

        if path.endswith('pdf') : text += get_text_from_pdf(path)
        elif path.endswith('doc') : text += get_text_from_doc(path)
        elif path.endswith('docx') : text += get_text_from_docx(path)
        elif path.endswith('csv') : text += get_text_from_csv(path)
        elif path.endsiwth('xls') : text += get_text_from_csv(path)
        elif path.endswith('xlsx') : text += get_text_from_csv(path)

    with open('final_text_base.txt' , 'a') as fil : fil.write(text)

def dump_text_files() : 

    text_file_paths = os.listdir(fp(
        '''
        DataBase/
            Texts
        '''))
    text_file_paths = [
        fp(
            '''
            DataBase/   
                Texts/
            '''
        ) + path 
        for path 
        in text_file_paths]

    text = ''
    for path in text_file_paths : text += get_text_from_text(path)

    with open('final_text_base.txt' , 'a') as fil : fil.write(text)
