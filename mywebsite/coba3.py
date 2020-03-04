from PIL import Image, ImageEnhance
import pytesseract
import cv2
import os

im = Image.open('Proposal_Test.jpeg')


def kode1():
    kode1x1 = 2098
    kode1y1 = 105
    kode1x2 = 2248
    kode1y2 = 150
    kode1 = im.crop((kode1x1,kode1y1,kode1x2,kode1y2))
    var_kode1 = (pytesseract.image_to_string(kode1))
   # kode1.show()
    print(var_kode1.replace("w","W"))

def kode2():
    kode2x1 = 2155
    kode2y1 = 175
    kode2x2 = 2240
    kode2y2 = 220
    kode2 = im.crop((kode2x1,kode2y1,kode2x2,kode2y2))
    var_kode2 = (pytesseract.image_to_string(kode2))
    #kode2.show()
    print(var_kode2.replace("O","0"))

def kode3():
    kode3x1 = 2008
    kode3y1 = 250
    kode3x2 = 2378
    kode3y2 = 305
    kode3 = im.crop((kode3x1,kode3y1,kode3x2,kode3y2))
    var_kode3 = (pytesseract.image_to_string(kode3))
    print(var_kode3.replace("O","0"))

def kode4():
    kode4x1 = 2008
    kode4y1 = 325
    kode4x2 = 2378
    kode4y2 = 370
    kode4 = im.crop((kode4x1,kode4y1,kode4x2,kode4y2))
    var_kode4 = (pytesseract.image_to_string(kode4))
    print(var_kode4)

def proposal():
    proposalx1 = 1013.64
    proposaly1 = 578.19
    proposalx2 = 1589.07
    proposaly2 = 638.95
    proposal = im.crop((proposalx1,proposaly1,proposalx2,proposaly2))
    var_proposal = (pytesseract.image_to_string(proposal))
    print(var_proposal)

def judul():
    judulx1 = 370
    juduly1 = 670
    judulx2 = 2190
    juduly2 = 1145
    judul = im.crop((judulx1,juduly1,judulx2,juduly2))
    var_judul = (pytesseract.image_to_string(judul))
    print(var_judul)

def nama():
    namax1 = 901.897
    namay1 = 2164.83
    namax2 = 1721.01
    namay2 = 2251.76
    nama = im.crop((namax1,namay1,namax2,namay2))
    val_nama = (pytesseract.image_to_string(nama))
    print(val_nama)

def nim():
    nimx1 = 1062.75
    nimy1 = 2267.54
    nimx2 = 1529.7
    nimy2 = 2376.11
    nim = im.crop((nimx1,nimy1,nimx2,nimy2))
    val_nim = (pytesseract.image_to_string(nim))
    print(val_nim)

def fakultas():
    fakultasx1 = 628.898
    fakultasy1 = 2519.17
    fakultasx2 = 1945.13
    fakultasy2 = 2923.11
    fakultas = im.crop((fakultasx1,fakultasy1,fakultasx2,fakultasy2))
    val_fakultas = (pytesseract.image_to_string(fakultas))
    print(val_fakultas)

def tahun():
    tahunx1 = 1223.32
    tahuny1 = 2943.93
    tahunx2 = 1391.19
    tahuny2 = 3033.86
    tahun = im.crop((tahunx1,tahuny1,tahunx2,tahuny2))
    val_tahun = (pytesseract.image_to_string(tahun))
    print(val_tahun)

#Printing Result
kode1()
kode2()
kode3()
kode4()
print('\n')

  








