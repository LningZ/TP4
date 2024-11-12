#Exercice 1.1

import numpy as np  # 如果要用 np.abs，需要引入 numpy 库

def affiche(p):
    """
    该函数用于将给定的多项式系数列表 p 转换为标准的多项式字符串表示形式。
    
    参数:
    p (list): 表示多项式各项系数的列表，p[i] 是 x^i 项的系数。
    
    返回:
    str: 表示多项式的标准字符串形式。
    """
    n = len(p) - 1  # 获取多项式的最高次项
    poly = ""  # 初始化空字符串用于存储多项式的字符串表示

    # 从最高次项开始遍历到常数项
    for i in range(n, -1, -1):
        coeff = p[i]  # 当前项的系数
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

# 示例用法
p = [1, 0, 3, 4]  # 表示 4x^3 + 3x^2 + 1
print(affiche(p))  # 输出：4x^3 + 3x^2 + 1


#Exercice 1.2

def get_valeur(p,x):
    valeur = 0
    for i in range (len(p)):
        valeur += p[i] * x**i
    return valeur

p = [1, 0, 3, 4]
print(affiche(p))
print(get_valeur(p,2))

#Exercice 1.3
def deriver(p):
    """
    计算并返回多项式 p 的导数形式（返回导数的多项式字符串，按从高次项到低次项排列）。
    
    参数:
    p (list): 表示多项式各项系数的列表，p[i] 是 x^i 项的系数（升幂排列）。
    
    返回:
    str: 导数多项式的字符串形式。
    """
    n = len(p) - 1  # 获取多项式的最高次幂
    derivative = ""  # 用于存储导数多项式的字符串

    # 从高次项到低次项遍历多项式，计算每项的导数
    for i in range(n, 0, -1):  # 忽略常数项，因为它的导数是 0
        coeff = i * p[i]  # 每项的导数是 i * p[i]
        if coeff != 0:  # 只处理系数不为 0 的项
            if derivative:  # 如果之前已经添加过项，则加上正负号
                if coeff > 0:
                    derivative += " + "
                else:
                    derivative += " - "
                coeff = abs(coeff)  # 处理完符号后，取系数的绝对值

            # 拼接多项式的不同项
            if i == 1:
                derivative += f"{coeff}x"  # 一次项
            else:
                derivative += f"{coeff}x^{i-1}"  # 高次项

    # 如果导数为空（即多项式是常数项），返回 0
    if not derivative:
        return "0"
    
    return derivative

# 示例用法
p = [1, 0, -3, 4]  # 表示多项式 4x^3 - 3x^2 + 1

print(affiche(p))  # 输出：4x^3 + 3x^2 + 1
print(deriver(p))  # 输出导数后的多项式字符串

#Exercice 1.4
# 定义一个主函数来测试三个函数
def main():
    # 定义一个多项式 p(x) = 4x^3 - 3x^2 + 1
    p = [1, 0, -3, 4]
    
    # 显示多项式的表达式
    print("Le polynôme est :")
    print(affiche(p))  # 调用 affiche 函数
    
    # 计算多项式在 x = 2 处的值
    x = 2
    print(f"Le polynôme évalué en x = {x} est :")
    print(get_valeur(p, x))  # 调用 get_valeur 函数
    
    # 显示多项式的导数
    print("Le polynôme dérivé est :")
    print(deriver(p))  # 调用 deriver 函数

# 调用主函数进行测试
main()