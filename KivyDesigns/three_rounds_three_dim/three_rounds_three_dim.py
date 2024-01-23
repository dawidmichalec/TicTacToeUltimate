from kivy.uix.screenmanager import Screen
from kivymd.uix.menu.menu import MDDropdownMenu
from kivy.factory import Factory
from kivy.app import App


class ThreeRoundsThreeDim(Screen):

    turn = "Circle"
    hidden_button = '/home/dawid/TicTacToeGame/TicTacToeUltimate/Assets/Standard/Icons/Button Background.png'
    circle_path = '/home/dawid/TicTacToeGame/TicTacToeUltimate/Assets/Standard/Icons/Circle.png'
    cross_path = '/home/dawid/TicTacToeGame/TicTacToeUltimate/Assets/Standard/Icons/Cross.png'
    circle_turn_highlight = \
        '/home/dawid/TicTacToeGame/TicTacToeUltimate/Assets/Standard/Icons/Circle Turn Highlighted.png'
    circle_turn_no_highlight = \
        '/home/dawid/TicTacToeGame/TicTacToeUltimate/Assets/Standard/Icons/Circle Turn No Highlight.png'
    cross_turn_highlight = \
        '/home/dawid/TicTacToeGame/TicTacToeUltimate/Assets/Standard/Icons/Cross Turn Highlighted.png'
    cross_turn_no_highlight = \
        '/home/dawid/TicTacToeGame/TicTacToeUltimate/Assets/Standard/Icons/Cross Turn No Highlight.png'
    filled_round_box_path = \
        '/home/dawid/TicTacToeGame/TicTacToeUltimate/Assets/Standard/Icons/Filled Round Box.png'
    empty_round_box_path = \
        '/home/dawid/TicTacToeGame/TicTacToeUltimate/Assets/Standard/Icons/Empty Round Box.png'
    turn_count = 1
    circle_win = 0
    cross_win = 0

    def reset_if_main_menu(self):
        self.reset_rounds()
        self.reset_playground()
        self.round = 1
        self.cross_win = 0
        self.circle_win = 0

    def on_enter(self):

        self.reset_rounds()
        self.reset_playground()
        return True


    def check_win_cross(self):
        # HORIZONTAL
        if self.ids.seven.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal\
                == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.cross_win += 1
            App.get_running_app().root.current = 'cross_wins'
            return True

        if self.ids.four.background_disabled_normal == self.cross_path and self.ids.five.background_disabled_normal\
                == self.cross_path and self.ids.six.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.cross_win += 1
            App.get_running_app().root.current = 'cross_wins'
            return True

        if self.ids.one.background_disabled_normal == self.cross_path and self.ids.two.background_disabled_normal\
                == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.cross_win += 1
            App.get_running_app().root.current = 'cross_wins'
            return True

        # VERTICAL

        if self.ids.seven.background_disabled_normal == self.cross_path and self.ids.four.background_disabled_normal\
                == self.cross_path and self.ids.one.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.cross_win += 1
            App.get_running_app().root.current = 'cross_wins'
            return True

        if self.ids.eight.background_disabled_normal == self.cross_path and self.ids.five.background_disabled_normal\
                == self.cross_path and self.ids.two.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.cross_win += 1
            App.get_running_app().root.current = 'cross_wins'
            return True

        if self.ids.nine.background_disabled_normal == self.cross_path and self.ids.six.background_disabled_normal\
                == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.cross_win += 1
            App.get_running_app().root.current = 'cross_wins'
            return True

        # DIAGONAL

        if self.ids.seven.background_disabled_normal == self.cross_path and self.ids.five.background_disabled_normal\
            == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.cross_win += 1
            App.get_running_app().root.current = 'cross_wins'
            return True

        if self.ids.nine.background_disabled_normal == self.cross_path and self.ids.five.background_disabled_normal\
            == self.cross_path and self.ids.one.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.cross_win += 1
            App.get_running_app().root.current = 'cross_wins'
            return True

    def check_win_circle(self):

        # HORIZONTAL

        if self.ids.seven.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal\
                == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.circle_win += 1
            App.get_running_app().root.current = 'circle_wins'
            return True

        if self.ids.four.background_disabled_normal == self.circle_path and self.ids.five.background_disabled_normal\
                == self.circle_path and self.ids.six.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.circle_win += 1
            App.get_running_app().root.current = 'circle_wins'
            return True

        if self.ids.one.background_disabled_normal == self.circle_path and self.ids.two.background_disabled_normal\
                == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.circle_win += 1
            App.get_running_app().root.current = 'circle_wins'
            return True

        # VERTICAL

        if self.ids.seven.background_disabled_normal == self.circle_path and self.ids.four.background_disabled_normal\
                == self.circle_path  and self.ids.one.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.circle_win += 1
            App.get_running_app().root.current = 'circle_wins'
            return True

        if self.ids.eight.background_disabled_normal == self.circle_path and self.ids.five.background_disabled_normal\
                == self.circle_path and self.ids.two.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.circle_win += 1
            App.get_running_app().root.current = 'circle_wins'
            return True

        if self.ids.nine.background_disabled_normal == self.circle_path and self.ids.six.background_disabled_normal\
                == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.circle_win += 1
            App.get_running_app().root.current = 'circle_wins'
            return True

        # DIAGONAL

        if self.ids.seven.background_disabled_normal == self.circle_path and self.ids.five.background_disabled_normal\
            == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.circle_win += 1
            App.get_running_app().root.current = 'circle_wins'
            return True

        if self.ids.nine.background_disabled_normal == self.circle_path and self.ids.five.background_disabled_normal\
            == self.circle_path and self.ids.one.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.circle_win += 1
            App.get_running_app().root.current = 'circle_wins'
            return True

    def announce_draw(self, turn_count, check_win_circle, check_win_cross):
        if turn_count == 10 and check_win_cross is not True and check_win_circle is not True:
            App.get_running_app().root.current = 'draw'
            self.circle_win += 1
            self.cross_win += 1
            return True

        return False

    def disable_and_check_win(self, btn):

        if self.turn == "Circle":
            btn.disabled = True
            btn.background_disabled_normal = self.circle_path
            self.ids.circle_turn.source = self.circle_turn_no_highlight
            self.ids.cross_turn.source = self.cross_turn_highlight
            self.turn_count += 1
            self.turn = "Cross"
        else:
            btn.disabled = True
            btn.background_disabled_normal = self.cross_path
            self.ids.cross_turn.source = self.cross_turn_no_highlight
            self.ids.circle_turn.source = self.circle_turn_highlight
            self.turn_count += 1
            self.turn = "Circle"

        self.announce_draw(self.turn_count, self.check_win_circle(), self.check_win_cross())

    def reset_playground(self):

        self.turn = "Circle"
        self.turn_count = 1
        self.ids.cross_turn.source = self.cross_turn_no_highlight
        self.ids.circle_turn.source = self.circle_turn_highlight

        self.ids.seven.disabled = False
        self.ids.eight.disabled = False
        self.ids.nine.disabled = False
        self.ids.four.disabled = False
        self.ids.five.disabled = False
        self.ids.six.disabled = False
        self.ids.one.disabled = False
        self.ids.two.disabled = False
        self.ids.three.disabled = False

        self.ids.seven.background_disabled_normal = ''
        self.ids.eight.background_disabled_normal = ''
        self.ids.nine.background_disabled_normal = ''
        self.ids.four.background_disabled_normal = ''
        self.ids.five.background_disabled_normal = ''
        self.ids.six.background_disabled_normal = ''
        self.ids.one.background_disabled_normal = ''
        self.ids.two.background_disabled_normal = ''
        self.ids.three.background_disabled_normal = ''

    def reset_rounds(self):

        self.ids.round_box_circle_one.source = self.empty_round_box_path
        self.ids.round_box_cross_one.source = self.empty_round_box_path
        self.ids.round_box_circle_two.source = self.empty_round_box_path
        self.ids.round_box_cross_two.source = self.empty_round_box_path
        self.ids.round_box_circle_three.source = self.empty_round_box_path
        self.ids.round_box_cross_three.source = self.empty_round_box_path
        self.round = 1

    def dropdown(self):
        menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text" : "SOUND ON",
                "theme_text_color": "Custom",
                "on_release": lambda x="SOUND ON": self.sound_off(menu_list[1]["text"]),
                "text_color": [1, 1, 1, 1],
                "text_style": "BUTTON",
                "font_style": "H6"
            },
            {
                "viewclass": "OneLineListItem",
                "text": "RETURN TO MAIN MENU",
                "on_release": lambda x="RETURN TO MAIN MENU": [Factory.get('MyPopup')().open(), menu.dismiss()],
                "theme_text_color": "Custom",
                "text_color": [1, 1, 1, 1],
                "text_style": "BUTTON",
                "font_style": "H6"
            }
        ]

        menu = MDDropdownMenu(
            caller=self.ids.burger_menu,
            items=menu_list,
            width_mult=4.2,
            background_color=[0,0,0,1],
            radius=10

        )

        menu.open()

    def sound_off(self, text_item):
        if text_item == "SOUND ON":
            text_item = "SOUND OFF"
            return text_item
        else:
            text_item = "SOUND ON"
            return text_item

