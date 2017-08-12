import os
import os.path as osp
from tkinter import *
from os import popen
import subprocess as sp
count = 0
fn = ""
def creater():
    global count
    count += 1
    if "Codes" not in os.listdir(osp.expanduser('/root/Desktop/PyruN')):
        os.mkdir(osp.join(osp.expanduser('/root/Desktop/PyruN') , "Codes"))
        os.chdir(osp.join(osp.expanduser('/root/Desktop/PyruN') , "Codes"))
    else:
        os.chdir(osp.join(osp.expanduser('/root/Desktop/PyruN') , "Codes"))
    if inpt.get() != "":
        xs = str(inpt.get())
        s = "/root/Desktop/PyruN/Codes/" + xs
        f = open(s,"a+")
        f.close()
    else:
        count = 0
    if count ==  1 and inpt.get() != "":
        b = Button(text = "Run", command = runfile)
        b.pack()
def runfile():
    os.system("clear")
    xs = str(inpt.get())
    s = "/root/Desktop/PyruN/Codes/" + xs
    runf = "python3 " + s
    os.system(runf)
    #rsp = sp.Popen(["python3",s], stdout=sp.PIPE)
    #out = rsp.communicate()
    #print(out)
def listfile():
    os.system("clear")
    files = os.listdir(osp.expanduser('/root/Desktop/PyruN/Codes'))
    for i in files:
        print(i)
def rmrf():
    global fn
    fils = os.listdir(osp.expanduser('/root/Desktop/PyruN/Codes'))
    ed = Tk()
    ed.geometry("250x400")
    ed.title("")
    m = Label(ed, text = "Remove Files")
    m.pack()
    for w in fils:
        f = Label(ed, text=w)
        f.pack( anchor = W )
    f_1 = Label(ed,text = "")
    f_1.pack( anchor = W)
    f_2 = Label(ed,text = "Enter Name of File:")
    fn = Entry(ed)
    f_2.pack( anchor = W )
    fn.pack( anchor = W )
    editt = Button(ed, text = "Remove", command = lastchance)
    editt.pack(anchor = W)
    ex = Button(ed, text = "Exit", command = ed.destroy)
    ex.pack(side="bottom")
    ed.mainloop()
def lastchance():
    global fn
    lc = Tk()
    def rmkill():
        removefile()
        lc.destroy()
    lc.geometry("250x100")
    lc.title("")
    q = Label(lc, text = ("Remove " + fn.get() + "?"))
    y = Button(lc, text = "Yes", command = rmkill)
    n = Button(lc, text = "No", command = lc.destroy)
    q.pack()
    y.pack()
    n.pack()
    lc.mainloop()  
def removefile():
    global fn
    if fn.get() != "":
        com = "rm /root/Desktop/PyruN/Codes/"+fn.get()
        os.system(com)
    else:
        os.system("clear")
def editfile():
    fils = os.listdir(osp.expanduser('/root/Desktop/PyruN/Codes'))
    ed = Tk()
    ed.geometry("250x400")
    ed.title("")
    m = Label(ed, text = "Edit Files")
    m.pack()
    for w in fils:
        f = Label(ed, text=w)
        f.pack( anchor = W )
    f_1 = Label(ed,text = "")
    f_1.pack( anchor = W)
    f_2 = Label(ed,text = "Enter Name of File:")
    inpt_2 = Entry(ed)
    f_2.pack( anchor = W )
    inpt_2.pack( anchor = W )
    editt = Button(ed, text = "Edit", command = lambda: os.system("gedit /root/Desktop/PyruN/Codes/" + inpt_2.get()))
    editt.pack(anchor = W)
    ex = Button(ed, text = "Exit", command = ed.destroy)
    ex.pack(side="bottom")
    ed.mainloop()
window = Tk()
music = Button(text = "Music",command = lambda: os.system("play /root/Desktop/PyruN/codex.mp3"))
window.geometry("400x250")
window.title("PyruN".center(64))
mes = Label(text = "Create or Open File")
inpt = Entry()
button = Button(text = "Create or Open", command = creater)
eb = Button(text = "Exit", command = window.destroy)
lis = Button(text = "List Files", command = listfile)
remove = Button(text = "Remove File", command = rmrf)
edit = Button(text = "Edit File", command = editfile)
mes.pack()
inpt.pack()
button.pack()
lis.pack()
edit.pack()
remove.pack()
music.pack()
eb.pack(side = "bottom")
window.mainloop()
