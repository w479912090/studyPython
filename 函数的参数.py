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

#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
	print('name:', name,'age:', age, 'other:', kw)

person('wang', 18)
person('wang', 18, city = 'hangzhou')
person('wang', 18, city = 'hangzhou', job = 'programmer')
extra = {'city': 'hangzhou', 'job': 'programmer'};
person('wang', 18, city = extra['city'], job = extra['job'])
person('wang', 18, **extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

 #关键字参数
 #如果要限制关键字参数的名字，就可以用命名关键字参数，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person1(name, age, *, city, job):
 	print(name, age, city, job)
person1('wang', 20, city = 'hangzhou', job = 'programmer')

def person2(name, age, *agrs, city, job):
	print(name, age, agrs, city, job)
person2('wang', 21, 1,2,3, city = 'hangzhou', job = 'programmer')

#命名关键字参数city具有默认值，调用时，可不传入city参数
def person3(name, age, *, city = 'hangzhou', job):
	print(name, age, city, job)
person3('wang', 22, job = 'programmer')

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, *d, e, **kw):
	print(a, b, d, e, kw)
f1(1,2,3,e = 4,f = 5)

agrs = (1,2,3)
kw = {'e': 100, 'x': 1}
f1(*agrs, **kw)
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
