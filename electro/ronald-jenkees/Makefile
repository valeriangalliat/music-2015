TOOLS = ../../tools

DL_OVERWRITE = $(TOOLS)/dl/dl-dir-log-overwrite

default:

ALL += ronald-jenkees
ronald-jenkees: force
	$(DL_OVERWRITE) $@ https://www.youtube.com/playlist?list=PL1iXN06gcIUaqyzIH1H4sRhJJzr-qli3G

ALL += disorganized-fun
disorganized-fun: force
	$(DL_OVERWRITE) $@ https://www.youtube.com/playlist?list=PL1iXN06gcIUbohj6OejyfI-4IJwt0owE2

ALL += days-away
days-away: force
	$(DL_OVERWRITE) $@ https://www.youtube.com/playlist?list=PL1iXN06gcIUYjLwnOJLvC5T-RpCNOZ3f9

ALL += sts9-collab.mp3
sts9-collab.mp3:
	youtube-dl -o $@ https://soundcloud.com/sskaar/ronald-jenkees-sts9-collab

all: $(ALL)

force:
