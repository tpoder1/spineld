
PREFIX=/
NAME=spineld
VERSION:=$(shell ./spineld -? | grep ver | cut -f2 -d:  | cut -f3 -d" ")
OWNER=root
GROUP=root
SBINDIR=$(PREFIX)/usr/sbin/
BINDIR=$(PREFIX)/usr/bin/
DOCDIR=$(PREFIX)/usr/share/doc/${NAME}-${VERSION}/
CFGDIR=$(PREFIX)/etc/
INITDIR=$(PREFIX)/etc/init.d/
MANDIR=$(PREFIX)/usr/share/man/man1/
DOCDIR=$(PREFIX)/usr/share/doc/${NAME}-${VERSION}/
INSTALL=install

all:

install:	
		mkdir -p $(SBINDIR) $(BINDIR) $(CFGDIR) $(DOCDIR) $(MANDIR)
		$(INSTALL) -o $(OWNER) -g $(GROUP) -m 755 spineld $(SBINDIR)
		$(INSTALL) -o $(OWNER) -g $(GROUP) -m 755 spinel $(BINDIR)
		$(INSTALL) -o $(OWNER) -g $(GROUP) -m 644 spineld.conf $(CFGDIR)
		$(INSTALL) -o $(OWNER) -g $(GROUP) -m 644 spineld.1 $(MANDIR)
		$(INSTALL) -o $(OWNER) -g $(GROUP) -m 644 spinel.1 $(MANDIR)
		$(INSTALL) -o $(OWNER) -g $(GROUP) -m 644 spineld.txt $(DOCDIR)

tar:
		rm -rfv dist
		rm -rfv $(NAME)-$(VERSION)
		mkdir $(NAME)-$(VERSION)
		# create documentation files
		pod2text < $(NAME) > spineld.txt
		pod2man < $(NAME) > spineld.1
		pod2man < $(NAME) > spinel.1
		pod2html < $(NAME) > spineld.html
		# update version in specfile
		cp spineld.spec tmp.spec
		sed "s/%define version.*/%define version\t\t$(VERSION)/" < tmp.spec > spineld.spec
		rm tmp.spec
		# copy files into dist directory 
		cp spinel spineld spineld.conf init.d-spineld spineld.spec spineld.html spinel.1 spineld.1 spineld.txt Makefile $(NAME)-$(VERSION)
		mkdir dist
		tar -czvf dist/$(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)
		rm -rf $(NAME)-$(VERSION)

rpm: tar
		cp dist/$(NAME)-${VERSION}.tar.gz /usr/src/redhat/SOURCES/
		rm -rfv /var/tmp/spineld-buildroot
		rpmbuild -ba --clean spineld.spec
		cp /usr/src/redhat/SRPMS/$(NAME)-$(VERSION)-1.src.rpm dist
		cp /usr/src/redhat/RPMS/noarch/$(NAME)-$(VERSION)-1.noarch.rpm dist

dist: tar rpm 
		ls -al dist/*

publish: dist 
		scp rdbackup.html tpoder,rdbackup@web.sourceforge.net:htdocs/index.html
		rsync -avP  dist/ tpoder@frs.sourceforge.net:uploads/


