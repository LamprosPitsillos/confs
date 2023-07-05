#
#   ___ _____ ___ _     _____
#  / _ \_   _|_ _| |   | ____|
# | | | || |  | || |   |  _|
# | |_| || |  | || |___| |___
#  \__\_\|_| |___|_____|_____|
#
import os
import subprocess


# from current_wallpaper import WALLPAPER
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import (
    Click,
    Drag,
    DropDown,
    Group,
    Key,
    KeyChord,
    Match,
    ScratchPad,
    Screen,
)
from libqtile.lazy import lazy
# import subprocess
from current_theme import THEME

# from libqtile.utils import guess_terminal

script = os.path.expanduser("~/.scripts/")
home = os.path.expanduser("~")

# wallpaper = "/home/inferno/pics/wallpapers/black-sand-dunes-2387793.jpg"
# wallpaper = "/home/inferno/pics/wallpapers/pexels-flora-westbrook-1924867.jpg"
# wallpaper = "/home/inferno/pics/wallpapers/skyrim_powerstones.jpg"
# wallpaper = "/home/inferno/pics/wallpapers/pexels-brady-knoll-5409751.jpg"

wallpaper = "/home/inferno/pics/wallpapers/hellish_depression_orange.jpg"


# @hook.subscribe.screen_change
# def set_screens(event):
#     subprocess.run(["autorandr", "--change"])
#     # lazy.spawn("mydock")
#     qtile.restart()
#

# @hook.subscribe.client_new
# def _swallow(window):
#     pid = window.window.get_net_wm_pid()
#     ppid = psutil.Process(pid).ppid()
#     cpids = {
#         c.window.get_net_wm_pid(): wid for wid, c in window.qtile.windows_map.items()
#     }
#     for i in range(5):
#         if not ppid:
#             return
#         if ppid in cpids:
#             parent = window.qtile.windows_map.get(cpids[ppid])
#             if parent.window.get_wm_class()[1] != "kitty":
#                 return
#             parent.minimized = True
#             window.parent = parent
#             return
#         ppid = psutil.Process(ppid).ppid()


@hook.subscribe.client_killed
def _unswallow(window):
    if hasattr(window, "parent"):
        window.parent.minimized = False
#


@lazy.function
def window_to_slice(qtile):
    if not qtile.current_layout.name == "ﯻ":
        return
    win = qtile.current_window
    slice = qtile.current_layout
    old_slice = slice._slice.window
    if old_slice:
        slice._slice.remove(old_slice)
        slice.fallback.add(old_slice)
        slice.layouts[old_slice] = slice.fallback
    slice.fallback.remove(win)
    slice._slice.add(win)
    slice.layouts[win] = slice._slice
    qtile.current_group.layout_all()


def get_monitors():
    xr = (
        subprocess.check_output(
            'xrandr --query | grep " connected"', shell=True)
        .decode()
        .split("\n")
    )
    monitors = len(xr) - 1
    return monitors


monitors = get_monitors()

mod = "mod4"
terminal = "kitty"

