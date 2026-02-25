'''
    入口程序
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
from kivy.config import Config
from kivy.resources import resource_add_path

from utils.gua import 六爻
from typing import List

resource_add_path('./fonts')
Config.read(".config.ini")
Config.set("kivy","default_font",['NotoSans','./fonts/NotoSansMonoCJKsc-VF.ttf','./fonts/NotoSansMonoCJKsc-VF.ttf','./fonts/NotoSansMonoCJKsc-VF.ttf','./fonts/NotoSansMonoCJKsc-VF.ttf'])
Config.write()


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def format_output(self,time,empty,original:六爻,changed:六爻,sixgod:List[str],change:List[str],*args) -> str:
        gua=f"\n   {original.卦名}      {changed.卦名}\n"
        for i in range(6):
            o_shi=" "
            c_shi=" "
            if original.世==i:
                o_shi="世"
            if original.应==i:
                o_shi="应"
            if changed.世==i:
                c_shi="世"
            if changed.应==i:
                c_shi="应"
            gua+=\
f"{sixgod[i]}\
{o_shi}{'___' if original.卦象[i] else '_ _'}{original.六亲[i]}{original.甲子[i]}{original.五行[i]}\
{' ' if not change[i] else change[i]}\
{c_shi}{'___' if changed.卦象[i] else '_ _'}{changed.六亲[i]}{changed.甲子[i]}{changed.五行[i]}\n"
        return f"{time}\n{empty}\n"+gua
class LiuYaoApp(App):
    def build(self):
        pass
        
if __name__ == '__main__':
    LiuYaoApp().run()

