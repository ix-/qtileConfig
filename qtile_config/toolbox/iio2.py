#!/usr/bin/env python2
'''check if we have a connection '''

import urllib2
import time


def isItOnline(reference):
    ''' return True if reference is reachable, else return False'''
    try:
        urllib2.urlopen(reference, timeout=1)
        return True
    except urllib2.URLError:
        return False


def waitForConnection(reference, sleeptime=1, times=10):
    '''wait for a connection to succeed, then return true'''
    for N in range(times):
        if isItOnline(reference):
            return True
        else:
            time.sleep(sleeptime)
    else:
        return False
