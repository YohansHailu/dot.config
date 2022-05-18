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
    Key([mod], "w",
        lazy.window.kill()),

    Key([mod, "control"], "r",
        lazy.restart()),
    Key([mod, "control"], "q",
        lazy.shutdown()),

    Key([mod], "d",
        lazy.spawn("rofi -show run")),
]

groups = [Group(i) for i in "yuiopbnm"]
for i in groups:
    keys.extend([
        Key([mod], i.name,
            lazy.group[i.name].toscreen(),),
        Key([mod, "shift"], i.name,
            lazy.window.togroup(i.name, switch_group=True)),
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

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    font="Ubuntu Bold",
                    fontsize=10,
                    rounded=False,
                    marginx=2,
                    paddingx=8,
                    borderwidth=1
                    ),
                widget.Spacer(
                    ),

                widget.Wlan(
                     interface="wlp4s0",
                     format='{essid} {quality}/70',
                     padding=3

                    ),
                widget.Net(
                     interface="enp0s25",
                     format='{essid} {quality}/70',
                     padding=3

                    ),

                widget.Net(
                        interface="wlp4s0",
                        format='{down} ↓↑ {up}',
                        padding=3
                    ),
                widget.Memory(
                   padding=3
                    ),
                widget.Clock(format="%I %M %P")
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
