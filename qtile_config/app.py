'''defines standard programs'''
import os


# common config files used by qtile
peripherals = "/".join((os.getenv("HOME"), "qtile-config", "peripherals"))

# common programs mapped to keys
screen = 'st -e screen -RD'
terminal = 'st'
browser = 'firefox-bin'

# init programs called by hooks.startup()
# Screenlock:
#    init is called by hook.py on startup
#    toggle is called by keys.py on keypress
LOCKER = {'init': ("xautolock",
                   "-time 10",
                   "-locker slock",
                   "-corners +-00",
                   "-cornerdelay 2",
                   "-cornerredelay 5"),
          'lock': 'xautolock -locknow'}

NETGUI = ('wpa_gui', '-t')
NTPDAEMON = ('chronyc', '-a', 'online')
REFERENCE = ('http://131.130.142.98')  # nawi.at for connection checking
WALLPAPER = ("conky",
             "-c",
             "/".join((peripherals, "conkyrc")),
             "--daemonize")
