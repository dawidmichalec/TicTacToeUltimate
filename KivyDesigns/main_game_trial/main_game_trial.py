from kivy.uix.screenmanager import Screen
from kivymd.uix.menu.menu import MDDropdownMenu
from kivy.factory import Factory


class MainGameTrial(Screen):

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

    def check_win_cross(self):
        # HORIZONTAL
        if self.ids.seven.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal\
                == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Cross Player Wins!")
            return True

        if self.ids.four.background_disabled_normal == self.cross_path and self.ids.five.background_disabled_normal\
                == self.cross_path and self.ids.six.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Cross Player Wins!")
            return True

        if self.ids.one.background_disabled_normal == self.cross_path and self.ids.two.background_disabled_normal\
                == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Cross Player Wins!")
            return True

        # VERTICAL

        if self.ids.seven.background_disabled_normal == self.cross_path and self.ids.four.background_disabled_normal\
                == self.cross_path and self.ids.one.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Cross Player Wins!")
            return True

        if self.ids.eight.background_disabled_normal == self.cross_path and self.ids.five.background_disabled_normal\
                == self.cross_path and self.ids.two.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Cross Player Wins!")
            return True

        if self.ids.nine.background_disabled_normal == self.cross_path and self.ids.six.background_disabled_normal\
                == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Cross Player Wins!")
            return True

        # DIAGONAL

        if self.ids.seven.background_disabled_normal == self.cross_path and self.ids.five.background_disabled_normal\
            == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Cross Player Wins!")
            return True

        if self.ids.nine.background_disabled_normal == self.cross_path and self.ids.five.background_disabled_normal\
            == self.cross_path and self.ids.one.background_disabled_normal == self.cross_path:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Cross Player Wins!")
            return True

    def check_win_circle(self):

        # HORIZONTAL

        if self.ids.seven.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal\
                == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Circle Player Wins!")
            return True

        if self.ids.four.background_disabled_normal == self.circle_path and self.ids.five.background_disabled_normal\
                == self.circle_path and self.ids.six.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Circle Player Wins!")
            return True

        if self.ids.one.background_disabled_normal == self.circle_path and self.ids.two.background_disabled_normal\
                == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Circle Player Wins!")
            return True

        # VERTICAL

        if self.ids.seven.background_disabled_normal == self.circle_path and self.ids.four.background_disabled_normal\
                == self.circle_path  and self.ids.one.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Circle Player Wins!")
            return True

        if self.ids.eight.background_disabled_normal == self.circle_path and self.ids.five.background_disabled_normal\
                == self.circle_path and self.ids.two.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Circle Player Wins!")
            return True

        if self.ids.nine.background_disabled_normal == self.circle_path and self.ids.six.background_disabled_normal\
                == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Circle Player Wins!")
            return True

        # DIAGONAL

        if self.ids.seven.background_disabled_normal == self.circle_path and self.ids.five.background_disabled_normal\
            == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Circle Player Wins!")
            return True

        if self.ids.nine.background_disabled_normal == self.circle_path and self.ids.five.background_disabled_normal\
            == self.circle_path and self.ids.one.background_disabled_normal == self.circle_path:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.disable_all_buttons()
            print("Circle Player Wins!")
            return True

    def announce_draw(self, turn_count, check_win_circle, check_win_cross):
        if turn_count == 10 and check_win_cross is not True and check_win_circle is not True:
            return True

        return False

    def disable_and_check_win(self, btn):

        if self.turn == "Circle":
            btn.disabled = True
            btn.background_disabled_normal = self.circle_path
            self.ids.circle_turn.source = self.circle_turn_no_highlight
            self.ids.cross_turn.source = self.cross_turn_highlight
            self.turn_count += 1
            print(self.turn_count)
            self.turn = "Cross"
        else:
            btn.disabled = True
            btn.background_disabled_normal = self.cross_path
            self.ids.cross_turn.source = self.cross_turn_no_highlight
            self.ids.circle_turn.source = self.circle_turn_highlight
            self.turn_count += 1
            print(self.turn_count)
            self.turn = "Circle"

        self.check_win_cross()
        self.check_win_circle()
        self.announce_draw(self.turn_count, self.check_win_circle(), self.check_win_cross())

    def disable_all_buttons(self):
        if self.ids.seven.disabled is False:
            self.ids.seven.disabled = True
            self.ids.seven.background_disabled_normal = self.hidden_button

        if self.ids.eight.disabled is False:
            self.ids.eight.disabled = True
            self.ids.eight.background_disabled_normal = self.hidden_button

        if self.ids.nine.disabled is False:
            self.ids.nine.disabled = True
            self.ids.nine.background_disabled_normal = self.hidden_button

        if self.ids.four.disabled is False:
            self.ids.four.disabled = True
            self.ids.four.background_disabled_normal = self.hidden_button

        if self.ids.five.disabled is False:
            self.ids.five.disabled = True
            self.ids.five.background_disabled_normal = self.hidden_button

        if self.ids.six.disabled is False:
            self.ids.six.disabled = True
            self.ids.six.background_disabled_normal = self.hidden_button

        if self.ids.one.disabled is False:
            self.ids.one.disabled = True
            self.ids.one.background_disabled_normal = self.hidden_button

        if self.ids.two.disabled is False:
            self.ids.two.disabled = True
            self.ids.two.background_disabled_normal = self.hidden_button

        if self.ids.three.disabled is False:
            self.ids.three.disabled = True
            self.ids.three.background_disabled_normal = self.hidden_button

    def reset_playground(self):
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

    def on_leave(self):

        self.reset_rounds()
        self.reset_playground()
        return True

    def dropdown(self):
        menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text" : "SOUND ON",
                "theme_text_color": "Custom",
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
            width_mult=4.5,
            background_color=[0,0,0,1],
            radius=10

        )

        menu.open()
