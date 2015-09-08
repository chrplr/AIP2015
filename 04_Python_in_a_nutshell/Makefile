# Time-stamp: <2015-09-08 13:06 christophe@pallier.org>

PANDOC_OPTS := --standalone -S --toc -t slidy -V slidy-url=../css

INPUT_MDS := $(wildcard *.md)

OUTPUT_HTML = $(INPUT_MDS:.md=-sol.html) $(INPUT_MDS:.md=-nosol.html)

OUTPUT_PDF = $(INPUT_MDS:.md=-sol.pdf) $(INPUT_MDS:.md=-nosol.pdf)

.PHONY: all html clean pdf

all: html pdf

%-nosol.md: %.md
	gpp  $< > $@

%-sol.md: %.md
	gpp -D ANSWERS=1 $< > $@

html: $(OUTPUT_HTML)


%.html: %.md
	pandoc $(PANDOC_OPTS) $< -o $@

pdf: $(OUTPUT_PDF)

%.pdf: %.md
	pandoc $< --toc -o $@


clean:
	@rm -f $(OUTPUT_HTML) $(OUTPUT_PDF)
