''' run hooks '''

from libqtile import hook
from qtile_config import app
import subprocess
from qtile_config.toolbox import iio2 as iio
from qtile_config.toolbox import proc


#  Execute on Startup; Set in apps
@hook.subscribe.startup
def startup():
    ''' executes on startup '''
    proc.executeOnce(*app.NETGUI)
    proc.executeOnce(*app.WALLPAPER)
    proc.executeOnce(*app.LOCKER['init'])
    if iio.waitForConnection(app.REFERENCE):  # if we have a connection
        proc.executeOnce(*app.NTPDAEMON)


@hook.subscribe.startup
def mousePointer():
    ''' display a left pointer as mouse '''
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])


#  Execute when new client is spawned
@hook.subscribe.client_new
def floatingDialogs(window):
    ''' sets dialog clients to 'floating' '''
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True
