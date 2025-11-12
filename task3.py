import tkinter as tk
import tkinter.ttk as ttk

w = tk.Tk()
w.title("ГДЗ")
w.resizable(False,False)

def solve():
    S = int( dist.get()  )
    v = int( velo.get()  )
    t = S/v
    time['text'] = "Ответ: " + str(t)

dist_help = ttk.Label(w,text="Расстояние")
dist = ttk.Entry(w)

velo_help = ttk.Label(w,text="Скорость")
velo = ttk.Entry(w)

enter = ttk.Button(w, text="Решить",width=20, command=solve)
time = ttk.Label(w, text="Ответ:")

dist_help.grid(column=0, row=0)
dist.grid(row=1, column=0)
velo_help.grid(row=0, column=1)
velo.grid(row=1,column=1)
enter.grid(row=2,column=0, columnspan=2)
time.grid(row=3,column=0, columnspan=2, sticky="W")

w.mainloop()