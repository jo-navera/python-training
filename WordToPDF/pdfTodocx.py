from pdf2docx import Converter
import os
import sys


def pdfTOword(path_input,path_output):
    for file in os.listdir(path_input): #list files inside file path
        cv = Converter(path_input+file) #convert using "Converter" Module
        cv.convert(path_output+file.replace(".pdf","")+'.docx', start=0, end=None) #Replace the ".pdf" in file name with ".docx"
        cv.close() #Close current docx
        print(file) #print file path
        
def main(input_path,output_path): #run the function in main
    pdfTOword(input_path, output_path) #initialize function - pdfTOWord with declared source & destination path

if __name__ == "__main__":
    input =f'C:\\B\\Test\\'
    output= f'C:\\B\\Test\\'

    main(input,output)
     
     
    