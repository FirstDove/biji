#!/usr/bin/env python
# -*- coding: utf8 -*-

a = [1, 3, 5, 7, 9]
b = {
    'a': 1,
    'b': 1,
    'c': 1,
    'd': 1,
}
for item in a:
    a.remove(item)

print a
print '======================='

for item in list(b.keys()):
    print item
    del b[str(item)]

print b