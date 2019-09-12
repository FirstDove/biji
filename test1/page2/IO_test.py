#!/usr/bin/env python
# -*- coding: utf8 -*-

# str = raw_input('请输入：')
# print str

# a = input('请输入==>')
# print a

import os

# open(name[, mode, buffering])
# name:  是一个包含了你要访问的文件名称的字符串值
# mode:  文件打开模式     默认为只读
# buffering:  0，1，负数， 大于1
#       0：  不会有寄存
#       1：  会寄存行
#      负数： 寄存区的缓冲大小为系统设置
#      大于1：寄存区的缓冲大小为该值
fo = open('../filetest/1.py', 'a+', 0)
# fo.write('\nabc')
# print fo.name
# print fo.closed
# print fo.mode
# print fo.softspace
# print fo.read()
# print fo.tell()

# 重新定位下一次读取的开始位置
# 第二个参数 0：文件的开头作为移动字节的参考位置；
#                   1：使用当前的位置作为参考位置；
#                   2：文件的末尾将作为参考位置。
fo.seek(4, 0)
print fo.tell()  # 字符下标0开始
print fo.readline(1)  # 只读首行  参数是读几个字符
print fo.tell()
print fo.readlines()  # 从上一次读取位置+1 的位置开始读取（包括该位置的字符）  返回一个列表（以换行符来作为分隔）
print fo
assert 'hh'
print 33
fo.close()
qq = None
print qq
if 33 > 22:
    print 'big'
