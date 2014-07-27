ROOT = ../..
OGG = -name '*.ogg'
ABS = sed 's/^\.\.\/\.\./codejam/'

default:

ALL += funk.m3u
funk.m3u: force
	find $(ROOT)/funk $(OGG) | $(ABS) > $@

ALL += rock.m3u
rock.m3u: force
	find $(ROOT)/rock $(OGG) | $(ABS) > $@

ALL += reggae.m3u
reggae.m3u: force
	find $(ROOT)/reggae $(OGG) | $(ABS) > $@

ALL += electro.m3u
electro.m3u: force
	find $(ROOT)/electro $(OGG) | $(ABS) > $@

ALL += rap.m3u
rap.m3u: force
	find $(ROOT)/rap $(OGG) | $(ABS) > $@

all: $(ALL)

force:
