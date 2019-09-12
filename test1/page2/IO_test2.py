#!/usr/bin/env python
# -*- coding: utf8 -*-

fo = open('./testfile', 'r+', 0)  # x, t, +, b 报错
print fo.next()
print fo.next()
print fo.next()
print fo.next()
print fo.tell()
fo.seek(0, 0)
print fo.readlines(1)
fo.seek(0, 0)
print fo.readline(6)
fo.seek(0, 0)
# print fo.truncate(13)  # 截取内容  并 write()
# fo.writelines(['abc\n', 'efg\n', 'qqq\n', 'ccc\n', 'ooo'])  # 相当于开启了insert模式
# fo.write('1\n')  # 相当于开启了insert模式  一个换行符就相当于2个字符
fo.close()


with open('./testfile', 'r+', 0) as ff:  # 类似于 try...finally   好处是不用调用 close() 关闭文件
    print ff.read()
    print ff.closed

print ff.closed
