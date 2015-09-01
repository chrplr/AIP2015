#! /bin/bash
# Time-stamp: <2015-08-24 18:27 christophe@pallier.org>

PANDOC_OPTS := --standalone -S --toc --chapters -t slidy -c css/slidy.css

INPUT_MDS := $(wildcard *.md)

OUTPUT_HTML = $(INPUT_MDS:.md=-sol.html) $(INPUT_MDS:.md=-nosol.html)

.PHONY: all html clean

all: html

%-sol.md: %.md
	gpp  $< > $@

%-nosol.md: %.md
	gpp -D ANSWERS=1 $< > $@

html: $(OUTPUT_HTML)

%.html: %.md
	pandoc $(PANDOC_OPTS) $< -o $@

clean:
	@rm -f $(OUTPUT_HTML)
