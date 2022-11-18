import tkinter as tk

option1 = ["celcius", "fahrenheit", "reamur", "kelvin"]
option2 = ["celcius", "fahrenheit", "reamur", "kelvin"]

def rumus():
    dar = variable.get()
    ke = variable1.get()
    jawab = float(e1.get())
    if (dar == ke):
        tot = jawab
    elif (dar == "celcius"):
        if ke == 'fahrenheit':
            tot = (jawab * 9/5) + 32
        elif ke == 'reamur':
            tot = (jawab * 4/5)
        else:
            tot = jawab + 273.15
    elif (dar == "fahrenheit"):
        if ke ==  'celcius':
            tot = (jawab - 32) * 5/9
        elif ke == 'reamur':
            tot = (jawab - 32) * 4/9
        else:
            tot =(jawab - 32) * 5/9 + 273.15
    elif (dar == "reamur"):
        if ke == 'celcius':
            tot = (jawab * 5/4)
        elif ke == 'fahrenheit':
            tot = (jawab * 9/4) + 32
        else:
            tot = (jawab * 5/4) + 273.15
    elif (dar == "kelvin"):
        if ke == 'fahrenheit':
            tot = (jawab - 273.15) * 9/5 + 32
        elif ke == 'reamur':
            tot = (jawab - 273.15) * 4/5
        else:
            tot = jawab - 273.15
    outText.set(tot)

win = tk.Tk()
win.geometry('350x200')
win.title('Konverter Suhu Menggunkan Gui')

variable = tk.StringVar(win)
variable.set(option1[0])

opt = tk.OptionMenu(win, variable, *option1)
opt.config(width=10, font=('Arial', 12))
opt.pack(side="top")

variable1 = tk.StringVar(win)
variable1.set(option2[0])

opt = tk.OptionMenu(win, variable1, *option2)
opt.config(width=10, font=('Arial', 12))
opt.pack(side="top")

global e1
global outText
outText = tk.StringVar()
labelText = tk.Label(text="", font=('Arial', 14), fg='red')
labelText.pack(side="top")

tk.Label(win, text="Dari").place(x=10, y=10)
tk.Label(win, text="Ke").place(x=10, y=50)
tk.Label(win, text="Suhu").place(x=10, y=90)

tk.Label(win, text="Hasil: ").place(x=10, y=160)
tk.Label(win, text="", font=('Arial', 14), fg='red', textvariable=outText).place(x=110, y=160)
tk.Button(win, text="Convert", command=rumus, height=1, width=8).place(x=110, y=120)

e1 = tk.Entry(win)
e1.place(x=80, y=80)

win.mainloop()
