import subprocess 
import os 

def format_path(path) : 

    path = path.replace('\n' , '')
    path = path.replace('\t' , '')
    path = path.replace(' ' , '')

    return path

def convert_doc_to_docx(
    doc_path , docx_path
) : 

    subprocess.run(
        [
            'soffice' , 
            '--headless' , 
            '--convert-to' , 
            'docx' , 
            doc_path , 
            '--outdir' , 
            os.path.driname(docx_path)
        ]
    )

    os.remove(doc_path)