

import numpy as np  # 如果要用 np.abs，需要引入 numpy 库

#EX1.4 TP4
class Polynom:

    def __init__(self,coefficient):
        self.coefficient = coefficient
        
    def affiche(self):

        n = len(self.coefficient) - 1  # 获取多项式的最高次项
        poly = ""  # 初始化空字符串用于存储多项式的字符串表示

        # 从最高次项开始遍历到常数项
        for i in range(n, -1, -1):
            coeff = self.coefficient[i]  # 当前项的系数
            if coeff != 0:  # 只有系数不为 0 时才输出对应项

                # 如果当前项不是最高次项，处理正负号
                if i != n:
                    if coeff > 0:
                        poly += " + "  # 系数为正时，添加 " + "
                    else:
                        poly += " - "  # 系数为负时，添加 " - "
                    coeff = np.abs(coeff)  # 取系数的绝对值，防止负号重复
                
                # 处理多项式的不同项次
                if i == 0:
                    poly += f"{coeff}"  # 常数项（x^0）
                elif i == 1:
                    poly += f"{coeff}x"  # 一次项（x^1）
                else:
                    poly += f"{coeff}x^{i}"  # 高次项（x^i）
        
        return poly  # 返回拼接好的多项式字符串


    def get_valeur(self,x):
        valeur = 0
        for i,coeff in enumerate (self.coefficient):
            valeur += coeff * (x**i)
        return valeur
            


p = Polynom([1.2, -0.1, -1.3, 0.1, 0.1])
print(p.affiche())
print(p.get_valeur(3))