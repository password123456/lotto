#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
__author__ = 'https://github.com/password123456/'

import random
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import urllib
import urllib2
import json
import datetime
import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def computer_random():
    """let the computer create a list of 6 unique random integers from 1 to 50"""
    ok = False
    lotto_num_list = np.arange(1,45)
    while not ok:
        ci = np.random.choice(lotto_num_list,6,replace=False)
        tmp = np.where(ci == 0)
        (m, )= tmp[0].shape
        if(m == 0):
            ok = True
    return ci

def user_random():
    time_now = time.strftime('%Y-%m-%d %H:%M:%S')
    print "============================="
    print "       로또 번호 조회기      "
    print "============================="
    print "[+] 시작: %s" % time_now
    print "[+] 조건: 1~45 중 임의의 번호 6 개를 만듭니다."

    ok = False
    lotto_num_list = np.arange(1,45)
    while not ok:
        ui = np.random.choice(lotto_num_list,6,replace=False)
        tmp = np.where(ui == 0)
        (m, )= tmp[0].shape
        if(m == 0):
            ok = True
    return ui

def match_lists(list1 , list2):
    """to find the number of matching items in each list use sets"""
    set1 = set(list1)
    set2 = set(list2)
    set3 = set1.intersection(set2)
    #print '컴퓨터번호-> %s | 내 번호-> %s | 일치번호 개수 %d' % (set1,set2,len(set3))
    return len(set3)

def calculate():
    # 사용자가 6개의 번호를 뽑는다.
    user_list = user_random()
    print "[+] 결과: %s" % user_list
    global match3
    global match4
    global match5
    global match6
    match3 = 0
    match4 = 0
    match5 = 0
    match6 = 0

    # computer는 아래의 숫자만큼 번호를 다시 뽑는다.
    tickets_sold = 8145060
    print "[+] 계산: 1/%d 개의 난수를 생성하여 생성된 번호와 일치할 확률을 계산합니다." % tickets_sold

  for k in range(tickets_sold):
	    comp_list = computer_random()
      # 뽑은번호를 서로 비교한다
	    matches = match_lists(comp_list, user_list)
	    if matches == 3:
	        match3 += 1
	    elif matches == 4:
	        match4 += 1
	    elif matches == 5:
	        match5 += 1
	    elif matches == 6:
	        match6 += 1

def main():
    count = 3
    while True:
        calculate()
        print "[+] 분석"
        print " - 5등/3 개 번호일치: %d 번" % match3
        print " - 4등/4 개 번호일치: %d 번" % match4
        print " - 3등/5 개 번호일치: %d 번" % match5
        print " - 1등/모두 일치: %d 번" % match6
        if (match6 >= count):
            print "[+] 6 개 번호가 일치하는 번호가 %d 번 탐지 되었습니다." % (match6)
            print "[-] 추첨을 종료합니다."
            print "[-] 걸리면 반띵 알지?"
            break
        else:
            print
            print " --> 맞는 조건이 없어 처음부터 다시 번호를 뽑습니다."
            print
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception, e:
        print '%s[-] Exception::%s%s' % (bcolors.WARNING, e, bcolors.ENDC)
