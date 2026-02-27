'''
    排盘程序
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
from __future__ import annotations

from tyme4py.sixtycycle import Element,HeavenStem,EarthBranch
import tyme4py
from typing import List
import ijson

纳甲表 = {
    # 阳卦：顺排阳支（子、寅、辰、午、申、戌）；阴卦：逆排阴支（未、巳、卯、丑、亥、酉）
    "乾": {"内干": "甲", "外干": "壬", "内支": ["子", "寅", "辰"], "外支": ["午", "申", "戌"]},
    "兑": {"内干": "丁", "外干": "丁", "内支": ["巳", "卯", "丑"], "外支": ["亥", "酉", "未"]},
    "离": {"内干": "己", "外干": "己", "内支": ["卯", "丑", "亥"], "外支": ["酉", "未", "巳"]},
    "震": {"内干": "庚", "外干": "庚", "内支": ["子", "寅", "辰"], "外支": ["午", "申", "戌"]},
    "巽": {"内干": "辛", "外干": "辛", "内支": ["丑", "亥", "酉"], "外支": ["未", "巳", "卯"]},
    "坎": {"内干": "戊", "外干": "戊", "内支": ["寅", "辰", "午"], "外支": ["申", "戌", "子"]},
    "艮": {"内干": "丙", "外干": "丙", "内支": ["辰", "午", "申"], "外支": ["戌", "子", "寅"]},
    "坤": {"内干": "乙", "外干": "癸", "内支": ["未", "巳", "卯"], "外支": ["丑", "亥", "酉"]},
}

六十四卦 = {
    # 下卦 = 乾 (0)
    (0, 0): "乾为天(六冲)",    (0, 1): "泽天夬",    (0, 2): "火天大有(归魂)",
    (0, 3): "雷天大壮(六冲)", (0, 4): "风天小畜",  (0, 5): "水天需(游魂)",
    (0, 6): "山天大畜",       (0, 7): "地天泰(六合)",

    # 下卦 = 兑 (1)
    (1, 0): "天泽履",         (1, 1): "兑为泽(六冲)", (1, 2): "火泽睽",
    (1, 3): "雷泽归妹(归魂)", (1, 4): "风泽中孚(游魂)", (1, 5): "水泽节(六合)",
    (1, 6): "山泽损",         (1, 7): "地泽临",

    # 下卦 = 离 (2)
    (2, 0): "天火同人(归魂)", (2, 1): "泽火革",     (2, 2): "离为火(六冲)",
    (2, 3): "雷火丰",         (2, 4): "风火家人",   (2, 5): "水火未济",
    (2, 6): "山火贲(六合)",   (2, 7): "地火明夷(游魂)",

    # 下卦 = 震 (3)
    (3, 0): "天雷无妄(六冲)", (3, 1): "泽雷随",   (3, 2): "火雷噬嗑",
    (3, 3): "震为雷(六冲)",   (3, 4): "风雷益",   (3, 5): "水雷屯",
    (3, 6): "山雷颐(游魂)",   (3, 7): "地雷复(六合)",

    # 下卦 = 巽 (4)
    (4, 0): "天风姤",         (4, 1): "泽风大过(游魂)", (4, 2): "火风鼎",
    (4, 3): "雷风恒",         (4, 4): "巽为风(六冲)", (4, 5): "水风井",
    (4, 6): "山风蛊(归魂)",   (4, 7): "地风升",

    # 下卦 = 坎 (5)
    (5, 0): "天水讼(游魂)",   (5, 1): "泽水困(六合)", (5, 2): "火水未济",
    (5, 3): "雷水解",         (5, 4): "风水涣",       (5, 5): "坎为水(六冲)",
    (5, 6): "山水蒙",         (5, 7): "地水师(归魂)",

    # 下卦 = 艮 (6)
    (6, 0): "天山遁",         (6, 1): "泽山咸",   (6, 2): "火山旅(六合)",
    (6, 3): "雷山小过(游魂)", (6, 4): "风山渐(归魂)", (6, 5): "水山蹇",
    (6, 6): "艮为山(六冲)",   (6, 7): "地山谦",

    # 下卦 = 坤 (7)
    (7, 0): "天地否(六合)",   (7, 1): "泽地萃",   (7, 2): "火地晋(游魂)",
    (7, 3): "雷地豫(六合)",   (7, 4): "风地观",   (7, 5): "水地比(归魂)",
    (7, 6): "山地剥",         (7, 7): "坤为地(六冲)"
}



class Bagua(tyme4py.LoopTyme):
    NAMES: List[str]=["乾", "兑", "离", "震", "巽", "坎", "艮", "坤"]
    def __init__(self, index_or_name: int | str):
        super().__init__(self.NAMES, index_or_name)

    @classmethod
    def from_name(cls,name:str)->Bagua:
        return cls(name)
    
    @classmethod
    def from_index(cls,index:int)->Bagua:
        return cls(index)
    
    def next(self, n: int) -> Bagua:
        return Bagua(self.next_index(n))
    
    def get_element(self) -> Element:
        return Element.from_name(["金", "金", "火", "木", "木", "水", "土", "土"][self.get_index()])

class 六爻:
    def __init__(self,卦象:List[bool]) -> None:
        if len(卦象) != 6:
            raise TypeError("卦象长度错误")
        self.卦象 = 卦象

    def 排盘(self):
        self.下卦 = 卦象到卦名(self.卦象[0:3])
        self.上卦 = 卦象到卦名(self.卦象[3:6])
        self.卦名 = 六十四卦[self.下卦.get_index(),self.上卦.get_index()]
        # 世
        地 = self.卦象[0] == self.卦象[3]
        人 = self.卦象[1] == self.卦象[4]
        天 = self.卦象[2] == self.卦象[5]
        self.世 = (地 and 人)* 0b100 \
                + ( not 地 and not 天 or 地 and not 人) * 0b10 \
                + (天^地^人) * 0b1
        self.应 = (self.世+3)%6
        # 归魂
        if 地 and 天 and not 人:
            self.宫=self.下卦
        # 四世 五世 游魂
        elif self.世 in [3,4]:
            self.宫=卦象到卦名( [ not x for x in self.卦象[0:3] ])
        else:
            self.宫=self.上卦
        # 纳甲
        下 = 纳甲表[self.下卦.get_name()]
        上 = 纳甲表[self.上卦.get_name()]

        # 天干：下卦三爻用内干，上卦三爻用外干
        self.天干 = [
            下["内干"], 下["内干"], 下["内干"],
            上["外干"], 上["外干"], 上["外干"]
        ]

        # 地支：下卦内支，上卦外支
        self.地支 = 下["内支"] + 上["外支"]

        # 组合成 甲子
        self.甲子 = [
            g + z for g, z in zip(self.天干, self.地支)
        ]

        # 六亲
        self.五行 = [ EarthBranch.from_name(x).get_element().get_name() for x in self.地支 ]
        self.宫五行 = self.宫.get_element()
        self.六亲 = [
                    "兄弟" if self.宫五行.get_name() == x 
                    else "父母" if self.宫五行.get_reinforced().get_name() == x
                    else "子孙" if self.宫五行.get_reinforce().get_name() == x
                    else "官鬼" if self.宫五行.get_restrained().get_name() == x
                    else "妻财"
                    for x in self.五行]
        
    def gua_ci(self, json_file="./utils/zhouyi.json") -> str:
        gua_key=f"{self.下卦}下{self.上卦}上" 
        try:
            with open(json_file, "rb") as f:
                kv_parser = ijson.kvitems(f, '')
                for key, value in kv_parser:
                    if key == gua_key:
                        return value
                return None
        except (FileNotFoundError):
            return None


def 卦象到卦名(卦象:List[bool] | List[int]) -> Bagua:
    先天八卦序 =~(卦象[2] *0b1+卦象[1]*0b10+卦象[0]*0b100)
    return Bagua(先天八卦序)