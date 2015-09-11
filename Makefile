# recursive make: runs make in all the immediate subdirs
# Time-stamp: <2015-09-11 11:55 christophe@pallier.org>
 
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
	pandoc -s -S -c pandoc.css $< -o $@

index.html: index.md
	pandoc -s -S $< -o $@


index.md:
	echo "<h1>Atelier d'Introduction a la Programmation AIP2015</h1>" > index.md
	echo 'Generated on ' $$( LANG=EN date ) 'by <christophe@pallier.org>' >> index.md
	echo '' >> index.md
	echo '(these pages maybe outdated; the latest version is always available in a git repository at <https://github.com/chrplr/AIP2015>)' >> index.md
	echo '' >> index.md
	echo '<a href="README.html">README first (course description)</a>' >> index.md
	echo "<h1>>HTML files:</h1>" >> index.md
	for f in `find -name '*.html' | sort `; do \
		echo "* <a href="$$f">$$f</a>"; \
	done >> index.md
	echo "<h1>>PDFs:</h1>" >> index.md
	for f in `find -name '*.pdf' | sort `; do \
		echo "* <a href="$$f">$$f</a>"; \
	done >> index.md

#putonftp:
#	ncftpput ...

