from kivy.app import App

from kivy.resources import resource_add_path
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.metrics import sp

from utils.gua import 六爻
from utils.calender import 排六神

class LiuYaoApp(App):
    def build(self):
        resource_add_path('./fonts')
        LabelBase.register(DEFAULT_FONT, 'NotoSerifSC-VF.ttf')
if __name__ == '__main__':
    LiuYaoApp().run()

