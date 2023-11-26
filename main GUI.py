from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from KivyDesigns.main_menu.main_menu import MainMenu
from KivyDesigns.template.template import HiddenButton, NavigationButton, ButtonMenu
from KivyDesigns.play.play import Play
from KivyDesigns.screen_size.screen_size import ScreenSize
from KivyDesigns.settings.settings import SettingsScreen
from KivyDesigns.standard_flow.standard_flow import StandardFlow
from KivyDesigns.ultimate_flow.ultimate_flow import UltimateFlow



class RoundChoiceThreeDim(Screen):
    pass


class RoundChoiceFourDim(Screen):
    pass


class RoundChoiceFiveDim(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MainGameTrial(Screen):

    def disable(self):

        if self.ids.seven.disabled is False:
            self.ids.seven.disabled = True
            self.ids.seven.background_disabled_normal = \
                '/home/dawid/TicTacToeGame/TicTacToeUltimate/Assets/Standard/Icons/Circle.png'

        print("Button was clicked and disabled")

    def replace_an_image(self):
        self.ids.round_box.source = \
            '/home/dawid/TicTacToeGame/TicTacToeUltimate/Assets/Standard/Icons/Filled Round Box.png'


class TicTacToeUltimateApp(App):
    def build(self):
        return Builder.load_file('tictactoeultimate.kv')


if __name__ == '__main__':
    TicTacToeUltimateApp().run()
