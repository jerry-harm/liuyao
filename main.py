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

resource_add_path('./fonts')
Config.read(".config.ini")
Config.set("kivy","default_font",['NotoSans','./fonts/NotoSansMonoCJKsc-VF.ttf','./fonts/NotoSansMonoCJKsc-VF.ttf','./fonts/NotoSansMonoCJKsc-VF.ttf','./fonts/NotoSansMonoCJKsc-VF.ttf'])
Config.write()

from kivy.loader import Loader

Loader.loading_image = "icon.png"

from kivy.app import App

from kivy.core.text import LabelBase, DEFAULT_FONT

class LiuYaoApp(App):
    def build(self):
        pass
        
if __name__ == '__main__':
    LiuYaoApp().run()

