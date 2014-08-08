Music
=====

My personal music directory.

Description
-----------

This repository contains my whole music directory, including scripts to
download everything from YouTube and other sites.

YouTube is always deleting videos [due to
copyright](http://ploum.net/im-a-pirate/), so the scripts will probably
not retrieve everything. You can see errors from `dl.log` in folders
downloaded from YouTube channels or playlists. You can ask me for a
guest SSH access if you want to `rsync` the complete folder, but it will
be way slower than YouTube, so it's best to download the most from
YouTube at first.

Most directories are generated using
[`youtube-dl`](https://github.com/rg3/youtube-dl/). I've some download
helpers in `tools/dl` that will convert all videos to Ogg files, and
dump video informations in a `.info.json` file. Also, if a target file
is already present, `youtube-dl` is configured to not download it again.
The only problem with the last point is that it will still download the
informations page before finding out that it was already downloaded, so
it takes a little time to incrementally download new stuff.

I don't track music and video files directly with Git since it takes
hundreds gigabytes and I don't believe Git is adapted for this kind
of storage. I look forward to use the awesome [IPFS](http://ipfs.io/)
for this when it will be ready! I also thought of BitTorrent, but it's
not suitable for a directory that changes that often. I'd like something
like an incremental torrent (what IPFS can shine at) but I don't know
any solution for this. Please tell me if you known a software or
protocol that can help! Actually, I'm `rsync`ing everything between my
computers using [these scripts](tools/sync).

Checking integrity
------------------

In a YouTube download directory, to check if all the videos were
retrieved, run the following:

```sh
echo 'Number of songs in the directory:'
find . -name '*.ogg' | wc -l
echo 'Number of songs in the playlist/channel:'
grep 'Downloading video #' dl.log | awk '{print $NF; exit}'
```

Index
-----

* [Playlists](playlists)
* [Tools](tools)
