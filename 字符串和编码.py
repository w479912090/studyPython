#在最新的Python 3版本中，字符串是以Unicode编码的

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('a'),ord('中'))
print(chr(66),chr(25991))
print('\u4e2d\u6587')

'''由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
Python对bytes类型的数据用带b前缀的单引号或双引号表示'''
x = b'ABC'
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
'''纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错
例如：print('中文'.encode('ascii'))'''

#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

'''如果bytes中包含无法解码的字节，decode()方法会报错
如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节'''
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

#要计算str包含多少个字符，可以用len()函数
print(len('abc'))
print(len('中文'))
#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len(b'abc'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

'''可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换
由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码'''

print(u'中文测试正常')

#在Python中，采用的格式化方式和C语言是一致的，用%实现
print('Hello,%s' % 'World')
print('Hi,%s,you have $%s.' % ('Wang',2000))

#常见的占位符  %d------整数   %f------浮点数    %s-----------字符串      %x------------十六进制整数

#格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

#%%来表示一个%   转义%
print( 'growth rate: %d %%' % 7)

#另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……
print('{0},成绩提升了{1:.1f}%'.format('小明',17.123))

s1 = 72
s2 = 85;
s = (s2 - s1)/s1*100
print('小明成绩提高了%.1f%%'%s)