keys = [
    # Switch between windows
    Key([mod], "f", lazy.hide_show_bar("all"), desc="Hide Bar"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "s", window_to_slice, desc="Move to slice"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "c", lazy.group.next_window(),
        desc="Move window focus to other window"),
    # App Launcher
    KeyChord(
        [mod],
        "o",
        [
            Key([], "c", lazy.spawn("qalculate-gtk"), desc="Launch vifm"),
            Key([],
                "i",
                lazy.spawn(f"qtile run-cmd -f kitty -e {script} notetaking"),
                desc="Note taking",
                ),
            Key([], "v", lazy.spawn(
                f"{terminal} -e vifm"), desc="Launch vifm"),
            Key([],
                "q",
                lazy.spawn(script + "qute_search.sh"),
                desc="Launch qutebrowser",
                ),
            Key([], "n", lazy.spawn("kitty -e nvim"), desc="Launch Nvim"),
            Key([],
                "s",
                lazy.spawn(
                    "qtile run-cmd -f zathura '/home/inferno/UoC/8ο Εξαμηνο/Scedule/8ο Εξαμηνο.pdf'"
            ),
            ),
        ],
    ),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod], "a", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
    Key([mod], "d", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),
    # Switch focus of monitors
    Key([mod], "s", lazy.next_screen(), desc="Move focus to next monitor"),
    # Key([mod], "comma",
    #     lazy.prev_screen(),
    #     desc='Move focus to prev monitor'
    #     ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
        ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
        ),
    Key([mod, "shift"], "t",
        lazy.window.toggle_floating(),
        desc="Toggle between floating and tiled of window",
        ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Custom
    Key([], "Print", lazy.spawn(script + "print_screen"), desc="Take a Screenshot"),
    Key(["shift"], "Print",
        lazy.spawn(script + "print_window"),
        desc="Take a Screenshot of a window",
        ),
    Key([mod], "Print", lazy.spawn("peek"), desc="Record portion of screen"),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn([script + "music_ctrl.sh", "toggle"]),
        desc="Toggle pause",
    ),
    Key(
        [],
        "XF86AudioPause",
        lazy.spawn([script + "music_ctrl.sh", "toggle"]),
        desc="Toggle pause",
    ),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn([script + "music_ctrl.sh", "prev"]),
        desc="Prev song",
    ),
    Key(
        [],
        "XF86AudioNext",
        lazy.spawn([script + "music_ctrl.sh", "next"]),
        desc="Next song",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn([script + "volume_mute.sh"]),
        desc="Mute",
    ),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn(["brightnessctl", "s", "10%+"]),
        desc="Increase Brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn(["brightnessctl", "s", "10%-"]),
        desc="Decrease Brightness",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn(script + "volume_up.sh"),
        desc="Increase Volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn(script + "volume_down.sh"),
        desc="Decrease Volume",
    ),
    Key([mod], "space", lazy.spawn("rofi -show drun -lines 8 "), desc="Run Rofi"),
    Key(
        [mod, "mod1"], "x", lazy.spawn(script + "poweroff.sh"), desc="Run Rofi Poweroff"
    ),
]
# groups = [
#     Group(name=""),
#     Group(name=""),
#     Group(name=""),
#     Group(name=""),
#     Group(name=""),
#     Group(name="λ")
# ]
dropdown_defaults = {
    "y": 0.35,
    "x": 0.2,
    "width": 0.6,
}
groups = [
    Group(name="TERM"),
    Group(name="WEB"),
    # Group(name="CODE"),
    Group(name="UNI"),
    Group(name="NOTES"),
    ScratchPad(
        "ScratchPad",
        [
            DropDown("term", "kitty", **dropdown_defaults),
            DropDown(
                "music", "kitty -e " + script + "mpv_music.sh", **dropdown_defaults
            ),
            DropDown("vifm", "kitty -e vifm", **dropdown_defaults),
        ],
    ),
]
for i, group in enumerate(groups[:4], start=1):
    keys.extend(
        [
            Key(
                [mod],
                str(i),
                lazy.group[group.name].toscreen(toggle=True),
                desc="Switch to group {}".format(group.name),
            ),
            Key(
                [mod, "shift"],
                str(i),
                lazy.window.togroup(group.name),
                desc="Switch to & move focused window to group {}".format(
                    group.name),
            ),
        ]
    )
keys.extend(
    [
        Key([mod], "period", lazy.group["ScratchPad"].dropdown_toggle("term")),
        Key([mod], "m", lazy.group["ScratchPad"].dropdown_toggle("music")),
        Key([mod], "comma", lazy.group["ScratchPad"].dropdown_toggle("vifm")),
    ]
)
layout_defaults = {
    # "border_focus": "#C5C8C6",
    "border_focus": "#ffb52a",
    "border_normal": "#222222",
    "border_width": 2,
}

layouts = [
    # layout.Columns(name="𤋮", margin=4, **layout_defaults),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(name="󰹬", fair=False, border_on_single=True, **layout_defaults),
    layout.Max(name="󰊓"),
    layout.Slice(
        name="󰛽",
        fallback=layout.Max(**layout_defaults),
        match=Match(title=["HW"]),
        width=760,
    ),
    # layout.Matrix(),
    # layout.Floating(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(name="舘", **layout_defaults),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Fira Code SemiBold",
    fontsize=13,
    padding=4,
)
extension_defaults = widget_defaults.copy()

# THEME = {
#     # -------------------------------------------------------------------#
#     #                               COLORS                               #
#     # -------------------------------------------------------------------#
#     "secondary": "#ffb53a",
#     "background": "#FAFAFA",
#     "accent": "#37383D",
#     "foreground": "#222222",
#     "primary": "#ef990e",
#     "important": "#ff5338"
#     # -------------------------------------------------------------------#
#     #                                MISC                                #
#     # -------------------------------------------------------------------#
# }
SEP_SIZE = 28
ICON_SIZE = 18


