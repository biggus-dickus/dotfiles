#!/bin/sh

sudo pacman -S dunst hyprland hyprlock hypridle waybar wofi

cp -rv ./hypr/* ~/.config/hypr
cp -rv ./waybar/* ~/.config/waybar
