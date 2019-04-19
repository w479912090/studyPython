class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s: %s' % (self.name, self.score))
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student('wang', 100)
bart.print_score()
print(bart.get_grade())

'''class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，
表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传'''


#访问限制
#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）

class Student1(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score

bart1 = Student1('wang1', 99)
bart1.print_score()
print(bart1._Student1__name)

#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
#但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名