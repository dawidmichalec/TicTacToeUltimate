from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.properties import BooleanProperty


class ThreeFourDimCrossWinsRoundTwo(Screen):

    def on_enter(self, *args):
        gif = self.ids.gif
        gif.textures_used = 0
        gif.num_textures = None
        gif.complete = False
        gif.anim_delay = 0.03  # starts the animation


class MyImage(Image):
    complete = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anim_loop = 1  # only allow one animation loop
        self.textures_used = 0
        self.num_textures = None

    def on_texture(self, image, texture):
        if self.num_textures is None:
            self.num_textures = len(self._coreimage.image.textures)
        self.textures_used += 1
        if (self.textures_used + 1) == self.num_textures:
            self.complete = True

