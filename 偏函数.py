#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
print(int('123'))

#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
print(int('123', base = 8))

def int2(x, base = 2):
	return int(x, base)
print(int2('1000000'))
print(int2('1000001'))

#functools.partial就是帮助我们创建一个偏函数的
import functools
int3 = functools.partial(int, base = 2)
print(int3('100000'))
print(int3('100001'))

#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
#上面的新的int3函数，仅仅是把base参数重新设定默认值为2

#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
int4 = functools.partial(int, base = 2)
int4('100000') #相当于
kw = {'base':2}
int('100000', **kw)

max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边
max2(4, 5, 6) #相当于
args = (10, 4, 5, 6)
max(*args)

print(max(*args))