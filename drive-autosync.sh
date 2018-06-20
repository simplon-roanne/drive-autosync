#!/bin/bash

source ~/.bashrc

pid=$(pgrep gnome-session | head -n 1)
dbus=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$pid/environ | sed 's/DBUS_SESSION_BUS_ADDRESS=//' )
export DBUS_SESSION_BUS_ADDRESS=$dbus

export DISPLAY=:0

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

python ${DIR}/drive-autosync.py >> ~/drive-autosync.log
