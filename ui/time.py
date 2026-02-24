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
KV="""
<TimeWidget>
    orientation: 'vertical'
    padding: 10
    Label:
        id: time
        text: "时辰"
        size_hint: 1,0.4
        halign: 'left'
        text_size: self.size
        font_size: self.height
    Label:
        id: empty
        text: "旬空"
        font_size: self.height
        size_hint: 1,0.4
        halign: 'left'
        text_size: self.size
        font_size: self.height
    BoxLayout:
        orientation: 'horizontal'
        padding: 10
        spacing: 10
        
        TextInput:
            id: input_time
            hint_text: "1999/02/01/12 (留空视为现在)"
            text: ""
        Button:
            text: "确定"
            on_press: root.get_time(input_time.text)
<SixGodWidget>:
    orientation: 'vertical'
    Label:
        text:''
        size_hint: 1, 0.4
    Label:
        id:5
        font_size: self.height/2
    Label:
        id:4
        font_size: self.height/2
    Label:
        id:3
        font_size: self.height/2
    Label:
        id:2
        font_size: self.height/2
    Label:
        id:1
        font_size: self.height/2
    Label:
        id:0
        font_size: self.height/2
"""

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.event import EventDispatcher

Builder.load_string(KV)

from datetime import datetime
from tyme4py.solar import SolarTime

from utils.calender import 排六神

class TimeWidget(BoxLayout,EventDispatcher):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_sixgod_updated')
        Clock.schedule_once(lambda x: self.get_time())

    def get_time(self,strtime="",*args):
        
        if len(strtime) != 0:
            use_time = datetime.strptime(strtime,"%Y/%m/%d/%H")
            pass
        else:
            use_time = datetime.now()
        
        sixty_cycle_hour=SolarTime.from_ymd_hms(use_time.year,use_time.month,use_time.day,use_time.hour,use_time.minute,use_time.second).get_sixty_cycle_hour()
        sixgod=排六神(sixty_cycle_hour.get_sixty_cycle_day())
        self.ids["time"].text = str(sixty_cycle_hour)
        
        self.ids["empty"].text =   "{}{}空{}{}空{}{}空{}{}空".format(*sixty_cycle_hour.get_year().get_extra_earth_branches(),
                                                                 *sixty_cycle_hour.get_month().get_extra_earth_branches(),
                                                                 *sixty_cycle_hour.get_day().get_extra_earth_branches(),
                                                                 *sixty_cycle_hour.get_sixty_cycle().get_extra_earth_branches()
                                                                 )

        self.dispatch('on_sixgod_updated', sixgod)
    def on_sixgod_updated(self,*args):
        pass

class SixGodWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def update(self,sixgod):
        for i in range(6):
            self.ids[f"{i}"].text=sixgod[i]