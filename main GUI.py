from kivy.app import App
from kivy.lang.builder import Builder
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.behaviors.hover_behavior import HoverBehavior
Window.size = (1280, 720)


class MainMenu(Screen):
    pass


class Play(Screen):
    pass


class SettingsScreen(Screen):

    def turn_the_sound_off_on(self):
        text = self.ids.sound_button.text

        if text == 'SOUND ON':
            self.ids.sound_button.text = 'SOUND OFF'
        else:
            self.ids.sound_button.text = 'SOUND ON'


class ScreenSize(Screen):
    def resize_up(self):
        if Window.size != (1920, 1080):
            Window.size = (1920, 1080)

    def resize_to_normal(self):
        if Window.size != (1280, 720):
            Window.size = (1280, 720)


class StandardFlow(Screen):
    pass


class UltimateFlow(Screen):
    pass


class RoundChoiceThreeDim(Screen):
    pass


class RoundChoiceFourDim(Screen):
    pass


class RoundChoiceFiveDim(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class ButtonMenu(Button, HoverBehavior):
    background = ListProperty((0, 0, 0, 1))
    color = ListProperty((1, 1, 1, 1))

    def on_enter(self):
        self.background = (1, 222/255, 89/255, 1)
        self.color = (0, 0, 0, 1)

    def on_leave(self):
        self.background = (0, 0, 0, 1)
        self.color = (1, 1, 1, 1)


class NavigationButton(Button, HoverBehavior):
    background = ListProperty((0, 0, 0, 1))
    color = ListProperty((1, 1, 1, 1))

    def on_enter(self):
        self.background = (1, 222/255, 89/255, 1)
        self.color = (0, 0, 0, 1)

    def on_leave(self):
        self.background = (0, 0, 0, 1)
        self.color = (1, 1, 1, 1)


class TicTacToeUltimateApp(App):
    def build(self):
        return Builder.load_file('tictactoeultimate.kv')


if __name__ == '__main__':
    TicTacToeUltimateApp().run()
