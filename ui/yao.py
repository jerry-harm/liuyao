'''
    双状态按钮组件
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
from typing import Callable

from kivy.event import EventDispatcher
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.properties import BooleanProperty,ObjectProperty
from kivy.clock import Clock

class YaoButton(ButtonBehavior,Widget,EventDispatcher):
   status = BooleanProperty(True)

   def __init__(self, **kwargs):
      self.register_event_type('on_change')
      super(YaoButton,self).__init__(**kwargs)
      # 一改状态就重画
      self.bind(status=self.update, size=self.update, pos=self.update)
      # 延迟画一次，防止初始化报错
      Clock.schedule_once(self.update)

   def update(self, *args):
      self.canvas.clear()
      if self.width <= 0:
         return
      if self.height <= 0:
         return

      with self.canvas:
         Color(1, 1, 1, 1)

         w = self.width * 0.8
         h = self.height * 0.5
         x = self.pos[0] + (self.width - w) / 2
         y = self.pos[1] + (self.height - h) / 2

         if self.status:
            Rectangle(pos=(x, y), size=(w, h))
         else:
            part = w * 0.4
            Rectangle(pos=(x, y), size=(part, h))
            Rectangle(pos=(x + w - part, y), size=(part, h))

   def on_press(self):
      self.status = not self.status
      self.dispatch('on_change')
   
   def on_change(self):
      pass

