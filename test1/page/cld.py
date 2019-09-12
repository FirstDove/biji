#!/usr/bin/env python
# -*- coding: utf8 -*-

import calendar
# import sys
# sys.path.append('..')
import ll


c = calendar.calendar(2019, 2, 1, 10)
# print c
sfw = calendar.setfirstweekday(3)
f = calendar.firstweekday()
print 'calendar.setfirstweekday()--->', sfw
print 'calendar.firstweekday()--->', f

print 'calendar.weekday()--->', calendar.weekday(2019, 8, 21)  # 0---星期一
