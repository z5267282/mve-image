#!/usr/bin/env dash

# note that dash is not always installed in /bin/dash
# but env is always in /usr/bin/env

# softlink mounted files to public folder of server
[ -L videos ] || ln -s /mnt/videos videos

npm run dev
