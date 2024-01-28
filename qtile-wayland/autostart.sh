#!/usr/bin/env bash

# xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --rate 59.96 &

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/bin/dunst &

#picom &
blueman-applet &

# w/o this, lxappearance won't enable your custom cursor on start.
# You may also need to manually edit the name of the cursor theme in `~/.icons/default/index.theme`.
# If some apps still do not respect the system setting,
# you should edit ~/.config/gtk-3.0/settings.ini, replacing the `cursor_theme_name` with the chosen one.
# https://wiki.archlinux.org/title/Cursor_themes#Configuration
#xsetroot -cursor_name left_ptr # xorg-xsetroot package may not be installed by default

#xscreensaver --no-splash &
#setxkbmap -option "compose:ralt" & # bind Compose key to the right Alt
# numlockx & # not installed by default
