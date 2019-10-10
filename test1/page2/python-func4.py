#!/usr/bin/env python
# -*- coding: utf8 -*-

import rexec

def log(x):
    print '============={0}==========='.format(x)
    pass


# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# map(function, iterable, ...)
#    function -- 函数
#    iterable -- 一个或多个序列
d = lambda x, y: x**y
a = map(d, [1, 2, 3], [4, 5, 6])
# b = map(d, [1, 2, 3], [4, 5, 6, 7], [8, 9])  # TypeError: <lambda>() takes exactly 2 arguments (3 given)
print a

# repr() 函数将对象转化为供解释器读取的形式。
# repr(object)
#    object -- 对象。
# 返回一个对象的 string 格式。
log('repr()')
rp = repr([])
print rp
print type(rp)


# xrange() 函数用法与 range 完全相同，所不同的是生成的不是一个数组，而是一个生成器。
# xrange(stop)
# xrange(start, stop[, step])
#           start: 计数从 start 开始。默认是从 0 开始。例如 xrange(5) 等价于 xrange(0， 5)
#           stop: 计数到 stop 结束，但不包括 stop。例如：xrange(0， 5) 是 [0, 1, 2, 3, 4] 没有 5
#           step：步长，默认为1。例如：xrange(0， 5) 等价于 xrange(0, 5, 1)
# 注： 在python 2中，range返回一个list，xrange放回生成器；python 3中，range放回一个生成器，xrange被移除出内置函数
log('xrange()')
print xrange(5), list(xrange(5))
print xrange(0, 5), list(xrange(0, 5))
print xrange(5, 20, 3), list(xrange(5, 20, 3))


# cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
# cmp( x, y )
#    x -- 数值表达式。
#    y -- 数值表达式。
log('cmp()')
print cmp(4, 6)
print cmp('4', 6)
print cmp('a', 'a')

# globals() 函数会以字典类型返回当前位置的全部全局变量。
# globals()
log('globals()')
print globals()
print locals()
print vars()
print dir()

# max() 方法返回给定参数的最大值，参数可以为序列。
# max( x, y, z, .... )
#    x -- 数值表达式。
#    y -- 数值表达式。
#    z -- 数值表达式。
log('max()')
m = ([1, 2, 3], [4, 5, 6], [4, 5, 6, 0])
print 'max(1, 2, 3)--->', max(1, 2, 3)
print 'max([1, 2, 3])--->', max([1, 2, 3])
print 'max([1, 2, 3], [4, 5, 6], [4, 7, 1])--->', max([1, 2, 3], [4, 5, 6], [4, 7, 1])
print 'max([1, 2, 3], [4, 5, 6, 0], [4, 7, 1])--->', max([1, 2, 3], [4, 5, 6, 0], [4, 7, 1])
print 'max([1, 2, 3], [4, 5, 6], [4, 5, 6, 0])--->', max([1, 2, 3], [4, 5, 6], [4, 5, 6, 0])
print 'max(m)--->', max(m)
print 'max(*m)--->', max(*m)
print "max({1: 2, 2: 3, 3: 'bb', 4: 'aa', 5: 0})--->", max({1: 2, 2: 3, 3: 'bb', 4: 'aa', 5: 0})
print "max({1: 2, 2: 3, 3: 'bb', 4: 'aa'})--->", max({1: 2, 2: 3, 3: 'bb', 4: 'aa'})

# min() 方法返回给定参数的最小值，参数可以为序列。
# min( x, y, z, .... )
#    x -- 数值表达式。
#    y -- 数值表达式。
#    z -- 数值表达式。
print 'min(1, 2, 3)--->', min(1, 2, 3)
print 'min([1, 2, 3])--->', min([1, 2, 3])
print 'min([1, 2, 3], [4, 5, 6], [4, 7, 1])--->', min([1, 2, 3], [4, 5, 6], [4, 7, 1])
print 'min([1, 2, 3], [4, 5, 6, 0], [4, 7, 1])--->', min([1, 2, 3], [4, 5, 6, 0], [4, 7, 1])
print 'min([1, 2, 3], [4, 5, 6], [4, 5, 6, 0])--->', min([1, 2, 3], [4, 5, 6], [4, 5, 6, 0])
print 'min(m)--->', min(m)
print 'min(*m)--->', min(*m)
print "min({1: 2, 2: 3, 3: 'bb', 4: 'aa', 5: 0})--->", min({1: 2, 2: 3, 3: 'bb', 4: 'aa', 5: 0})
print "min({1: 2, 2: 3, 3: 'bb', 4: 'aa'})--->", min({1: 2, 2: 3, 3: 'bb', 4: 'aa'})

# compile() 函数将一个字符串编译为字节代码。
# compile(source, filename, mode[, flags[, dont_inherit]])
#    source    -- 字符串或者AST（Abstract Syntax Trees）对象。。
#    filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
#    mode     -- 指定编译代码的种类。可以指定为 exec, eval, single。
#    flags       -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
#    flags和dont_inherit是用来控制编译源码时的标志
# 返回表达式执行结果。
log('compile()')
execStr = 'for i in range(5): print i'
comExec = compile(execStr, '', 'exec')
# comExec2 = compile(execStr, '', 'eval')  # 报错  SyntaxError: invalid syntax
print "comExec--->", comExec
exec comExec
evalStr = '3*4+5'
comEval = compile(evalStr, '', 'eval')
comEval2 = compile(evalStr, '', 'exec')
print 'comEval--->', comEval
print 'comEval2--->', comEval2
print 'eval(comEval)--->', eval(comEval)
print 'eval(comEval2)--->', eval(comEval2)

# memoryview() 函数返回给定参数的内存查看对象(Momory view)。
# 所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问。
# memoryview(obj)
#    obj -- 对象  # python3 只支持bytes和bytearray 对象
# 返回元组列表。
log('memoryview()')
qq = 'abcd'
memory = memoryview(qq)
print memory

# round() 方法返回浮点数x的四舍五入值。
# round( x [, n]  )
#    x -- 数值表达式。  需要四舍五入的数值   >5才进一位
#    n -- 数值表达式。  需要保留的小数位数   默认值 0 ，保留小数最大位数为原数值小数的位数
log('round()')
rnum = 4568.5623
print 'round(rnum)--->', round(rnum)
print 'round(rnum, 0)--->', round(rnum, 0)
print 'round(rnum, 3)--->', round(rnum, 3)
print 'round(rnum, 5)--->', round(rnum, 5)

# __import__() 函数用于动态加载类和函数 。
# 如果一个模块经常变化就可以使用 __import__() 来动态载入。
# __import__(name[, globals[, locals[, fromlist[, level]]]])
#     name -- 模块名
# 返回元组列表。
log('__import__()')
print 'import--return', __import__('IO_test'), type(__import__('IO_test'))

# complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
# complex([real[, imag]])
#    real -- int, long, float或字符串；
#    imag -- int, long, float；
# 返回一个复数。
log('complex()')
comp = complex(1)
comp1 = complex(1, 2)
comp2 = complex('3')
# comp3 = complex('c')  # ValueError: complex() arg is a malformed string
comp4 = complex()
print "complex(1)--->", comp
print "complex(1, 2)--->", comp1, type(comp1)
print "complex('3')--->", comp2, type(comp2)
# print "complex('c')--->", comp3
print "complex()--->", comp4
print "complex(1 + 2j)--->", complex(1 + 2j)


log('iterDef()')
def iterDef():
    print 3
    pass


it = iter(iterDef, 'abc')
print it
# for i in it:
#     pass
print it.next()




























































