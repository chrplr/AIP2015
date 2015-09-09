# Time-stamp: <2015-09-08 18:00 christophe@pallier.org>

PANDOC_OPTS := --standalone -S --toc 

INPUT_MDS := $(wildcard *.md)

OUTPUT_HTML = $(INPUT_MDS:.md=.html)

OUTPUT_PDF = $(INPUT_MDS:.md=.pdf)

.PHONY: all html clean pdf

all: html pdf


html: $(OUTPUT_HTML)


%.html: %.md
	pandoc $(PANDOC_OPTS) $< -o $@

pdf: $(OUTPUT_PDF)

%.pdf: %.md
	pandoc $< -o $@


clean:
	@rm -f $(OUTPUT_HTML) $(OUTPUT_PDF)
