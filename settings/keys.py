# https://github.com/antoniosarosi/dotfiles
# https://gist.github.com/cjbarnes18/4151805

# Qtile keybindings
# Mod+shift + {1,3,4,5,6} Mueves tu programa a otro workspace dependiendo del numero ingresado.
#-----------

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4" # Tecla de windows
alt = "mod1" # Tecla alt
ctl = "control"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    #([mod], "j", lazy.layout.down()),
    #([mod], "k", lazy.layout.up()),
    ([mod], "F11", lazy.window.toggle_fullscreen()),
    #Switch window focus toother pane of stack
    #([mod], "Tab", lazy.layout.next()),
    #([mod, "shift"], "Tab", lazy.layout.up()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "h", lazy.layout.previous()),
    ([mod], "l", lazy.layout.next()),

    ([mod ,alt], "h", lazy.layout.left()),
    ([mod ,alt], "l", lazy.layout.right()),

    ([mod], "Tab", lazy.group.next_window()),

    # Usarlo solo cuando es frotante, mueve la ventana hasta enfrente.
    ([mod, "shift"], "Tab", lazy.window.bring_to_front() ),

    # These are unique to stack layout
    #--------------------------------------------------  
    # Para colocar una window del otro lado.
    ([mod, alt], "l", lazy.layout.client_to_next()),
    ([mod, alt], "h", lazy.layout.client_to_previous()),
     # Split (stack)
    ([mod, "shift"], "Return", lazy.layout.toggle_split()),
     #Swap pane of split (stack)
    ([mod, "shift"], "space", lazy.layout.rotate()),

    #([mod, alt], "space", lazy.layout.add()),
    #([mod, alt, "shift"], "space", lazy.layout.delete()),
    ([mod, "control"], "h", lazy.layout.add()),
    ([mod, "control"], "l", lazy.layout.delete()),
    #--------------------------------------------------  

    # (MonadTall) 
    #--------------------------------------------------  
    # Change window sizes 
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),
    # Move windows up or down in current toggle (stack) or monatall
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    ([mod, ctl], "space", lazy.layout.flip()),
    ([mod, ctl], "m", lazy.layout.maximize()),
    ([mod, ctl], "n", lazy.layout.normalize()),

    # Examples:
    # ([mod, ctl], "k", lazy.layout.shrink().when('xmonad-tall')),
    # ([mod, ctl], "j",  lazy.layout.grow().when('xmonad-tall')),
    # ([mod, "shift"], "j", lazy.layout.shuffle_down().when('xmonad-tall')),
    # ([mod, "shift"], "k", lazy.layout.shuffle_up().when('xmonad-tall')),
    #-------------------------------------------------- 
    # Mueve el programa
    #([mod], "space", lazy.layout.client_to_next()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Toggle between different layouts as defined below
    ([mod],"Right", lazy.next_layout()),
    ([mod], "Left", lazy.prev_layout()),
    
    # Aumenta y baja la opacidad
    ([mod, alt],"Up", lazy.window.up_opacity()),
    ([mod, alt],"Down", lazy.window.down_opacity()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ([mod, "control"], "space", lazy.window.toggle_fullscreen()),

    # Change workspace
    ([mod, "control"], "Right", lazy.screen.next_group()),
    ([mod, "control"], "Left", lazy.screen.prev_group()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "f", lazy.spawn("firefox")),

    # File Explorer
    # ([mod], "e", lazy.spawn("pcmanfm")),
    ([mod], "e", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift (cambia el brillo a modo-lectura para las noches)
    ([mod], "r", lazy.spawn("redshift -O 4400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot -e 'mv $f ~/Pictures/scrot' ")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
