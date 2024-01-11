from kivy.uix.screenmanager import Screen
from kivy.factory import Factory
from kivymd.uix.behaviors.hover_behavior import HoverBehavior
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.modalview import ModalView
from kivy.app import App


class Result(Screen):

    def on_enter(self):

        Factory.get('ResultPopup')().open()


class ResultPopup(ModalView):
    pass


class ResultButton(Button, HoverBehavior):

    background = ListProperty((120/255, 120/255, 120/255, 1))
    color = ListProperty((1, 1, 1, 1))

    def on_enter(self):
        self.background = (1, 222/255, 89/255, 1)
        self.color = (0, 0, 0, 1)

    def on_leave(self):
        self.background = (120/255, 120/255, 120/255, 1)
        self.color = (1, 1, 1, 1)
