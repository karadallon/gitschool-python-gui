import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER


class MyApp(toga.App):
    def startup(self):
        # Главный контейнер
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=10))

        # Текстовое поле
        self.label = toga.Label("Привет, мир!", style=Pack(padding=10))

        # Кнопка
        btn = toga.Button("Нажми меня", on_press=self.on_click, style=Pack(padding=10))

        # Добавляем элементы в окно
        main_box.add(self.label)
        main_box.add(btn)

        # Создаём и показываем главное окно
        self.main_window = toga.MainWindow(title="Пример на Toga")
        self.main_window.content = main_box
        self.main_window.show()

    def on_click(self, widget):
        self.label.text = "Кнопка нажата!"


def main():
    return MyApp("Моё приложение", "org.example.myapp")


if __name__ == "__main__":
    main().main_loop()