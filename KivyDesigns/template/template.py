from kivymd.uix.behaviors.hover_behavior import HoverBehavior
from kivy.uix.button import Button
from kivy.properties import ListProperty


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


class HiddenButton(Button):
    pass


class HamburgerButton(Button):
    pass


class ExitButton(Button, HoverBehavior):
    background = ListProperty((120/255, 120/255, 120/255, 1))
    color = ListProperty((1, 1, 1, 1))

    def on_enter(self):
        self.background = (1, 222/255, 89/255, 1)
        self.color = (0, 0, 0, 1)

    def on_leave(self):
        self.background = (120/255, 120/255, 120/255, 1)
        self.color = (1, 1, 1, 1)
