from kivy.uix.widget import Widget
from kivy.properties import ListProperty

from yao import YaoWidget

from utils.gua import 六爻

class SixYaoWidget(Widget):
    gua_xiang=ListProperty([1,1,1,1,1,1])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    