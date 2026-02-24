'''
    时间选择和显示组件
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
from kivy.uix.boxlayout import BoxLayout

KV="""
<TimeWidget>
    orientation: 'vertical'
    Label:
        id: time
        text: "时辰"
    Label:
        id: empty
        text: "旬空"
    BoxLayout:
        orientation: 'horizontal'
        TextInput:
            hint_text: 1999/02/01
"""

class TimeWidget(BoxLayout):
    ...