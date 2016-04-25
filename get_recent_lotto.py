#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
__author__ = 'https://github.com/password123456/'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import urllib
import urllib2
import json
import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_recent_lotto():

    url = 'http://www.nlotto.co.kr/common.do?method=getLottoNumber'

    try:
        r = requests.get(url)
        data = json.loads(r.text)
    except Exception, e:
        print '%s[-] Exception::%s%s' % (bcolors.WARNING, e, bcolors.ENDC)
        sys.exit(0)
    else:
        r.close()

    drwNoDate = data['drwNoDate']
    drwNo = data['drwNo']
    firstWinamnt = data['firstWinamnt']
    drwtNo1 = data['drwtNo1']
    drwtNo2 = data['drwtNo2']
    drwtNo3 = data['drwtNo3']
    drwtNo4 = data['drwtNo4']
    drwtNo5 = data['drwtNo5']
    drwtNo6 = data['drwtNo6']
    bnusNo = data['bnusNo']

    # 당첨금 자리수 변환
    firstWinamnt = format(firstWinamnt, ',')

    content = '** 최근 로또 조회 **\n'
    content = content + ' [+] 로또 : http://www.nlotto.co.kr\n [+] 추첨일자: %s\n [+] 회차: %d 회\n [+] 당첨번호: %d %d %d %d %d %d\n [+] 보너스: %d \n [*] 당첨금: %s 원\n' % (drwNoDate, drwNo, drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6, bnusNo, firstWinamnt )
    #print content
    return content

content = get_recent_lotto()

def main():

    get_recent_lotto()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception, e:
        print '%s[-] Exception::%s%s' % (bcolors.WARNING, e, bcolors.ENDC)
