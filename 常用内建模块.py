#datetime
from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(type(now))

dt = datetime(2019, 4, 29, 15, 1)
print(dt)

#datetime转为timestamp(时间戳)
print(dt.timestamp())

#timestamp转为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))
#timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的

#datetime转换为str
print(now.strftime('%a, %b, %d, %H:%M'))

#datetime加减   需要导入timedelta这个类
print(now + timedelta(hours=10))
print(now - timedelta(days=1))

#collections
#namedtuple
#namedtuple是一个函数，用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p) 
print(isinstance(p, tuple))

#deque
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q.popleft())

#defaultdict
#使用dict时,如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
print(dd['k'])

#OrderedDict
#使用dict时，Key是无序的,如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
#OrderedDict的Key会按照插入的顺序排列，不是Key本身排序

#Counter  Counter是一个简单的计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    print(c[ch])
    c[ch] = c[ch] + 1
print(c)

#hashlib
#Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等,摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in'.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in'.encode('utf-8'))
sha1.update('python haslib?'.encode('utf-8'))
print(sha1.hexdigest())

#itertools
#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
import itertools
natuals = itertools.count(1)  #无限迭代器
cs = itertools.cycle('ABC')
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

#通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
ps = itertools.takewhile(lambda x: x <= 10, natuals)
print(ps)
print(list(ps))

#chain  chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'DEF'):
    print(c)

#groupby  groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AaaBbbCcc', lambda c: c.upper()):
    print(key, list(group))