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
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

from kivy.properties import ObjectProperty, StringProperty, NumericProperty

from .yao import YaoButton

from utils import 六爻

KV="""
<YaoWidget>
    orientation: 'horizontal'
    shiyin: "text"
    jiazi:"text"
    index: -1
    Label:
        id: shiyin
        text: root.shiyin
        size_hint: 0.3, 1
        font_size: self.height * 0.7

    YaoButton:
        on_release: root.yao_change(root.index, self, *args[1:])
    
    Label:
        id: jiazi
        text: root.jiazi
        font_size: self.height * 0.7

<SixYaoWidget>
    orientation:'vertical'
    Label:
        id: name
        text:'text'
        font_size: self.height
        size_hint: 1, 0.4
    YaoWidget:
        index: 5
        yao_change:  root.on_change
    YaoWidget:
        index: 4
        yao_change:  root.on_change
    YaoWidget:
        index: 3
        yao_change:  root.on_change
    YaoWidget:
        index: 2
        yao_change:  root.on_change
    YaoWidget:
        index: 1
        yao_change:  root.on_change
    YaoWidget:
        index: 0
        yao_change:  root.on_change
"""

Builder.load_string(KV)

class YaoWidget(BoxLayout):
    yao_change = ObjectProperty(None)
    shiyin = StringProperty("")
    jiazi = StringProperty("")
    index = NumericProperty(-1)

class SixYaoWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gua = 六爻([True,True,True,True,True,True])
        self.gua.排盘()
        Clock.schedule_once(self.update)

    def on_change(self,index,instanse:YaoButton,*args):
        self.gua.卦象[index]=instanse.status
        self.gua.排盘()
        self.update()
    
    def update(self,*args):
        self.ids["name"].text = self.gua.卦名
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
        