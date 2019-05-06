#set是一个无序的， 为空或是更多不可变Python数据对象集合。集合中的值不允许重复，以逗号分隔，写在大括号中。空集合由set()表示
mySet = {False, 4.5, 3, 6, 'cat'}
yourSet = {99, 3, 100}
print(len(mySet))
print(False in mySet)
print('dog' in mySet)
print(mySet.union(yourSet))
print(mySet | yourSet)
print(mySet.intersection(yourSet))
print(mySet & yourSet)
print(mySet.difference(yourSet))
print(mySet - yourSet)
print({3, 100}.issubset(yourSet))
print({3, 100}<=yourSet)
mySet.add('house')
print(mySet)
mySet.remove(4.5)
print(mySet.pop())
print(mySet.clear())
print(mySet)

#字典
phoneext={'david':1410,'brad':1137}
print(phoneext.keys())
print(list(phoneext.keys()))
print(list(phoneext.values()))
print(list(phoneext.items()))
print(phoneext.get('kent'))
print(phoneext.get('kent', 'NO ENTRY'))