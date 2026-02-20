from operator import xor
import string

import tyme4py.sixtycycle as 干支
import tyme4py
from typing import List,Union

八卦: List[str] = ["乾", "兑", "离", "震", "巽", "坎", "艮", "坤"]

class 六爻:
    def __init__(self,卦象:List[bool] | List[int]) -> None:
        if len(卦象) != 6:
            raise TypeError("卦象长度错误")
        self.卦象=卦象


    def 排盘(self):
        # 世
        地 = self.卦象[0] == self.卦象[3]
        人 = self.卦象[1] == self.卦象[4]
        天 = self.卦象[2] == self.卦象[5]
        self.世 = (地 and 人)* 0b100 \
                + ( not 地 and not 天 or 地 and not 人) * 0b10 \
                + (天^地^人) * 0b1
        # 归魂
        if 地 and 天 and not 人:
            self.宫=卦象到卦名(self.卦象[0:3])
        # 四世 五世 游魂
        elif self.世 in [3,4]:
            self.宫=卦象到卦名( [ not x for x in self.卦象[0:3] ])
        else:
            self.宫=卦象到卦名(self.卦象[3:6])

def 卦象到卦名(卦象:List[bool] | List[int]) -> str:
    先天八卦序 =~(卦象[2] *0b1+卦象[1]*0b10+卦象[0]*0b100)
    return 八卦[先天八卦序]

test=六爻([0,0,0,0,1,0])
test.排盘()
print(test.世)
print(test.宫)