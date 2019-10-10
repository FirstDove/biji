#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

print '---------------------'
print sys.getdefaultencoding()
print '---------------------'

# bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
# class bytearray([source[, encoding[, errors]]])
#    如果 source 为整数，则返回一个长度为 source 的初始化数组；
#    如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；默认是 'ASCII'(python2);python3没有默认值
#    如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
#    如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
#    如果没有输入任何参数，默认就是初始化数组为0个元素。
b = bytearray('adfaaadsads')
print b
print b[0]
print b[1]
print type(b)

# float() 函数用于将整数和字符串转换成浮点数。
# float([x])
#    x -- 整数或字符串
f1 = float()
f2 = float(123)
f3 = float('111')
f4 = float('156.12')
print "float()--->", f1
print "float(123)--->", f2
print "float('111')--->", f3
print "float('156.12')--->", f4

'''callable() 函数用于检查一个对象是否是可调用的。
如果返回 True，object 仍然可能调用失败；
但如果返回 False，调用对象 object 绝对不会成功。'''
# 对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。
# callable(object)
ca = 123
cb = 'abc'


def cc():
    pass


cd = lambda x: x ** x


class A(object):
    def oo(self):
        print 'ofo'
        pass

    @staticmethod
    def ob():
        print 'ob'
        pass

    pass


class B(object):
    def __call__(self, *args, **kwargs):
        pass

    pass


cf = A()
cg = B()

print '数字--->', callable(ca)
print '字符串--->', callable(cb)
print '函数--->', callable(cc)
print 'lambda--->', callable(cd)
print '未实现__call__方法的类的实例的方法--->', callable(cf.oo)
print '未实现__call__方法的类的方法--->', callable(A.oo)
print '未实现__call__方法的类--->', callable(A)
print '实现了__call__方法的类--->', callable(cd)
print '实现了__call__方法的类的实例--->', callable(cf)
print '未实现__call__方法的类的实例--->', callable(cg)


def kkk(*c):
    print c
    pass


kk = [1, 2, 3]
kkk()
kkk(kk)
kkk(*kk)

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))
print("网站名：{0}, 地址 {1}".format(*my_list))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
print("网站名：{0[name]}, 地址 {0[url]}".format(site))

# locals() 函数会以字典类型返回当前位置的全部局部变量。
# 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
print "locals()--->", locals()

# reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
#       用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
#       得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
# reduce(function, iterable[, initializer])
#    function -- 函数，有两个参数
#    iterable -- 可迭代对象
#    initializer -- 可选，初始参数
print 'reduce=============='
aq = [1, 5, 9]
aw = reduce(lambda x, y: x*y, aq)
aw2 = reduce(lambda x, y: x*y, aq, 5)
print aw
print aw2

# frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
# frozenset([iterable])
#    iterable -- 可迭代的对象，比如列表、字典、元组等等。
beforeIt = [1, 2, 3]
afterIt = frozenset(beforeIt)
print "id(beforeIt)--->", id(beforeIt)
print "id(afterIt)--->", id(afterIt)
print "beforeIt--->", beforeIt
print "afterIt--->", afterIt
beforeIt.append(4)
print '------------------------'
print "beforeIt--->", beforeIt
print "afterIt--->", afterIt, type(afterIt)
print "frozenset('abc')--->", frozenset('abc')


# long() 函数将数字或字符串转换为一个长整型。(十进制的值)
# class long(x, base=10)
#    x -- 字符串或数字。
#    base -- 可选，进制数，默认十进制。
l1 = long('010101', base=2)
l2 = long('010101', base=10)
print '-------------------------'
print l1, type(l1)
print l2

# reload() 用于重新载入之前载入的模块。
# reload 会重新加载已加载的模块，但原来已经使用的实例还是会使用旧的模块，而新生产的实例会使用新的模块；
# reload 后还是用原来的内存地址；
# reload 不支持 from ××× import ××× 格式的模块进行重新加载。
reload(sys)  # 如果不加入这行代码，那么 模块调用一些方法会失败
sys.setdefaultencoding('utf-8')
print '---------------------'
print sys.getdefaultencoding()
print '---------------------'

# vars() 函数返回对象object的属性和属性值的字典对象。
# vars([object])
#    object -- 对象
# 返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()。
print "vars()--->", vars()
print "vars(str)--->", vars(str)
# print "vars(3)--->", vars(3)  # TypeError: vars() argument must have __dict__ attribute

# classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
# 但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
# 返回函数的类方法。
print '---------classmethod------------'
class A(object):
    # 属性默认为类属性（可以给直接被类本身调用）
    bar = 1

    # 实例化方法（必须实例化类之后才能被调用）
    def func1(self):  # self : 表示类的实例化
        print 'self', self, type(self)
        print ('func1')
        pass

    # 类方法（不需要实例化类就可以被类本身调用）
    @classmethod
    def func2(cls):   # cls : 表示没有被实例化的类本身
        print ('func2')
        print (cls)
        print (cls.bar)
        cls().func1()  # 调用 foo 方法

    # 静态方法（不需要实例化类就可以被类本身调用）
    @staticmethod
    def func3():
        pass
    pass


A.func2()

# getattr() 函数用于返回一个对象属性值。
# getattr(object, name[, default])
#    object -- 对象。
#    name -- 字符串，对象属性。
#    default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。
print '---------getattr------------'
print getattr(A, 'func2')
print getattr(A, 'bar')
print getattr(A, 'func4', 'ccc')

# hasattr() 函数用于判断对象是否包含对应的属性。
# hasattr(object, name)
#    object -- 对象。
#    name -- 字符串，属性名。
# 如果对象有该属性返回 True，否则返回 False。
print '---------hasattr------------'
print hasattr(A, 'func2')
print hasattr(A, 'bar')
print hasattr(A, 'func4')

# delattr 函数用于删除属性。
# delattr(x, 'foobar') 相等于 del x.foobar。
# delattr(object, name)
#    object -- 对象。
#    name -- 必须是对象的属性。
print '---------delattr------------'
print 'vars(A)--->', vars(A)
print delattr(A, 'func2')
print delattr(A, 'bar')
# print delattr(A, 'func4')  # AttributeError: func4
print 'vars(A)--->', vars(A)

# setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的。
# setattr(object, name, value)
#    object -- 对象。
#    name -- 字符串，对象属性。
#    value -- 属性值。
print '---------setattr------------'
print 'vars(A)--->', vars(A)
setattr(A, 'GG', 123)
print 'vars(A)--->', vars(A)



