#try
#Python的错误其实也是class，所有的错误类型都继承自BaseException
try:
	print('try...')
	r = 10/int('2')
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:', e)
else:
	print('no error')
finally:
	print('finally')
print('END')

#使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用

#调用栈
#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息

#Python内置的logging模块可以非常容易地记录错误信息
#程序打印完错误信息后会继续执行
import logging
def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
main()
print('END')

#抛出错误   用raise语句抛出一个错误的实例