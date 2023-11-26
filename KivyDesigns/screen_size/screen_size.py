from kivy.uix.screenmanager import Screen
from kivy.core.window import Window


class ScreenSize(Screen):
    Window.size = (1280, 720)

    def resize_up(self):
        if Window.size != (1920, 1080):
            Window.size = (1920, 1080)

    def resize_to_normal(self):
        if Window.size != (1280, 720):
            Window.size = (1280, 720)
