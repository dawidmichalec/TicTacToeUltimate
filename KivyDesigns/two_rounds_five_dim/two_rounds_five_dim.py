from kivy.uix.screenmanager import Screen
from kivymd.uix.menu.menu import MDDropdownMenu
from kivy.factory import Factory
from kivy.app import App


class TwoRoundsFiveDim(Screen):

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
    round = 1
    str_cross_win = "0"
    str_circle_win = "0"

    def reset_if_main_menu(self):
        self.reset_rounds()
        self.reset_playground()
        self.round = 1
        self.cross_win = 0
        self.circle_win = 0
        self.str_circle_win = "0"
        self.str_cross_win = "0"

    def on_enter(self):
        self.reset_playground()
        return True

    def two_cross_wins_round_two(self):
        self.ids.round_box_cross_one.source = self.filled_round_box_path
        self.cross_win += 1
        self.str_cross_win = str(self.cross_win)
        self.round += 1
        self.reset_playground()
        App.get_running_app().root.current = 'two_five_dim_cross_wins_round_two'
        return True

    def two_cross_wins_final_round(self):
        self.ids.round_box_cross_one.source = self.filled_round_box_path
        self.cross_win += 1
        self.str_cross_win = str(self.cross_win)
        self.round += 1
        self.reset_playground()
        App.get_running_app().root.current = 'two_five_dim_cross_wins_final_round'
        return True

    def cross_wins(self):
        self.ids.round_box_cross_two.source = self.filled_round_box_path
        self.cross_win += 1
        self.round += 1
        self.str_cross_win = str(self.cross_win)
        App.get_running_app().root.current = 'two_five_dim_cross_wins_the_match'
        return self.str_cross_win

    def two_circle_wins_round_two(self):
        self.ids.round_box_circle_one.source = self.filled_round_box_path
        self.circle_win += 1
        self.str_circle_win = str(self.circle_win)
        self.round += 1
        self.reset_playground()
        App.get_running_app().root.current = 'two_five_dim_circle_wins_round_two'
        return True

    def two_circle_wins_final_round(self):
        self.ids.round_box_circle_one.source = self.filled_round_box_path
        self.circle_win += 1
        self.str_circle_win = str(self.circle_win)
        self.round += 1
        self.reset_playground()
        App.get_running_app().root.current = 'two_five_dim_circle_wins_final_round'
        return True

    def circle_wins(self):
        self.ids.round_box_circle_two.source = self.filled_round_box_path
        self.circle_win += 1
        self.round += 1
        self.str_circle_win = str(self.circle_win)
        App.get_running_app().root.current = 'two_five_dim_circle_wins_the_match'
        return self.str_circle_win

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def check_win_cross(self, round):
        match round:
            case 1:

                # HORIZONTAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.cross_path and self.ids.twenty_two.background_disabled_normal \
                        == self.cross_path and self.ids.twenty_three.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 2

                if self.ids.twenty_two.background_disabled_normal == self.cross_path and self.ids.twenty_three.background_disabled_normal \
                        == self.cross_path and self.ids.twenty_four.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 3

                if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.twenty_four.background_disabled_normal \
                        == self.cross_path and self.ids.twenty_five.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 4

                if self.ids.sixteen.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                        == self.cross_path and self.ids.eighteen.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 5

                if self.ids.seventeen.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                        == self.cross_path and self.ids.nineteen.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()


                # 6

                if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                        == self.cross_path and self.ids.twenty.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()


                # 7

                if self.ids.eleven.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                        == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()


                # 8

                if self.ids.twelve.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                        == self.cross_path and self.ids.fourteen.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()


                # 9

                if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                        == self.cross_path and self.ids.fifteen.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 10

                if self.ids.six.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                        == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 11

                if self.ids.seven.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                        == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 12

                if self.ids.eight.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                        == self.cross_path and self.ids.ten.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 13

                if self.ids.one.background_disabled_normal == self.cross_path and self.ids.two.background_disabled_normal \
                        == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 14

                if self.ids.two.background_disabled_normal == self.cross_path and self.ids.three.background_disabled_normal \
                        == self.cross_path and self.ids.four.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 15

                if self.ids.three.background_disabled_normal == self.cross_path and self.ids.four.background_disabled_normal \
                        == self.cross_path and self.ids.five.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # VERTICAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.cross_path and self.ids.sixteen.background_disabled_normal \
                        == self.cross_path and self.ids.eleven.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 2

                if self.ids.sixteen.background_disabled_normal == self.cross_path and self.ids.eleven.background_disabled_normal \
                        == self.cross_path and self.ids.six.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 3

                if self.ids.eleven.background_disabled_normal == self.cross_path and self.ids.six.background_disabled_normal \
                        == self.cross_path and self.ids.one.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 4

                if self.ids.twenty_two.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                        == self.cross_path and self.ids.twelve.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 5

                if self.ids.seventeen.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                        == self.cross_path and self.ids.seven.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 6

                if self.ids.twelve.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                        == self.cross_path and self.ids.two.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 7

                if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                        == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 8

                if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                        == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 9

                if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                        == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 10

                if self.ids.twenty_four.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                        == self.cross_path and self.ids.fourteen.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 11

                if self.ids.nineteen.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                        == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 12

                if self.ids.fourteen.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                        == self.cross_path and self.ids.four.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 13

                if self.ids.twenty_five.background_disabled_normal == self.cross_path and self.ids.twenty.background_disabled_normal \
                        == self.cross_path and self.ids.fifteen.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 14

                if self.ids.twenty.background_disabled_normal == self.cross_path and self.ids.fifteen.background_disabled_normal \
                        == self.cross_path and self.ids.ten.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 15

                if self.ids.fifteen.background_disabled_normal == self.cross_path and self.ids.ten.background_disabled_normal \
                        == self.cross_path and self.ids.five.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # DIAGONAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                        == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 2

                if self.ids.twenty_two.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                        == self.cross_path and self.ids.fourteen.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 3

                if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                        == self.cross_path and self.ids.fifteen.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 4

                if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                        == self.cross_path and self.ids.eleven.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 5

                if self.ids.twenty_four.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                        == self.cross_path and self.ids.twelve.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 6

                if self.ids.twenty_five.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                        == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 7

                if self.ids.sixteen.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                        == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 8

                if self.ids.seventeen.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                        == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 9

                if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                        == self.cross_path and self.ids.ten.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 10

                if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                        == self.cross_path and self.ids.six.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 11

                if self.ids.nineteen.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                        == self.cross_path and self.ids.seven.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 12

                if self.ids.twenty.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                        == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 13

                if self.ids.eleven.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                        == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 14

                if self.ids.twelve.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                        == self.cross_path and self.ids.four.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 15

                if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                        == self.cross_path and self.ids.five.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 16

                if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                        == self.cross_path and self.ids.one.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 17

                if self.ids.fourteen.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                        == self.cross_path and self.ids.two.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

                # 18

                if self.ids.fifteen.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                        == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
                    self.two_cross_wins_round_two()

            case 2:

                # HORIZONTAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.cross_path and self.ids.twenty_two.background_disabled_normal \
                        == self.cross_path and self.ids.twenty_three.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 2

                if self.ids.twenty_two.background_disabled_normal == self.cross_path and self.ids.twenty_three.background_disabled_normal \
                        == self.cross_path and self.ids.twenty_four.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 3

                if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.twenty_four.background_disabled_normal \
                        == self.cross_path and self.ids.twenty_five.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 4

                if self.ids.sixteen.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                        == self.cross_path and self.ids.eighteen.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 5

                if self.ids.seventeen.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                        == self.cross_path and self.ids.nineteen.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 6

                if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                        == self.cross_path and self.ids.twenty.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 7

                if self.ids.eleven.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                        == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 8

                if self.ids.twelve.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                        == self.cross_path and self.ids.fourteen.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 9

                if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                        == self.cross_path and self.ids.fifteen.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 10

                if self.ids.six.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                        == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 11

                if self.ids.seven.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                        == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 12

                if self.ids.eight.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                        == self.cross_path and self.ids.ten.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 13

                if self.ids.one.background_disabled_normal == self.cross_path and self.ids.two.background_disabled_normal \
                        == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 14

                if self.ids.two.background_disabled_normal == self.cross_path and self.ids.three.background_disabled_normal \
                        == self.cross_path and self.ids.four.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 15

                if self.ids.three.background_disabled_normal == self.cross_path and self.ids.four.background_disabled_normal \
                        == self.cross_path and self.ids.five.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # VERTICAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.cross_path and self.ids.sixteen.background_disabled_normal \
                        == self.cross_path and self.ids.eleven.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 2

                if self.ids.sixteen.background_disabled_normal == self.cross_path and self.ids.eleven.background_disabled_normal \
                        == self.cross_path and self.ids.six.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 3

                if self.ids.eleven.background_disabled_normal == self.cross_path and self.ids.six.background_disabled_normal \
                        == self.cross_path and self.ids.one.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 4

                if self.ids.twenty_two.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                        == self.cross_path and self.ids.twelve.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 5

                if self.ids.seventeen.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                        == self.cross_path and self.ids.seven.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 6

                if self.ids.twelve.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                        == self.cross_path and self.ids.two.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 7

                if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                        == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 8

                if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                        == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 9

                if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                        == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 10

                if self.ids.twenty_four.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                        == self.cross_path and self.ids.fourteen.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 11

                if self.ids.nineteen.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                        == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 12

                if self.ids.fourteen.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                        == self.cross_path and self.ids.four.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 13

                if self.ids.twenty_five.background_disabled_normal == self.cross_path and self.ids.twenty.background_disabled_normal \
                        == self.cross_path and self.ids.fifteen.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 14

                if self.ids.twenty.background_disabled_normal == self.cross_path and self.ids.fifteen.background_disabled_normal \
                        == self.cross_path and self.ids.ten.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 15

                if self.ids.fifteen.background_disabled_normal == self.cross_path and self.ids.ten.background_disabled_normal \
                        == self.cross_path and self.ids.five.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # DIAGONAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                        == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 2

                if self.ids.twenty_two.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                        == self.cross_path and self.ids.fourteen.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 3

                if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                        == self.cross_path and self.ids.fifteen.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 4

                if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                        == self.cross_path and self.ids.eleven.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 5

                if self.ids.twenty_four.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                        == self.cross_path and self.ids.twelve.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 6

                if self.ids.twenty_five.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                        == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 7

                if self.ids.sixteen.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                        == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 8

                if self.ids.seventeen.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                        == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 9

                if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                        == self.cross_path and self.ids.ten.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 10

                if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                        == self.cross_path and self.ids.six.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 11

                if self.ids.nineteen.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                        == self.cross_path and self.ids.seven.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 12

                if self.ids.twenty.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                        == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 13

                if self.ids.eleven.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                        == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 14

                if self.ids.twelve.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                        == self.cross_path and self.ids.four.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 15

                if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                        == self.cross_path and self.ids.five.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 16

                if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                        == self.cross_path and self.ids.one.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 17

                if self.ids.fourteen.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                        == self.cross_path and self.ids.two.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

                # 18

                if self.ids.fifteen.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                        == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
                    if self.cross_win == 0:
                        self.two_cross_wins_final_round()
                    else:
                        self.cross_wins()

            case 3:

                # HORIZONTAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.cross_path and self.ids.twenty_two.background_disabled_normal \
                        == self.cross_path and self.ids.twenty_three.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 2

                if self.ids.twenty_two.background_disabled_normal == self.cross_path and self.ids.twenty_three.background_disabled_normal \
                        == self.cross_path and self.ids.twenty_four.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 3

                if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.twenty_four.background_disabled_normal \
                        == self.cross_path and self.ids.twenty_five.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 4

                if self.ids.sixteen.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                        == self.cross_path and self.ids.eighteen.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 5

                if self.ids.seventeen.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                        == self.cross_path and self.ids.nineteen.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 6

                if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                        == self.cross_path and self.ids.twenty.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 7

                if self.ids.eleven.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                        == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 8

                if self.ids.twelve.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                        == self.cross_path and self.ids.fourteen.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 9

                if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                        == self.cross_path and self.ids.fifteen.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 10

                if self.ids.six.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                        == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 11

                if self.ids.seven.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                        == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 12

                if self.ids.eight.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                        == self.cross_path and self.ids.ten.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 13

                if self.ids.one.background_disabled_normal == self.cross_path and self.ids.two.background_disabled_normal \
                        == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 14

                if self.ids.two.background_disabled_normal == self.cross_path and self.ids.three.background_disabled_normal \
                        == self.cross_path and self.ids.four.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 15

                if self.ids.three.background_disabled_normal == self.cross_path and self.ids.four.background_disabled_normal \
                        == self.cross_path and self.ids.five.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # VERTICAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.cross_path and self.ids.sixteen.background_disabled_normal \
                        == self.cross_path and self.ids.eleven.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 2

                if self.ids.sixteen.background_disabled_normal == self.cross_path and self.ids.eleven.background_disabled_normal \
                        == self.cross_path and self.ids.six.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 3

                if self.ids.eleven.background_disabled_normal == self.cross_path and self.ids.six.background_disabled_normal \
                        == self.cross_path and self.ids.one.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 4

                if self.ids.twenty_two.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                        == self.cross_path and self.ids.twelve.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 5

                if self.ids.seventeen.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                        == self.cross_path and self.ids.seven.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 6

                if self.ids.twelve.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                        == self.cross_path and self.ids.two.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 7

                if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                        == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 8

                if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                        == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 9

                if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                        == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 10

                if self.ids.twenty_four.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                        == self.cross_path and self.ids.fourteen.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 11

                if self.ids.nineteen.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                        == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 12

                if self.ids.fourteen.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                        == self.cross_path and self.ids.four.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 13

                if self.ids.twenty_five.background_disabled_normal == self.cross_path and self.ids.twenty.background_disabled_normal \
                        == self.cross_path and self.ids.fifteen.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 14

                if self.ids.twenty.background_disabled_normal == self.cross_path and self.ids.fifteen.background_disabled_normal \
                        == self.cross_path and self.ids.ten.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 15

                if self.ids.fifteen.background_disabled_normal == self.cross_path and self.ids.ten.background_disabled_normal \
                        == self.cross_path and self.ids.five.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # DIAGONAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                        == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 2

                if self.ids.twenty_two.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                        == self.cross_path and self.ids.fourteen.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 3

                if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                        == self.cross_path and self.ids.fifteen.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 4

                if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                        == self.cross_path and self.ids.eleven.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 5

                if self.ids.twenty_four.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                        == self.cross_path and self.ids.twelve.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 6

                if self.ids.twenty_five.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                        == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 7

                if self.ids.sixteen.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                        == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 8

                if self.ids.seventeen.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                        == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 9

                if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                        == self.cross_path and self.ids.ten.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 10

                if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                        == self.cross_path and self.ids.six.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 11

                if self.ids.nineteen.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                        == self.cross_path and self.ids.seven.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 12

                if self.ids.twenty.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                        == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 13

                if self.ids.eleven.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                        == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 14

                if self.ids.twelve.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                        == self.cross_path and self.ids.four.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 15

                if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                        == self.cross_path and self.ids.five.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 16

                if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                        == self.cross_path and self.ids.one.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 17

                if self.ids.fourteen.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                        == self.cross_path and self.ids.two.background_disabled_normal == self.cross_path:
                    self.cross_wins()

                # 18

                if self.ids.fifteen.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                        == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
                    self.cross_wins()

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

    def check_win_circle(self, round):
        match round:
            case 1:

                # HORIZONTAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.circle_path and self.ids.twenty_two.background_disabled_normal \
                        == self.circle_path and self.ids.twenty_three.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 2

                if self.ids.twenty_two.background_disabled_normal == self.circle_path and self.ids.twenty_three.background_disabled_normal \
                        == self.circle_path and self.ids.twenty_four.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 3

                if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.twenty_four.background_disabled_normal \
                        == self.circle_path and self.ids.twenty_five.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 4

                if self.ids.sixteen.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                        == self.circle_path and self.ids.eighteen.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 5

                if self.ids.seventeen.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                        == self.circle_path and self.ids.nineteen.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 6

                if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                        == self.circle_path and self.ids.twenty.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 7

                if self.ids.eleven.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                        == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 8

                if self.ids.twelve.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                        == self.circle_path and self.ids.fourteen.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 9

                if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                        == self.circle_path and self.ids.fifteen.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 10

                if self.ids.six.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                        == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 11

                if self.ids.seven.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                        == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 12

                if self.ids.eight.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                        == self.circle_path and self.ids.ten.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 13

                if self.ids.one.background_disabled_normal == self.circle_path and self.ids.two.background_disabled_normal \
                        == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 14

                if self.ids.two.background_disabled_normal == self.circle_path and self.ids.three.background_disabled_normal \
                        == self.circle_path and self.ids.four.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 15

                if self.ids.three.background_disabled_normal == self.circle_path and self.ids.four.background_disabled_normal \
                        == self.circle_path and self.ids.five.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # VERTICAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.circle_path and self.ids.sixteen.background_disabled_normal \
                        == self.circle_path and self.ids.eleven.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 2

                if self.ids.sixteen.background_disabled_normal == self.circle_path and self.ids.eleven.background_disabled_normal \
                        == self.circle_path and self.ids.six.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 3

                if self.ids.eleven.background_disabled_normal == self.circle_path and self.ids.six.background_disabled_normal \
                        == self.circle_path and self.ids.one.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 4

                if self.ids.twenty_two.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                        == self.circle_path and self.ids.twelve.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 5

                if self.ids.seventeen.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                        == self.circle_path and self.ids.seven.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 6

                if self.ids.twelve.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                        == self.circle_path and self.ids.two.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 7

                if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                        == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 8

                if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                        == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 9

                if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                        == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 10

                if self.ids.twenty_four.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                        == self.circle_path and self.ids.fourteen.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 11

                if self.ids.nineteen.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                        == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 12

                if self.ids.fourteen.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                        == self.circle_path and self.ids.four.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 13

                if self.ids.twenty_five.background_disabled_normal == self.circle_path and self.ids.twenty.background_disabled_normal \
                        == self.circle_path and self.ids.fifteen.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 14

                if self.ids.twenty.background_disabled_normal == self.circle_path and self.ids.fifteen.background_disabled_normal \
                        == self.circle_path and self.ids.ten.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 15

                if self.ids.fifteen.background_disabled_normal == self.circle_path and self.ids.ten.background_disabled_normal \
                        == self.circle_path and self.ids.five.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # DIAGONAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                        == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 2

                if self.ids.twenty_two.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                        == self.circle_path and self.ids.fourteen.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 3

                if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                        == self.circle_path and self.ids.fifteen.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 4

                if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                        == self.circle_path and self.ids.eleven.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 5

                if self.ids.twenty_four.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                        == self.circle_path and self.ids.twelve.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 6

                if self.ids.twenty_five.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                        == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 7

                if self.ids.sixteen.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                        == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 8

                if self.ids.seventeen.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                        == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 9

                if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                        == self.circle_path and self.ids.ten.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 10

                if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                        == self.circle_path and self.ids.six.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 11

                if self.ids.nineteen.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                        == self.circle_path and self.ids.seven.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 12

                if self.ids.twenty.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                        == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 13

                if self.ids.eleven.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                        == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 14

                if self.ids.twelve.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                        == self.circle_path and self.ids.four.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 15

                if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                        == self.circle_path and self.ids.five.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 16

                if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                        == self.circle_path and self.ids.one.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 17

                if self.ids.fourteen.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                        == self.circle_path and self.ids.two.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

                # 18

                if self.ids.fifteen.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                        == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
                    self.two_circle_wins_round_two()

            case 2:

                # HORIZONTAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.circle_path and self.ids.twenty_two.background_disabled_normal \
                        == self.circle_path and self.ids.twenty_three.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 2

                if self.ids.twenty_two.background_disabled_normal == self.circle_path and self.ids.twenty_three.background_disabled_normal \
                        == self.circle_path and self.ids.twenty_four.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 3

                if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.twenty_four.background_disabled_normal \
                        == self.circle_path and self.ids.twenty_five.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 4

                if self.ids.sixteen.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                        == self.circle_path and self.ids.eighteen.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 5

                if self.ids.seventeen.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                        == self.circle_path and self.ids.nineteen.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 6

                if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                        == self.circle_path and self.ids.twenty.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 7

                if self.ids.eleven.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                        == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 8

                if self.ids.twelve.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                        == self.circle_path and self.ids.fourteen.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 9

                if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                        == self.circle_path and self.ids.fifteen.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 10

                if self.ids.six.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                        == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 11

                if self.ids.seven.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                        == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 12

                if self.ids.eight.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                        == self.circle_path and self.ids.ten.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 13

                if self.ids.one.background_disabled_normal == self.circle_path and self.ids.two.background_disabled_normal \
                        == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 14

                if self.ids.two.background_disabled_normal == self.circle_path and self.ids.three.background_disabled_normal \
                        == self.circle_path and self.ids.four.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 15

                if self.ids.three.background_disabled_normal == self.circle_path and self.ids.four.background_disabled_normal \
                        == self.circle_path and self.ids.five.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # VERTICAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.circle_path and self.ids.sixteen.background_disabled_normal \
                        == self.circle_path and self.ids.eleven.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 2

                if self.ids.sixteen.background_disabled_normal == self.circle_path and self.ids.eleven.background_disabled_normal \
                        == self.circle_path and self.ids.six.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 3

                if self.ids.eleven.background_disabled_normal == self.circle_path and self.ids.six.background_disabled_normal \
                        == self.circle_path and self.ids.one.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 4

                if self.ids.twenty_two.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                        == self.circle_path and self.ids.twelve.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 5

                if self.ids.seventeen.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                        == self.circle_path and self.ids.seven.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 6

                if self.ids.twelve.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                        == self.circle_path and self.ids.two.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 7

                if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                        == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 8

                if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                        == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 9

                if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                        == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 10

                if self.ids.twenty_four.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                        == self.circle_path and self.ids.fourteen.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 11

                if self.ids.nineteen.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                        == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 12

                if self.ids.fourteen.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                        == self.circle_path and self.ids.four.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 13

                if self.ids.twenty_five.background_disabled_normal == self.circle_path and self.ids.twenty.background_disabled_normal \
                        == self.circle_path and self.ids.fifteen.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 14

                if self.ids.twenty.background_disabled_normal == self.circle_path and self.ids.fifteen.background_disabled_normal \
                        == self.circle_path and self.ids.ten.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 15

                if self.ids.fifteen.background_disabled_normal == self.circle_path and self.ids.ten.background_disabled_normal \
                        == self.circle_path and self.ids.five.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # DIAGONAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                        == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 2

                if self.ids.twenty_two.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                        == self.circle_path and self.ids.fourteen.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 3

                if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                        == self.circle_path and self.ids.fifteen.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 4

                if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                        == self.circle_path and self.ids.eleven.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 5

                if self.ids.twenty_four.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                        == self.circle_path and self.ids.twelve.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 6

                if self.ids.twenty_five.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                        == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 7

                if self.ids.sixteen.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                        == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 8

                if self.ids.seventeen.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                        == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 9

                if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                        == self.circle_path and self.ids.ten.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 10

                if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                        == self.circle_path and self.ids.six.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 11

                if self.ids.nineteen.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                        == self.circle_path and self.ids.seven.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 12

                if self.ids.twenty.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                        == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 13

                if self.ids.eleven.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                        == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 14

                if self.ids.twelve.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                        == self.circle_path and self.ids.four.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 15

                if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                        == self.circle_path and self.ids.five.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 16

                if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                        == self.circle_path and self.ids.one.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 17

                if self.ids.fourteen.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                        == self.circle_path and self.ids.two.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

                # 18

                if self.ids.fifteen.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                        == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
                    if self.circle_win == 0:
                        self.two_circle_wins_final_round()
                    else:
                        self.circle_wins()

            case 3:

                # HORIZONTAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.circle_path and self.ids.twenty_two.background_disabled_normal \
                        == self.circle_path and self.ids.twenty_three.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 2

                if self.ids.twenty_two.background_disabled_normal == self.circle_path and self.ids.twenty_three.background_disabled_normal \
                        == self.circle_path and self.ids.twenty_four.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 3

                if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.twenty_four.background_disabled_normal \
                        == self.circle_path and self.ids.twenty_five.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 4

                if self.ids.sixteen.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                        == self.circle_path and self.ids.eighteen.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 5

                if self.ids.seventeen.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                        == self.circle_path and self.ids.nineteen.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 6

                if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                        == self.circle_path and self.ids.twenty.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 7

                if self.ids.eleven.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                        == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 8

                if self.ids.twelve.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                        == self.circle_path and self.ids.fourteen.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 9

                if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                        == self.circle_path and self.ids.fifteen.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 10

                if self.ids.six.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                        == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 11

                if self.ids.seven.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                        == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 12

                if self.ids.eight.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                        == self.circle_path and self.ids.ten.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 13

                if self.ids.one.background_disabled_normal == self.circle_path and self.ids.two.background_disabled_normal \
                        == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 14

                if self.ids.two.background_disabled_normal == self.circle_path and self.ids.three.background_disabled_normal \
                        == self.circle_path and self.ids.four.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 15

                if self.ids.three.background_disabled_normal == self.circle_path and self.ids.four.background_disabled_normal \
                        == self.circle_path and self.ids.five.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # VERTICAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.circle_path and self.ids.sixteen.background_disabled_normal \
                        == self.circle_path and self.ids.eleven.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 2

                if self.ids.sixteen.background_disabled_normal == self.circle_path and self.ids.eleven.background_disabled_normal \
                        == self.circle_path and self.ids.six.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 3

                if self.ids.eleven.background_disabled_normal == self.circle_path and self.ids.six.background_disabled_normal \
                        == self.circle_path and self.ids.one.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 4

                if self.ids.twenty_two.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                        == self.circle_path and self.ids.twelve.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 5

                if self.ids.seventeen.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                        == self.circle_path and self.ids.seven.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 6

                if self.ids.twelve.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                        == self.circle_path and self.ids.two.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 7

                if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                        == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 8

                if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                        == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 9

                if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                        == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 10

                if self.ids.twenty_four.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                        == self.circle_path and self.ids.fourteen.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 11

                if self.ids.nineteen.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                        == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 12

                if self.ids.fourteen.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                        == self.circle_path and self.ids.four.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 13

                if self.ids.twenty_five.background_disabled_normal == self.circle_path and self.ids.twenty.background_disabled_normal \
                        == self.circle_path and self.ids.fifteen.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 14

                if self.ids.twenty.background_disabled_normal == self.circle_path and self.ids.fifteen.background_disabled_normal \
                        == self.circle_path and self.ids.ten.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 15

                if self.ids.fifteen.background_disabled_normal == self.circle_path and self.ids.ten.background_disabled_normal \
                        == self.circle_path and self.ids.five.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # DIAGONAL

                # 1

                if self.ids.twenty_one.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                        == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 2

                if self.ids.twenty_two.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                        == self.circle_path and self.ids.fourteen.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 3

                if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                        == self.circle_path and self.ids.fifteen.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 4

                if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                        == self.circle_path and self.ids.eleven.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 5

                if self.ids.twenty_four.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                        == self.circle_path and self.ids.twelve.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 6

                if self.ids.twenty_five.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                        == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 7

                if self.ids.sixteen.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                        == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 8

                if self.ids.seventeen.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                        == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 9

                if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                        == self.circle_path and self.ids.ten.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 10

                if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                        == self.circle_path and self.ids.six.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 11

                if self.ids.nineteen.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                        == self.circle_path and self.ids.seven.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 12

                if self.ids.twenty.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                        == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 13

                if self.ids.eleven.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                        == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 14

                if self.ids.twelve.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                        == self.circle_path and self.ids.four.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 15

                if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                        == self.circle_path and self.ids.five.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 16

                if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                        == self.circle_path and self.ids.one.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 17

                if self.ids.fourteen.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                        == self.circle_path and self.ids.two.background_disabled_normal == self.circle_path:
                    self.circle_wins()

                # 18

                if self.ids.fifteen.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                        == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
                    self.circle_wins()

    def announce_draw(self, turn_count, check_win_circle, check_win_cross, round):
        if turn_count == 26 and check_win_cross is not True and check_win_circle is not True:
            match round:
                case 1:
                    self.ids.round_box_circle_one.source = self.filled_round_box_path
                    self.ids.round_box_cross_one.source = self.filled_round_box_path
                    self.round += 2
                    self.circle_win += 1
                    self.cross_win += 1
                    App.get_running_app().root.current = 'two_five_dim_draw_final_round'
                    return True
                case 2:
                    if self.circle_win == 1:
                        self.circle_wins()
                    elif self.cross_win == 1:
                        self.cross_wins()
                case 3:
                    self.ids.round_box_circle_two.source = self.filled_round_box_path
                    self.ids.round_box_cross_two.source = self.filled_round_box_path
                    self.round += 1
                    self.circle_win += 1
                    self.cross_win += 1
                    self.str_cross_win = str(self.cross_win)
                    self.str_circle_win = str(self.circle_win)
                    App.get_running_app().root.current = 'two_rounds_five_dim_draw'
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

        self.announce_draw(self.turn_count, self.check_win_circle(self.round), self.check_win_cross(self.round), self.round)
    def reset_playground(self):

        self.turn = "Circle"
        self.turn_count = 1
        self.ids.cross_turn.source = self.cross_turn_no_highlight
        self.ids.circle_turn.source = self.circle_turn_highlight

        self.ids.twenty_one.disabled = False
        self.ids.twenty_two.disabled = False
        self.ids.twenty_three.disabled = False
        self.ids.twenty_four.disabled = False
        self.ids.twenty_five.disabled = False

        self.ids.sixteen.disabled = False
        self.ids.seventeen.disabled = False
        self.ids.eighteen.disabled = False
        self.ids.nineteen.disabled = False
        self.ids.twenty.disabled = False

        self.ids.eleven.disabled = False
        self.ids.twelve.disabled = False
        self.ids.thirteen.disabled = False
        self.ids.fourteen.disabled = False
        self.ids.fifteen.disabled = False

        self.ids.six.disabled = False
        self.ids.seven.disabled = False
        self.ids.eight.disabled = False
        self.ids.nine.disabled = False
        self.ids.ten.disabled = False

        self.ids.one.disabled = False
        self.ids.two.disabled = False
        self.ids.three.disabled = False
        self.ids.four.disabled = False
        self.ids.five.disabled = False

        self.ids.twenty_one.background_disabled_normal = ''
        self.ids.twenty_two.background_disabled_normal = ''
        self.ids.twenty_three.background_disabled_normal = ''
        self.ids.twenty_four.background_disabled_normal = ''
        self.ids.twenty_five.background_disabled_normal = ''

        self.ids.sixteen.background_disabled_normal = ''
        self.ids.seventeen.background_disabled_normal = ''
        self.ids.eighteen.background_disabled_normal = ''
        self.ids.nineteen.background_disabled_normal = ''
        self.ids.twenty.background_disabled_normal = ''

        self.ids.eleven.background_disabled_normal = ''
        self.ids.twelve.background_disabled_normal = ''
        self.ids.thirteen.background_disabled_normal = ''
        self.ids.fourteen.background_disabled_normal = ''
        self.ids.fifteen.background_disabled_normal = ''

        self.ids.six.background_disabled_normal = ''
        self.ids.seven.background_disabled_normal = ''
        self.ids.eight.background_disabled_normal = ''
        self.ids.nine.background_disabled_normal = ''
        self.ids.ten.background_disabled_normal = ''

        self.ids.one.background_disabled_normal = ''
        self.ids.two.background_disabled_normal = ''
        self.ids.three.background_disabled_normal = ''
        self.ids.four.background_disabled_normal = ''
        self.ids.five.background_disabled_normal = ''

    def reset_rounds(self):

        self.ids.round_box_circle_one.source = self.empty_round_box_path
        self.ids.round_box_cross_one.source = self.empty_round_box_path
        self.ids.round_box_circle_two.source = self.empty_round_box_path
        self.ids.round_box_cross_two.source = self.empty_round_box_path
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