from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from wand.image import Image as Img
from PIL import Image, ImageEnhance
import cv2
import numpy as np
import os
#BoundingObject
import pytesseract
#RemoveLogo
from skimage.io import imread, imshow, imsave
from skimage.color import rgb2gray
from skimage import img_as_float
from skimage.morphology import disk
from matplotlib import pyplot as plt
#YOLO
import tensorflow


UPLOAD_FOLDER = 'C:/Users/Aditiya/SKRIPSI/mywebsite/' # plus MEDIA_URL
ALLOWED_EXTENSION = set(['pdf'])
SAVE_REMOVELOGO = 'C:/Users/Aditiya/SKRIPSI/mywebsite/removelogo/'


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
                removelogo(fs,UPLOAD_FOLDER,context,nama_file)
                kode1(fs,SAVE_REMOVELOGO,context,nama_file)
                kode2(fs,SAVE_REMOVELOGO,context,nama_file)
                proposal(fs,SAVE_REMOVELOGO,context,nama_file)
                judul(fs,SAVE_REMOVELOGO,context,nama_file)
                nama(fs,SAVE_REMOVELOGO,context,nama_file)
                nim(fs,SAVE_REMOVELOGO,context,nama_file)
                fakultas(fs,SAVE_REMOVELOGO,context,nama_file)
                tahun(fs,SAVE_REMOVELOGO,context,nama_file)
                #print(path)
                #print(upload_file.name)
                #print(nama_file)
                #print(UPLOAD_FOLDER + context['url'])
                #print(UPLOAD_FOLDER + context['img'])
    return render(request, 'upload.html', context)

def removelogo(fs,UPLOAD_FOLDER,context,nama_file):
    gambar = img_as_float(imread(UPLOAD_FOLDER + context['img']))
    idx_old = 0
    idx_new = 0
    for idxr, row in enumerate(gambar):
        new_row = []
        for idxc, column in enumerate(row):
            new_column = []
            if np.sum(column)/3 > 0.1:
                row[idxc] = [1.0, 1.0, 1.0]
                idx_old+=1
    gambar[idxr] = row
    new_gambar = gambar * 255
    imsave(os.path.join(SAVE_REMOVELOGO + nama_file), new_gambar)
    return new_gambar

def kode1(fs,SAVE_REMOVELOGO,context,nama_file):
    im = Image.open(SAVE_REMOVELOGO + nama_file)
    kode1x1 = 2008.17
    kode1y1 = 99.9658
    kode1x2 = 2378.5
    kode1y2 = 158.305
    kode1 = im.crop((kode1x1,kode1y1,kode1x2,kode1y2))
    var = (pytesseract.image_to_string(kode1))
    print(var)
    return var

def kode2(fa,SAVE_REMOVELOGO,context,nama_file):
    im = Image.open(SAVE_REMOVELOGO + nama_file)
    kode2x1 = 2155
    kode2y1 = 175
    kode2x2 = 2240
    kode2y2 = 220
    kode2 = im.crop((kode2x1,kode2y1,kode2x2,kode2y2))
    var_kode2 = (pytesseract.image_to_string(kode2))
    kode2_replace = (var_kode2.replace("O","0"))
    print(kode2_replace)
    return var_kode2

def proposal(fs,SAVE_REMOVELOGO,context,nama_file):
    im = Image.open(SAVE_REMOVELOGO + nama_file)
    proposalx1 = 1013.64
    proposaly1 = 578.19
    proposalx2 = 1589.07
    proposaly2 = 638.95
    proposal = im.crop((proposalx1,proposaly1,proposalx2,proposaly2))
    var_proposal = (pytesseract.image_to_string(proposal))
    print(var_proposal)
    return var_proposal

def judul(fs,SAVE_REMOVELOGO,context,nama_file):
    im = Image.open(SAVE_REMOVELOGO + nama_file)
    judulx1 = 466.044
    juduly1 = 680.645
    judulx2 = 2135.36
    juduly2 = 1133.64
    judul = im.crop((judulx1,juduly1,judulx2,juduly2))
    var_judul = (pytesseract.image_to_string(judul))
    return var_judul

def nama(fs,SAVE_REMOVELOGO,context,nama_file):
    im = Image.open(SAVE_REMOVELOGO + nama_file)
    namax1 = 901.897
    namay1 = 2164.83
    namax2 = 1721.01
    namay2 = 2251.76
    nama = im.crop((namax1,namay1,namax2,namay2))
    val_nama = (pytesseract.image_to_string(nama))
    print(val_nama)
    return val_nama

def nim(fs,SAVE_REMOVELOGO,context,nama_file):
    im = Image.open(SAVE_REMOVELOGO + nama_file)
    nimx1 = 1062.75
    nimy1 = 2267.54
    nimx2 = 1529.7
    nimy2 = 2376.11
    nim = im.crop((nimx1,nimy1,nimx2,nimy2))
    val_nim = (pytesseract.image_to_string(nim))
    print(val_nim)
    return val_nim

def fakultas(fs,SAVE_REMOVELOGO,context,nama_file):
    im = Image.open(SAVE_REMOVELOGO + nama_file)
    fakultasx1 = 628.898
    fakultasy1 = 2519.17
    fakultasx2 = 1945.13
    fakultasy2 = 2923.11
    fakultas = im.crop((fakultasx1,fakultasy1,fakultasx2,fakultasy2))
    val_fakultas = (pytesseract.image_to_string(fakultas))
    print(val_fakultas)
    return val_fakultas

def tahun(fs,SAVE_REMOVELOGO,context,nama_file):
    im = Image.open(SAVE_REMOVELOGO + nama_file)
    tahunx1 = 1223.32
    tahuny1 = 2943.93
    tahunx2 = 1391.19
    tahuny2 = 3033.86
    tahun = im.crop((tahunx1,tahuny1,tahunx2,tahuny2))
    val_tahun = (pytesseract.image_to_string(tahun))
    print(val_tahun)
    return val_tahun