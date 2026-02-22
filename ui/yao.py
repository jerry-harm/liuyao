from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.properties import BooleanProperty
from kivy.clock import Clock

class BarWidget(Widget):
    # 像 Label 一样用属性（这是唯一关键）
    
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

      with self.canvas:
         Color(1, 1, 1, 1)

         w = self.width * 0.8
         h = 20
         x = self.x + (self.width - w) / 2
         y = self.y + (self.height - h) / 2

         if self.status:
            Rectangle(pos=(x, y), size=(w, h))
         else:
            part = w * 0.4
            Rectangle(pos=(x, y), size=(part, h))
            Rectangle(pos=(x + w - part, y), size=(part, h))

   def on_touch_down(self, touch):
      if self.collide_point(*touch.pos):
         self.status = not self.status
         return True
      return super().on_touch_down(touch)

class TestApp(App):
   def build(self):
      return BarWidget(size=(400, 100))

if __name__ == '__main__':
    TestApp().run()
