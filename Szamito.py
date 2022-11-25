from tkinter import *
from tkinter import ttk
from main import *
import webbrowser

win = Tk()
win.title("Téglalap terület, kerület")
win.geometry("250x550")
global mertekegyseg, mertekegyseg_szamitott
tegla = Teglalap()
label_cim = Label(win, text="Téglalap terület,\n és kerület \nszámító", font='Century 15 bold')
label_cim.pack(pady=5)


def get_value():
    global mertekegyseg, mertekegyseg_szamitott
    if var.get() == 1:
        mertekegyseg = "cm"
    elif var.get() == 2:
        mertekegyseg = "dm"
    if var_mibe.get() == 1:
        mertekegyseg_szamitott = "cm"
    elif var_mibe.get() == 2:
        mertekegyseg_szamitott = "dm"
    a_text = entry.get()
    b_text = entry2.get()

    tegla.bekeres(a_text, b_text)
    szamitas_text1, szamitas_text2 = tegla.szamitas(mertekegyseg, mertekegyseg_szamitott)

    # label1 = Label(win, text="", font='Century 15 bold')
    label1.config(text="A terület: {} {}2".format(szamitas_text1, mertekegyseg_szamitott))
    # label1.pack(pady=5)

    # label2 = Label(win, text="", font='Century 15 bold')
    label2.config(text="A kerület: {} {}".format(szamitas_text2, mertekegyseg_szamitott))
    # label2.pack(pady=5)


def bongeszo():
    edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge))
    # webbrowser.open("https://hu.wikipedia.org/wiki/T%C3%A9glalap")
    webbrowser.get('edge').open('https://hu.wikipedia.org/wiki/T%C3%A9glalap')


label_radio1 = Label(win, text="Miből ", font='Century 10 bold')
label_radio1.pack()
var = IntVar()
R1 = Radiobutton(win, text="cm", font='Century 10 bold', variable=var, value=1)
R1.pack()
R2 = Radiobutton(win, text="dm", font='Century 10 bold', variable=var, value=2)
R2.pack()

label_radio2 = Label(win, text="Mibe ", font='Century 10 bold')
label_radio2.pack()
var_mibe = IntVar()
R3 = Radiobutton(win, text="cm", font='Century 10 bold', variable=var_mibe, value=1)
R3.pack()
R4 = Radiobutton(win, text="dm", font='Century 10 bold', variable=var_mibe, value=2)
R4.pack()

label_a = Label(win, text="", font='Century 12 bold')
label_a.config(text="Adja meg az 'A' oldalt:")
label_a.pack(pady=5)
entry = ttk.Entry(win, font="Century 12", width=20)
entry.pack(pady=15)

label_b = Label(win, text="", font='Century 12 bold')
label_b.config(text="Adja meg az 'B' oldalt:")
label_b.pack(pady=5)
entry2 = ttk.Entry(win, font='Century 12', width=20)
entry2.pack(pady=15)

button = ttk.Button(win, text="Számol", command=get_value)
button.pack()

button_url = ttk.Button(win, text="Téglalapról bővebben", command=bongeszo)
button_url.pack()

label1 = Label(win, text="", font='Century 12 bold')
label2 = Label(win, text="", font='Century 12 bold')
label1.pack(pady=5)
label2.pack(pady=5)

win.mainloop()
