# This Makefile knows how to build the various
# pieces of this repo, including converting
# Markdown to HTML.

README_INPUTS := $(shell find . -type f -name README.md)
README_OUTPUTS := $(README_INPUTS:README.md=index.html)

.PHONY: build
build: readmes

.PHONY: readmes
readmes: ${README_OUTPUTS}

.PHONY: serve
serve:
	@echo "Serving on http://localhost:8080"
	@echo "Use ctrl-c to terminate the server"
	@python3 -m http.server 8080

.PHONY: debug
debug:
	@echo "README_INPUTS  = ${README_INPUTS}"
	@echo "README_OUTPUTS = ${README_OUTPUTS}"

index.html: README.md
	@pandoc -o "$@" "$<"

%/index.html: %/README.md
	@pandoc -o "$@" "$<"

