from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

KV="""
<ZhouYiScreen>:
    name: 'zhouyi'
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
            on_press: root.manager.current = 'main'
"""

Builder.load_string(KV)

class ZhouYiScreen(Screen):
    def update(self,instance,text1,text2,*args):
        self.ids['text'].text=text1+text2