from libqtile import layout
from libqtile.config import Match

from settings import layout_theme

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

# Floating rules
floating_layout = layout.Floating(
    float_rules=[
        # Run `xprop WM_CLASS` to see the wm class and name of an X client.
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
        Match(title="zoom "),  # zoom notifications
    ]
)
