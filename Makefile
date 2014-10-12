.include "config.mk"

all:
	@echo 'There'\''s no `all` target.'
	@echo
	@echo '`make dl`: Download the musics.'
	@echo '`make index`: Build the musics index.'
	@echo '`make database`: Build the MPD database.'
	@echo '`make playlists`: Build the dynamic playlists.'

.include "dl.mk"

index: force
	tools/index > $@

database: force
	tools/mpdb > $@

playlists: force
	playlists/build

readme: README.md

README.md: force
	cat $@ | tools/process-readme > $@.new
	mv $@.new $@

force:
