MAKE             = /usr/bin/make
RST2HTML         = rst2html.py
STYLESHEET       = stylesheet.css
RST2HTML_OPTIONS = --strip-comments             \
                   --report=3                   \
                   --no-doc-title               \
                   --no-toc-backlinks           \
                   --cloak-email-addresses      \
	               --stylesheet=$(STYLESHEET)   \
                   --link-stylesheet

SUBDIRS = spine style simple image grid one-line showcase voronoi

all: index.html

%.rst: $(SUBDIRS)
	@./make-figures.py

%.html: %.rst
	@echo "Building $@"
	@$(RST2HTML) $(RST2HTML_OPTIONS) $< $@

$(SUBDIRS):
	@echo "Building all in $@"
	@$(MAKE) -f ../Makefile.sub -C $@

clean:
	@for d in $(SUBDIRS); do (cd $$d; $(MAKE) -f ../Makefile.sub clean ); done

distclean: clean
	@-rm -f `find . -name "*~"`
	@-rm -f `find . -name "*.pyc"`

.PHONY: all clean distclean $(SUBDIRS)
