Summary:	Portable.NET
Summary(pl):	Przeno¶ny.NET
Name:		pnet
Version:	0.5.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
URL:		http://www.southern-storm.com.au/portable_net.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	treecc >= 0.1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portable interpreter for .NET platform binaries.

%description -l pl
Przenaszalny interpreter dla programów pisanych na platformê .NET.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
#athlon optimization broken in gcc3
%ifarch athlon
CFLAGS="-O0" 
%endif
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*.a
%dir %{_libdir}/cscc
%{_libdir}/%{name}/lib*.a
%{_libdir}/%{name}/lib*.la
%attr(755,root,root) %{_libdir}/%{name}/lib*.so.*
%attr(755,root,root) %{_libdir}/cscc/plugins
%{_includedir}/pnet/
%{_mandir}/man?/*
%{_infodir}/pnet*
