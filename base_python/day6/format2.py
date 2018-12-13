# -*- conding:utf-8 -*-
#新式格式化
# 使用str类型的format方法实现
# 格式化模板，format（替换值
#格式化模板中，使用（）来表示占位符

# {[字段名][！转换类型][：格式说明]}
print ('{}'.format("替换值"))
print ('{}-{}'.format('替换值','替换值2'))
#指定序号来进行替换
print ('{1}-{0}-{0}'.format('替换值','替换值2'))
# 也可以指定关键字进行对应的替换
print ('{back}—{front}'.format(front='前面的',back='后面的'))

c=5+4j
print ('{0.real}-{0.imag}'.format(c))
#5.0-4.0

print ("{data.real}-{data.imag}".format(data=c))

# 指定参数的索引值进行替换
print ('{0[2]}'.format([1,2,3]))

#如果要使用不同的{}.则需要转义处理
print ('{}{{}}'.format(3))

# 格式说明，!a  !s  !r
print ('{0!a}'.format('中国'))
print ('{0!s}'.format('中国'))
print ('{0!r}'.format('中国'))

# 格式说明
#  {[字段名][！转换类型][：格式说明]}  []可以省略的
# :< 左对齐 >右对齐
print ('{:<10}'.format('abc'))
# :^ 居中对齐
print ('{:^10}'.format('2323'))
# 对齐时，可以在对齐符号前面指定填充符
print ('{:#>10}'.format('aaaa'))
print ('{:#=10}'.format(-100))

# 符号
# + 对正数 补充前缀+
print ('{:+}'.format(500))