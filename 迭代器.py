'''可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
可以使用isinstance()判断一个对象是否是Iterable对象'''
from collections.abc import Iterable
print(isinstance([], Iterable))
print(isinstance('abc', Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance(123, Iterable))

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
from collections.abc import Iterator
print(isinstance([], Iterator))
t = [x for x in range(10)]
print(isinstance(t, Iterator))
t = (x for x in range(10))
print(isinstance(t, Iterator))

#把list、dict、str等Iterable变成Iterator可以使用iter()函数
t = iter([x for x in range(10)])
print(isinstance(t, Iterator))

#Python的for循环本质上就是通过不断调用next()函数实现的
for x in [1, 2, 3, 4, 5]:
	pass
#等价于
it = iter([1, 2, 3, 4, 5])
while True:
	try:
		print(next(it))
	except StopIteration:
		break