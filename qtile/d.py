import os
import subprocess

def autostart():

    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run(['/bin/sh',home])

autostart()
