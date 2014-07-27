from libqtile import layout
layouts = [
    layout.MonadTall(),
    layout.Stack(stacks=2),
    layout.Matrix(),
    layout.TreeTab(),
    layout.RatioTile(),
    layout.Zoomy(),
    layout.Max(),
    layout.Tile(ratio=0.50, masterWindows=2),
]

floating_layout = layout.Floating(auto_float_types=[
    "notification",
    "toolbar",
    "splash",
    "dialog",
    "utility",
])
