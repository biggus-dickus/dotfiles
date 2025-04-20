#!/bin/sh

sudo pacman -S dunst hyprland hyprlock hypridle otf-font-awesome waybar wofi 

cp -rv ./hypr/* ~/.config/hypr
cp -rv ./waybar/* ~/.config/waybar
