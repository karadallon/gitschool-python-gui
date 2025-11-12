import tkinter as tk
import tkinter.ttk as ttk
import random

def throw():
    res = random.randint(1,6)
    t.delete(0,'end')
    t.insert(0, str(res))

w = tk.Tk()
w.resizable(False,False)
w.title('Бросатель кубиков')

b = ttk.Button(w,text="Бросить кубик", width='60', command=throw)
b.pack()

t = ttk.Entry(w, width="60")
t.pack()

w.mainloop()