import tkinter as tk
import tkinter.ttk as ttk
from easygui import fileopenbox, filesavebox

w = tk.Tk()

#Блокнот

def open_file_button():
    path = fileopenbox(title="Открываем файл")
    with open(path,"r",encoding="utf-8") as f:
        t = f.read()
        text.delete("0.0","end")
        text.insert("0.0",t)

def save_file_button():
    path = filesavebox(title="Сохраняем файл")
    with open(path,"w",encoding="utf-8") as f:
        f.write( text.get("0.0","end") )
        f.close()


exit = w.quit

def new_file():
    text.delete("0.0","end")

def about():
    a = tk.Toplevel(w)
    a.geometry("500x300")
    info = ttk.Label(a, text="Эта программа сделана мной!", font=("Helvetica",20))
    info.pack()

w.title("Тетрадка")

m = tk.Menu(w)
w.config(menu=m)

file_menu = tk.Menu(m, tearoff=False)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть...", command=open_file_button)
file_menu.add_command(label="Сохранить...", command=save_file_button)
file_menu.add_separator()
file_menu.add_command(label="Выйти", command=exit)

m.add_cascade(label="Файл", menu=file_menu)

help_menu = tk.Menu(m, tearoff=False)
help_menu.add_command(label="О программе", command=about)
m.add_cascade(label="Справка", menu=help_menu)

scroll_bar = ttk.Scrollbar(w)
scroll_bar.pack(side="right",fill="y")

text = tk.Text(w, yscrollcommand=scroll_bar.set)
text.pack(expand=True, fill='both')

scroll_bar.config(command = text.yview)


# openfile = ttk.Button(w,text='Открыть файл...', command=open_file_button)
# openfile.pack(expand=True, fill="x")

# savefile = ttk.Button(w,text='Сохранить файл...', command=save_file_button)
# savefile.pack(expand=True, fill="x")


w.mainloop()