%define name		spinled
%define version		2.05
%define release		1

Name:				%{name}
Summary:			Daemon to collect data by the spinel protocol
Version:			%{version}
Release:			%{release}
License:			GPL
Group:				Development/Other
URL:				http://rdbackup.sourceforge.net
Source:				%{name}-%{version}.tar.gz
Requires:			rsync, tar, gzip
BuildArch:			noarch
Buildroot:			%{_tmppath}/%{name}-buildroot
Packager:			Tomas Podermanski <tpoder@cis.vutbr.cz>

%description
Backup the systems defined in a config file. Rdbackup uses rsync tool to
create the backups. The backuped data are stored as a exactly up to date
mirror of a backuped directory. Rdbackup also store an incremental
backups. The incremental backups are based on changes between data on
client side and current copy on the backup server.

One of the the importatnt part in rdbackup are tools to check a backup
status. The rdbackup could create report with backup statistics and send
it through an email. Nex way how to check the backup consistency is
checking through snmp protocol or zabbix protocol. You could easy check 
backups statuses via your preffered monitoring system. Actually rdbackup 
is fully integrated with the zabbix monitoring system. 

web: http://rdbackup.sourceforge.net/

%prep 

%setup

%install
make PREFIX=$RPM_BUILD_ROOT/ install

%files 
%defattr(-,root,root)
%config /etc/cron.d/rdbackup.cron
%config /etc/rdbackup.conf-sample
%config /etc/snmp/snmpd.conf-rdbackup
%doc /usr/share/man/man1/rdbackup.1.gz
%doc /usr/share/doc/%{name}-%{version}/RDBACKUP.txt
%doc /usr/share/doc/%{name}-%{version}/rdbackup-zabbix.xml
/usr/sbin/rdbackup
/usr/sbin/rdbackup-snmp
/usr/sbin/rdbackup-maile
/usr/share/snmp/mibs/RDBACKUP-MIB.txt


%changelog

