from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import ttk
from tkinter import messagebox
import arabic_reshaper as ar
from bidi.algorithm import get_display

v = 'Vazir'
def on_closing():
    a = messagebox.askyesno(" Schools_V1 ","  آیا می خواهید خارج شوید ؟")
    if a:
        messagebox.showinfo(" Schools_V1 ", " ! به امید دیدار ")
        exit()
    else :
        messagebox.showinfo(" Schools_V1 ", " ! خروج لغو شد")
Root_Window = tk.Tk(
#    screenName = "Schools_V1" ,
#    baseName = "Schools_V1" ,
)
Root_Window.title(" Schools_V1 ")
Root_Window.geometry("700x500")
Root_Window.protocol("WM_DELETE_WINDOW", on_closing)

 #Menu Bar
menubar = Menu(Root_Window)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='فایل', menu = file)
file.add_command(label ='خروج', command = on_closing)
Root_Window.config(menu = menubar)
tk.Label(Root_Window,text="  ",font=(v, 5)).pack(side=TOP)
tk.Label(Root_Window,text="  ",font=(v, 5)).pack(side=RIGHT)
tk.Label(Root_Window,text="  ",font=(v, 5)).pack(side=LEFT)
tk.Label(Root_Window,text="  ",font=(v, 5)).pack(side=BOTTOM)
tk.Label(Root_Window,text=get_display(ar.reshape(" . امیرحسین عباسی فاروجی . تمامی حقوق محفوظ است ")),font=(v,10)).pack(side=BOTTOM)

# Right Main Button Panel
btn_frm = tk.Frame(Root_Window)
btn_frm.pack(side=RIGHT, anchor=N)
btn_frm.config(bg = "#337AFF")
tk.Label(btn_frm, text="", bg="#337AFF").pack(side=TOP)
tk.Label(btn_frm, text="", bg="#337AFF").pack(side=RIGHT)
tk.Label(btn_frm, text="", bg="#337AFF").pack(side=LEFT)
tk.Label(btn_frm, text="", bg="#337AFF").pack(side=BOTTOM)

hidden = True

btn_frm_b1 = tk.Frame(btn_frm)
btn_frm_b1.pack(expand=1, anchor=N)
btn_frm_b1.config(bg="#337AFF")

btn_frm_b2 = tk.Frame(btn_frm)
btn_frm_b2.pack(expand=1)
btn_frm_b2.config(bg="#337AFF")

# First Group
def frst_grp_mvn_ejr():
    def mdrt_ansh_amz():
        global hidden
        if hidden:
            lb_fsl.pack()
            sbt_dnsh_amz_jdd.pack()
        else:
            lb_fsl.pack_forget()
            sbt_dnsh_amz_jdd.pack_forget()
        hidden = not hidden
    mdrt_ansh_amz_btn = ttk.Button(btn_frm_b1, text=" < مدیریت دانش آموزان ", command=mdrt_ansh_amz).pack(side=TOP)
    lb_fsl = tk.Label(btn_frm_b1, bg="#337AFF")
    sbt_dnsh_amz_jdd = ttk.Button(btn_frm_b1, text=" ثبت نام دانش آموز جدید ")

frst_grp_mvn_ejr()
# Second Group
def scnd_grp_mvn_ejr():
    tk.Label(btn_frm_b2, text="", bg="#337AFF").pack()
    mdrt_sbt = ttk.Button(btn_frm_b2, text=" امور ثبتی ").pack()
scnd_grp_mvn_ejr()
Root_Window.mainloop()
