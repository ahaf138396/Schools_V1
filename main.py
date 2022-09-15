from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
from notifypy import Notify
from tkinter import messagebox
from tkinter import ttk
import arabic_reshaper as ar
from bidi.algorithm import get_display as gtdsp
import sys
import os

# Start Notification
notification = Notify(
    default_notification_application_name=" Schools_V1",
    default_notification_title="هشدار"
)
notification.message = "برنامه در حال اجرا شدن می باشد"
notification.send()
# Main Window
Root_Window = tk.Tk(
    baseName = "Schools_V1" , 
)
Root_Window.title(" Schools_V1 ")


def on_closing():
    a = messagebox.askyesno(" Schools_V1 ",gtdsp(ar.reshape(" آیا میخواهید خارج شوید ؟") ))
    if a:
        messagebox.showinfo(" Schools_V1 ", gtdsp(ar.reshape(" به امید دیدار .")))
        exit()
    else:
        messagebox.showinfo(" Schools_V1 ", gtdsp(ar.reshape(" خروج لغو شد . ")))


Root_Window.resizable(0, 0)

# Menu Bar
menubar = Menu(Root_Window)
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label=gtdsp(ar.reshape(' فایل ')), menu=file)
file.add_command(label = gtdsp(ar.reshape(' خروج ')), command=on_closing)
Root_Window.config(menu=menubar)

empty_1 = ttk.Label(text=" ").grid(row=0, column=3)
empty_2 = ttk.Label(text="   ").grid(row=0, column=0)
empty_2 = ttk.Label(text="   ").grid(row=0, column=4)

l1 = ttk.Label(text=gtdsp(ar.reshape(" سامانه جامع اداری ")), font=('Vazir', 14)).grid(row=1, column=2)
l2 = ttk.Label(text=gtdsp(ar.reshape(" نام کاربری : ")), font=('Vazir', 12)).grid(row=2, column=3)
l3=ttk.Label(text=gtdsp(ar.reshape(" کلمه عبور : ")) ,font=('Vazir', 12)).grid(row=3, column=3)

name_var=tk.StringVar()
pswd_var=tk.StringVar()
e1=ttk.Entry(textvariable=name_var).grid(row=2, column=2)
e2=ttk.Entry(textvariable=pswd_var, show='*').grid(row=3, column=2)

def submit():
    usr=name_var.get()
    pswd=pswd_var.get()
    if usr == "1" or usr == "2":
        #messagebox.showinfo(" Schools_V1 ", get_display(ar.reshape(". خوش آمدید . لطفا کمی صبر کنید")))
        def open_Toplevel1():
            def top1():
                top1=Toplevel(Root_Window)
                top1.title(" Schools_V1 ")
                tp_lbl=ttk.Label(top1, text=gtdsp(ar.reshape(" . لطفا تا بارگذاری اطلاعات شکیبا باشید ")), font=('Vazir', 13)).pack()
                tp_btn=Button(top1, text=gtdsp(ar.reshape(" خروج ")), command=Root_Window.destroy).pack()
            # top1()
        #open_Toplevel1()
        Root_Window.destroy()
        import ent
    else:
        messagebox.showerror(
            " Schools_V1 ", gtdsp(ar.reshape(" . هشدار ! نام کاربری یا کلمه عبور اشتباه است"))
        )

def entr_prs(event):
    key=event.char
    submit()
Root_Window.bind('<Return>', entr_prs)
sbmt_btn=ttk.Button(
    text=gtdsp(ar.reshape(' تأیید ')),
    command=submit
)

sbmt_btn.grid(row=5, column=3)
link=Label(Root_Window, text=gtdsp(ar.reshape(" فراموشی رمز عبور ")),
           font=('Vazir', 8), cursor="hand2")
link.grid(row=5, column=2)
link.bind(
    "<Button-1>", lambda e: messagebox.showerror(
        " Schools_V1 ", gtdsp(ar.reshape(" لطفا برای تغییر رمز عبور با مدیر سیستم تماس بگیرید .")))
)

l_end=ttk.Label(
    text=gtdsp(ar.reshape(" امیرحسین عباسی فاروجی . تمامی حقوق محفوظ است . ")) ,
    font=('Vazir', 9),
).grid(row=20, column=2)

Root_Window.mainloop()

# Main window finished
