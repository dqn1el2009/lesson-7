import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

class Main_App(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]
        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                     background_color=random.choice(colors),
                     color=random.choice(colors))
            layout.add_widget(btn)
        return layout

Main_App().run()