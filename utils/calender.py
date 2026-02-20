from tyme4py.solar import SolarDay
from tyme4py.sixtycycle import SixtyCycle
import datetime

ymd=datetime.date.today()

today=SolarDay.from_ymd(ymd.year,ymd.month,ymd.day).get_sixty_cycle_day()
