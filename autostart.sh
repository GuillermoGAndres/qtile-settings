#!/bin/sh

# referencia: https://github.com/antoniosarosi/dotfiles/tree/master/.config/qtile

# systray volume
volumeicon &

# if you want tranparency and fancy looking things, install a compositor:
# picom &
feh --bg-scale ~/Pictures/fondos/estrellas.jpg &
# Para que funcione la tranparency y tambien hace que tenga efectos las ventanas (fade out)
picom &

# Para controlar la ilumninacion de la pantalla
# Al parecer es un proceso que no tiene que ser esperado por el padre, por lo tanto no se necesita el &.
# Se debe presionar click derecho al icono para que aparezca la ventatana
xfce4-power-manager

