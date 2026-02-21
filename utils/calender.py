from tyme4py.solar import SolarDay
from tyme4py.sixtycycle import SixtyCycle
import datetime

ymd=datetime.date.today()

today=SolarDay.from_ymd(ymd.year,ymd.month,ymd.day).get_sixty_cycle_day()

def 排六神(day):
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