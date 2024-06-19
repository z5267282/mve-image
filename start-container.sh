#!/bin/sh

# note that dash is not always installed in /bin/dash
# but env is always in /usr/bin/env

# TODO: SOFTLINK this from mve.py
[ -L videos ] || ln -s /mnt/videos videos

npm run start
