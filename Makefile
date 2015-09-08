# recursive make: runs make in all the immediate subdirs
# Time-stamp: <2015-09-08 17:46 christophe@pallier.org>
 
SHELL=/bin/bash

SUBDIRS := $(wildcard */.)

all: README.html index.html
	@for a in $(SUBDIRS); do \
		if [ -f $$a/Makefile ]; then \
			echo "processing folder $$a"; \
			$(MAKE) -C $$a; \
		fi; \
	done;

README.html: README.md
	pandoc $< -o $@

index.html: index.md
	pandoc $< -o $@


index.md:
	echo "<h1>>HTML files:</h1>" > index.md
	for f in `find -name '*.html' | sort `; do \
		echo "* <a href="$$f">$$f</a>"; \
	done >> index.md
	echo "<h1>>PDFs:</h1>" >> index.md
	for f in `find -name '*.pdf' | sort `; do \
		echo "* <a href="$$f">$$f</a>"; \
	done >> index.md

aga:
	#	echo "* [$$f]($$f)"; 

