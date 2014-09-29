.include "config.mk"

all:
	@echo 'There'\''s no `all` target.'
	@echo
	@echo '`make dl`: Download the musics.'
	@echo '`make index`: Build the musics index.'
	@echo '`make playlists`: Build the dynamic playlists.'

.include "dl.mk"

index: force
	tools/index > $@

playlists: force
	playlists/build

force:
