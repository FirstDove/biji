#!/usr/bin/env python
# -*- coding: utf8 -*-

# basestring() 方法是 str 和 unicode 的超类（父类），也是抽象类，
# 因此不能被调用和实例化，但可以被用来判断一个对象是否为 str 或者 unicode 的实例，
# isinstance(obj, basestring) 等价于 isinstance(obj, (str, unicode))。

print isinstance(u'abc', basestring)


# execfile() 函数可以用来执行一个文件。
# execfile(filename[, globals[, locals]])
#    filename -- 文件名。
#    globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
#    locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
# execfile('../func.py')

# issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类。类似于isinstance  只是参数不一样罢了
# issubclass(class, classinfo)
#    class -- 类。
#    classinfo -- 类。
class A(object):
    a = 3
    pass


class B(A):
    b = 9
    pass


print(issubclass(B, A))

# print() 方法用于打印输出，最常见的一个函数。
# print 在 Python3.x 是一个函数，但在 Python2.x 版本不是一个函数，只是一个关键字。
# print(*objects, sep=' ', end='\n', file=sys.stdout)
#    objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
#    sep -- 用来间隔多个对象，默认值是一个空格。
#    end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
#    file -- 要写入的文件对象。
print ('hh', 'bb', 'cc')


# super() 函数是用于调用父类(超类)的一个方法。
# super 是用来解决多重继承问题的，
#    直接用类名调用父类方法在使用单继承的时候没问题，
#    但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
# MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
# super(type[, object-or-type])
#    type -- 类。
#    object-or-type -- 类，一般是 self

class OO(object):
    def qq(self, x):
        print x ** x
        pass

    pass


class PP(OO):
    def tt(self, n):
        print n * n
        pass

    def qt(self, m):
        super(PP, self).qq(m)
        pass

    def qq(self, x):
        print x + 3
        pass

    pass


class Cc(PP):
    def abc(self, n):
        super(Cc, self).qq(n)
        pass

    def adc(self, m):
        super(PP, self).qq(m)
        pass

    pass


b = PP()
b.tt(3)  # 9
b.qt(3)  # 27
b.qq(4)  # 7
print '=========='
cc = Cc()
cc.abc(6)  # 9
cc.adc(6)  # 46656

# bin() 返回一个整数 int 或者长整数 long int 的二进制表示(字符串)。
# bin(x)
#    x -- int 或者 long int 数字
binstr = bin(73)
print "binstr--->", binstr, type(binstr)

# file() 函数用于创建一个 file 对象，它有一个别名叫 open()，更形象一些，它们是内置函数。参数是以字符串的形式传递的。
# file(name[, mode[, buffering]])
#    name -- 文件名
#    mode -- 打开模式
#    buffering -- 0 表示不缓冲,如果为 1 表示进行行缓冲，大于 1 为缓冲区大小。

# iter() 函数用来生成迭代器。
# iter(object[, sentinel])
#    object -- 支持迭代的集合对象。
#    sentinel -- 如果传递了第二个参数，
#                   则参数 object 必须是一个可调用的对象（如，函数），
#                   此时，iter 创建了一个迭代器对象，
#                   每次调用这个迭代器对象的__next__()方法时，都会调用 object。
print "iter('abcdefg')--->", iter('abcdefg')
print "list(iter('abcdefg'))--->", list(iter('abcdefg'))

# Python 元组 tuple() 函数将可迭代对象转换为元组。
# tuple( seq )
#    seq -- 要转换为元组的可迭代对象。
print "tuple('abc')--->", tuple('abc')
print "tuple({'a':123,'b':456,'c':789})--->", tuple({'a': 123, 'b': 456, 'c': 789})


# list() 方法用于将可迭代对象转换为列表。
# 注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
# list( tup )
print "list({'a':123,'b':456,'c':789})--->", list({'a': 123, 'b': 456, 'c': 789})
print "list('abc')--->", list('abc')

# dict() 函数用于创建一个字典。
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
#    **kwargs -- 关键字
#    mapping -- 元素的容器。
#    iterable -- 可迭代对象。
fd = dict(a=123, b=456, c=789)    # 普通传参
td = dict(zip(['a', 'b', 'c'], [7, 8, 9]))  # 映射
thd = dict([('a', 6), ('b', 9)])  # 列表
print "dict(a=123, b=456, c=789)--->", fd
print "dict(zip(['a', 'b', 'c'], [7, 8, 9]))--->", td
print "dict([('a', 6), ('b', 9)])--->", thd

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
# zip 方法在 Python 2 和 Python 3 中的不同：
#                       在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。
# zip([iterable, ...])
#    iterable -- 一个或多个迭代器;
z = zip(['a', 'b', 'c'], [1, 2], ['x', 'y', 'z', 'p'])
print "zip(['a', 'b', 'c'], [1, 2], ['x', 'y', 'z', 'p'])--->", z
print "zip('abc', '12')--->", zip('abc', '12')
print "dict(zip('abc', '12'))--->", dict(zip('abc', '12'))


# property() 函数的作用是在新式类中返回属性值。并可以重新定义属性的get、set、del方法
# class property([fget[, fset[, fdel[, doc]]]])
#    fget -- 获取属性值的函数
#    fset -- 设置属性值的函数
#    fdel -- 删除属性值函数
#    doc -- 属性描述信息

class OP(object):
    def __init__(self):
        self.n = None
        pass

    def odel(self):
        del self.n
        pass

    def oget(self):
        return self.n

    def oset(self, val):
        self.n = val
        pass

    on = property(oget, oset, odel, 'fffffffff')
    pass


op = OP()
print op.n
op.on = 123
print "op.on--->", op.on
print "op.n--->", op.n


class OX(object):
    def __init__(self):
        self.kk = None
        pass

    @property  # 将 valreq() 方法转化成同名只读属性的 getter 方法。  同时声明valreq属性
    def valreq(self):
        print 456
        return self.kk

    @valreq.setter  # 函数名要与对象名一致
    def valreq(self, n):
        self.kk = n
        pass

    @valreq.getter  # 函数名要与对象名一致   覆盖 @property  后的方法
    def valreq(self):
        return self.kk

    @valreq.deleter  # 函数名要与对象名一致
    def valreq(self):
        del self.kk
        pass

    pass


ox = OX()
ox.kk = 123
# print ox.kk
# # print ox.w
print ox.valreq


# bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
# bool 是 int 的子类。
# class bool([x])
#    x -- 要进行转换的参数。
print "bool('a')--->", bool('a')
print "bool(0)--->", bool(0)
print "bool()--->", bool()
print "bool(1)--->", bool(1)

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。(注意: Pyhton2.7 返回列表，Python3.x 返回迭代器对象)
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# filter(function, iterable)
#    function -- 判断函数。
#    iterable -- 可迭代对象。

fl = filter(lambda x: x > 2, [2, 3, 4])   # 返回满足条件的列表项
print "filter(lambda x: x > 2, [2, 3, 4])--->", fl

# Python len() 方法返回对象（字符、列表、元组等）长度或项目个数。
# len( s )
#    s -- 对象。
print "len([])--->", len([])
print "len('abc')--->", len('abc')
print "len({'a': 123, 'b': 456})--->", len({'a': 123, 'b': 456})

# python range() 函数可创建一个整数列表，一般用在 for 循环中。
# range(start, stop[, step])
#    start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
#    stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
#    step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

range1 = list(range(6))
range2 = list(range(5, 10))
range3 = list(range(5, 20, 3))
print range1
print range2
print range3


