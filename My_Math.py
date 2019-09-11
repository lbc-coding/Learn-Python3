# -*- coding:utf-8 -*-
# 这是liubaochang自己创建的数学函数组模块
# 既可以练习，又可以实用。

# 1、计算绝对值函数，函数名my_abs(),参数x
def my_abs(x):
    if not isinstance(x,(float,int)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 2、给定参数a,b,c，求一元二次方程的根。
def my_quadratic(a,b,c):
    import math
    if b * b < 4 * a * c:
        return '无实根'
    else:
        x1 = (-b + math.sqrt(b * b - 4 * a * c))/(2*a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c))/(2*a)
        return x1, x2

# 3、计算任意个数的乘积
def my_product(*args):
    if len(args) == 0:
        return 0
    else:
        product = 1
        for i in args:
            product = product * i
        return product

# 4、
