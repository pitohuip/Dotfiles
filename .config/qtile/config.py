##   IMPORTS   ##
import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder

##   VARIABLES   ##
mod = "mod4"
myTerm = "alacritty"      # My terminal of choice
myBrowser = "firefox" # My browser of choice

##   KEYBINDINGS   ##
keys = [
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch my terminal"),
    Key([mod, "shift"], "Return", lazy.spawn("dmenu_run"), desc='Run Launcher'),
    Key(["control", "shift"], "e", lazy.spawn("emacsclient -c"), desc='Doom Emacs'),
    Key([mod], "b", lazy.spawn(myBrowser), desc='Launch firefox'),

    Key([mod, "shift"], "c", lazy.window.kill(), desc='Kill active window'),
    Key([mod, "shift"], "q", lazy.shutdown(), desc='Shutdown Qtile'),

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
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
#    Key(
#        [mod, "shift"],
#        "Return",
#        lazy.layout.toggle_split(),
#        desc="Toggle between split and unsplit sides of stack",
#    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

##   WORKSPACES   ##
groups = [Group("DEV", layout='monadtall'),
          Group("WWW", layout='monadtall'),
          Group("www", layout='monadtall'),
          Group("SYS", layout='monadtall'),
          Group("DOC", layout='monadtall'),
          Group("VBOX", layout='monadtall'),
          Group("CHAT", layout='monadtall'),
          Group("MUS", layout='monadtall'),
          Group("VID", layout='monadtall'),
          Group("GFX", layout='floating')]

dgroups_key_binder = simple_key_binder("mod4")

##   WINDOW STYLE IN LAYOUTS   ##
layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(
        border_width=2,
        border_focus="e1acff",
        border_normal="1D2330"
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

##   BAR   ##
widget_defaults = dict(
    font="JetbrainsMono Nerd Font Bold",
    fontsize=16,
    padding=6,
    background="#1a1b26"
)
extension_defaults = widget_defaults.copy()

def left_arrow(background_color, color2):
    return widget.TextBox(
        text = '\uE0B2',
        background = background_color,
        foreground = color2,
        fontsize=28,
        padding=0
    )

screens = [
    Screen(
        top=bar.Bar(
            [

                #widget.Memory(fmt = 'Mem: {}', padding = 5),

                widget.GroupBox(
                    font = "JetbrainsMono Nerd Font Medium",
                    fontsize = 14,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 15,
                    borderwidth = 3,
                    active = "#ffffff",
                    rounded = False,
                    highlight_method = "line",
                ),
                widget.CurrentLayout(),
                widget.Prompt(),
                widget.WindowName(),
                #widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                #widget.TextBox("my config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                #widget.Systray(),
                #widget.QuickExit(),
                #widget.HDDBusyGraph(),
                widget.Net(
                    interface = "enp0s3",
                    format='{down} {up}',
                    prefix='k',
                    foreground="#F7768E",
                    fontshadow="#000000",
                ),
                left_arrow("#1a1b26", "#2b2f40"),
                widget.OpenWeather(
                    location='Tyumen',
                    format="﨎 {temp}º{units_temperature}",
                    foreground="#39D7E5",
                    background="#2b2f40",
                    fontshadow="#000000",
                ),
                left_arrow("#2b2f40", "#1a1b26"),
                widget.Clock(
                    format="羽 %a %b %d - %R",
                    foreground="#9ECE6A",
                    fontshadow="#000000",
                ),
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            #margin=[5, 8, 0, 8]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

wmname = "LG3D"
