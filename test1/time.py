#!/usr/bin/env python
# -*- coding: utf8 -*-

import time
import calendar

a = time.time()
b = time.localtime(a)
print a
print b
print b[0]
print b.tm_year

c = time.asctime(b)
print c

# class AssignValue(object):
#     def __init__(self, value):
#         # print self, value
#         self.value = value
# my_value = AssignValue(6)
# print my_value
# print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

d = time.strftime('%Y-%m-%d %H:%M:%S', b)
print d

print calendar.month(2019, 2)
print 'time.clock()', time.clock()
print 'time.altzone', time.altzone  # 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
print 'time.timezone', time.timezone  # 属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。
print 'time.tzname', time.tzname  # 属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。
print 'time.asctime()', time.asctime()
timeList = [2018, 5, 27, 1, 5, 27, 6, 147, -1]
print 'time.asctime()', time.asctime(timeList)
print 'time.ctime()', time.ctime()
p = time.ctime(1566551994.5)
print 'time.ctime(sec)', p, type (p)
print 'calendar.timegm()', calendar.timegm([2019, 3, 10, 0, 0, 0, 0, 0, 0])
print 'time.gmtime()', time.gmtime(a)
print 'time.mktime', time.mktime(timeList)
print 'time.sleep()', time.sleep(1)
print 'time.localtime()', time.localtime(a)
print 'time.time()', time.time()  # 返回当前时区的时间戳
struct_time = time.strptime("30 Nov 00", "%d %b %y")
print "time.strptime()---返回的元组: ", struct_time

# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身
ta = time.localtime()
t = time.strftime('%Y-%m-%d %H:%M:%S %p %A %B %W %X %U', ta)
tsmall = time.strftime('%Y-%m-%d %I:%M:%S %p %a %b %w %x', ta)  # 0---星期日
tcjz = time.strftime('%c  %j   %z   %%', ta)
print ta
print ta[6]  # 0---星期一
print "time.strftime()---返回指定格式时间: ", t
print "time.strftime()---返回指定格式时间small: ", tsmall
print "time.strftime()---返回指定格式时间tcjz: ", tcjz

# 系统不支持
# print 'time.tzset', time.tzset()  # 根据环境变量TZ重新初始化时间相关设置。
# os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
# time.tzset()
# print 'time.tzset', time.strftime('%X %x %Z')
#
# os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
# time.tzset()
# print 'time.tzset',  time.strftime('%X %x %Z')

f = "time.altzone %d ,%s"
q = f % (time.altzone, 'aaa')
print q
print f

print '============================'
kkk = time.mktime([2018, 9, 30, 0, 0, 0, 0, 0, 0])
print 'kkk--->', kkk
ggg = time.localtime(kkk)
print 'ggg--->', ggg
print 'ggg--->', type (ggg)