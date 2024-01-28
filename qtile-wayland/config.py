# https://github.com/david35mm/.files/blob/main/.config/qtile/config.py
# https://github.com/tralph3/.dotfiles/blob/master/.config/qtile/config.py
# https://gitlab.com/dwt1/dotfiles/-/blob/master/.config/qtile/config.py

import os
import shutil
import subprocess

from libqtile import bar, hook
from libqtile.config import Key, Screen
from libqtile.lazy import lazy

from options import *
from settings import mod, widget_defaults

# Init config partials
from groups_conf import groups
from keys_conf import keys
from layouts_conf import layouts, floating_layout
from widgets_conf import BAR_HEIGHT, widgets


extension_defaults = widget_defaults.copy()

def get_widgets(widget_list):
  return bar.Bar(widget_list, BAR_HEIGHT, opacity=0.8)

screens = [
    Screen(
        top=get_widgets(widgets),
        wallpaper='/usr/share/backgrounds/archlinux/awesome.png',
        wallpaper_mode='fill',
    ),
]

'''
connected_monitors = int(
    subprocess.run(
        "xrandr -d :0 -q | grep ' connected' | wc -l",
        check=True,
        shell=True,
        stdout=subprocess.PIPE,
    ).stdout.decode("UTF-8")
)

if connected_monitors > 1:
    for i in range(1, connected_monitors):
        screens.append(
            Screen(
                # top=get_widgets(widgets[0:3]),
                wallpaper='~/Pictures/wallpapers/0213.jpg',
                wallpaper_mode='fill'
            )
        )
'''

# Hooks
@hook.subscribe.restart
def delete_cache():
  shutil.rmtree(os.path.expanduser('~/.config/qtile/__pycache__'))

@hook.subscribe.startup_once
def autostart():
   autolaunch = os.path.expanduser('~/.config/qtile/autostart.sh')
   subprocess.Popen([autolaunch])

@hook.subscribe.shutdown
def stop_apps():
  delete_cache()
