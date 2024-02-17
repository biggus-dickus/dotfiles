from libqtile import widget
from libqtile.lazy import lazy

from settings import colours

BAR_HEIGHT = 26
DEFAULT_UPDATE_INTERVAL = 2.0
SEPARATOR = widget.Sep(foreground=colours['text'], linewidth=1, padding=10)

widgets = [
    widget.GroupBox(
        active=colours['highlight'],
        borderwidth=2,
        disable_drag=True,
        font='SauceCodePro Nerd Font Mono',
        fontsize=24,
        highlight_method='line',
        inactive=colours['text'],
        other_current_screen_border=colours['warning'],
        other_screen_border=colours['text'],
        this_current_screen_border=colours['highlight'],
        this_screen_border=colours['text'],
        toggle=False,
        urgent_alert_method='text',
        urgent_border=colours['error'],
        urgent_text=colours['error'],
    ),
    SEPARATOR,
    widget.CurrentLayoutIcon(scale=0.75),
    widget.Prompt(),
    widget.WindowName(max_chars=50),
    widget.Net(
        foreground=colours['accent'],
        format="{down:.0f}{down_suffix} ↓↑{up:.0f}{up_suffix}",
        interface='wlp4s0',
    ),
    SEPARATOR,
    widget.CPU(
        foreground=colours['highlight'],
        update_interval=DEFAULT_UPDATE_INTERVAL,
    ),
    SEPARATOR,
    widget.Memory(
        foreground=colours['success'],
        format="{MemUsed:.0f}{mm} {MemPercent:.0f}%",
        update_interval=DEFAULT_UPDATE_INTERVAL,
    ),
    SEPARATOR,
    widget.Wlan( # requires python-iwlib
        disconnected_message='off',
        foreground=colours['lighter'],
        format="\uf1eb   {percent:2.0%}",
        interface='wlp4s0',
        update_interval=DEFAULT_UPDATE_INTERVAL,
    ),
    SEPARATOR,
    widget.Backlight(
        backlight_name="nvidia_wmi_ec_backlight", # ls /sys/class/backlight/
        change_command="brightnessctl set {0}%", # brightnessctl must be installed
        foreground=colours['warning'],
        foreground_alert=colours['error'],
        format="☼ {percent:2.0%}",
    ),
    SEPARATOR,
    widget.Battery(
        foreground=colours['info'],
        format="{char} {percent:2.0%}",
        charge_char="",
        discharge_char="",
        empty_char="",
        full_char="",
        unknown_char="",
        low_foreground=colours['error'],
        low_percentage=0.15,
        show_short_text=False,
        notify_below=5
    ),
    SEPARATOR,
    widget.Clock(
        format="%a %d %b %H:%M",
        mouse_callbacks={'Button1': lazy.group['scratchpad'].dropdown_toggle('calendar')}
    ),
    # https://github.com/akkaky/qtile-wttr-widget
    widget.Wttr(
        location={
            '51.94816,33.93299': 'Svessa'
        },
        format='%t %c',
        padding=3,
        units='m',
        update_interval=1800,
    ),
    SEPARATOR,
    widget.KeyboardLayout(configured_keyboards=['us', 'ru', 'ua']),
    widget.Systray(),
    widget.Volume(
        fontsize=14,
        fmt="墳 {}",
        # icons names: audio-volume-high, audio-volume-medium, audio-volume-low, audio-volume-muted
        # theme_path="~/.local/share/icons/Qogir/24/panel/",
        padding=5,
        volume_app='pavucontrol',
    ),
    widget.Spacer(length=3),
]
