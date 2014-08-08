Tools
=====

[`dl`](dl)
----------

This directory contain all download helpers used by makefiles in music
directories, to retrieve and convert music from YouTube and other sites
using `youtube-dl`.

There's a way to log `youtube-dl` output in a `dl.log` file, overwriting
it or appending content.

[`sync`](sync)
--------------

This are the scripts I use to `rsync` the whole music directory between
my computers.

[`mpdignore`](mpdignore)
------------------------

A simple script used by `dl/dl-dir` to link the main `.mpdignore` file
in all subdirectories (because MPD wants a `.mpdignore` per directory).

[`update`](update)
------------------

This script will update the MPD database to add music titles from
`.info.json` files. See the header comment for more.

[`youtube-check`](youtube-check)
--------------------------------

Checks if the number of Ogg files in the current directory equals
the total number of items in `dl.log`. Otherwise, print numbers and grep
for errors.
