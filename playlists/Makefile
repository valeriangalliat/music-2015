ROOT = ..
OGG = -name '*.ogg'
ABS = sed 's/^\.\./codejam/'

default: all

ALL += all-funk.m3u
all-funk.m3u: force
	find $(ROOT)/funk $(OGG) | $(ABS) > $@

ALL += all-rock.m3u
all-rock.m3u: force
	find $(ROOT)/rock $(OGG) | $(ABS) > $@

ALL += all-rock-n-roll.m3u
all-rock-n-roll.m3u: force
	find $(ROOT)/rock-n-roll $(OGG) | $(ABS) > $@

ALL += all-reggae.m3u
all-reggae.m3u: force
	find $(ROOT)/reggae $(OGG) | $(ABS) > $@

ALL += all-electro.m3u
all-electro.m3u: force
	find $(ROOT)/electro $(OGG) | $(ABS) > $@

ALL += all-rap.m3u
all-rap.m3u: force
	find $(ROOT)/rap $(OGG) | $(ABS) > $@

ALL += all-classical.m3u
all-classical.m3u: force
	find $(ROOT)/classical $(OGG) | $(ABS) > $@

all: $(ALL)

force:
