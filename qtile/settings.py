import os

from libqtile.utils import guess_terminal


terminal = guess_terminal()
mod = "mod4" # xmodmap

BRIGHTNESS_STEP = 5

VOLUME_SCRIPT = os.path.expanduser('~/bin/volume-notify')

commands = dict(
    brightness_down=f"brightnessctl set {BRIGHTNESS_STEP}%-",
    brightness_up=f"brightnessctl set {BRIGHTNESS_STEP}%+",
    launch="rofi -show drun",
    lock="dm-tool lock",
    logout="qtile cmd-obj -o cmd -f shutdown",
    next_audio="playerctl next",
    play_pause_audio="playerctl play-pause",
    poweroff="poweroff",
    prev_audio="playerctl previous",
    reboot="reboot",
    screenshot="flameshot gui",
    stop_audio="playerctl stop",
    suspend="systemctl suspend",
    switch_window="rofi -show window",
    toggle_mute_mic="amixer set Capture toggle",
    volume_down=f"sh {VOLUME_SCRIPT} down",
    volume_mute=f"sh {VOLUME_SCRIPT} mute",
    volume_up=f"sh {VOLUME_SCRIPT} up",
)

colours = dict(
    dark="#1f2329",
    lighter="#dcdcdc",
    text="#535965", # grey
    error="#e55561", # red
    success="#8ebd6b", # green
    warning="#e2b86b", # orange
    info="#4fa6ed", # blue
    accent="#bf68d9", # magenta
    highlight="#48b0bd", # teal
)

layout_theme = {
    'border_focus': colours['info'],
    'border_normal': colours['text'],
    'margin': 4,
    'border_width': 2,
}

widget_defaults = dict(
    font="Fira Sans Bold",
    fontsize=12,
    padding=3,
)
