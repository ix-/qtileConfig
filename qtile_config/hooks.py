from libqtile import hook
from qtile_config import app
import subprocess
import re


def isRunning(process):
    '''checks if process is running'''
    subprocs = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)

    for proc in subprocs.stdout:
        if re.search(process, proc):
            return True
    return False


def executeOnce(process, *args):
    ''' executes process if it is not running '''
    if not isRunning(process):
        options = " ".join(args)
        process = " ".join((process, options))
        return subprocess.Popen(process.split())


#  Execute on Startup
@hook.subscribe.startup
def startup():
    ''' executes on startup '''
    executeOnce("wpa_gui", "-t")


@hook.subscribe.startup
def mousePointer():
    ''' display a left pointer as mouse '''
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])


@hook.subscribe.startup
def lockOnIdle():
    ''' calls a screenlock  after a given time (in min) of inactivity'''
    executeOnce(app.locker['init'])


#  Execute when new client is spawned
@hook.subscribe.client_new
def floating_dialogs(window):
    ''' sets dialog clients to 'floating' '''
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True
