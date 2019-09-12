#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
sys.path.append('..')  # 作用就是在单独用 python 运行该脚本的时候  可以找到引入的自定义模块；但是在test1根目录下 python ac\ac_first.py 会报错 没有该模块名
import page.model
import func
