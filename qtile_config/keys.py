from libqtile.config import Key
from libqtile.command import lazy

from qtile_config  import app

from .modifiers import mod

command_keys = [
    # Switch screens
    Key(
        [mod], "1",
        lazy.to_screen(0),
        lazy.group.toscreen(0)
    ),
    Key(
        [mod], "2",
        lazy.to_screen(1),
        lazy.group.toscreen(1)
    ),

    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    # Widen or shrink a pane
    Key([mod], "bracketright", lazy.layout.increase_ratio()),
    Key([mod], "bracketleft", lazy.layout.decrease_ratio()),
    Key([mod], "v", lazy.layout.grow()),
    Key([mod], "b", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "m", lazy.layout.maximize()),
    Key([mod, "shift"], "m", lazy.layout.flip()),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.nextlayout()),
    
    # Control clients and qtile
    Key([mod], "w", lazy.window.kill()),  # kill a client
    Key([mod, "control"], "r", lazy.restart()),  # restart qtile
    Key([mod], "Delete", lazy.shutdown()),  # shutdown qtile

    # Spawn programs
    Key([mod], "Return", lazy.spawn(app.screen)),  # start multiplexing termial
    Key([mod], "c", lazy.spawn(app.browser)),  # start browser
    Key([mod], "x", lazy.spawncmd()),  # start dmenu style cmd line
    Key([mod], "z", lazy.spawn(app.terminal)),  # start single terminal
    Key([mod, "shift"], "l", lazy.spawn(app.LOCKER['lock'])),  # lock screen

    # Volume control
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Toggle floating
    Key([mod], "l", lazy.window.toggle_floating()),

]
