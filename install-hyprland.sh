#!/bin/sh

sudo pacman -S dunst hyprland hyprlock hypridle waybar wofi

cp -rv ./hypr/* ~/.config
cp -rf waybar/* ~/.config
