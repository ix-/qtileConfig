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
    Key([mod], "Tab",    lazy.nextlayout()),
    Key([mod], "w",      lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod], "Delete", lazy.shutdown()),

    # Spawn programs
    Key([mod], "Return", lazy.spawn(app.screen)),
    Key([mod], "c", lazy.spawn(app.browser)),
    Key([mod], "x", lazy.spawncmd()),
    Key([mod], "z", lazy.spawn(app.terminal)),

    # Volume control
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Toggle floating
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

]
