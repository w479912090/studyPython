def now():
	print(123)
f = now
f()
print(now.__name__)

#在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#本质上，decorator就是一个返回函数的高阶函数
def log(func):
	def wrapper(*agrs, **kw):
		print('call %s():' % func.__name__)
		return func(*agrs, **kw)
	return wrapper

#log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处
@log
def now():
	print(123)
now()

#把@log放到now()函数的定义处，相当于执行了语句 now = log(now)
#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数

def log1(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log1('execute')
def now1():
	print(123)
now1()
#3层嵌套的效果是这样的:
now2 = log1('execute')(now1)
print(now2.__name__)

#首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
#以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，

#所以，一个完整的decorator的写法如下
import functools
def log2(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
@log2('hole')
def now3():
	print('end')
now3()
print(now3.__name__)

#在定义wrapper()的前面加上@functools.wraps(func)即可