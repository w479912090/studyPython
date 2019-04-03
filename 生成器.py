#在Python中，这种一边循环一边计算的机制，称为生成器：generator
#一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
print(g)

#通过next()函数获得generator的下一个返回值
print(next(g))

for i in g:
	print(i)

#斐波拉契数列
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'
fib(5)

#一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib1(max):
	n, a, b, = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
#generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
print(next(fib1(4)))
for i in fib1(4):
	print(i)

#用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib1(6)
while True:
	try:
		x = next(g)
		print('x:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

#杨辉三角
#我们把每一次层看作一个list， 通过一个for循环，通过迭代，每次生成一个list，而生成器就在每一行生成list中起作用
#对于每一行，list 的第一个元素和最后一个元素是不变的。如果用L = [] 表示的话， L[0], L[n],是 不变的
def triangles(n):
    l, index = [1], 0
    while index < n:
        yield l
        l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]
        index += 1

for i in triangles(10):
	print(i)