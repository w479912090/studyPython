def lazy_sum(*args):
	def sum():
		ax = 0
		for x in args:
			ax += x
		return ax
	return sum
l = lazy_sum(1, 2, 3, 4, 5)
print(l)
print(l())
#内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力

#闭包
#当一个函数返回了一个函数后，其内部的局部变量还被新函数引用,返回的函数并没有立刻执行，而是直到调用了f()才执行
def count():
	fs = []
	for i in range(1, 4):
		print('执行f前i:', i)
		def f():
			print('执行f时i:', i)
			return i * i
		fs.append(f)
	return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
#返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量

#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count1():
	def f(i):
		print('执行g前i:', i)
		def g():
			print('执行g时i:', i)
			return i*i
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs
g1, g2, g3 = count1()
print(g1())
print(g2())
print(g3())