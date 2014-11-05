qtileConfig
===========

My modular qtile (0.7) config.py

qtile_config.groups
-------------------
8 virtual desktops 'a s d f u i o p'

qtile_config.hooks
------------------
* isRunning(process) - checks if process is running
* executeOnce(process, *args) - executes process if it is not running
* startup() - executes on startup (needs rewriting to startup(process))
* mousePointer() - display a left pointer as mouse
* floating_dialogs(window) - make 'dialog' clients float

qtile_config.keys
-----------------
* mod+{asdfuiop} - change to the corresponding virtual desktop
* mod,shift+{asdfuiop} - send active client to the corresponding virtual desktop
* mod+{vbnm} - grow, shrink, normalize, maximize the client
* mod,shift+M - flip the panes
* mod+Tab - next layout
* mod,shift+F - toggle floating
* mod+w - kill the active client
* mod+Return - spawn the app.screen()
* mod+c - spawn the app.browser
* mod+x - spawn the dmenu-style cmdline
* mod+z - spawn the app.terminal 
* mod+l - lock screen (needs app.LOCKER to be defined)
qtile_config.layouts
--------------------
<+TODO+>

qtile_config.modifiers
----------------------
mod = mod4

qtile_config.mouse
------------------
<+TODO+>

qtile_config.screens
--------------------
<+TODO+>

qtile_config.toolbox
--------------------
### toolbox.iio2 ###
iio2 is a python2 connection checker that depends on urllib2

* iio2.isItOnline(reference): check if the reference can be connected (via http 'GET' request) 
* iio2.waitForConnection(reference, sleeptime=1, times=10): checks 10 times for the reference to be reachable.

### toolbox.proc ###
proc handles processes

* proc.isRunning(process): check if process is running
* proc.executeOnce(process): executes process if it was not already started
