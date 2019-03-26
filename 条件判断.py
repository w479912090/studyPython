#elif是else if的缩写
age = 3;
if age >= 18:
	print('adult')
elif age >= 6:
	print('teenage')
else:
	print('kid')

#input返回的数据类型是str
birth = int(input('birth:'))
if birth >= 2001:
	print('adult')
else:
	print('young')

#int()函数发现一个字符串并不是合法的数字时就会报错
#比较符号居然可以连续使用   9 < a < 11   ==   9 < a and a < 11
a = int(input('输入数字:'))
if 100 < a < 200:
	print(True)
else:
	print(False)