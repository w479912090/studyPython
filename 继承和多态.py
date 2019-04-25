class Animal(object):
	def run(self):
		print('animal is running')

class Dog(Animal):
	def run(self):
		print('dog is running')

class Cat(Animal):
	def run(self):
		print('cat is running')

ani = Animal()
ani.run()
dog = Dog()
dog.run()
cat = Cat()
cat.run()

#判断一个变量是否是某个类型可以用isinstance()判断
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(ani, Dog))
#在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行