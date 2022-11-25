from tkinter import *
from tkinter import ttk
from main import *

win = Tk()
win.title("Téglalap terület, kerület")
win.geometry("250x650")
global mertekegyseg, mertekegyseg_szamitott
tegla = Teglalap()

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

    label1 = Label(win, text="", font=('Century 15 bold'))
    label1.config(text="A terület: {} {}2".format(szamitas_text1, mertekegyseg_szamitott))
    label1.pack(pady=5)

    label2 = Label(win, text="", font=('Century 15 bold'))
    label2.config(text="A kerület: {} {}".format(szamitas_text2, mertekegyseg_szamitott))
    label2.pack(pady=5)

label_radio1 = Label(win, text="Miből ")
label_radio1.pack()
var = IntVar()
R1 = Radiobutton(win, text="cm", variable=var, value=1)
R1.pack()
R2 = Radiobutton(win, text="dm", variable=var, value=2)
R2.pack()

label_radio2 = Label(win, text="Mibe ")
label_radio2.pack()
var_mibe = IntVar()
R3 = Radiobutton(win, text="cm", variable=var_mibe, value=1)
R3.pack()
R4 = Radiobutton(win, text="dm", variable=var_mibe, value=2)
R4.pack()


entry = ttk.Entry(win, font=("Century 12"), width=20)
entry.pack(pady=15)
entry2 = ttk.Entry(win, font=('Century 12'), width=20)
entry2.pack(pady=15)

button = ttk.Button(win, text="Enter", command=get_value)
button.pack()
win.mainloop()
