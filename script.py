from pypdf import PdfMerger
import os

def sort_by_last_number(filename):
    #change before-number-text with the according substring
    last_number = int((filename.split('before-number-text',1)[1]).split('.pdf',1)[0])
    return(last_number)

pdfs = []
#put the folder of the pdf files you want to merge here
file_list = os.listdir(f"origin-folder-name")
for filename in sorted(file_list, key = sort_by_last_number):
    pdfs.append(filename)

merger = PdfMerger()
for pdf in pdfs:
    merger.append(f"origin-folder-name\\{pdf}")


merger.write(f"destination-folder\\result.pdf")
merger.close()
