#用def定义函数
def my_abs(x):
	if x > 0:
		return x
	else:
		return -x

x = int(input())
print(my_abs(x))

#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return

#如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
	pass
#pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来

#数据类型检查可以用内置函数isinstance()实现
def test_abs(x):
	if not isinstance(x, (int,float)):
		raise TypeError('bad operand type')
	if x >=0:
		return x
	else:
		return -x
x = int(input())
print(test_abs(x))
#print(test_abs('A'))  会报错

import math
def move(x,y,step,angle = 0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny
print(move(100,100,60,math.pi/6))
#Python的函数返回多值其实就是返回一个tuple

#practice    求解ax2 + bx + c = 0
def quadratic(a, b, c):
	pass#先放着不会写