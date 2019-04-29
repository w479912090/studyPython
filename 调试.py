#print()
#凡是用print()来辅助查看的地方,都可以用断言（assert）来替代
def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 / n
#assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错
#启动Python解释器时可以用-O参数来关闭assert

#logging
#和assert比，logging不会抛出错误，而且可以输出到文件
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %s' % n)
print(10/n)
#这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
#当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
#这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息

#pdb
#启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
s = '0'
n = int(s)
print(10/n)
#    python -m pdb err.py
#输入命令l来查看代码
#输入命令n可以单步执行代码
#可以输入命令p 变量名来查看变量
#输入命令q结束调试，退出程序

#pdb.set_trace()

import pdb
s = '0'
n = int(s)
pdb.set_trace()#运行到这里会自动暂停
print(10/n)