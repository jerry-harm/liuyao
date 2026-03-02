#Copyright (C) 2026  jerry <jerry_harm@163.com>
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
from kivy.uix.boxlayout import BoxLayout
from ui.zhouyi import ZhouYiPopup
from kivy.lang.builder import Builder
from utils.gua import 六爻
from typing import List

YIN="\u268b"
YANG="\u268a"

KV="""
#:import SixYaoWidget ui.sixyao.SixYaoWidget
#:import TimeWidget ui.time.TimeWidget
#:import SixGodWidget ui.time.SixGodWidget
#:import ChangeWidget ui.change.ChangeWidget
#:import Clipboard kivy.core.clipboard.Clipboard

<RootWidget>:
    orientation: 'vertical'
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: 0.3
        TimeWidget:
            id:time
            on_sixgod_updated: sixgod.update(sixgod=args[1])
        
        Button:
            text: '导出到\\n剪切板'
            size_hint: 0.1, 1
            on_press: Clipboard.copy(root.format_output(time.ids['time'].text,time.ids['empty'].text,original.gua,changed.gua,sixgod.sixgod,change.change))
        Button:
            text: '易经'
            size_hint: 0.1,1
            on_press: root.popup_zhouyi(original.gua.gua_ci(),changed.gua.gua_ci())
    BoxLayout:
        orientation: 'horizontal'
        SixGodWidget:
            id: sixgod
            size_hint_x: 0.1
        BoxLayout:
            orientation: 'horizontal'
            SixYaoWidget:
                id: original
                on_change: change.update(0,self.gua.卦象)
            ChangeWidget:
                id: change
                size_hint_x:0.1
            SixYaoWidget:
                id: changed
                on_change: change.update(1,self.gua.卦象)
"""

Builder.load_string(KV)

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def format_output(self,time,empty,original:六爻,changed:六爻,sixgod:List[str],change:List[str],*args) -> str:
        gua=f"\n\u3000\u3000\u3000{original.卦名}" + "\u3000" * (8-len(original.卦名)) +f"{changed.卦名}\n"
        for i in range(6):
            o_shi="\u3000"
            c_shi="\u3000"
            if original.世==i:
                o_shi="世"
            if original.应==i:
                o_shi="应"
            if changed.世==i:
                c_shi="世"
            if changed.应==i:
                c_shi="应"
            if original.卦象[i]:
                o_yao=YANG
            else:
                o_yao=YIN
            if changed.卦象[i]:
                c_yao=YANG
            else:
                c_yao=YIN
            gua+=sixgod[i]+\
o_shi+o_yao+original.六亲[i]+original.甲子[i]+original.五行[i]+\
('\u3000' if not change[i] else change[i])+\
c_shi+c_yao+changed.六亲[i]+changed.甲子[i]+changed.五行[i]+"\n"
        return f"{time}\n{empty}\n"+gua
    def popup_zhouyi(self,text1,text2,**kwargs):
        popup=ZhouYiPopup()
        popup.update(text1+text2)
        popup.open()

