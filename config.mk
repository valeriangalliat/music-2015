YOUTUBE_DL = ~/opt/youtube-dl/youtube_dl/__main__.py

YOUTUBE_DL_FLAGS += --extract-audio
YOUTUBE_DL_FLAGS += --id
YOUTUBE_DL_FLAGS += --ignore-errors
YOUTUBE_DL_FLAGS += --no-progress
YOUTUBE_DL_FLAGS += --write-info-json
YOUTUBE_DL_FLAGS += --download-archive archive.log
