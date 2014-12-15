Car
===

This Rakefile will, for all defined playlists, deploy all musics in
`DESTDIR`, slugifying the song title as filename, and converting in MP3
because my FM transmitter can only read MP3 files.

```sh
rake DESTDIR=/mnt
```

It will build only the files that don't already exist in `DESTDIR`, so
the command is the same when you just want to update the storage
when the actual playlists have changed.
