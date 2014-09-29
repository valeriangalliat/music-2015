.include "config.mk"

all:
	@echo 'There'\''s no `all` target.'
	@echo
	@echo '`make dl`: Download the musics.'
	@echo '`make index`: Build the musics index.'

.include "dl.mk"

index:
	tools/index > $@

force:
