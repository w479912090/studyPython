#求解x的n次方
def power(x, n):
	s = 1
	while n > 0:
		s = s * x
		n = n - 1
	return s
print(power(int(input()),int(input())))

def add_end(L = []):
	L.append('END')
	return L
print(add_end())
print(add_end())#此时会输出两个END

'''Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，
每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了'''

#定义默认参数要牢记一点：默认参数必须指向不变对象

def add_end1(L = None):
	if L is None:
		L = []
	L.append('END')
	return L
print(add_end1())
print(add_end1())#此时只会输出一个END

def cal1(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(cal1([1,2,3]))
print(cal1((1,2,3)))

#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
def cal2(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(cal2(1,2,3))

#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1,2,3]
print(cal2(*nums))