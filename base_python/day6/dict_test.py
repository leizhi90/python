# -*- conding:utf-8 -*-
# 字典类型

# 字典类型来源于现实中使用的字典，现实中的字典提供一个字到页码的映射
# python 中字典提供一个键到值得映射

# 创建方式

# 指定键值创建
d={1:'a',2:'b',3:'c'}
print (type(d))

# 使用dict函数，参数传递一个包含元祖的列表
d=dict([(1,'a'),(2,'b'),(3,'c')])
print (d)

#使用dict函数 ，参数用zip
d= dict(zip([4,5,6],['t','d','g']))
print (d)
# 使用dict函数，使用关键字参数
d=dict(a=10,d=43,k='None')
print (d)
# 通过key 查找对应的值
print (d['d'])
# 键不存在 错误 **KeyError: 'l'
# print (d['l'])
# 没有的话 None
print (d.get('l'))#None
print (d.get('k'))
print (d.get('l') == d.get('k'))
print (type(d.get('l')))
print (type(d.get('k')))
print (None==None)
# Null和None是Python的特殊类型，Null对象或者是NoneType，它只有一个值None.
# 它不支持任何运算也没有任何内建方法。
# None和任何其他的数据类型比较永远返回False。
# None有自己的数据类型NoneType。
# 你可以将None复制给任何变量，但是你不能创建其他NoneType对象。
#增加或修改 ，取决于key是否存在字典中（有则覆盖，无则增加）
d['p']='444'

#删除键值对
del d['p']
# 字典的特征

# 1 字典中的键值对是无序的，没有索引
# 2、字典中的键是不能重复的，键唯一
d2={1:4,1:6,1:'1'}
print (d2)
# 3、字典中的键必须是可哈希类型（hashtable）
# int float complex str bytes tuple 为可哈希类型
# list 不可哈希的
# d3={[1,5]:'d'}
# print (d3)
#TypeError: unhashable type: 'list'

# 哈希表 散列表 hashtable
# 可哈希类型：在程序同一次运行过程中，同一个键多次调用哈希函数产生的值（地址）完全相同
