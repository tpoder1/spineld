%define name		spineld
%define version		1.03
%define release		1

Name:				%{name}
Summary:			Daemon to collect data by the spinel protocol
Version:			%{version}
Release:			%{release}
License:			GPL
Group:				Development/Other
URL:				http://code.google.com/p/spineld/
Source:				%{name}-%{version}.tar.gz
Requires:			perl
BuildArch:			noarch
Buildroot:			%{_tmppath}/%{name}-buildroot
Packager:			Tomas Podermanski <tpoder@cis.vutbr.cz>

%description
This daemon allows load data from devices which spinel protocol 
support(http://www.papouch.com/shop/scripts/_spinel.asp). This 
protocol is supported by almost measure boards and other equipments 
produced by Papouch s.r.o. (http://www.papouch.com/en/). The daemon 
periodically gains data from configured sensors and provides output 
for other system. The one of the included module is the module for 
zabbix monitoring system.

web: http://code.google.com/p/spineld/

%prep 

%setup

%install
make PREFIX=$RPM_BUILD_ROOT/ install

%post
ln -s /usr/sbin/spineld /usr/bin/spinel

%files 
%defattr(-,root,root)
%config /etc/spineld.conf
%doc /usr/share/man/man1/spineld.1.gz
%doc /usr/share/man/man1/spinel.1.gz
%doc /usr/share/doc/%{name}-%{version}/spineld.txt
#%doc /usr/share/doc/%{name}-%{version}/spineld-zabbix.xml
/usr/sbin/spineld
/usr/bin/spinel

%changelog

