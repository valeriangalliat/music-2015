Tools
=====

[play](play)
------------

Remotely play a [playlist](../playlists) from YouTube with MPlayer.
[youtube-dl] is needed to get stream from YouTube.

[youtube-dl]: https://github.com/rg3/youtube-dl/

Play 42 songs from shuffled funk playlist:

```sh
cat ../playlists/funk.m3u \
    | shuf \
    | head -42 \
    | ./play
```

Use playlist from GitHub:

```sh
curl -s https://raw.githubusercontent.com/valeriangalliat/music/master/playlists/funk.m3u \
    | shuf \
    | ./play
```

Note videos are regularly deleted from YouTube, so they won't all be
available. I need to setup a mirror from my server to fallback when
a video was censored.

[index](index)
--------------

Find all the musics from the current directory and outputs the filename
followed by the title from `.info.json` file.

[mpdb](mpdb)
------------

Build the [MPD] database from all the files having a corresponding
`.info.json` in the current (or given) directory.

[MPD]: http://www.musicpd.org/

[cjdb](cjdb)
------------

Prefix all directories from MPD playlist in stdin with `codejam/`.

[cjdb](cjdb)
------------

Convert stdin MPD database to old format (for Debian Wheezy MPD
version). It's just the matter of changing the database header.

[process-readme](process-readme)
--------------------------------

Dynamically fill the tasks table from stdin readme.

[sync](sync)
------------

This are the scripts I use to rsync the whole music directory between
my computers.

[car](car)
----------

A Rakefile to deploy playlists I listen in my car.
