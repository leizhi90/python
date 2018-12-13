# -*- conding:utf-8 -*-
#函数的说明文档
#说明文档：惯例
#说明文档使用三引号标注
#第一行：函数功能的简要说明，接下来一个空行，再接下来为函数的详细说明
def add(a,b):
      """该函数实现两个数值的求和

      这里是详细说明
      :param a:
      :param b:
      :return:
      """
      return a+b
#函数说明文档与普通注释的区别
# 1、函数说明文档我们可以获得
#2、函数说明文档我们也可以通过help函数获取
print(add.__doc__)
help(id)
help(add)

#函数注解，python中，函数没有明确标记参数的类型与返回值类型（鸭子类型），为了让程序具有更好的可读性与易用性，可以为函数中的参数与返回值增加类型描述，这种类型描述就是函数的注解
#参数：类型 惯例：
def annotation_test(a:int,b:int):
      return 's'
print(annotation_test.__annotations__)