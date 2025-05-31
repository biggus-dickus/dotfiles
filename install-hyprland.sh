#!/bin/sh

sudo pacman -S dunst hyprland hyprlock hypridle otf-font-awesome swaybg waybar wofi xdg-desktop-portal-hyprland 

cp -rv ./hypr/* ~/.config/hypr
cp -rv ./waybar/* ~/.config/waybar
