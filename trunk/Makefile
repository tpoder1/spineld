
PREFIX=/
NAME=spineld
VERSION:=$(shell ./spineld -? | grep ver | cut -f2 -d:  | cut -f2 -d" ")
OWNER=root
GROUP=root
SBINDIR=$(PREFIX)/usr/sbin/
BINDIR=$(PREFIX)/usr/bin/
DOCDIR=$(PREFIX)/usr/share/doc/${NAME}-${VERSION}/
CFGDIR=$(PREFIX)/etc/
INITDIR=$(PREFIX)/etc/init.d/
INSTALL=install

all:

install:	
		mkdir -p $(SBINDIR) $(BINDIR) $(CFGDIR) 
		$(INSTALL) -o $(OWNER) -g $(GROUP) -m 755 spineld $(SBINDIR)
		$(INSTALL) -o $(OWNER) -g $(GROUP) -m 755 spinel $(BINDIR)
		$(INSTALL) -o $(OWNER) -g $(GROUP) -m 644 spineld.conf $(CFGDIR)

tar:
		rm -rfv dist
		rm -rfv $(NAME)-$(VERSION)
		mkdir $(NAME)-$(VERSION)
		# create documentation files
		pod2text < $(NAME) > spineld.txt
		pod2man < $(NAME) > spineld.1
		pod2html < $(NAME) > spineld.html
		# update version in specfile
		cp rdbackup.spec tmp.spec
		sed "s/%define version.*/%define version\t\t$(VERSION)/" < tmp.spec > rdbackup.spec
		rm tmp.spec
		# copy files into dist directory 
		cp spineld spinel spineld.conf init.d-spineld spined.spec Makefile $(NAME)-$(VERSION)
		mkdir dist
		tar -czvf dist/$(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)
		rm -rf $(NAME)-$(VERSION)

rpm: tar
		cp dist/$(NAME)-${VERSION}.tar.gz /usr/src/redhat/SOURCES/
		rm -rfv /var/tmp/rdbackup-buildroot
		rpmbuild -ba --clean rdbackup.spec
		cp /usr/src/redhat/SRPMS/$(NAME)-$(VERSION)-1.src.rpm dist
		cp /usr/src/redhat/RPMS/noarch/$(NAME)-$(VERSION)-1.noarch.rpm dist

dist: tar rpm 
		ls -al dist/*

publish: dist 
		scp rdbackup.html tpoder,rdbackup@web.sourceforge.net:htdocs/index.html
		rsync -avP  dist/ tpoder@frs.sourceforge.net:uploads/


