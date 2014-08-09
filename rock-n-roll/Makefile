TOOLS = ../tools

DL_OVERWRITE = $(TOOLS)/dl/dl-dir-log-overwrite

default:

ALL += beatles
beatles: force
	$(DL_OVERWRITE) $@ https://www.youtube.com/playlist?list=PLE4AD9E497212EBC0

ALL += val
val: force
	$(DL_OVERWRITE) $@ https://www.youtube.com/playlist?list=PL3gQ6-WYh7kWJLS9Q9bt0wQzLFewnvL3F

all: $(ALL)

force:
