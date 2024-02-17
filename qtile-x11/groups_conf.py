import re
from libqtile.config import DropDown, Group, Match, ScratchPad

from settings import terminal

groups = [
    Group("1", label="\uf120"),
    Group(
        "2",
        label="\uf268",
        matches=[Match(wm_class='chromium')],
    ),
    Group(
        "3",
        label="\uf269",
        matches=[Match(wm_class='firefox')],
    ),
    Group(
        "4",
        label="\ue796",
        matches=[Match(wm_class='jetbrains-webstorm')],
    ),
    Group(
        "5",
        label="\uf198",
        matches=[Match(wm_class='slack')],
    ),
    Group(
        "6",
        label="\uf118",
        matches=[Match(wm_class=re.compile(r"^(Lxappearance|Nitrogen)$"))],
    ),
    Group(
        "7",
        label="\uf03e",
        matches=[Match(wm_class=re.compile(r"^(ristretto|gimp\-2\.10)$"))],
    ),
    Group(
        "8",
        label="\uf1b6",
        layout='max',
        matches=[Match(wm_class=re.compile(r"^(Steam|vlc)$"))],
    ),
    Group(
        "9",
        label="\uf03d",
        matches=[Match(wm_class=re.compile(r"^(zoom|roam)$"))],
    ),
]

groups.append(
    ScratchPad(
        'scratchpad', [
            DropDown(
                'notepad', 'mousepad', x=0.25, y=0.2, width=0.42, height=0.5, opacity=1, on_focus_lost_hide=False
            ),
            DropDown(
                # Must install khal
                'calendar', terminal + " --hold -e khal calendar", x=0.70, width=0.25
            ),
        ]
    ),
)
