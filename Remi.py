# Импорт необходимых модулей Remi
import remi.gui as gui
from remi import start, App

# Создание класса приложения
class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    # Это основной метод для построения интерфейса
    def main(self):
        # Основной контейнер (вертикальный)
        container = gui.VBox(width=400, height=200, margin='10px')
        
        # Заголовок
        self.title_label = gui.Label("Привет! Введи текст ниже и нажми кнопку:", width='100%', height='30px')
        container.append(self.title_label)
        
        # Текстовое поле
        self.input_text = gui.TextInput(single_line=True, width='100%')
        container.append(self.input_text)
        
        # Кнопка
        self.button = gui.Button("Показать текст", width='100%')
        container.append(self.button)
        
        # Лейбл для вывода текста
        self.output_label = gui.Label("", width='100%', height='30px')
        container.append(self.output_label)
        
        # Привязка события кнопки
        self.button.onclick.do(self.on_button_pressed)
        
        return container

    # Метод для обработки нажатия кнопки
    def on_button_pressed(self, widget):
        user_text = self.input_text.get_text()
        self.output_label.set_text(f"Вы ввели: {user_text}")

# Запуск приложения на локальном сервере
if __name__ == "__main__":
    start(MyApp, address='0.0.0.0', port=8081, start_browser=True)