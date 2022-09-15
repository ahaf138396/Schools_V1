
from logging.handlers import RotatingFileHandler
from sqlite3 import Row
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttkimport  
import os
import time
import datetime
from notifypy import Notify
import pybase64
from tkinter import messagebox
from time import strftime
import pyperclip as pc
from tkinter import ttk
import arabic_reshaper as ar
from bidi.algorithm import get_display as gtdsp

m = "2"
v = 'Vazir'
def acs_dnld_ht_k(self):
    if m == "2":
        messagebox.showerror(" Schools_V1",gtdsp(ar.reshape(" ! دسترسی شما به این قسمت رد شده است ")))
    else:
        print("hi")
        exit()
def acs_dnld():
    messagebox.showerror(" Schools_V1"," ! دسترسی شما به این قسمت رد شده است ")
def on_closing():
    a = messagebox.askyesno(" Schools_V1 ",gtdsp(ar.reshape(" آیا میخواهید خارج شوید ؟") ))
    if a:
        messagebox.showinfo(" Schools_V1 ", gtdsp(ar.reshape(" به امید دیدار .")))
        exit()
    else:
        messagebox.showinfo(" Schools_V1 ", gtdsp(ar.reshape(" خروج لغو شد . ")))


Root_Window = tk.Tk(
#    screenName = "Schools_V1" ,
#    baseName = "Schools_V1" ,
)
Root_Window.title(" Schools_V1 ")
Root_Window.geometry("700x500")
Root_Window.protocol("WM_DELETE_WINDOW", on_closing)
Root_Window.bind(
    '<Control-Alt-t>',
    acs_dnld_ht_k
)

# Menu Bar
menubar = Menu(Root_Window)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = gtdsp(ar.reshape(' فایل ')) , menu = file)
file.add_command(label =gtdsp(ar.reshape(' خروج ')), command = on_closing)
Root_Window.config(menu = menubar)
ttk.Label(Root_Window, text="  ", font=(v)).pack(side=LEFT)
ttk.Label(Root_Window, text="  ", font=(v,)).pack(side=RIGHT)
ttk.Label(Root_Window, text="  ", font=(v)).pack(side=TOP)
ttk.Label(Root_Window, text="  ", font=(v)).pack(side=BOTTOM)
ttk.Label(Root_Window, text=gtdsp(ar.reshape(" . امیرحسین عباسی فاروجی . تمامی حقوق محفوظ است "))).pack(side=BOTTOM)
def tarahi():
    messagebox.showerror(" Schools_V1",gtdsp(ar.reshape("  . متأسفانه این قسمت طراحی نشده است . ورود شما ممکن نیست   . از صبر شما سپاس گذاریم")))
ttk.Label(Root_Window, text=gtdsp(ar.reshape(" نرم افزار اداری "))).pack(side=TOP)
btn_1 = ttk.Button(Root_Window, text=gtdsp(ar.reshape(" مدیر مجموعه ")),  command=tarahi).pack(pady=18)
btn_2 = ttk.Button(Root_Window, text=gtdsp(ar.reshape("معاون آموزشی")), command=tarahi).pack(pady=18)
def mvn_ejr():
    Root_Window.destroy()
    import ent.mvn_ejr
    
btn_3 = ttk.Button(Root_Window, text=  gtdsp(ar.reshape(" معاونت اجرایی ")) ,command=mvn_ejr).pack(pady=18)
ttk.Label(Root_Window, text="  ").pack(side=BOTTOM)
btn_5 = ttk.Button(Root_Window, text= gtdsp(ar.reshape(" ورود تکنسین ")) , command=acs_dnld).pack(side=BOTTOM)

btn_ext = ttk.Button(Root_Window, text=gtdsp(ar.reshape(" خروج ")), command=on_closing).pack(pady=18)


Root_Window.mainloop()
