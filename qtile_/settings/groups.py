# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile workspaces

from libqtile.command import lazy
from libqtile.config import Group, Key, ScratchPad, DropDown

from .keys import keys, mod

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-fa-firefox, 
# nf-fae-python, 
# nf-dev-terminal, 
# nf-fa-code, 
# nf-oct-git_merge, 
# nf-linux-docker,
# nf-mdi-image, 
# nf-mdi-layers

groups = [Group(i) for i in [
    "#", " ", " ", " ", "1", "2","3","4","5"
]]
#       

binding = "wcui12345"


for i, group in enumerate(groups):
    actual_key = str(binding[i])
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
        Key([mod],"Return", lazy.group["scratchPad"].dropdown_toggle("term")),
        Key([mod],"f", lazy.group["scratchPad"].dropdown_toggle("fileManager")),
    ])

groups.append(
    ScratchPad("scratchPad",[
               DropDown("term","alacritty", opacity=1, height=0.7, width=0.8, y=0.1),
               DropDown("fileManager","alacritty -e ranger", opacity=1, height=0.7, width=0.8, y=0.1),
               DropDown("timer45","alacritty -e termdown -s 45m", opacity=1, height=0.7, width=0.5, y=0.1),
               DropDown("timer5","alacritty -e termdown -s 5m", opacity=1, height=0.7, width=0.5, y=0.1),
               DropDown("timer10","alacritty -e termdown -s 10m", opacity=1, height=0.7, width=0.5, y=0.1)
           ]))





