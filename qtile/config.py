import os
import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Group, Key, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"

keys = [
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),

    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up()),

    Key([mod, "control"], "h",
        lazy.layout.grow_left()),
    Key([mod, "control"], "l",
        lazy.layout.grow_right()),
    Key([mod, "control"], "j",
        lazy.layout.grow_down()),

    Key([mod, "control"], "k",
        lazy.layout.grow_up()),
    Key([mod], "n",
        lazy.layout.normalize()),

    Key([mod], "Return",
        lazy.spawn(terminal)),

    Key([mod], "Tab",
        lazy.next_layout()),
    Key([mod], "q",
        lazy.window.kill()),

    Key([mod, "control"], "r",
        lazy.restart()),
    Key([mod, "control"], "q",
        lazy.shutdown()),

    Key([mod], "d",
        lazy.spawn("rofi -show run")),
]

names = ["code", "www", "book", "leet"] + list('uiop')
map = "cwbluiop"

groups = [Group(i) for i in names]
for i in range(len(groups)):
    keys.extend([
        Key([mod], map[i],
            lazy.group[names[i]].toscreen(),),
        Key([mod, "shift"], map[i],
            lazy.window.togroup(names[i], switch_group=True)),
    ])

layout_theme = {
        "border_width": 2,
        "margin": 12,
        "border_focus": "a0a0a0",
        "border_normal": "000000"
        }

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=14,
    margin_x=6
)
extension_defaults = widget_defaults.copy()

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#696764", "#696764"],
          ["#a9a1e1", "#a9a1e1"],
          ["#000000", "#000000"]]


screens = [
    Screen(
        bottom=bar.Bar(
            [

              widget.GroupBox(
                       font="Ubuntu Bold",
                       fontsize=14,
                       margin_y=3,
                       margin_x=0,
                       padding_y=0,
                       padding_x=3,
                       borderwidth=3,
                       active=colors[5],
                       inactive=colors[8],
                       rounded=True,
                       highlight_color=colors[1],
                       highlight_method="line",
                       this_current_screen_border=colors[5],
                       this_screen_border=colors[4],
                       other_current_screen_border=colors[6],
                       other_screen_border=colors[4],
                       foreground=colors[10],
                       background=colors[1]
                       ),
              widget.Spacer(
                       background=colors[1]
                       ),
              widget.TextBox(
                       text='|',
                       font="Ubuntu Mono",
                       foreground=colors[5],
                       background=colors[1],
                       padding=0,
                       fontsize=37
                       ),
              widget.Wlan(
                       interface="wlp4s0",
                       format='{essid} {quality}/70',
                       foreground=colors[5],
                       background=colors[1],
                       padding=0
                       ),
              widget.Net(
                        interface="wlp4s0",
                        format='{down}',
                        foreground=colors[5],
                        background=colors[1],
                        padding=3
                    ),
              widget.TextBox(
                       text='|',
                       font="Ubuntu Mono",
                       foreground=colors[5],
                       background=colors[1],
                       padding=0,
                       fontsize=37
                       ),
              widget.CPU(
                        format="Cpu {load_percent}%",
                        foreground=colors[5],
                        background=colors[1],
                        update_interval=2,
                ),
              widget.TextBox(
                       text='|',
                       font="Ubuntu Mono",
                       foreground=colors[5],
                       background=colors[1],
                       padding=0,
                       fontsize=37
                       ),
              widget.Memory(
                       foreground=colors[5],
                       background=colors[1],
                       fmt='Mem: {}',
                       padding=5
                       ),
              widget.TextBox(
                       text='|',
                       font="Ubuntu Mono",
                       foreground=colors[5],
                       background=colors[1],
                       padding=0,
                       fontsize=37
                       ),
              widget.TextBox(
                       tex='|',
                       font="Ubuntu Mono",
                       foreground=colors[5],
                       background=colors[1],
                       padding=0,
                       fontsize=37
                       ),
              widget.Battery(
                       foreground=colors[5],
                       background=colors[1],
                       format="{percent:2.0%}"
                       ),
              widget.TextBox(
                       text='|',
                       font="Ubuntu Mono",
                       foreground=colors[5],
                       background=colors[1],
                       padding=0,
                       fontsize=37
                       ),
              widget.Volume(
                       foreground=colors[5],
                       background=colors[1],
                       fmt='Vol: {}',
                       padding=0
                       ),
              widget.TextBox(
                       text='|',
                       font="Ubuntu Mono",
                       foreground=colors[5],
                       background=colors[1],
                       padding=0,
                       fontsize=37
                       ),
              widget.Clock(
                       foreground=colors[5],
                       background=colors[1],
                       format="%A, %B %d - %H:%M "
                       ),
            ],
            24,
        ),
    ),
]


dgroups_key_binder = None
dgroups_app_rules = []
bring_front_click = False
cursor_warp = False
Ruto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = False
auto_minimize = False
wmname = "LG3D"


@hook.subscribe.startup
def autostart():
    path = os.path.expanduser(".config/qtile/autostart.sh")
    subprocess.run(["/bin/sh", path])
