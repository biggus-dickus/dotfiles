# https://github.com/david35mm/.files/blob/main/.config/qtile/config.py
# https://github.com/tralph3/.dotfiles/blob/master/.config/qtile/config.py
# https://gitlab.com/dwt1/dotfiles/-/blob/master/.config/qtile/config.py

import os
import shutil
import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from settings import colours, layout_theme, widget_defaults


mod = "mod4" # xmodmap
terminal = guess_terminal()
screen_lock = "dm-tool lock"

VOLUME_SCRIPT = os.path.expanduser('~/bin/volume-notify')

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc='Grow window to the left'),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc='Grow window to the right'),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc='Grow window down'),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc='Grow window up'),
    Key([mod], "n", lazy.layout.normalize(), desc='Reset all window sizes'),

    # Grow/shrink windows left/right. 
    # This is mainly for the 'monadtall' and 'monadwide' layouts,
    # although it does also work in the 'bsp' and 'columns' layouts.
    Key([mod], "equal",
        lazy.layout.grow_left().when(layout=["bsp", "columns"]),
        lazy.layout.grow().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left"
    ),
    Key([mod], "minus",
        lazy.layout.grow_right().when(layout=["bsp", "columns"]),
        lazy.layout.shrink().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left"
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack',
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc='Launch terminal'),

    Key([mod], "Tab", lazy.next_layout(), desc='Toggle between layouts'),
    Key([mod], "w", lazy.window.kill(), desc='Kill focused window'),
    Key([mod, "shift"], "r", lazy.reload_config(), desc='Reload the config'),
    Key([mod, "shift"], "q", lazy.shutdown(), desc='Shutdown Qtile'),

    Key([mod], "r", lazy.spawncmd(), desc='Spawn a command using a prompt widget'),
    Key([mod], "p", lazy.spawn("rofi -show drun"), desc='Run the application launcher'),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window"), desc='Open the window switcher'),

    Key(["mod1"], "Shift_L", lazy.widget["keyboardlayout"].next_keyboard(), desc='Next keyboard layout'),

    # Multimedia keys (required packages must be installed: amixer, dunst)
    # Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"), desc='Mute volume'),
    Key([], "XF86AudioMute", lazy.spawn(f"sh {VOLUME_SCRIPT} mute"), desc='Mute volume'),
    # Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%- unmute"), 'Turn volume down'),
    Key([], "XF86AudioLowerVolume", lazy.spawn(f"sh {VOLUME_SCRIPT} down"), 'Turn volume down'),
    # Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+ unmute"), 'Turn volume up'),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(f"sh {VOLUME_SCRIPT} up"), 'Turn volume up'),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),
    
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 10%+")),

    # Toggle the scratchpads
    Key([mod], "z", lazy.group['scratchpad'].dropdown_toggle('notepad')),

    # Custom shortcuts
    Key([mod, "mod1"], "l", lazy.spawn(screen_lock), desc='Lock screen'),
    Key(["control"], "backslash", lazy.spawn("flameshot gui"), desc='Capture a region using the GUI'),
]

groups = [
    Group("1", label="\uf120"),
    Group(
        "2",
        label="\ue743",
        matches=[Match(wm_class=['chromium'])],
    ),
    Group(
        "3",
        label="\uf269",
        matches=[Match(wm_class=['firefox'])],
    ),
    Group(
        "4",
        label="\ue796",
        layout='max',
        matches=[Match(wm_class=['jetbrains-webstorm'])],
    ),
    Group(
        "5",
        label="\uf198",
        matches=[Match(wm_class=['slack'])],
    ),
    Group(
        "6",
        label="\uf118",
        matches=[Match(wm_class=['Lxappearance', 'Nitrogen'])],
    ),
    Group(
        "7",
        label="\uf03e",
        matches=[Match(wm_class=['ristretto', 'gimp-2.10'])],
    ),
    Group(
        "8",
        label="\uf1b6",
        layout='max',
        matches=[Match(wm_class=['Steam', 'vlc'])],
    ),
    Group(
        "9",
        label="\uf03d",
        layout='max',
        matches=[Match(wm_class=['zoom'])],
    ),
]

# indexes = list(
#     map(lambda n: str(n), list(range(1, len(groups) + 1)))
# )
# for i, group in zip(indexes, groups):
#     keys.extend(
#         [
#             Key(
#                 [mod],
#                 i,
#                 lazy.group[group.name].toscreen(),
#                 desc="Switch to group {}".format(group.name),
#             ),
#             Key(
#                 [mod, "shift"],
#                 i,
#                 lazy.window.togroup(group.name, switch_group=True),
#                 desc="Switch to & move focused window to group {}".format(group.name),
#             ),
#         ]
#     )

