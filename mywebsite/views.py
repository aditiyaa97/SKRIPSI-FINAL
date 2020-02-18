from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from wand.image import Image as Img
from PIL import Image
import cv2
import numpy as np
import os
# importing all the required modules
import PyPDF2
import tensorflow


UPLOAD_FOLDER = 'C:/Users/Aditiya/SKRIPSI/mywebsite/' # plus MEDIA_URL
ALLOWED_EXTENSION = set(['pdf'])
SAVE_GRAYSCALE = 'C:/Users/Aditiya/SKRIPSI/mywebsite/grayscale'
SAVE_BOUNDING = 'C:/Users/Aditiya/SKRIPSI/mywebsite/boundingbox'

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def upload(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        context['url'] = fs.url(name)
        context['main'] = UPLOAD_FOLDER
        context['img'] = context['url'].replace('pdf','jpeg')
        
        path = UPLOAD_FOLDER + context['img'] # url ending with .pdf
        direktori, nama_file = os.path.split(path) # direktori = path--tanpa filename, nama_file = proposalAditya.jpeg

        with Img(filename=UPLOAD_FOLDER+context['url'], resolution=300) as pic:
            with Img(pic.sequence[0]) as first_page:
                first_page.save(filename=UPLOAD_FOLDER+context['img'])
                gray(fs,UPLOAD_FOLDER,context,nama_file)
                boundingbox(fs,UPLOAD_FOLDER,context)

                #print(path)
                #print(upload_file.name)
                #print(nama_file)
                #print(UPLOAD_FOLDER + context['url'])
                #print(UPLOAD_FOLDER + context['img'])
    return render(request, 'upload.html', context)

def gray(fs,UPLOAD_FOLDER,context,nama_file):
    img = cv2.imread(UPLOAD_FOLDER + context['img'])
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.imwrite (os.path.join(SAVE_GRAYSCALE, nama_file), gray_img)

    return gray_img

def boundingbox(fs,UPLOAD_FOLDER,context):
    image = cv2.imread(UPLOAD_FOLDER + context['img'])
    #print(image)
    # image = cv2.resize(image_original,None,fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
    #cv2.namedWindow("Image")
    #cv2.imshow('Image',image)
    # image = cv2.resize(image_original,None,fx=4, fy=4, interpolation = cv2.INTER_CUBIC)

    #grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # original_resized = cv2.resize(gray, (0,0), fx=.2, fy=.2)
    #cv2.imshow('gray',gray)
    #cv2.waitKey(0)

    #Remove Salt and pepper noise
    saltpep = cv2.fastNlMeansDenoising(gray,None,9,13)
    # original_resized = cv2.resize(saltpep, (0,0), fx=.2, fy=.2)
    #cv2.imshow('Grayscale',saltpep)
    #cv2.waitKey(0)

    #blur
    blured = cv2.blur(saltpep,(3,3))
    # original_resized = cv2.resize(blured, (0,0), fx=.2, fy=.2)
    #cv2.imshow('blured',blured)
    #cv2.waitKey(0)

    #binary
    ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    # original_resized = cv2.resize(thresh, (0,0), fx=.2, fy=.2)
    #cv2.imshow('Threshold',thresh)
    #cv2.waitKey(0)

    #dilation
    kernel = np.ones((5,100), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    # original_resized = cv2.resize(img_dilation, (0,0), fx=.2, fy=.2)
    #cv2.imshow('dilated',img_dilation)
    #cv2.waitKey(0)

    #find contours
    ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[1])

    #read lines
    #ctr_word=0
    ctr_line=0

    for i, ctr in enumerate(sorted_ctrs):
        ctr_line=ctr_line+1
        if(ctr_line<4):
            print(ctr_line)
        #function compare segment dengan gambar
        if(ctr_line>6):
            break
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)
    
        # Getting ROI
        roi = image[y:y+h, x:x+w]
        ##   show ROI
        #image = image.save(ctr_line + ".jpg")
        
        #cv2.imshow('segment no:' +str(i),roi)
        cv2.imwrite(str(i) + SAVE_BOUNDING + " .jpg", roi) #kendalanya tidak dapat ke simpan pada path (SAVE_BOUNDING)
        #cv2.waitKey(0)
    return roi

