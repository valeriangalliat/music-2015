Music
=====

> My personal music directory.

Description
-----------

This repository contains my whole music directory, including scripts to
download everything from YouTube and other sites.

YouTube is always deleting videos [due to copyright], so the scripts
will probably not retrieve everything. You can see errors from `dl.log`
in folders downloaded from YouTube channels or playlists. You can ask me
for a guest SSH access if you want to `rsync` the complete folder, but
it will be way slower than YouTube, so it's best to download the most
from YouTube at first.

[due to copyright]: http://ploum.net/im-a-pirate/

Most directories are generated using [youtube-dl]. Basically, the
`configure` script generates a `dl.mk` from all the `music.yaml` files
it finds, which is included by the makefile to download songs from
YouTube channels or playlists. The youtube-dl settings can be found
in `config.mk`.

[youtube-dl]: https://github.com/rg3/youtube-dl/

Basically, every song is downloaded with its YouTube ID as filename,
along with a `.info.json` file containing the YouTube metadata.

An `archive.log` is maintained in each directory by youtube-dl to
avoid downloading multiple times the same songs, and the output is
redirected to `dl.log`.

I don't track music and video files directly with Git since it takes
hundreds gigabytes and I don't believe Git is adapted for this kind
of storage. I look forward to use the awesome [IPFS](http://ipfs.io/)
for this when it will be ready! I also thought of BitTorrent, but it's
not suitable for a directory that changes that often. I'd like something
like an incremental torrent (what IPFS can shine at) but I don't know
any solution for this. Please tell me if you known a software or
protocol that can help! Actually, I'm `rsync`ing everything between my
computers using [these scripts](tools/sync).

Although, I'm tracking an `index` file which contains the path and song
title for every single music in this directory.

Building
--------

Everything is in the makefile:

<!-- BEGIN TASKS -->
| Task | Description |
| ---- | ----------- |
| `make all` |  Do all the below. |
| `make dl` |  Download the musics. |
| `make index` |  Build the musics index. |
| `make database` |  Build the MPD database. |
| `make playlists` |  Build the dynamic playlists. |
| `make readme` |  Update readme tasks table. |
<!-- END TASKS -->

Handling large channels
-----------------------

youtube-dl channel extractor uses the AJAX pagination from the web
interface that is limited to 1048 videos. By default, youtube-dl asks
YouTube to sort this pagination by date (thus getting the 1048 oldest
videos). This is a problem for large channels where the script will be
stuck with these videos, without downloading newer ones.

To fix this, I've written a patch for youtube-dl that removes the
sort, falling back to the default of "recent videos first":

```sh
sed -i 's/&sort=da//g' youtube_dl/extractor/youtube.py
```

A good workaround for channels with more than 1048 videos is to run the
download without the patch (to get oldest videos), then with the patch
(to get newer videos). Though, if the channel has more than 2096 videos,
I currently don't know any way to retrieve them missing videos, other
than contacting the channel author (I believe they have exhaustive
pagination in the YouTube admin page).

Index
-----

* [Playlists](playlists)
* [Tools](tools)
