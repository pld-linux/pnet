Summary:	Portable.NET
Summary(pl):	Przeno¶ny.NET
Name:		pnet
Version:	0.1.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
URL:		http://www.southern-storm.com.au/
BuildRequires:	treecc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portable interpreter for .NET platform binaries.

%description -l pl
Przenaszalny interpreter dla programów pisanych na platformê .NET.

%prep
%setup -q

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README* doc/*.html

%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
%{_includedir}/pnet/
%{_mandir}/man?/*