def get_day_info():
    qtile.cmd_spawn(script + "get_day_info.sh")


default_bar = bar.Bar(
    [
        widget.Spacer(
            background=THEME["accent"], foreground=THEME["foreground"], length=10
        ),
        widget.CurrentLayout(
            background=THEME["accent"],
            foreground=THEME["foreground"],
            fontsize=20,
            padding=0,
        ),
        widget.Spacer(
            background=THEME["accent"], foreground=THEME["foreground"], length=10
        ),
        widget.TextBox(
            background=THEME["background"],
            foreground=THEME["accent"],
            text="",
            padding=0,
            fontsize=SEP_SIZE,
        ),
        widget.GroupBox(
            this_current_screen_border=THEME["secondary"],
            block_highlight_text_color=THEME["background"],
            active=THEME["foreground"],
            fontsize=12,
            highlight_method="block",
            rounded=False,
            disable_drag=True,
        ),
        widget.TextBox(
            background=THEME["background"],
            foreground=THEME["accent"],
            text="",
            padding=0,
            fontsize=SEP_SIZE,
        ),
        widget.Spacer(length=20),
        widget.WindowName(
            background=THEME["background"],
            foreground=THEME["foreground"],
            max_chars=100,
            format="{name}",
        ),
        widget.TextBox(
            background=THEME["background"],
            foreground=THEME["accent"],
            text="",
            padding=0,
            fontsize=SEP_SIZE,
        ),
        widget.Systray(background=THEME["background"]),
        widget.TextBox(text="", fontsize=ICON_SIZE),
        widget.Volume(
            mouse_callbacks={"Button3": lazy.spawn("pavucontrol")},
        ),
        widget.Spacer(length=2),
        widget.TextBox(
            background=THEME["background"],
            foreground=THEME["secondary"],
            text="",
            padding=0,
            fontsize=SEP_SIZE,
        ),
        widget.TextBox(
            background=THEME["secondary"],
            foreground=THEME["background"],
            text="",
            fontsize=ICON_SIZE,
        ),
        widget.Battery(
            low_background=THEME["important"],
            low_foreground=THEME["background"],
            background=THEME["secondary"],
            foreground=THEME["background"],
            format="{percent:2.0%}{char}",
            charge_char="+",
            discharge_char="",
            update_interval=20,
            notify_below=30,
        ),
        widget.TextBox(
            background=THEME["secondary"],
            foreground=THEME["primary"],
            text="",
            padding=0,
            fontsize=28,
        ),
        widget.Spacer(
            length=2,
            background=THEME["primary"],
            foreground=THEME["background"],
        ),
        widget.TextBox(
            text="",
            fontsize=ICON_SIZE,
            background=THEME["primary"],
            foreground=THEME["background"],
        ),
        widget.Clock(
            format="%d-%m-%Y",
            mouse_callbacks={"Button1": get_day_info},
            background=THEME["primary"],
            foreground=THEME["background"],
        ),
        widget.TextBox(
            background=THEME["primary"],
            foreground=THEME["accent"],
            text="",
            padding=0,
            fontsize=SEP_SIZE,
        ),
        widget.TextBox(
            text="󱑎",
            fontsize=ICON_SIZE,
            background=THEME["primary"],
            foreground=THEME["background"],
        ),
        widget.Clock(
            format="%I:%M %p",
            background=THEME["primary"],
            foreground=THEME["background"],
        ),
        widget.Spacer(
            length=10,
            background=THEME["primary"],
            foreground=THEME["background"],
        ),
    ],
    25,
    background=THEME["background"],
    margin=[6, 150, 6, 150],
)

screens = [
    Screen(top=default_bar, wallpaper=wallpaper, wallpaper_mode="fill"),
]

for monitor in range(1, monitors):
    screens.append(
        Screen(
            wallpaper=wallpaper,
            wallpaper_mode="fill"
            # top=default_bar,
        )
    )

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod, "shift"],
        "Button1",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="yad"),  # gitk
        # Match(wm_class="mpv"),  # gitk
        Match(wm_class="qalculate-gtk"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="pinentry-gtk-2"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    **layout_defaults,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
