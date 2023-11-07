import gc
import tkinter as tk
from tkinter import filedialog
from django.shortcuts import render
import cv2
import time
import pytesseract
import csv
import os
import sys
gc.disable()


def CamScan(a):
    b = cv2.VideoCapture(0)
    if not b.isOpened():
        exit()
    ret, frame = b.read()
    if not ret:
        exit()
    k = cv2.imwrite(a, frame)
    b.release()
    gc.enable()
    return k
def ImgRecognize(a):
    if os.path.exists(a):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        b = cv2.imread(a)
        c = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        d = pytesseract.image_to_string(c)
    else:
        print('the vehicle image with name ', a, 'not exist in your devise')
        sys.exit()
    gc.enable()
    return d
def index(request):
    return render(request, 'index.html')
def DataFetch(a, b):
    global c1
    global c2
    global c3
    global c4
    global c5
    with open(a, 'r') as file:
        reader = csv.reader(file)
        matching_rows = []
        for row in reader:
            if b in row:
                matching_rows.append(row)
            else:
                c1 = c2 = c3 = c4 = c5 = ''
                c = 0
        for row in matching_rows:
            c1 = row[0]
            c2 = row[1]
            c3 = row[2]
            c4 = row[3]
            c5 = row[4]
            c = 1
    gc.enable()
    return c
def image(request):
    global subc
    global sub
    global G
    if request.method == 'POST':
        image1 = request.POST.get('image1')
        if image1 == 'Browse':
            root = tk.Tk()
            root.withdraw
            a = filedialog.askopenfilename(
                initialdir="/",
                title="close this popup after selecting the image",
                filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.gif"), ("All files", "*.*"))
            )
            root.destroy()
            img = ImgRecognize(a)

        elif image1 == 'Camera':
            CamScan("photo.jpg")
            print('waite for 5 seconds')
            time.sleep(5)
            img = ImgRecognize("photo.jpg")
        man = ''.join(char.upper() for char in img if char.isalnum())
        g = man
        if g == '':
            w=0
            h=0
            man='#C0C0C0'
            sub=''
            G = '🧐👎'
        else:
            w=100
            h=20
            man = '#6600CC'
            G = g
            sub=f'get information'
        a='license number :'
        x=f'({G})'
        gc.enable()
        return render(request, 'index.html', {'a': a,'G':G,'krr':'⬅⬅','x':x,'sub':sub,'man':man,'w':w,'h':h})
def execute_process(request):
    if request.method == 'POST':
        selected_process = request.POST.get('selected_process')
        if selected_process == 'Process 1':
            z = DataFetch('details.csv', G)
            if z == 1:
                a = 'vehicle licence number    :- '
                b = '        vehicle type    :- '
                c = '           owner name    :- '
                d = '    register in state    :- '
                e = '      registretion id    :- '
            else:
                a = 'vehicle not exist'
                b = c = d = e = ''
        elif selected_process == 'Process 2':
            z = DataFetch('aportment security.csv', G)
            if z == 1:
                a = 'vehicle licence number    :- '
                b = '         vehicle type    :- '
                c = '           owner name    :- '
                d = '   owner\'s flat number  :- '
                e = 'is this vehicle allowed   :_ '
            else:
                a = 'not belongs to this flat'
                b = c = d = e = ''
        elif selected_process == 'Process 3':
            z = DataFetch('stolen vehicle.csv', G)
            if z == 1:
                a = 'vehicle licence number    :- '
                b = '         vehicle type    :- '
                c = '           owner name    :- '
                d = '    date of compleant    :- '
                e = 'mobile number of owner    :- '
            else:
                a = 'it is not a stolen vehicle'
                b = c = d = e = ''
        elif selected_process == 'Process 4':
            z = DataFetch('tole plaza.csv', G)
            if z == 1:
                a = 'vehicle licence number    :- '
                b = '         vehicle type    :- '
                c = '           owner name    :- '
                d = ' is it have a fastrack    :- '
                e = 'charges for this vehicl   :- '
            else:
                a = 'take cash'
                b = c = d = e = ''
        elif selected_process == 'Process 5':
            z = DataFetch('showroom service.csv', G)
            if z == 1:
                a = 'vehicle licence number    :- '
                b = '         vehicle type    :- '
                c = '           owner name    :- '
                d = ' previes service date    :- '
                e = 'status of free service    :- '
            else:
                a = 'this vehil is not belongs to this showroom'
                b = c = d = e = ''
        gc.enable()
        return render(request, 'results.html', { 'c1':c1,'c2':c2,'c3':c3,'c4':c4,'c5':c5,'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'G': G})
