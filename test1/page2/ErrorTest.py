#!/usr/bin/env python
# -*- coding: utf8 -*-

try:
    fo = open('../filetest/1.py', 'w', 0)
    # fo.read()
    fo.close()
    b = {'a': 122300, None: 123}
    print b.s
except IOError:
    print '文件读取操作失败'
except NameError:
    print '未声明/初始化对象 (没有属性)'
except AttributeError:
    print '访问没有的属性错误'
except KeyError:
    print '访问没有的键'
else:
    print '文件读取操作成功'

try:
    fo = open('../filetest/1.py', 'w', 0)
    # fo.read()
    fo.close()
    b = {'a': 122300, None: 123}
    print b.s
except:
    print '只要报错就到这里来'
else:
    print '文件读取操作成功'

try:
    fo = open('../filetest/1.py', 'w', 0)
    # fo.read()
    fo.close()
    b = {'a': 122300, None: 123}
    print b.s
except (AttributeError, NameError, TypeError):
    print '类型，属性，名称 报错'
else:
    print '文件读取操作成功'

try:
    fo = open('../filetest/1.py', 'w', 0)
    # fo.read()
    fo.close()
    b = {'a': 122300, None: 123}
    # print b.s
except (AttributeError, NameError, TypeError):
    print '类型，属性，名称 报错2'
else:
    print '文件读取操作成功--finally'
finally:
    print '无论是成功还是报错导致失败，都会执行这个代码块'

try:
    fh = open("testfile", "w")
    try:
        fh.read()
        fh.write("这是一个测试文件，用于测试异常!!")
    except IOError, acd:  # 如果内部捕获了异常 就不会触发到外部except
        print '内部try--->', acd
    finally:
        print "关闭文件"
        fh.close()
except IOError:
    print "Error: 没有找到文件或读取文件失败"


def testError1(val):
    try:
        if val > 0:
            raise Exception('cuowu', 999)
        return int(val)  # else 没用了      this code is unreachable   并且 return 在finally之后执行
    except ValueError, Argument:
        print '123', Argument
    except Exception, ac:
        print '456--->', ac
    # else:
    #     print 'aaaa'
    finally:
        print 'zong'


testError1('aaa')
print testError1(-1)

fh = open("testfile", "w")
class Networkerror(AttributeError):
    def __init__(self, arg):
        self.q = arg


try:
    raise Networkerror('abcdefg')
except Networkerror, ee:
    print 'aa--->', ee.q
