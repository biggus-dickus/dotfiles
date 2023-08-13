from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

from settings import commands, mod, terminal

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
    Key([mod], "p", lazy.spawn(commands['launch']), desc='Run the application launcher'),
    Key(["mod1"], "Tab", lazy.spawn(commands['switch_window']), desc='Open the window switcher'),

    # Multimedia keys (required packages must be installed: amixer, dunst, playerctl)
    Key([], "XF86AudioMute", lazy.spawn(commands['volume_mute']), desc='Mute volume'),
    Key([], "XF86AudioLowerVolume", lazy.spawn(commands['volume_down']), 'Turn volume down'),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(commands['volume_up']), 'Turn volume up'),

    Key([], "XF86AudioPlay", lazy.spawn(commands['play_pause_audio']), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn(commands['next_audio']), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn(commands['prev_audio']), desc="Skip to previous"),
    
    Key([], "XF86MonBrightnessDown", lazy.spawn(commands['brightness_down'])),
    Key([], "XF86MonBrightnessUp", lazy.spawn(commands['brightness_up'])),

    # Toggle the scratchpads
    Key([mod], "z", lazy.group['scratchpad'].dropdown_toggle('notepad')),

    # Custom shortcuts
    Key(["mod1"], "Shift_L", lazy.widget["keyboardlayout"].next_keyboard(), desc='Next keyboard layout'),
    Key([mod, "mod1"], "l", lazy.spawn(commands['lock']), desc='Lock screen'),
    Key(["control"], "backslash", lazy.spawn(commands['screenshot']), desc='Capture a region using the GUI'),
]

# swich groups
for i in [str(x) for x in range(1, 10)]:
    keys.extend(
        [
            Key(
                [mod],
                i,
                lazy.group[i].toscreen(),
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

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
