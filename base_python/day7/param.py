# -*- conding:utf-8 -*-
#函数参数

#函数体现的是一个功能，而参数，就是可以控制功能的细节
#在定义函数时，给出的参数称为形式参数（形参
#在调用函数时，给出的参数称为实际参数（实参
#在调用的过程中，实际参数会赋值给对应的形式参数，参数传递

#通过定义参数，可以控制函数的功能细节，令函数更加灵活

def pring_star(line):
    for i in range(line):
        print ('****')
#在调用函数时，传递一个具体的值
pring_star(7)