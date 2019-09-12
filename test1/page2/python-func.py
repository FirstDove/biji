#!/usr/bin/env python
# -*- coding: utf8 -*-

a = -2.5
print 'abs() --->', abs(a)  # 返回一个值的绝对值，不改变原始值
# print abs('a')  # TypeError: bad operand type for abs(): 'str'

print 'abs(9, 2.0) --->', divmod(9, 2.0)  # 把除数和被除数的运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
print 'abs(9, 2) --->', divmod(9, 2)  # 把除数和被除数的运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
print 9 / 2.0

# b = input('请输入--->')  # 相当于  eval(raw_input())
# c = raw_input('raw_input--->')
# print "input('请输入--->') ", b
# print 'eval(raw_input())--->', eval(c)

# open() 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。
fo = open('./a', 'r+')
print fo.read()
fo.close()


class Ad():
    @staticmethod  # 声明该方法是静态方法  可以 Ad.acd()  也可以 Ad().acd()
    def acd():
        print 'static'

    def abc(self):
        print 'no static'


Ad().acd()
Ad.acd()
Ad().abc()

# all(iterable)   iterable: 可迭代对象   列表、元祖、字典
# 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
# 元素除了是 0、空、None、False 外都算 True。
# 返回值  True  or  False
print "all([])--->", all([])
print "all(())--->", all(())
print "all({})--->", all({})
print "all('')--->", all('')
print "all([1,2,3])--->", all([1, 2, 3])
print "all([1,2,3,0])--->", all([1, 2, 3, 0])
print "all([1,2,3,None])--->", all([1, 2, 3, None])
print "all([1,2,3,''])--->", all([1, 2, 3, ''])
print "all({'a': 123})--->", all({'a': 123})
print "all({'a': 123, False: 222})--->", all({'a': 123, False: 222})

# any(iterable) 函数用于判断给定的可迭代参数 iterable 的元素项是否全部为== False，如果有一个为 True，则返回 True，否则返回 False。
# 元素除了是 0、空、FALSE 外都算 TRUE。
print "any([])--->", any([])
print "any(())--->", any(())
print "any({})--->", any({})
print "any('')--->", any('')
print "any([0,False,None,''])--->", any([0, False, None, ''])
print "any([1,2,3,0])--->", any([1, 2, 3, 0])
print "any([1,2,3,None])--->", any([1, 2, 3, None])
print "any([1,2,3,''])--->", any([1, 2, 3, ''])
print "any({'a': 123})--->", any({'a': 123})
print "any({'a': 123, False: 222})--->", any({'a': 123, False: 222})

# enumerate(sequence, [start=0]) 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
# 返回一个enumerate对象    <enumerate object at 0x00000000024215A0>
# start   标识可迭代对象的元素项的原始下标位置+start   并不是从可迭代对象的第几个下标位置开始运算
print "list(enumerate(['a', 'ad', 'af', 'ag', 'ah', 'ak']))--->", list(enumerate(['a', 'ad', 'af', 'ag', 'ah', 'ak']))
print "list(enumerate(['a', 'ad', 'af', 'ag', 'ah', 'ak'], 2))--->", list(
    enumerate(['a', 'ad', 'af', 'ag', 'ah', 'ak'], 2))

# int(x, base=10) 函数用于将一个字符串或数字转换为整型。（转换成10进制的整数）
#       x -- 字符串或数字。
#       base -- 进制数，默认十进制。标明转换对象 x 的进制类型
print "int(2.5)--->", int(2.5)
print "int('12')--->", int('12')
print "int()--->", int()
print "int('0110', 2)--->", int('0110', 2)

# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
# 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
# 如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
# chr(x)   返回x对应的ASCII字符串    x(整数)         例子： chr(97)  --->  'a'
# unichr(x)   返回x对应的Unicode对象    x(整数)         例子： chr(97)  --->  u'a'
# ord(str)   返回str字符（长度为1的字符串）对应的数字        例子： ord('a')  --->  97   /   ord(u'a')  --->  97
