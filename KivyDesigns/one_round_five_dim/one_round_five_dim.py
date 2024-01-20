from kivy.uix.screenmanager import Screen
from kivymd.uix.menu.menu import MDDropdownMenu
from kivy.factory import Factory
from kivy.app import App


class OneRoundFiveDim(Screen):

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
    cross_win = 0
    circle_win = 0
    str_cross_win = "0"
    str_circle_win = "0"

    def circle_wins(self, check_win_circle):
        if check_win_circle is True:
            self.ids.round_box_circle_one.source = self.filled_round_box_path
            self.circle_win += 1
            self.str_circle_win = str(self.circle_win)
            return self.str_circle_win

        return self.str_circle_win

    def cross_wins(self, check_win_cross):
        if check_win_cross is True:
            self.ids.round_box_cross_one.source = self.filled_round_box_path
            self.cross_win += 1
            self.str_cross_win = str(self.cross_win)
            return self.str_cross_win

        return self.str_cross_win

    def on_enter(self):

        self.cross_win = 0
        self.circle_win = 0
        self.str_cross_win = "0"
        self.str_circle_win = "0"

    def on_leave(self):
        self.reset_rounds()
        self.reset_playground()
        return True

    def check_win_cross(self):

        # HORIZONTAL

        #1

        if self.ids.twenty_one.background_disabled_normal == self.cross_path and self.ids.twenty_two.background_disabled_normal \
                == self.cross_path and self.ids.twenty_three.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        #2

        if self.ids.twenty_two.background_disabled_normal == self.cross_path and self.ids.twenty_three.background_disabled_normal \
                == self.cross_path and self.ids.twenty_four.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        #3

        if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.twenty_four.background_disabled_normal \
                == self.cross_path and self.ids.twenty_five.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        #4

        if self.ids.sixteen.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                == self.cross_path and self.ids.eighteen.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        #5

        if self.ids.seventeen.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                == self.cross_path and self.ids.nineteen.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        #6

        if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                == self.cross_path and self.ids.twenty.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        #7

        if self.ids.eleven.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        #8

        if self.ids.twelve.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                == self.cross_path and self.ids.fourteen.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        #9

        if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                == self.cross_path and self.ids.fifteen.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        #10

        if self.ids.six.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 11

        if self.ids.seven.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 12

        if self.ids.eight.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                == self.cross_path and self.ids.ten.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 13

        if self.ids.one.background_disabled_normal == self.cross_path and self.ids.two.background_disabled_normal \
                == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 14

        if self.ids.two.background_disabled_normal == self.cross_path and self.ids.three.background_disabled_normal \
                == self.cross_path and self.ids.four.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 15

        if self.ids.three.background_disabled_normal == self.cross_path and self.ids.four.background_disabled_normal \
                == self.cross_path and self.ids.five.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # VERTICAL

        # 1

        if self.ids.twenty_one.background_disabled_normal == self.cross_path and self.ids.sixteen.background_disabled_normal \
                == self.cross_path and self.ids.eleven.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 2

        if self.ids.sixteen.background_disabled_normal == self.cross_path and self.ids.eleven.background_disabled_normal \
                == self.cross_path and self.ids.six.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 3

        if self.ids.eleven.background_disabled_normal == self.cross_path and self.ids.six.background_disabled_normal \
                == self.cross_path and self.ids.one.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 4

        if self.ids.twenty_two.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                == self.cross_path and self.ids.twelve.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 5

        if self.ids.seventeen.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                == self.cross_path and self.ids.seven.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 6

        if self.ids.twelve.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                == self.cross_path and self.ids.two.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 7

        if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 8

        if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 9

        if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 10

        if self.ids.twenty_four.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                == self.cross_path and self.ids.fourteen.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 11

        if self.ids.nineteen.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 12

        if self.ids.fourteen.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                == self.cross_path and self.ids.four.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 13

        if self.ids.twenty_five.background_disabled_normal == self.cross_path and self.ids.twenty.background_disabled_normal \
                == self.cross_path and self.ids.fifteen.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 14

        if self.ids.twenty.background_disabled_normal == self.cross_path and self.ids.fifteen.background_disabled_normal \
                == self.cross_path and self.ids.ten.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 15

        if self.ids.fifteen.background_disabled_normal == self.cross_path and self.ids.ten.background_disabled_normal \
                == self.cross_path and self.ids.five.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # DIAGONAL

        # 1

        if self.ids.twenty_one.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 2

        if self.ids.twenty_two.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                == self.cross_path and self.ids.fourteen.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 3

        if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                == self.cross_path and self.ids.fifteen.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 4

        if self.ids.twenty_three.background_disabled_normal == self.cross_path and self.ids.seventeen.background_disabled_normal \
                == self.cross_path and self.ids.eleven.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 5

        if self.ids.twenty_four.background_disabled_normal == self.cross_path and self.ids.eighteen.background_disabled_normal \
                == self.cross_path and self.ids.twelve.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 6

        if self.ids.twenty_five.background_disabled_normal == self.cross_path and self.ids.nineteen.background_disabled_normal \
                == self.cross_path and self.ids.thirteen.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 7

        if self.ids.sixteen.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 8

        if self.ids.seventeen.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                == self.cross_path and self.ids.nine.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 9

        if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                == self.cross_path and self.ids.ten.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 10

        if self.ids.eighteen.background_disabled_normal == self.cross_path and self.ids.twelve.background_disabled_normal \
                == self.cross_path and self.ids.six.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 11

        if self.ids.nineteen.background_disabled_normal == self.cross_path and self.ids.thirteen.background_disabled_normal \
                == self.cross_path and self.ids.seven.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 12

        if self.ids.twenty.background_disabled_normal == self.cross_path and self.ids.fourteen.background_disabled_normal \
                == self.cross_path and self.ids.eight.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 13

        if self.ids.eleven.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 14

        if self.ids.twelve.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                == self.cross_path and self.ids.four.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 15

        if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                == self.cross_path and self.ids.five.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 16

        if self.ids.thirteen.background_disabled_normal == self.cross_path and self.ids.seven.background_disabled_normal \
                == self.cross_path and self.ids.one.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 17

        if self.ids.fourteen.background_disabled_normal == self.cross_path and self.ids.eight.background_disabled_normal \
                == self.cross_path and self.ids.two.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        # 18

        if self.ids.fifteen.background_disabled_normal == self.cross_path and self.ids.nine.background_disabled_normal \
                == self.cross_path and self.ids.three.background_disabled_normal == self.cross_path:
            App.get_running_app().root.current = 'one_round_five_dim_cross_wins'
            return True

        return False

    def check_win_circle(self):

        # HORIZONTAL

        #1

        if self.ids.twenty_one.background_disabled_normal == self.circle_path and self.ids.twenty_two.background_disabled_normal \
                == self.circle_path and self.ids.twenty_three.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        #2

        if self.ids.twenty_two.background_disabled_normal == self.circle_path and self.ids.twenty_three.background_disabled_normal \
                == self.circle_path and self.ids.twenty_four.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        #3

        if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.twenty_four.background_disabled_normal \
                == self.circle_path and self.ids.twenty_five.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        #4

        if self.ids.sixteen.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                == self.circle_path and self.ids.eighteen.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        #5

        if self.ids.seventeen.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                == self.circle_path and self.ids.nineteen.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        #6

        if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                == self.circle_path and self.ids.twenty.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        #7

        if self.ids.eleven.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        #8

        if self.ids.twelve.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                == self.circle_path and self.ids.fourteen.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        #9

        if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                == self.circle_path and self.ids.fifteen.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        #10

        if self.ids.six.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 11

        if self.ids.seven.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 12

        if self.ids.eight.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                == self.circle_path and self.ids.ten.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 13

        if self.ids.one.background_disabled_normal == self.circle_path and self.ids.two.background_disabled_normal \
                == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 14

        if self.ids.two.background_disabled_normal == self.circle_path and self.ids.three.background_disabled_normal \
                == self.circle_path and self.ids.four.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 15

        if self.ids.three.background_disabled_normal == self.circle_path and self.ids.four.background_disabled_normal \
                == self.circle_path and self.ids.five.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # VERTICAL

        # 1

        if self.ids.twenty_one.background_disabled_normal == self.circle_path and self.ids.sixteen.background_disabled_normal \
                == self.circle_path and self.ids.eleven.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 2

        if self.ids.sixteen.background_disabled_normal == self.circle_path and self.ids.eleven.background_disabled_normal \
                == self.circle_path and self.ids.six.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 3

        if self.ids.eleven.background_disabled_normal == self.circle_path and self.ids.six.background_disabled_normal \
                == self.circle_path and self.ids.one.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 4

        if self.ids.twenty_two.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                == self.circle_path and self.ids.twelve.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 5

        if self.ids.seventeen.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                == self.circle_path and self.ids.seven.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 6

        if self.ids.twelve.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                == self.circle_path and self.ids.two.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 7

        if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 8

        if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 9

        if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 10

        if self.ids.twenty_four.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                == self.circle_path and self.ids.fourteen.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 11

        if self.ids.nineteen.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 12

        if self.ids.fourteen.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                == self.circle_path and self.ids.four.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 13

        if self.ids.twenty_five.background_disabled_normal == self.circle_path and self.ids.twenty.background_disabled_normal \
                == self.circle_path and self.ids.fifteen.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 14

        if self.ids.twenty.background_disabled_normal == self.circle_path and self.ids.fifteen.background_disabled_normal \
                == self.circle_path and self.ids.ten.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 15

        if self.ids.fifteen.background_disabled_normal == self.circle_path and self.ids.ten.background_disabled_normal \
                == self.circle_path and self.ids.five.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # DIAGONAL

        # 1

        if self.ids.twenty_one.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 2

        if self.ids.twenty_two.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                == self.circle_path and self.ids.fourteen.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 3

        if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                == self.circle_path and self.ids.fifteen.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 4

        if self.ids.twenty_three.background_disabled_normal == self.circle_path and self.ids.seventeen.background_disabled_normal \
                == self.circle_path and self.ids.eleven.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 5

        if self.ids.twenty_four.background_disabled_normal == self.circle_path and self.ids.eighteen.background_disabled_normal \
                == self.circle_path and self.ids.twelve.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 6

        if self.ids.twenty_five.background_disabled_normal == self.circle_path and self.ids.nineteen.background_disabled_normal \
                == self.circle_path and self.ids.thirteen.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 7

        if self.ids.sixteen.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 8

        if self.ids.seventeen.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                == self.circle_path and self.ids.nine.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 9

        if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                == self.circle_path and self.ids.ten.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 10

        if self.ids.eighteen.background_disabled_normal == self.circle_path and self.ids.twelve.background_disabled_normal \
                == self.circle_path and self.ids.six.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 11

        if self.ids.nineteen.background_disabled_normal == self.circle_path and self.ids.thirteen.background_disabled_normal \
                == self.circle_path and self.ids.seven.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 12

        if self.ids.twenty.background_disabled_normal == self.circle_path and self.ids.fourteen.background_disabled_normal \
                == self.circle_path and self.ids.eight.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 13

        if self.ids.eleven.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 14

        if self.ids.twelve.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                == self.circle_path and self.ids.four.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 15

        if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                == self.circle_path and self.ids.five.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 16

        if self.ids.thirteen.background_disabled_normal == self.circle_path and self.ids.seven.background_disabled_normal \
                == self.circle_path and self.ids.one.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 17

        if self.ids.fourteen.background_disabled_normal == self.circle_path and self.ids.eight.background_disabled_normal \
                == self.circle_path and self.ids.two.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        # 18

        if self.ids.fifteen.background_disabled_normal == self.circle_path and self.ids.nine.background_disabled_normal \
                == self.circle_path and self.ids.three.background_disabled_normal == self.circle_path:
            App.get_running_app().root.current = 'one_round_five_dim_circle_wins'
            return True

        return False

    def announce_draw(self, turn_count, check_win_circle, check_win_cross):
        if turn_count == 26 and check_win_cross is not True and check_win_circle is not True:
            App.get_running_app().root.current = 'one_round_five_dim_draw'
            self.circle_win += 1
            self.cross_win += 1
            self.str_circle_win = str(self.circle_win)
            self.str_cross_win = str(self.cross_win)
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

        self.cross_wins(self.check_win_cross())
        self.circle_wins(self.check_win_circle())
        self.announce_draw(self.turn_count, self.check_win_circle(), self.check_win_cross())

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

