from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.popup import Popup

from kivy.properties import  StringProperty

KV="""
<ZhouYiPopup>:
    title: "易经"
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            size_hint: 1,0.8
            do_scroll_x: False
            do_scroll_y: True
            Label:
                id: text
                text: ""
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
        Button:
            size_hint:1,0.1
            text: "关闭"
            on_press: root.dismiss()
"""

Builder.load_string(KV)

class ZhouYiPopup(Popup):
    def update(self,text):
        self.ids["text"].text=text