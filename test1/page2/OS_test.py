#!/usr/bin/env python
# -*- coding: utf8 -*-


import os, stat
#  access(path, mode)  检验权限模式
#  path: 要用来检测是否有访问权限的路径
#  mode:
#           os.F_OK     测试path是否存在
#           os.R_OK     测试path是否可读
#           os.W_OK    测试path是否可写
#           os.X_OK     测试path是否可执行
access = os.access('../filetest/', os.X_OK)
print 'access--->',  access

print '当前目录--->', os.getcwd()
# os.chdir(path) 方法用于改变当前工作目录到指定的路径。 允许返回True，否则False
os.chdir('../filetest')
fo = open('1.py', 'r')
print fo.read()
fo.close()
print '改变之后的目录--->', os.getcwd()

# os.chflags(path, flags)
#    path: 文件名路径或目录路径。
#    flags:  可以是以下值
#              stat.UF_NODUMP     非转储文件
#              stat.UF_IMMUTABLE      文件是只读的
#              stat.UF_APPEND    文件只能追加内容
#              stat.UF_NOUNLINK     文件不可删除
#              stat.UF_OPAQUE     目录不透明，需要通过联合堆栈查看
#
#              stat.SF_IMMUTABLE     文件是只读的（超级用户可设）
#              stat.SF_APPEND    文件只能追加内容（超级用户可设）
#              stat.SF_NOUNLINK      文件不可删除（超级用户可设）
#              stat.SF_ARCHIVED     可存档文件（超级用户可设）
#              stat.SF_SNAPSHOT    快照文件（超级用户可设）

# os.chflags('./a.txt', stat.UF_IMMUTABLE)  # AttributeError: 'module' object has no attribute 'chflags'


