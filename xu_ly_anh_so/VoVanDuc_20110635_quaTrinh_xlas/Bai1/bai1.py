#tien hanh su dung thu vien tkinter, image tu pil, filedialog de load anh
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import numpy as np
#Python Tkinter (and TK) offer a set of dialogs that you can use when working with files. By using these you don’t have to design standard dialogs your self. Example dialogs include an open file dialog, a save file dialog and many others. Besides file dialogs there are other standard dialogs, but in this article we will focus on file dialogs.

root = Tk()
root.geometry("450x350+250+110")
root.resizable(width=True, height=True)
root.img = None

#su dung root R, G, B de lay du lieu tu tk
root.R =tk.StringVar()
root.G =tk.StringVar()
root.B =tk.StringVar()


#tao file moHinhAnh de load anh tu may len
def moHinhAnh():
    hinhAnh = filedialog.askopenfilename(title='Mo Thu Muc')
    return hinhAnh

#tao file open_img de hien thi anh sau khi moHInhanh ra tk
def open_img():
    x = moHinhAnh()
    hinhAnh = Image.open(x)
    root.img = hinhAnh
    hinhAnh1 = hinhAnh.resize((200, 200), Image.ANTIALIAS)
    hinhAnh1 = ImageTk.PhotoImage(hinhAnh1)
    #sau khi hien thi hinhAnh1 ra man hinh, tao mot panel chua noi dung la hinhAnh1, su dung cac dinh dang nhu column, row, columnspan de co the dinh dang panel nay
    panel = Label(root, image=hinhAnh1)
    panel.image = hinhAnh1
    panel.grid(column=0,row=2,columnspan = 2)

#viet ham thayDoiMau de tao ra mot hinh anh moi voi du lieu input la r.g.b
def thayDoiMau(r=0,g=0,b=0):
    img = root.img.convert("RGB")
    diLieu = img.getdata()
    #su dung bien diLieu de lay duoc du lieu hinh anh cua hinh duoc load len
    #su dung bien hinhAnhDuLieuMoi de luu cac input nguoi dung nhap duoi dang mang
    hinhAnhDuLieuMoi = []

    for i in diLieu:
        # change all white (also shades of whites) pixels to yellow
        if i[0] in list(range(0, 255)):
            hinhAnhDuLieuMoi.append((r, g, b))
        else:
            hinhAnhDuLieuMoi.append(i)
    #tien hanh add du lieu moi de thay doi hinh anh hien tai
    img.putdata(hinhAnhDuLieuMoi)
    return img

def capNhatMau():

    a = int(root.R.get())
    b = int(root.G.get())
    c = int(root.B.get())
    #goi ham thay doi mau
    hinhAnh2 = thayDoiMau(a,b,c)
    #tien hanh thay doi kich thuong
    hinhAnh2 = hinhAnh2.resize((200, 200), Image.ANTIALIAS)
    hinhAnh2 = ImageTk.PhotoImage(hinhAnh2)
    panel2 = Label(root, image=hinhAnh2)
    panel2.image = hinhAnh2
    panel2.grid(column=2,row=2,columnspan = 2)
    #load anh 2 ra panel moi tao

#tien hanh them cac buton vao tk
#buttons
btn = tk.Button(root, text='Chon anh', command=open_img).grid(column=0,row=0)
#input

G = tk.Entry(root,textvariable=root.G).grid(column=1,row=1)

R = tk.Entry(root,textvariable=root.R).grid(column=0,row=1)

B = tk.Entry(root,textvariable=root.B).grid(column=2,row=1)

btn = tk.Button(root, text='Cap Nhat Image', command=capNhatMau).grid(column=3,row=1)

root.mainloop()