import fitz
import sys
import os
import glob

# pdf_path: the folder of all the PDF files
# saved_path: the path of the saved page images
def clean_folder(saved_path: str):
    """Cleans folder designated with single argument"""
    if not os.path.exists(saved_path):
        os.mkdir(saved_path)
    else:
        files = glob.glob(f'{saved_path}/*')
        for f in files:
            os.remove(f)

def convert_pdf_to_image(pdf_path, pdf_file, saved_path):
    """
    Takes input path, input pdf file, and output path
    From inputs, outputs pdf into output path as a series of images
    """
    try:
        fitz.TOOLS.mupdf_warnings()  # empty the problem message container
        doc = fitz.open(pdf_path + "/" + pdf_file)
        warnings = fitz.TOOLS.mupdf_warnings()
        if warnings:
            print(warnings)
            raise RuntimeError()

        for page in doc:  # iterate through the pages
            pix = page.get_pixmap()  # render page to an image
            pix.save(saved_path + "/" + f"{pdf_file[:-4]}-{page.number}.png")  # store image as a PNG
        return 

    except:
        print("error when opening the pdf file {}".format(pdf_file))
        return None
    
data_path = "raw_pdfs"
converted_path = "data/train/images"

dir = os.listdir(data_path)
clean_folder(converted_path)
for file in dir:
   pdf_name = file
   convert_pdf_to_image(data_path, pdf_name, converted_path)