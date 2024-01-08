from kivy.uix.screenmanager import Screen
from kivy.factory import Factory
from kivymd.uix.behaviors.hover_behavior import HoverBehavior
from kivy.uix.button import Button
from kivy.properties import ListProperty
from TicTacToeUltimate.KivyDesigns.one_round_three_dim.one_round_three_dim import OneRoundThreeDim
from kivy.uix.modalview import ModalView


class Result(Screen):

    def on_enter(self):

        Factory.get('ResultPopup')().open()


class ResultPopup(ModalView):

    def on_open(self):
        one_round_three_dim = OneRoundThreeDim()
        ortd_check_win_cross = one_round_three_dim.check_win_cross()
        ortd_check_win_circle = one_round_three_dim.check_win_circle()
        circle_score_one_dim = str(one_round_three_dim.circle_wins(ortd_check_win_circle))
        cross_score_one_dim = str(one_round_three_dim.cross_wins(ortd_check_win_cross ))
        print(circle_score_one_dim)
        print(cross_score_one_dim)
        self.ids.circle_score.text = circle_score_one_dim
        self.ids.cross_score.text = cross_score_one_dim


class ResultButton(Button, HoverBehavior):

    background = ListProperty((120/255, 120/255, 120/255, 1))
    color = ListProperty((1, 1, 1, 1))

    def on_enter(self):
        self.background = (1, 222/255, 89/255, 1)
        self.color = (0, 0, 0, 1)

    def on_leave(self):
        self.background = (120/255, 120/255, 120/255, 1)
        self.color = (1, 1, 1, 1)
