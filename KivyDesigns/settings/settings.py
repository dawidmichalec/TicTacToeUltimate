from kivy.uix.screenmanager import Screen


class SettingsScreen(Screen):

    def turn_the_sound_off_on(self):
        text = self.ids.sound_button.text

        if text == 'SOUND ON':
            self.ids.sound_button.text = 'SOUND OFF'
        else:
            self.ids.sound_button.text = 'SOUND ON'
