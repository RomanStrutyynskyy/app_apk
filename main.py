import os
# Залишаємо налаштування, які спрацювали
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class MyRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        # Малюємо білий фон
        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1) # Світло-сірий
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Текст
        self.label = Label(
            text="Kivy на Android",
            font_size='32sp',
            color=(0.2, 0.2, 0.2, 1) # Темний текст
        )
        
        # Кнопка
        self.btn = Button(
            text="Змінити колір",
            size_hint=(1, 0.2),
            background_normal='', # Прибираємо стандартну текстуру
            background_color=(0.1, 0.6, 0.8, 1) # Блакитний
        )
        self.btn.bind(on_press=self.change_text)

        self.add_widget(self.label)
        self.add_widget(self.btn)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def change_text(self, instance):
        self.label.text = "Готово до збірки APK!"
        self.btn.background_color = (0.2, 0.8, 0.2, 1) # Змінюємо на зелений

class ProApp(App):
    def build(self):
        return MyRoot()

if __name__ == "__main__":
    ProApp().run()