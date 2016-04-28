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
import dateutil.relativedelta as REL

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
    print "       로또 번호 생성기      "
    print "============================="
    print "[+] 시작시간: %s" % time_now
    print "[+] 번호생성: 1~45 중 임의의 번호 6 개를 만듭니다."

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
    global user_list
    # 사용자가 6개의 번호를 뽑는다.
    user_list = user_random()
    print "[+] 생성번호: %s" % user_list
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
    print "[+] 번호분석: 1/%d 개의 난수를 생성하여 생성된 번호와 일치할 확률을 계산" % tickets_sold

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

def get_next_saturday():
    today = datetime.date.today()
    rd = REL.relativedelta(days=1, weekday=REL.SA)
    next_saturday = today + rd
    return next_saturday

def read_file(saved_lotto_file):
    f = open(saved_lotto_file, 'r')
    lines = f.readlines()
    data = ''
    line_count = 0
    for line in lines:
        line_count += 1
        data = data + '%s' % line
    f.close()
    return data,line_count

def delete_file(saved_lotto_file):
    import os
    if os.path.isfile(saved_lotto_file):
        os.remove(saved_lotto_file)
    else:    
        print("Error: %s file not found" % saved_lotto_file)

def main():
    saved_lotto_file = './lotto_numbers.txt'
    count = 2
    games = 0

    while True:
        calculate()
        print "[+] 번호선택: 생성번호가 컴퓨터가 생성한 번호와 1개 이상 같을 경우 선택함"
        print "[+] 분석결과"
        print "----------------------------"
        print " 1. 5등/3 개 번호일치: %d 번" % match3
        print " 2. 4등/4 개 번호일치: %d 번" % match4
        print " 3. 3등/5 개 번호일치: %d 번" % match5
        print " 4. 1등/모두 일치: %d 번" % match6
        print "----------------------------"
        print ">>>>>>>>>>"
        if (match6 >= count):
            games += 1
            print "[+] 생성 번호: %s" % user_list
            print "[+] 6 개 번호가 모두 일치 하는 경우가 %d 번 탐지 / 이 번호 저장함." % (match6)
            print "[+] 총5 게임을 진행합니다. 현재는 %d 게임째 입니다." % games

            f = open(saved_lotto_file, 'a')
            f.write('자 동 %s\n' % (user_list))
            f.close()
        else:
            print " [+] 맞는 조건이 없어 처음부터 다시 번호를 뽑습니다."
            print
            continue

        if games == 5:
            print "[+] %d 게임이 완료되어 추첨을 종료합니다." % games
            print "[+] 추첨된 번호는 $YOUR API 로 전송합니다."

            next_saturday = get_next_saturday()
            read_lotto_data, read_lotto_data_line_count = read_file(saved_lotto_file)

            game_price = 1000
            total_price = game_price * read_lotto_data_line_count

            contents = '\
** 언제나 좋아요 로또 **\n\n\
「절반의 행운, 절반의 기부\n\
\t\t나눔 Lotto 6/45\n\
추 첨 일 : %s (토)\n\
-----------------------------------\n\
%s\
-----------------------------------\n\
총 %d 게임\n\
금액 %d원\n\
>> 걸리면 반띵알지?' % (next_saturday,read_lotto_data,read_lotto_data_line_count,total_price)
            print
            print ">>>>>> 메시지 시작 <<<<<<<"
            print
            print contents
            print
            print ">>>>>> 메시지 끝  <<<<<<<"
            try:
                # send contents your SMS, API
                # to here

            except Exception, e:
                print '%s[-] Exception::%s%s' % (bcolors.WARNING, e, bcolors.ENDC)
                pass
            else:
                delete_file(saved_lotto_file)
                break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception, e:
        print '%s[-] Exception::%s%s' % (bcolors.WARNING, e, bcolors.ENDC)
