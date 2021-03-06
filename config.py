
# Allow me to store my stuff in a package
from os import sys, path

sys.path.append(
    path.abspath(path.join(path.dirname(__file__), 'qtile_config'))
)

from qtile_config.groups import groups, group_keys
from qtile_config.keys import command_keys
from qtile_config.layouts import layouts, floating_layout
from qtile_config.screens import screens
from qtile_config.mouse import mouse
from qtile_config import hooks

keys = group_keys + command_keys

dgroups_key_binder = None
dgroups_app_rules = []

main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
wmname = "qtile"
