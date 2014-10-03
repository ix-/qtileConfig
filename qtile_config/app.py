'''defines standard programs'''

screen = 'st -e screen -RD'
terminal = 'st'
browser = 'firefox-bin'
# Screenlock:
#    init is called by hook.py on startup
#    toggle is called by keys.py on keypress
locker = {'init': 'xautolock -time 10 -locker slock -corners +-00 -cornerdelay 2',
          'lock': 'xautolock -locknow'}
