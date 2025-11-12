import customtkinter as ctk

# Настройка внешнего вида
ctk.set_appearance_mode("Dark")  # Темная тема
ctk.set_default_color_theme("blue")  # Цветовая тема

# Создание основного окна
app = ctk.CTk()
app.title("Мое первое приложение на CustomTkinter")
app.geometry("400x200")

# Функция для кнопки
def button_click_event():
    label.configure(text=entry.get() + " - это круто!")

# Создание элементов интерфейса
label = ctk.CTkLabel(app, text="Введите ваше имя:")
label.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text="Ваше имя здесь...")
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Нажми меня!", command=button_click_event)
button.pack(pady=10)

# Запуск главного цикла
app.mainloop()