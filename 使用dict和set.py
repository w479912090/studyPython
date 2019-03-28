d = {'A': 95, 'B': 85, 'C': 75}

#通过in判断key是否存在
print('A' in d)

#通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('A'))
print(d.get('D'))
print(d.get('D',-1))

#用pop()方法删除一个key
d.pop('A')
print(d)

#dict内部存放的顺序和key放入的顺序是没有关系的

'''和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。

而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法'''

#通过key计算位置的算法称为哈希算法（Hash）  要保证hash的正确性，作为key的对象就不能变

#set和dict类似，也是一组key的集合，但不存储value
#要创建一个set，需要提供一个list作为输入集合
s = set([1,2,3,4])
print(s)

#通过add(key)方法可以添加元素到set中,重复元素会被过滤掉
s.add(5)
print(s)

#通过remove(key)方法可以删除元素
s.remove(5)
print(s)

#两个set可以做数学意义上的交集、并集等操作
s1 = set([1,2,3])
s2 = set([2,3,4])
s3 = s1 & s2
print(s3)
s3 = s1 | s2
print(s3)

#set和dict的唯一区别仅在于没有存储对应的value

list = ['c','a','b'];
list.sort()
print(list)

#list的count()方法可以获取元素个数
print(list.count('c'))
#list的index()方法获取元素下标
print(list.index('c'))