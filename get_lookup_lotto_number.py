#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
__author__ = 'https://github.com/password123456/'

import random
import numpy as np
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

time_now = time.strftime('%Y-%m-%d %H:%M:%S')

def computer_random():
    """컴퓨터가 1-45 사이 번호 6개를 뽑는다."""
    ok = False
    lotto_num_list = np.arange(1,45)

    while not ok:
        ci = np.random.choice(lotto_num_list,6,replace= False)
        #ci.sort()
        tmp = np .where(ci == 0)
        (m, )= tmp[0].shape
        if (m == 0):
            ok = True
    return ci

def user_random():
    print "============================="
    print "       로또 번호 조회기      "
    print "============================="
    print "[+] 시간: %s" % time_now
    print "[+] 1 에서 45중 임의의 번호 6 개를 입력해주세요:"
    ui = []
    while len(ui) < 6:
        print len(ui) + 1,
        try :
            i = input( "번째 번호: " )
            # check if i is unique and has a value from 1 to 50
            # and is an integer, otherwise don't append
            if (i not in ui) and (1 <= i <= 45) and type(i) == type (7):
                ui.append(i)
        except :
            print "[-] 범위안(1~45) 의 번호로 넣어주세요.!"
    return ui
def match_lists(list1 , list2):
    """컴퓨터 번호와 나의 번호를 대입한다"""
    set1 = set( list1)
    set2 = set( list2)
    set3 = set1.intersection(set2)
    return len(set3)

user_list = user_random()
print "[+] 입력한 번호는: %s" % user_list

match3 = 0
match4 = 0
match5 = 0
match6 = 0
# 컴퓨터는 아래 수만큰 랜덤 6개 숫자를 뽑는다.
tickets_sold = 8145060
print "[+] 시간: %s" % time_now
print "[+] %d 확률로 입력한 번호를 계산 중입니다.." % tickets_sold
for k in range(tickets_sold):
    comp_list = computer_random()
    # 2개를 비교해서 내번호가 컴퓨터가 뽑은 번호와 일치하는 번호의 개수를 구한다.
    matches = match_lists(comp_list, user_list)
    if matches == 3:
        match3 += 1
    elif matches == 4:
        match4 += 1
    elif matches == 5:
        match5 += 1
    elif matches == 6:
        match6 += 1

print "[+] %d 확률로 계산한 결과는 다음과 같습니다." % tickets_sold
print " [*] 내 번호가 컴퓨터가 뽑은 번호와 3 개의 번호가 맞는 경우(5등) = %d" % match3
print " [*] 내 번호가 컴퓨터가 뽑은 번호와 4 개의 번호가 맞는 경우(4등) = %d" % match4
print " [*] 내 번호가 컴퓨터가 뽑은 번호와 5 개의 번호가 맞는 경우(3등) = %d" % match5
print " [*] 내 번호가 컴퓨터가 뽑은 번호와 6 개의 번호가 맞는 경우(1등) = %d" % match6
print " [-] %s 끝 " % time_now
