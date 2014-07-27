from libqtile.config import Screen
from libqtile import bar, widget

widget_defaults = {
    'font': 'Ubuntu Mono'
}

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(**widget_defaults),
                widget.Sep(),
                widget.CPUGraph(),
                widget.NetGraph(graph_color='F62217', fill_color='F88017'),
                widget.NetGraph(graph_color='CC6600', fill_color='FFBB11', bandwidth_type='up'),
                widget.Sep(),
                widget.Prompt(**widget_defaults),
                widget.WindowName(**widget_defaults),
                widget.Sep(),
                widget.Systray(),
                widget.CurrentLayout(),
                # widget.Canto(),
                widget.Volume(**widget_defaults),
                widget.ThermalSensor(tag_sensor='Core 0'),
                # widget.Battery(
                #     energy_now_file='charge_now',
                #     energy_full_file='charge_full',
                #     power_now_file='current_now',
                #     **widget_defaults
                #      ),
                widget.Sep(),
                widget.Clock('%Y-%m-%d %a %I:%M %p', **widget_defaults),
            ],
            30,
        ),
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(**widget_defaults),
                widget.Prompt(**widget_defaults),
                widget.WindowName(**widget_defaults),
            ],
            20,
        ),
    ),
]
