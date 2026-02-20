import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Paipan(Widget):
    ...

class LiuYaoApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    LiuYaoApp.run()

