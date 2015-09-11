# Time-stamp: <2015-09-11 11:32 christophe@pallier.org>

#PANDOC_OPTS := --standalone -S --toc -t slidy -V slidy-url=../css 
PANDOC_OPTS :=  -s -S -c pandoc.css --toc

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
	pandoc -s $< -o $@

clean:
	@rm -f $(OUTPUT_HTML) $(OUTPUT_PDF)
