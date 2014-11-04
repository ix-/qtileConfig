#!/usr/bin/env python2
'''handles  processes'''

import subprocess
import re


def executeOnce(process, *args):
    ''' executes process if it is not running '''
    if not isRunning(process):
        options = " ".join(args)
        process = " ".join((process, options))
        return subprocess.Popen(process.split())


def isRunning(process):
    ''' checks if process is running '''
    subprocs = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)

    for proc in subprocs.stdout:
        if re.search(process, proc):
            return True
    return False
