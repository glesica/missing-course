INPUTS := $(shell find . -type f -name '*.original.jpg')
OUTPUTS := $(INPUTS:.original.jpg=.thumb.jpg)

# Size of the thumbnails to be created.
SIZE := $(shell cat thumb-size.txt)

# The first target listed in the file is treated as the default target and will
# be run if `make` is invoked without a target name. In this case, the default
# behavior is to create thumbnails, one for each input matched by the `find`
# command above.
.PHONY: build
build: ${OUTPUTS}

# This is a conventional target that removes output files to return the working
# directory to its pristine state. After this target has been run, the `build`
# target should run as though it were running for the first time.
.PHONY: clean
clean:
	@rm -f ${OUTPUTS}

# This target transforms an original image and a file containing the thumbnail
# size into a thumbnail image. The size is stored in a file so that it can be
# used as a prerequisite. This way, if you decide to change the thumbnail size,
# all existing thumbnails will be regenerated.
%.thumb.jpg: %.original.jpg thumb-size.txt
	@echo "resizing $<"
	@convert -resize ${SIZE}x${SIZE} $< $@

