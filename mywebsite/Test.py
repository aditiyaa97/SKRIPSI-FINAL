#!C:/Python27/python.exe
#
# Convert PDF files to Microsoft Office Word compatible doc/docx files, 
# using LibreOffice's command line interface.
#
# http://stackoverflow.com/questions/26358281/convert-pdf-to-doc-python-bash
# http://ask.libreoffice.org/en/question/20111/converting-files-using-soffice-convert-to-with-embedded-images-html-to-doc/
# http://cgit.freedesktop.org/libreoffice/core/tree/filter/source/config/fragments/filters
#

import os
import sys
import subprocess
import PyPDF2

print("a")

# pdf source file(s) and target paths
basedir = 'C:/Users/Aditiya/SKRIPSI/mywebsite/mywebsite/Proposal_Aditiya.pdf'
pdfdir = os.path.normpath(basedir + '/pdf')
docdir = os.path.normpath(basedir + '/doc')
docxdir = os.path.normpath(basedir + '/docx')
print("a")

# absolute path to libre office writer application
const lowriter = 'C:/Program Files/LibreOffice/program/swriter.exe'
print("a")

# output-filter for conversion
#outfilter = ':"Office Open XML Text"'
#outfilter = ':"MS Word 2003 XML"'
#outfilter = ':"MS Word 2007 XML"'
#outfilter = ':"MS Word 97"'
outfilter = ':"MS Word 2007 XML"'

file = open('Proposal_Aditiya.pdf','rb')
print (file)
subprocess.call(lowriter +'--invisible --convert-to doc "{}"'.format(basedir), shell=True)







