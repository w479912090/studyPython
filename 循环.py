#Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
#range(x)生成的序列是从0开始小于x的整数
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
	sum += n
	n -= 2
print(sum)

#continue跳过本次循环，继续下次循环
n = 0
while n < 10:
	n += 1
	if n % 2 == 0:
		continue
	print(n)
print('end')

#break结束循环
n = 0
while n <= 10:
	n += 1
	if n > 3:
		break
	print(n)
print('end')