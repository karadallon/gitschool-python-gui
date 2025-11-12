import tkinter as tk
import tkinter.ttk as ttk

def caps():
    input_text = t.get()
    res = input_text.upper()
    l['text'] = res

w = tk.Tk()
w.resizable(False,False)
w.title('Увеличитель текста')

b = ttk.Button(w,text="Hello", command=caps, width='60')
b.pack()

l = ttk.Label(w, text="Здесь будет текст")
l.pack()

t = ttk.Entry(w, width="60")
t.pack()

w.mainloop()
