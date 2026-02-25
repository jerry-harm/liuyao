'''
    六爻组件
    Copyright (C) 2026  jerry <jerry_harm@163.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

from kivy.properties import ObjectProperty,  NumericProperty

from .yao import YaoButton

from utils import 六爻

KV="""
<YaoWidget>
    orientation: 'horizontal'
    index: -1
    Label:
        id: shiyin
        text: ""
        font_size: min(self.width  ,self.height )
        size_hint: 0.2, 1

    YaoButton:
        on_change: root.yao_change(root.index, self, *args)
        

    Label:
        id: jiazi
        text: ""
        font_size: min(self.width * 0.2 ,self.height * 0.6)
        size_hint: 0.9, 1

<SixYaoWidget>
    orientation:'vertical'
    Label:
        id: name
        text:'text'
        font_size: self.height
        size_hint: 1, 0.4
    YaoWidget:
        index: 5
        yao_change:  root.change
    YaoWidget:
        index: 4
        yao_change:  root.change
    YaoWidget:
        index: 3
        yao_change:  root.change
    YaoWidget:
        index: 2
        yao_change:  root.change
    YaoWidget:
        index: 1
        yao_change:  root.change
    YaoWidget:
        index: 0
        yao_change:  root.change
"""

Builder.load_string(KV)

class YaoWidget(BoxLayout):
    yao_change = ObjectProperty(None)
    index = NumericProperty(-1)

class SixYaoWidget(BoxLayout,EventDispatcher):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_change')
        self.gua = 六爻([True,True,True,True,True,True])
        Clock.schedule_once(self.update)

    def change(self,index,instanse:YaoButton,*args):
        self.gua.卦象[index]=instanse.status
        self.update()
        self.dispatch('on_change')

    def on_change(self,*args):
        pass
    
    def update(self,*args):
        self.gua.排盘()
        self.ids["name"].text =self.gua.宫.get_name() + " " + self.gua.卦名
        for child in self.children:
            if isinstance(child,YaoWidget):
                i = child.index
                if child.index == self.gua.世:
                    child.ids["shiyin"].text="世"
                elif child.index == self.gua.应:
                    child.ids["shiyin"].text="应"
                else:
                    child.ids["shiyin"].text=""
                child.ids["jiazi"].text = self.gua.六亲[i]+self.gua.甲子[i]+self.gua.五行[i]
        