# recursive make: runs make in all the immediate subdirs
# Time-stamp: <2015-08-24 10:55 christophe@pallier.org>
 
SHELL=/bin/bash

SUBDIRS := $(wildcard */.)

all:
	@for a in $(SUBDIRS); do \
		if [ -f $$a/Makefile ]; then \
			echo "processing folder $$a"; \
			$(MAKE) -C $$a; \
		fi; \
	done;
	@echo "Done!"
