from libqtile import widget

from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors["light"],
        'background': colors["dark"]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="|",
        fontsize=37,
        padding=1
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=0, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),
    
    powerline(fg="color3"),
    icon(bg="color1", text=' '),  # Icon: nf-fa-feed
    widget.Wlan(**base(bg='color1'),interface="wlp4s0", format='{essid} {quality}/70'),
    #widget.Net(**base(bg='color1'), interface='wlp4s0'),

    powerline(fg="color3"),
    widget.Volume(**base(bg='color1'),fmt='墳 {}'),
    widget.Battery(**base(bg='color1'), format=" {percent:2.0%}"),
    powerline(fg="color3"),
    widget.CPU(**base(bg='color1'), format=" {load_percent}%"),
    widget.Memory(**base(bg='color1'), fmt='{}', padding=1, measure_mem='G'),
    powerline(fg="color3"),
    widget.Clock(**base(bg='color1'), format="%A, %B %d - %H:%M "),

]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
