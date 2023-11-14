import os
import sys
from docx2pdf import convert

def convert_docx_to_pdf(folder_path):
    if not os.path.exists(folder_path):
        print("Folder path does not exist.")
        return

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(".docx"):
                docx_file = os.path.join(root, filename)
                print(f"Converting: {docx_file}")
                convert(docx_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_docx_to_pdf.py folder_path")
    else:
        folder_path = sys.argv[1]
        convert_docx_to_pdf(folder_path)
