# -*- conding:utf-8 -*-
#字典提过的相关方法
#
d={1:'a',2:'b',3:'c'}
#返回参数指定key所绑定的值 d.get(key) d[key]
# 如果key 不存在，d[key]报错 get 返回None

#get 指定第二个参数，不存在时返回指定的值
print (d.get('p','返回指定的值'))

#pop 删除参数指定key所对应的键值对，返回kye————value
# 如果Key 不存在 产生错误
# 指定第二个参数
print (d.pop("o",'默认值'))
print (d)

# 返回字典中所有的键
print (d.keys())#dict_keys([1, 2, 3])
print (d.values())#dict_values(['a', 'b', 'c'])
#返回字典中所有的键值对
print (d.items())#dict_items([(1, 'a'), (2, 'b'), (3, 'c')])
#删除字典中所有的键值对
d.clear()
#返回参数key所绑定的v ，如果不存在 ，则此key 存入 默认v=None
print (d.setdefault(1))
print (d.setdefault(55))
print (d.setdefault('b','指定默认'))

d2={5:'e',6:'t'}
d2.update({2:'r',5:'o'})
print (d2)
print (d2.popitem())

d3=d2.fromkeys([1,2,3],[5,6,7])
print (d3)