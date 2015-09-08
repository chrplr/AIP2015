#
# Makefile for creating HTML.
#
# Pandoc is used for the conversion. Thanks to Olivier Couet for the Markdown
# ROOT documentation generation scripts.
#

PANDOC_OPTS := --standalone -S --toc --chapters -t slidy -c css/slidy.css
PANDOC_OPTS_INDEX := --standalone -S -t slidy -c css/slidy.css

INPUT_MDS := command_line.md

INDEX_MD := index.md
INDEX_HTML := index.html

OUTPUT_HTML = $(INPUT_MDS:.md=.html)

.PHONY: all html clean

all: html

html: idx $(OUTPUT_HTML)

idx:
	@echo Generating HTML index
	@(echo "Index" > $(INDEX_MD) ; \
	  echo "=====" >> $(INDEX_MD) ; \
	  echo "" >> $(INDEX_MD) ; \
	  for Md in $(INPUT_MDS) ; do \
	    echo "1. [$$(head -n1 $$Md)]($${Md%.*}.html)" ; \
	  done >> $(INDEX_MD) )
	@pandoc $(PANDOC_OPTS_INDEX) $(INDEX_MD) -o $(INDEX_HTML)

%.html: %.md
	@echo Generating HTML: $@
	pandoc $(PANDOC_OPTS) $< -o $@

clean:
	@echo Cleaning up
	@rm -f $(OUTPUT_HTML) $(INDEX_MD) $(INDEX_HTML)
