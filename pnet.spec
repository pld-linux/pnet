Summary:	Portable.NET
Name:		pnet
Version:	0.1.0
Release:	1
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
BuildRequires:	treecc
URL:		http://www.southern-storm.com.au/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portable interpreter for .NET platform binaries.

%description -l pl
Przenaszalny interpreter dla programów pisanych na platformê .NET.

%prep
%setup -q

%build
aclocal
autoconf
automake -a -c
%configure

%{__make} 

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README doc/*.txt

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* doc/*

%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
%{_includedir}/pnet/
%{_mandir}/man?/*