# # swich groups
for i in [str(x) for x in range(1, 10)]:
    keys.extend(
        [
            Key(
                [mod],
                i,
                lazy.group[i].toscreen(toggle=True),
                desc=f"Switch to group {i}",
            ),

            Key(
                [mod, "shift"],
                i,
                lazy.window.togroup(i),
                desc=f"Switch to & move focused window to group {i}",
            ),
        ]
    )

groups.append(
    ScratchPad(
        'scratchpad', [
            DropDown(
                'notepad', 'mousepad', x=0.25, y=0.2, width=0.42, height=0.5, opacity=1, on_focus_lost_hide=False
            ),
            DropDown(
                # Must install khal
                'calendar', terminal + " --hold -e khal calendar", x=0.71, width=0.25
            ),
        ]
    ),
)    

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Floating(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]

extension_defaults = widget_defaults.copy()

DEFAULT_UPDATE_INTERVAL = 2.0
SEPARATOR = widget.Sep(foreground=colours['text'], linewidth=1, padding=10)

# cb = lambda: qtile.cmd_spawn(terminal + " -e ytop")

widgets = [
    widget.GroupBox(
        active=colours['highlight'],
        borderwidth=2,
        center_aligned=False,
        disable_drag=True,
        fontsize=24,
        highlight_method='line',
        inactive=colours['text'],
        other_current_screen_border=colours['warning'],
        other_screen_border=colours['text'],
        this_current_screen_border=colours['highlight'],
        this_screen_border=colours['text'],
        urgent_alert_method='text',
        urgent_border=colours['error'],
        urgent_text=colours['error'],
    ),
    SEPARATOR,
    widget.CurrentLayout(
        foreground=colours['accent'],
    ),
    widget.Prompt(),
    widget.WindowName(max_chars=50),
    widget.CPU(
        foreground=colours['highlight'],
        # mouse_callbacks={
        #     "Button1": cb,
        # },
        update_interval=DEFAULT_UPDATE_INTERVAL,
    ),
    SEPARATOR,
    widget.Memory(
        foreground=colours['success'],
        format="{MemUsed:.0f} MB",
        update_interval=DEFAULT_UPDATE_INTERVAL,
    ),
    SEPARATOR,
    widget.Net(
        foreground=colours['accent'],
        format="{down} ↓↑{up}",
        interface='wlp4s0',
    ),
    SEPARATOR,
    widget.Wlan( # requires python-iwlib
        disconnected_message='off',
        foreground=colours['lighter'],
        format="\uf1eb {percent:2.0%}",
        interface='wlp4s0',
        update_interval=DEFAULT_UPDATE_INTERVAL,
    ),
    # SEPARATOR,
    # widget.PulseVolume(
    #     fmt="墳 {}",
    #     foreground=colours['info'],
    #     step=5,
    #     update_interval=0.1,
    #     volume_app="pavucontrol",
    # ),
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
        foreground=colours['accent'],
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
        padding=5,
        units='m',
        update_interval=1200,
    ),
    SEPARATOR,
    widget.KeyboardLayout(configured_keyboards=['us', 'ru', 'ua']),
    widget.Spacer(length=3),

    # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
    # widget.StatusNotifier(),
    widget.Systray(),
]

def get_widgets(widget_list):
  return bar.Bar(widget_list, 26, opacity=0.9)

screens = [
    Screen(
        top=get_widgets(widgets),
        wallpaper='~/Pictures/wallpapers/0253.jpg',
        wallpaper_mode='fill',
    ),
]

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

    for i in range(connected_monitors):
        keys.extend([Key([mod, "mod1"], str(i+1), lazy.window.toscreen(i))])
 
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="Arandr"),
        Match(wm_class="Blueman-adapters"),
        Match(wm_class="Blueman-manager"),
        Match(wm_class="confirm"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="eog"), # Eye of Gnome (image viewer)
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="flameshot"),
        Match(wm_class="galculator"),
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="pavucontrol"),
        Match(wm_class="ssh-askpass"),

        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

wmname = "LG3D"


# Hooks
@hook.subscribe.restart
def delete_cache():
  shutil.rmtree(os.path.expanduser("~/.config/qtile/__pycache__"))

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

@hook.subscribe.shutdown
def stop_apps():
  delete_cache()
