from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class Main_App(App):
    def build(self):
        img = Image(source='C:/Users/Impact/Downloads/test.jpg',
                      size_hint=(1, .5),
                      pos_hint={'center_y': .5, 'center_x': .5})
        return img

Main_App().run()