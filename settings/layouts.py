# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

from libqtile import layout
from settings.theme import colors

# Layouts and layout rules


layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 3
}

layouts = [    
    layout.Max(**layout_conf),
    layout.Stack(num_stack=2, margin=5, border_width=1, border_focus=colors['focus'][0]),
    layout.MonadTall(margin=10, border_width=1,border_focus=colors['focus'][0]),
    layout.MonadWide(margin=10, border_width=1,border_focus=colors['focus'][0]),
    layout.RatioTile(**layout_conf),   
    # layout.Matrix(columns=2, **layout_conf),
    layout.Columns(num_columns=1, margin=20, split=False, border_width=5,border_focus=colors['focus'][0]),
    # layout.Bsp(**layout_conf),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        {'wmclass': 'confirm'},
        {'wmclass': 'dialog'},
        {'wmclass': 'download'},
        {'wmclass': 'error'},
        {'wmclass': 'file_progress'},
        {'wmclass': 'notification'},
        {'wmclass': 'splash'},
        {'wmclass': 'toolbar'},
        {'wmclass': 'confirmreset'},
        {'wmclass': 'makebranch'},
        {'wmclass': 'maketag'},
        {'wname': 'branchdialog'},
        {'wname': 'pinentry'},
        {'wmclass': 'ssh-askpass'},
    ],
    border_focus=colors["color4"][0]
)
