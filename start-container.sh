#!/bin/sh

# note that dash is not always installed in /bin/dash
# but env is always in /usr/bin/env

# to make it easy, we serve static files from the current folder
# we just symlink the original source folder to the current directory
ln -s "$SOURCE_DOCKER" videos

git clone --depth=1 https://github.com/z5267282/mve.git && rm -rf mve/.git

npm run start
