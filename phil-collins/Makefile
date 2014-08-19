TOOLS = ../tools

DL_OVERWRITE = $(TOOLS)/dl/dl-dir-log-overwrite

default:

ALL += top-100
top-100: force
	$(DL_OVERWRITE) $@ https://www.youtube.com/playlist?list=PL07B1DB028D800C8D

ALL += val
val: force
	$(DL_OVERWRITE) $@ https://www.youtube.com/playlist?list=PL3gQ6-WYh7kWX5RgFLDtly7Sw8Fnj0VQW

all: $(ALL)

force:
