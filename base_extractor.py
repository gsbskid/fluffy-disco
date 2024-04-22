from base_utilites import (
    format_path as fp , 
    convert_doc_to_docx as cdtd
)

from unstructured.partition.pdf import partition_pdf
from unstructured.partition.docx import partition_docx

import docx
import PyPDF2

def get_text_from_text(path) : 

    text = open(path).read()

    return text

def get_text_from_pdf(path) : 

    raw_pdf_elements = partition_pdf(
        filename = path , 
        extract_images_in_pdf = True , 
        infer_table_structure = True , 
        chunking_strategy = 'by_title' , 
        max_characters = 4000 , 
        new_after_n_chars = 3800 , 
        combine_text_under_n_chars = 2000 , 
        extract_image_block_output_dir =  fp(
            '''
            DataBase/
                Images
            '''
        )
    )

    del raw_pdf_elements

    pdf_reader = PyPDF2.PdfFileReader(open(path , 'rb'))
    num_pages = pdf_reader.getNumPages()
    text = ''

    for page_num in range(num_pages) : text += pdf_reader.getPage(page_num).extractText()

    return text

def get_text_from_doc(path) : 

    cdtd(
        path , 
        path + 'x'
    )

    text = get_text_from_docx(path)

    return text   

def get_text_from_docx(path) : 

    elements = partition_docx(filename = path)
    doc = docx.Document(path)

    text = ''
    for element in elements : text += element

    # for image in doc.inline_shapes : image_data = image.image.blob # TODO Complete pipeline conncection for images 

    return text

def get_text_from_csv(path) : 

    text = open(path).read()

    return text