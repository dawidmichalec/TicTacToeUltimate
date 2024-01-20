from kivymd.app import MDApp
from kivy.lang.builder import Builder
from window_manager import WindowManager


class TicTacToeUltimateApp(MDApp):
    def build(self):
        Builder.load_file('tictactoeultimate.kv')


if __name__ == '__main__':
    TicTacToeUltimateApp().run()