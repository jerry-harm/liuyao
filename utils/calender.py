'''
    排六神程序
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
from tyme4py.solar import SolarDay
from tyme4py.sixtycycle import SixtyCycle
import datetime

ymd=datetime.date.today()

today=SolarDay.from_ymd(ymd.year,ymd.month,ymd.day).get_sixty_cycle_day()

def 排六神(day=today):
    初神 = {
    '甲': 0, '乙': 0,
    '丙': 1, '丁': 1,
    '戊': 2, '己': 3,
    '庚': 4, '辛': 4,
    '壬': 5, '癸': 5
}
    六神 = ['青龙','朱雀','勾陈','螣蛇','白虎','玄武']

    当日六神=  [ 六神[(初神[day.get_sixty_cycle().get_heaven_stem().get_name()] + i) % 6] for i in range(6)]
    return 当日六神