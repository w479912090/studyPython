#函数可以传入一个匿名函数当做参数
l = list(map(lambda x:x * x, [1, 2, 3, 4, 5]))
print(l)

'''匿名函数lambda x:x * x实际上就是
def f(x):
	return x * x 
关键字lambda表示匿名函数，冒号前面的x表示函数参数'''

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果

f = lambda x:x * x
print(f)
print(f(5))

#可以把匿名函数作为返回值返回
def build(x, y):
	return lambda: x * x + y * y
print(build(3, 4))