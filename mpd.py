#!/usr/bin/env python3

'''Usage: mpdpg [options] [<dir>]

Arguments:
  <dir>  Music directory [default: .].
'''

import docopt
import json
import os
import os.path
import subprocess
import sys


def duration(file):
    args = ['ffprobe', '-show_format', '-v', 'quiet', file]

    p = subprocess.Popen(args, stdout=subprocess.PIPE,
                         universal_newlines=True)

    time = None

    for line in p.stdout:
        try:
            k, v = line.strip().split('=')
        except:
            continue

        if k == 'duration':
            time = int(float(v))
            break

    code = p.wait()

    if code != 0:
        raise subprocess.CalledProcessError(code)

    if time is None:
        raise Exception('`duration` not found')

    return time


def title(file):
    info = os.path.splitext(file)[0] + '.info.json'
    return json.load(open(info))['title']


def walk(dir, root=None):
    if root is None:
        root = dir

    for file in os.listdir(dir):
        file = os.path.join(dir, file)

        if os.path.isdir(file):
            base = file[len(root) + 1:]

            print('directory:', os.path.basename(base))
            print('mtime:', int(os.path.getmtime(file)))
            print('begin:', base)

            walk(file, root)

            print('end:', base)

            continue

        try:
            time = duration(file)
        except:
            continue

        print('song_begin:', os.path.basename(file))
        print('Time:', time)

        try:
            print('Title:', title(file))
        except:
            pass

        print('mtime:', int(os.path.getmtime(file)))
        print('song_end')


def main():
    args = docopt.docopt(__doc__, version='0.1')
    dir = os.path.realpath(args['<dir>'] or '.')

    print('info_begin')
    print('format: 1')
    #print('mpd_version: ')
    print('fs_charset: UTF-8')
    print('tag: Title')
    print('info_end')

    walk(dir)


if __name__ == '__main__':
    main()
