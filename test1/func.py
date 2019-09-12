#!/usr/bin/env python
# -*- coding: utf8 -*-

import ll
import sys
# sys.path.append("/")

import page.model as model
yy = [1, 5, 9]
model.clearList(yy)
print yy

def test():
    """abc"""
    print 'da'


test()

def ab(d, k):
    a = k
    print d, '---', a
    if a > d:
        return a
    elif a == d:
        return d
    else:
        return a-d


ab(k=5, d=3)
def printa(k,*b, **args):
    print k
    print b
    print args


printa(1, **{'qq': 123})
df = 2
kkk3 = lambda x, y: str(x+y+df) if x>y else y
print kkk3(5, 3)

kkk4 = lambda: test()
kkk4()

ad = {'qq': 123}




