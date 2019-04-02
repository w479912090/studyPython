#只要是可迭代对象，无论有无下标，都可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
	print(k)

for v in d.values():
	print(v)

for k,v in d.items():
	print(k,v)

for k in 'ABC':
	print(k)

#通过collections模块的Iterable类型判断对象是不是可迭代对象
from collections.abc import Iterable
print(isinstance('ABC',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))#整数是不能迭代的

#Python内置的enumerate函数可以把一个list变成索引-元素对
for k,v in enumerate(['A', 'B', 'C']):
	print(k,v)

for x,y in ((1, 1), (2, 2), (3, 3)):
	print(x,y)