from kivy.event import EventDispatcher
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.properties import BooleanProperty
from kivy.clock import Clock

class YaoButton(ButtonBehavior,Widget):
   status = BooleanProperty(True)

   def __init__(self, **kwargs):
      super().__init__(**kwargs)
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

