Summary:	The DotGNU Portable .NET tools
Summary(pl):	Narz�dzia Portable .NET z projektu DotGNU
Name:		pnet
Version:	0.5.6
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-alpha.patch
URL:		http://www.southern-storm.com.au/portable_net.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	treecc >= 0.2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of this project is to build a suite of Free Software tools to
build and execute portable executable (.NET, JavaTM, Parrot)
applications, including compilers, an assembler, a disassembler, and
runtime engine capable of executing multiple stack-based bytecode
formats.

%description -l pl
Celem tego projektu jest stworzenie zestawu Wolnych narz�dzi to
budowania i uruchamiania przeno�nych plik�w wykonywalnych (.NET,
JavaTM, Parrot); aplikacji (w��czaj�c kompilatory, asembler,
disasembler; oraz silnika zdolnego wykonywa� r�ne formaty dla maszyn
stosowych.

%package interpreter
Summary:	The DotGNU Portable .NET runtime engine
Summary(pl):	Silnik wykonawczy Portable .NET z projektu DotGNU
Group:		Applications/Emulators
Obsoletes:	pnet

%description interpreter
The Converted Virtual Machine supports executing multiple kinds of
portable executables, including IL (".NET") and JavaTM classes.

%description interpreter -l pl
Konwertowana Maszyna Wirtualna wspiera uruchamiania wielu rodzaji
przeno�nych plik�w wykonywalnych w��czaj�c IL (".NET") oraz klasy
JavaTM.

%package compiler
Summary:	The Portable .NET compiler collection
Summary(pl):	Zestaw kompilator�w Portable .NET
Group:		Development/Languages
Obsoletes:	pnet
Requires:	pnet-interpreter = %{version}

%description compiler
The cscc compiler collection allows multiple input languages and
multiple output bytecodes, much like GCC. Current languages include C#
and C; current output formats include IL assembly (".NET"), JavaTM
assembly, and imcc (Parrot (Perl6) high-level assembly).

%description compiler -l pl
Zestaw kompilator�w cscc t�umaczy wiele j�zyk�w �r�d�owych na wiele
j�zyk�w wynikowych, podobnie jak GCC. W chwili obecnej obs�uguje C# i
C jako wej�cie oraz asembler IL (".NET"), asembler JavaTM, oraz imcc
(wysokopoziomowy asembler Parrot (Perl6)).

%package tools
Summary:	Miscellaneous tools for DotGNU Portable .NET
Summary(pl):	R�ne narz�dzia Portable .NET z projektu DotGNU
Group:		Development/Tools
Obsoletes:	pnet
Requires:	pnet-interpreter = %{version}

%description tools
The general toolkit provided along with the pnet compiler and runtime
engines. This includes csant, a replacement for make, and various
tools to deal with IL binaries.

%description tools -l pl
Zestaw og�lnych narz�dzi dostarczanych razem z kompilatorem i
�rodowiskiem wykonawczym. M. in. csant (zamiennik make) oraz r�ne
narz�dzia do obs�ugi binarii IL.

%prep
%setup -q
%patch -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
# "-O2 -march={i686|athlon} -fno-gcse" with gcc 3.x causes "no register to spill"
# (GNATS#10017 - qualified as "invalid user input", not a bug)
# -fomit-frame-pointer is needed on i686/athlon to recover one more register
# (which x86 have too less...)
CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

# shutup check-files
rm -f $RPM_BUILD_ROOT%{_bindir}/al # just a link
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/pnet/*.a
rm -rf $RPM_BUILD_ROOT%{_includedir}/pnet

%clean
rm -rf $RPM_BUILD_ROOT

%post tools
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun tools
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files interpreter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ilrun
%attr(755,root,root) %{_bindir}/clrwrap
%dir %{_libdir}/cscc
%{_mandir}/man1/ilrun.1*
%{_mandir}/man1/clrwrap.1*

%files compiler
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING INSTALL NEWS README doc/*.html
%attr(755,root,root) %{_bindir}/cscc
%attr(755,root,root) %{_bindir}/csant
%attr(755,root,root) %{_bindir}/ilasm
%attr(755,root,root) %{_bindir}/ilalink
%attr(755,root,root) %{_bindir}/resgen
%dir %{_libdir}/cscc/plugins
%attr(755,root,root) %{_libdir}/cscc/plugins/*
%{_mandir}/man1/resgen.1*
%{_mandir}/man1/ilasm.1*
%{_mandir}/man1/cscc.1*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ilheader
%attr(755,root,root) %{_bindir}/ildb
%attr(755,root,root) %{_bindir}/ildasm
%attr(755,root,root) %{_bindir}/ildiff
%attr(755,root,root) %{_bindir}/ildd
%attr(755,root,root) %{_bindir}/ilfind
%attr(755,root,root) %{_bindir}/ilsize
%attr(755,root,root) %{_bindir}/ilnative
%attr(755,root,root) %{_bindir}/ilverify
%attr(755,root,root) %{_bindir}/csdoc
%attr(755,root,root) %{_bindir}/csdoc2html
%attr(755,root,root) %{_bindir}/csdoc2hier
%attr(755,root,root) %{_bindir}/csdoc2texi
%{_mandir}/man1/ilheader.1*
%{_mandir}/man1/ilfind.1*
%{_mandir}/man1/ildd.1*
%{_mandir}/man1/ildb.1*
%{_mandir}/man1/ildasm.1*
%{_mandir}/man1/ilsize.1*
%{_mandir}/man1/ilnative.1*
%{_mandir}/man1/ildiff.1*
%{_mandir}/man1/csdoc*
%{_datadir}/info/pnettools.info*
