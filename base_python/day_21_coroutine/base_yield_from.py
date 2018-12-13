# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/17 11:16
def squares():
    for i in range(10):
        yield  i**2
def generator_all_in_one():
    for i in squares():
        yield i+1
def generator_splitted():
    yield from squares()
li = [i for i in generator_all_in_one()]
print(li)
ll = [i for i in generator_splitted()]
print(ll)