#!/usr/bin/env python
# -*- coding: utf8 -*-

def clearList(list):
    tp = type(list)
    print type(tp)
    if tp != type([]):
        print 'haha'
        return
    else:
        print 'baibai'
    print 3
    for item in list[:]:
        print item
        list.remove(item)


