#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &

nitrogen --restore
setxkbmap -option caps:swapescape
unclutter --ignore-scrolling --hide-on-touch --start-hidden --timeout 0.4 &
xcompmgr &
xset r rate 300 50
date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"


