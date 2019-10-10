#!/usr/bin/env python
# -*- coding: utf8 -*-

def log(x):
    print '============={0}==========='.format(x)
    pass


# hash() 用于获取取一个对象（字符串或者数值等）的哈希值。
# hash(object)
#    object -- 对象
# 返回对象的哈希值。
# hash() 函数的对象字符不管有多长，返回的 hash 值都是固定长度的
log('hash()')
print hash('we')
print hash('test')
print hash(12)
print hash(log)

# id() 函数用于获取对象的内存地址。
# id(object)
#    object -- 对象。
# 返回对象的内存地址。
log('id()')
print id([])

# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
# 带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。
# 如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
# dir([object])
#    object -- 对象、变量、类型。
# 返回模块的属性列表。
log('dir()')
print 'dir()--->', dir()
print 'dir([])--->', dir([])
print 'vars()--->', vars()  # 返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()
print 'globals()--->', globals()  # globals() 函数会以字典类型返回当前位置的全部全局变量。
print 'locals()--->', locals()  # locals() 函数会以字典类型返回当前位置的全部局部变量。

# help() 函数用于查看函数或模块用途的详细说明。
# help([object])
#    object -- 对象；
# log('help()')
# print help()  # 若无参数，则进入help模式  输入对象名称即可
# print help([])  # 返回参数对象的用途以及该参数对象的函数方法

# sorted() 函数对所有可迭代的对象进行排序操作。返回重新排序的列表，不改变原可迭代对象。
# sort 与 sorted 区别：
#        sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
#        list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
# sorted(iterable, cmp=None, key=None, reverse=False)
#    iterable -- 可迭代对象。
#    cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
#    key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
#    reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
log('sorted()')
st1 = [23, 5, 98, 14, 2, 69, 5]
print 'st1--before->', st1
print 'sorted(st1)--->', sorted(st1)
print 'sorted(st1, reverse=True)--->', sorted(st1, reverse=True)
print 'st1--after->', st1

print 'sorted(st1, cmp=lambda x, y: cmp(x, y))--->', sorted(st1, cmp=lambda x, y: cmp(x, y))
print 'sorted(st1, cmp=lambda x, y: cmp(x, y), reverse=True)--->', sorted(st1, cmp=lambda x, y: cmp(x, y), reverse=True)

st2 = {'a': 1, 'b': 5, 'c': 2}
print 'sorted(st2)--->', sorted(st2)  # 默认比较的key是字典key
print 'sorted(st2, key=lambda x: x)--->', sorted(st2, key=lambda x: x)
print 'sorted(st2, key=lambda x: st2[x])--->', sorted(st2, key=lambda x: st2[x])

# slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
# class slice(stop)
# class slice(start, stop[, step])
#    start -- 起始位置
#    stop -- 结束位置
#    step -- 间距
log('slice()')
sl = slice(5)  # 相当于 slice(None, 5, None)
print 'slice(5)--->', sl
arr = range(10)
print 'range(10)--->', arr
print 'arr[:5]--->', arr[:5]
print 'arr[sl]--->', arr[sl]
print 'arr[0::2]--->', arr[0::2]
print 'arr[slice(0, len(arr), 2)]--->', arr[slice(0, len(arr), 2)]

# next() 返回迭代器的下一个项目。
# next(iterator[, default])
#    iterator -- 可迭代对象   #【iter(obj)   obj:支持迭代的集合对象。】返回可迭代对象
#    default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，又没有下一个元素则会触发 StopIteration 异常。
# 返回对象帮助信息。
dictO = iter({'a': 9, 'b': 2, 'c': 96})
listO = range(10)
tupleO = tuple(listO)
xrangeO = xrange(10)

print next(dictO, None)
print next(dictO, None)
print next(dictO, None)
print next(dictO, None)
print next(dictO, None)
# print next(dictO)  #  StopIteration
print next(dictO, None)

# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
# set([iterable])
#    iterable -- 可迭代对象；
# 返回新的集合对象。
log('set()')
setO = {1, 22, 3, 3, 4, 5, 6, 4, 1, 2, 8, 5, 2, 9}
print setO

sa = {'a', 'b', 1, 3, 5, 'g'}
sc = {'b', 'q', '1', 'q', 5, 8}
print 'sc - sa --差集->', sc - sa
print 'sa - sc --差集->', sa - sc
print 'sa | sc --并集->', sa | sc
print 'sa & sc --交集->', sa & sc
