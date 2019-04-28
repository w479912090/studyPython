#type()  type()函数可以查看一个类或变量的类型
#动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
#type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义

def fn(self, name='World'):
	print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello = fn))
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

'''要创建一个class对象，type()函数依次传入3个参数：
	1.class的名称；
	2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
	3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
通过type()函数创建的类和直接写class是完全一样的,
因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class'''

#metaclass
'''metaclass，直译为元类，简单的解释就是：
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。'''