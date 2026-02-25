'''
    变爻组件
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

from kivy.lang import Builder


KV="""
<ChangeWidget>
    orientation:'vertical'
    Label:
        text:''
        size_hint: 1, 0.4
    Label:
        id: l5
        font_size:self.width
    Label:
        id: l4
        font_size:self.width
    Label:
        id: l3
        font_size:self.width
    Label:
        id: l2
        font_size:self.width
    Label:
        id: l1
        font_size:self.width
    Label:
        id: l0
        font_size:self.width

"""

Builder.load_string(KV)

from typing import List

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

class ChangeWidget(BoxLayout):
    def __init__(self, **kwargs):
        self.original=[True,True,True,True,True,True]
        self.changed=[True,True,True,True,True,True]
        self.change=["","","","","",""]
        super().__init__(**kwargs)
    
    def update(self,type:int ,gua:List[bool]):
        if type == 0:
            self.original=gua
        else:
            self.changed=gua
        for i in range(6):
            if self.original[i]==self.changed[i]:
                self.ids[f"l{i}"].text=""
                self.change[i]=""
            else:
                if self.original[i]==True:
                    self.ids[f"l{i}"].text="o"
                    self.change[i]="o"
                else:
                    self.ids[f"l{i}"].text="x"
                    self.change[i]="x"