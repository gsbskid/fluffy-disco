
from dump import (
    dump_doc_files , 
    dump_text_files
)

import os 

from base_utilites import (
    format_path as fp
)

def final_dump() : 

    folders = os.listdir(
        fp(
            '''
            DataBase
            '''
        ))
    folders = ['DataBase/' + path for path in folders]

    open('final_text_base.txt', 'w').close() # Erase contents of the file 

    dump_text_files()
    dump_doc_files()

final_dump()