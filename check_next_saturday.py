#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
__author__ = 'https://github.com/password123456/'

# http://dateutil.readthedocs.io/en/stable/relativedelta.html

import datetime as DT
import dateutil.relativedelta as REL
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

today = DT.date.today()
print '오늘은 %s 입니다.' % today

rd = REL.relativedelta(days=1, weekday=REL.SA)
next_saturday = today + rd

print '돌아오는 토요일은 %s 입니다.' % next_saturday
