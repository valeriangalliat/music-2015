ffmpeg -i  iUXviay0Yw4.mp4 -acodec copy -vn iUXviay0Yw4.m4a
for musics deleted from youtube where i have the mp4

trim ogg files:
mp3splt -r -p th=-72 foo.ogg

will trim foo.ogg with a threshold of -72 dB (which is lower than the
default value to be sure to trip only "real" blank without alteratr fades.
after testing, seems a right value, but will not trim recorded blank.

funk missing:

D8VgzmRfOug.ogg
0v2hhFTl3GE.ogg
brPWoxqInxQ.ogg
TjokhrUxrs4.ogg
z2Msz2sKCHc.ogg
7dDRsbG6R5A.ogg
Lm-MrQleVPY.ogg

see error logs for info
