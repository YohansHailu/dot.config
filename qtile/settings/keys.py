# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.command import lazy
from libqtile.config import Key

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),
    ([mod], "space", lazy.layout.next()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "q", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "d", lazy.spawn("rofi -show run")),

    #/home/yohans/.config/qtile/wifi_rofi.sh

    # Window Nav
    ([mod, "shift"], "d", lazy.spawn("/home/yohans/.config/qtile/rofi_wifi_menu.sh")),

    # Browser
    ([mod], "b", lazy.spawn("firefox")),
    #([mod], "p", lazy.spawn("alacritty -e python")),
    ([mod], "n", lazy.spawn("alacritty -e lvim /home/yohans/nots/plan ")),

    # File Explorer
    #([mod], "e", lazy.spawn("pcmanfm")),

    # Terminal
    ([mod], "t", lazy.spawn("alacritty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screensho
    ([mod], "s", lazy.spawn("scrot")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

    # Volume
    ([mod], "v", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +10%"
    )),
    ([mod,"shift"], "v", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -10%"
    )),

    # Brightness
    ([mod], "x", lazy.spawn("brightnessctl set +2%")),
    ([mod, "shift"], "x", lazy.spawn("brightnessctl set 2%-")),
]]
