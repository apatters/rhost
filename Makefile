prefix	?= $(HOME)
DESTDIR	?= /
PYTHON	?= python2

all:
	$(PYTHON) setup.py build

install:
	$(PYTHON) setup.py install --prefix=$(prefix) --root=$(DESTDIR) --force

clean:
	rm -rf .pybuild/
	rm -rf build/
	rm -f debian/files
	rm -f debian/*.postinst.debhelper
	rm -f debian/*.prerm.debhelper
	rm -f debian/*.substvars
	rm -f debian/*.debhelper.log
	rm -rf debian/rhost/
	rm -f debian/debhelper-build-stamp

.PHONY: all install clean
