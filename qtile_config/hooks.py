from libqtile import hook
import subprocess, re

def isRunning(process):
    '''checks if process is running'''
    s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
    for proc in s.stdout:
        if re.search(process, proc):
            return True
    return False

def executeOnce(process, *args):
    '''executes process if it is not running'''
    if not isRunning(process):
        options = " ".join(args)
        process = " ".join((process, options))
        return subprocess.Popen(process.split())

# Execute on Startup
@hook.subscribe.startup
def startup():
    '''executes on startup'''
    executeOnce("wpa_gui", "-t")
