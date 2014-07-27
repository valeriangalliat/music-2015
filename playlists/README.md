Playlists
=========

The `all` directory contains playlists for each genre, with a makefile
to generate them.

This very directory contains custom playlists.

To add a playlist to MPD, run the following:

```sh
cat playlist.m3u | mpc add
```

See `mpc add` options to control more precisely where you add the
playlist in your main playlist.
