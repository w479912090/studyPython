#创建了一个class的实例后，我们可以给该实例绑定任何属性和方法
class Student(object):
	pass
s = Student()
#绑定一个属性
s.name = 'Wang'
print(s.name)
#绑定一个方法
from types import MethodType
def set_age(self, age):
	self.age = age
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)
#给一个实例绑定的方法，对另一个实例是不起作用的
#为了给所有实例都绑定方法，可以给class绑定方法
Student.set_age = set_age
s2 = Student()
s2.set_age(20)
print(s2.age)

#__slots__   
#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student1(object):
	__slots__ = ('name', 'age')
s3 = Student1()
s3.name = 'Li'
s3.age = 18
#s3.score = 100	不能绑定__slots__包含之外的属性
print(s3.name, s3.age)
#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

#@property
#Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student2(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			print('score must be an integer!')
		if value < 0 and value > 100:
			print('score must between 0~100!')
		self._score = value
	@property
	def age(self):
		self._birth = 1993
		return 2019 - self._birth

s4 = Student2()
s4.score = 59	#实际转化为s.set_score(60)
print(s4.score)	#实际转化为s.get_score()
print(s4.age)#score是一个可读写属性，age是一个只读属性

#多重继承
class Animal(object):
	def life(self):
		print('animal lifing...')
class Runnable(object):
	def run(self):
		print('runnable running...')
class Dog(Animal, Runnable):
	pass
d = Dog()
d.run()
d.life()