#type()
#基本类型的对象类型都可以用type()判断
class Animal(object):
	pass

a = Animal()

print(type(123))
print(type('123'))
print(type(None))
print(type(abs))
print(type(a))

print(type(123) == int)
print(type('123') == str)

#要判断一个对象是否是函数,可以使用types模块中定义的常量
import types
def fn():
	pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

#isinstance()
#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数

class Dog(Animal):
	pass
class Husky(Dog):
	pass

d = Dog()
h = Husky()
print(isinstance(d, Animal))
print(isinstance(h, Dog))
print(isinstance(a, Dog))
print(type(d) == type(a))
print(isinstance(b'c', bytes))

#判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

#dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir('ABC'))

class MyDog(object):
	def __len__(self):
		return 100
dog = MyDog()
print(len(dog))
print(dog.__len__())

class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x')) #有x属性吗？
setattr(obj, 'y', 10) #设置属性y
print(getattr(obj, 'y')) #获取属性y
#可以传入一个默认参数，如果属性不存在，返回默认参数
print(getattr(obj, 'z', 404))

print(hasattr(obj, 'power')) #有属性power吗？
fn = getattr(obj, 'power') #获取属性power并赋值到fn
print(fn())


#实例属性和类属性
class Student(object):
	name = 'Student'
stu = Student()
print(stu.name)
print(Student.name)
stu.name = 'Wang' #实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(stu.name)
print(Student.name)
del stu.name	#如果删除实例的name属性,类的name属性就显示出来了
print(stu.name)