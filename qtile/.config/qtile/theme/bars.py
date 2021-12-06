from libqtile import bar, widget
from theme.colors import gruvbox
import os
import subprocess

widget_defaults = dict(
    font='Iosevka Nerd Font',
    fontsize=16,
    padding=3,
    background = gruvbox['bg'],
    foreground = gruvbox['fg'],
)
extension_defaults = widget_defaults.copy()

def draw_arrow_right(bg,fg,font_size=24):
    "Creates a textbox widget with a right-pointing arrow."
    return widget.TextBox(text="",
                          padding=0,
                          fontsize=font_size,
                          background=bg,
                          foreground=fg)

def draw_arrow_left(bg,fg,font_size=24):
    "Creates a textbox widget with a right-pointing arrow."
    return widget.TextBox(text="\ue0b2",
                          padding=0,
                          fontsize=font_size,
                          background=bg,
                          foreground=fg)

mainbar = bar.Bar([
    widget.GroupBox(disable_drag=True),
    widget.Chord(),
    widget.PulseVolume(emoji=True, fontsize=14), 
    widget.GenPollText(update_interval=None, func=lambda: subprocess.check_output(os.path.expanduser("~/.dotfiles/qtile/.config/qtile/scripts/printvol.sh")).decode('utf-8')),
    ], 33, background=gruvbox['bg'])
