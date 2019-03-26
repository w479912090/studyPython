classmates = ['Michael', 'Bob', 'Tracy']
#用-1做索引，直接获取最后一个元素
print(classmates[-1])
#以此类推，可以获取倒数第2个、倒数第3个
print(classmates[-2])
print(classmates[-3])

#使用append在list后面添加元素
classmates.append('Adam')
print(classmates[-1])

#使用insret在指定位置插入元素
classmates.insert(1,'Jack')
print(classmates[1])

#pop删除指定位置的元素
classmates.pop(1)
print(classmates)

#有序列表叫元组：tuple，tuple一旦初始化就不能修改
books = ('语文','数学','英语')
#books这个tuple不能变，它没有append(),insert()这些方法,其他获取元素的方法和list是一样的，但不能赋值成另外的元素
print(books[0],books[1])
#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
t = (1,2)
print(t)
t = ()
print(t)
t = (1)		#这种情况下定义的不是tuple，是1这个数
print(t)
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)


#“可变的”tuple   变得是list,并不是tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
