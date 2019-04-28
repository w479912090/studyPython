#__str__
class Student(object):
	def __init__(self, name):
		self._name = name
	def __str__(self):
		return 'Student object (name: %s)' % self._name
print(Student('Wang'))

class Student1(object):
	def __init__(self, name):
		self._name = name
	def __str__(self):
		return 'Student object (name: %s)' % self._name
	__repr__ = __str__
s = Student1('Li')
s

#__iter__
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
#然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环

class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
	def __iter__(self):
		return self
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if(self.a > 20):
			raise StopIteration
		return self.a
for n in Fib():
	print(n)

#__getitem__
class Fib1(object):
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L
f = Fib1()
print(f[0])
print(f[10])
print(f[0:5])

#__getattr__
#当我们调用类的方法或属性时，如果不存在,Python解释器会试图调用__getattr__()来尝试获得属性
#__call__ 直接对实例进行调用

class Animal(object):
	def  __init__(self):
		self.name = 'Dog'
	def __getattr__(self, attr):
		if attr == 'age':
			return '没有age属性'
		if attr == 'run':
			return lambda: 'running'
	def __call__(self):
		print('Animal\'s name is %s' % self.name)
d = Animal()
print(d.name)
print(d.age)
print(d.run())
d()

#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
print(callable(Animal()))
print(callable(1))
print(callable(max))


#实现Chain().users('michael').repos输出/users/michael/repos

class Chain(object):
	def __init__(self, path=''):
		self._path = path
	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))
	def __call__(self, path):
		return Chain('%s/%s' % (self._path, path))
	def __str__(self):
		return self._path
	__repr__ = __str__
print(Chain().users('michael').repos)