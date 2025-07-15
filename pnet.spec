#
# Conditional build:
%bcond_with	libjit	# libjit instead of CVM engine

Summary:	The DotGNU Portable .NET tools
Summary(pl.UTF-8):	Narzędzia Portable .NET z projektu DotGNU
Summary(pt_BR.UTF-8):	Ferramentas Portable .NET DotGNU
Name:		pnet
Version:	0.8.0
Release:	5
License:	GPL v2+
Group:		Development/Languages
Source0:	http://download.savannah.gnu.org/releases/dotgnu-pnet/%{name}-%{version}.tar.gz
# Source0-md5:	84cb3612d7175bd9e476c88e66fe19f9
Patch0:		%{name}-systemffi.patch
Patch1:		%{name}-systemgc.patch
Patch2:		format-security.patch
Patch3:		no-regex_syntax.patch
Patch4:		%{name}-info.patch
Patch5:		%{name}-link.patch
Patch6:		%{name}-opt.patch
Patch7:		x32.patch
Patch8:		%{name}-no-common.patch
URL:		http://www.gnu.org/software/dotgnu/pnet.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gc-devel
BuildRequires:	libffi-devel
%{?with_libjit:BuildRequires:	libjit-devel}
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	texinfo
BuildRequires:	treecc >= 0.3.6
BuildRequires:	zlib-devel
Requires:	%{name}-compiler = %{version}
Requires:	%{name}-tools = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of this project is to build a suite of Free Software tools to
build and execute portable executable (.NET, JavaTM, Parrot)
applications, including compilers, an assembler, a disassembler, and
runtime engine capable of executing multiple stack-based bytecode
formats.

This is metapackage including pnet-compiler, pnet-interpreter and
pnet-tools packages.

%description -l pl.UTF-8
Celem tego projektu jest stworzenie zestawu Wolnych narzędzi to
budowania i uruchamiania przenośnych plików wykonywalnych (.NET,
JavaTM, Parrot); aplikacji (włączając kompilatory, asembler,
disasembler; oraz silnika zdolnego wykonywać różne formaty dla maszyn
stosowych.

Jest to metapakiet zawierający pnet-compiler, pnet-interpreter i
pnet-tools.

%description -l pt_BR.UTF-8
A meta do projeto é construir um conjunto de ferramentas de software
livre para construit e executar aplicações .NET, incluindo um
compilador C#, assembler, disassembler, e runtime engine.

%package interpreter
Summary:	The DotGNU Portable .NET runtime engine
Summary(pl.UTF-8):	Silnik wykonawczy Portable .NET z projektu DotGNU
Summary(pt_BR.UTF-8):	A engine runtime da Portable .NET
Group:		Applications/Emulators

%description interpreter
The Converted Virtual Machine supports executing multiple kinds of
portable executables, including IL (".NET") and JavaTM classes.

Install it if you want to execute IL executables. You should also
install pnetlib.

%description interpreter -l pl.UTF-8
Konwertowana Maszyna Wirtualna wspiera uruchamiania wielu rodzaji
przenośnych plików wykonywalnych włączając IL (".NET") oraz klasy
JavaTM.

Zainstaluj jeżeli chcesz uruchamiać programy IL. Powinieneś także
zainstalować pnetlib

%description interpreter -l pt_BR.UTF-8
A enfine runtime executa os binários .NET. É uma máquina virtual para
o bytecode .NET

%package compiler
Summary:	The Portable .NET compiler collection
Summary(pl.UTF-8):	Zestaw kompilatorów Portable .NET
Summary(pt_BR.UTF-8):	A coleção de compiladores do Portable .NET
Group:		Development/Languages
Requires:	%{name}-compiler-bf = %{version}
Requires:	%{name}-compiler-c = %{version}
Requires:	%{name}-compiler-common = %{version}
Requires:	%{name}-compiler-csharp = %{version}
Requires:	%{name}-compiler-java = %{version}
Requires:	%{name}-compiler-visualbasic = %{version}

%description compiler
The cscc compiler collection allows multiple input languages and
multiple output bytecodes, much like GCC. Current languages include
C#, JavaTM, Brainf**k, VB, and C; current output formats include IL
assembly (".NET"), JavaTM assembly, and imcc (Parrot (Perl6)
high-level assembly).

Other common compiling tools are included, such as csant, a
replacement for make.

This is a virtual package that installs all compilers included with
the pnet distribution. If you only want some of them, get
`pnet-compiler-common' and `pnet-compiler-<insert language here>'.

%description compiler -l pl.UTF-8
Zestaw kompilatorów cscc tłumaczy wiele języków źródłowych na wiele
języków wynikowych, podobnie jak GCC. W chwili obecnej obsługuje C#,
JavaTM, Brainf**k, VB i C jako wejście oraz asembler IL (".NET"),
asembler JavaTM, oraz imcc (wysokopoziomowy asembler Parrot (Perl6)).

Są także załączone inne narzędzia do kompilacji takie jak csant -
zastępca make.

Jest to wirtualny pakiet który instaluje wszystkie kompilatory
załączone z dystrybucją pnet. Jeżeli chcesz tylko niektóre z nich weź
pnet-compiler-common i pnet-compiler-<język>

%description compiler -l pt_BR.UTF-8
Os compiladores para C# e C são incluídos neste pacote. O wrapper cscc
provê uma interface padrão de compilação

%package compiler-common
Summary:	Common files for Portable .NET compilers
Summary(pl.UTF-8):	Pliki wspólne dla kompilatorów Portable .NET
Group:		Development/Languages
Requires:	%{name}-interpreter = %{version}
Requires:	ilasm
Obsoletes:	pnet-libgc < 0.6.2-3

%description compiler-common
The cscc compiler collection allows multiple input languages and
multiple output bytecodes, much like GCC. Current languages include
C#, JavaTM, Brainf**k, VB, and C; current output formats include IL
assembly (".NET"), JavaTM assembly, and imcc (Parrot (Perl6)
high-level assembly).

Other common compiling tools are included, such as csant, a
replacement for make.

You should install at least one of the specific language packages;
otherwise, this package is pretty useless.

%description compiler-common -l pl.UTF-8
Zestaw kompilatorów cscc tłumaczy wiele języków źródłowych na wiele
języków wynikowych, podobnie jak GCC. W chwili obecnej obsługuje C#,
JavaTM, Brainf**k, VB i C jako wejście oraz asembler IL (".NET"),
asembler JavaTM, oraz imcc (wysokopoziomowy asembler Parrot (Perl6)).

Są także załączone inne narzędzia do kompilacji takie jak csant -
zastępca make.

Powinieneś zainstalować co najmniej jeden z pakietów językowych pnet,
inaczej ten pakiet będzie bezużyteczny.

%package compiler-ilasm
Summary:	IL Assembler for Portable.NET
Summary(pl.UTF-8):	Assembler IL dla Portable.NET
Group:		Development/Languages
Provides:	ilasm
Obsoletes:	mono-ilasm

%description compiler-ilasm
IL Assembler from Portable.NET package.

%description compiler-ilasm -l pl.UTF-8
Assembler IL z pakietu Portable.NET.

%package compiler-csharp
Summary:	C# backend for cscc
Summary(pl.UTF-8):	Nakładka do C# na cscc
Group:		Development/Languages
Requires:	%{name}-compiler-common = %{version}

%description compiler-csharp
C# language backend for cscc. Install this if you want to compile C#
programs with cscc. It's pretty useless without package pnetlib,
however.

%description compiler-csharp -l pl.UTF-8
Nakładka języka C# dla cscc. Zainstaluj ją jeżeli chcesz kompilować
programy w cscc. Zazwyczaj jest bezużyteczna bez pnetlib.

%package compiler-java
Summary:	Java backend for cscc
Summary(pl.UTF-8):	Nakładka do Javy na cscc
Group:		Development/Languages
Requires:	%{name}-compiler-common = %{version}

%description compiler-java
Java language backend for cscc. Install this if you want to compile
Java programs with cscc. It's pretty useless until you manually
install something like classpath, however.

%description compiler-java -l pl.UTF-8
Nakładka języka Java dla cscc. Zainstaluj ją jeżeli chcesz kompilować
programy Java w cscc. Zazwyczaj jest bezużyteczna dopóki nie
zainstalujesz czegoś jak classpath.

%package compiler-bf
Summary:	Brainf**k backend for cscc
Summary(pl.UTF-8):	Nakładka do Brainf**k na cscc
Group:		Development/Languages
Requires:	%{name}-compiler-common = %{version}

%description compiler-bf
Brainf**k language backend for cscc. Install this if you want to
compile Brainf**k programs with cscc. Brainf**k is pretty useless,
however.

%description compiler-bf -l pl.UTF-8
Nakładka języka Brainf**k dla cscc. Zainstaluj ją jeżeli chcesz
kompilować programy Brainf**k w cscc. Zazwyczaj jest bezużyteczna.

%package compiler-visualbasic
Summary:	Visual Basic backend for cscc
Summary(pl.UTF-8):	Nakładka do Visual Basica na cscc
Group:		Development/Languages
Requires:	%{name}-compiler-common = %{version}

%description compiler-visualbasic
Visual Basic language backend for cscc. Install this if you want to
compile Visual Basic programs with cscc. Not as useless as
Brainf**k...probably.

%description compiler-visualbasic -l pl.UTF-8
Nakładka języka Brainf**k dla cscc. Zainstaluj ją jeżeli chcesz
kompilować programy Visual Basica w cscc. Nie aż tak bardzo
bezużyteczna jak Brainf**k, ale...

%package compiler-c
Summary:	C backend for cscc
Summary(pl.UTF-8):	Nakładka do C na cscc
Group:		Development/Languages
Requires:	%{name}-compiler-common = %{version}

%description compiler-c
C language backend for cscc. Install this if you want to compile C
programs with cscc.

C programs require a support library packaged in pnetlib called
`OpenSystem.C.dll'. It's like libgcc. Also, a minimal libc that
compiles with cscc-c-s is in pnetC.

%description compiler-c -l pl.UTF-8
Nakładka języka C dla cscc. Zainstaluj ją jeżeli chcesz kompilować
programy C w cscc.

%package tools
Summary:	Miscellaneous tools for DotGNU Portable .NET
Summary(pl.UTF-8):	Różne narzędzia Portable .NET z projektu DotGNU
Summary(pt_BR.UTF-8):	As ferramentas da Portable .NET
Group:		Development/Tools
Requires:	%{name}-interpreter = %{version}

%description tools
The general toolkit provided along with the pnet compiler and runtime
engines. This includes csant, a replacement for make, and various
tools to deal with IL binaries.

%description tools -l pl.UTF-8
Zestaw ogólnych narzędzi dostarczanych razem z kompilatorem i
środowiskiem wykonawczym. M. in. csant (zamiennik make) oraz różne
narzędzia do obsługi binarii IL.

%description tools -l pt_BR.UTF-8
O kit de ferramentas provido junto com o compilador e o runtime. Ele
include o csant, um substituto para make, e várias ferramentas para
lidar com binários IL

%package devel
Summary:	The Portable.Net devel headers
Summary(pl.UTF-8):	Pliki nagłówkowe Portable.Net
Summary(pt_BR.UTF-8):	Header de desenvolviemnto da Portable.Net
Group:		Development/Libraries

%description devel
The Portable .NET devel headers.

%description devel -l pl.UTF-8
Pliki nagłówkowe Portable.NET.

%description devel -l pt_BR.UTF-8
Header de desenvolviemnto da Portable .NET.

%prep
%setup -q
%patch -P0 -p1
# pnet uses gc incompatible with system lib and links statically to it
#%patch1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%ifarch %{ix86}
%patch -P6 -p1
%endif
%patch -P7 -p1
%patch -P8 -p1

%{__rm} ilasm/ilasm_grammar.c

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# "-O2 -march={i686|athlon} -fno-gcse" with gcc 3.x causes "no register to spill"
# (GNATS#10017 - qualified as "invalid user input", not a bug)
# -fomit-frame-pointer is needed on i686/athlon to recover one more register
# (which x86 have too less...)
CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer} -I/usr/include/ncurses `pkg-config --cflags libffi`"
CPPFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer} -I/usr/include/ncurses `pkg-config --cflags libffi`"
%configure \
	--enable-threads=pthreads \
	%{?with_libjit:--with-jit}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# junk removal
%{__rm} $RPM_BUILD_ROOT%{_bindir}/{al,cli-unknown-*}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/{al.1*,cli-unknown-*}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/{,pnet-}resgen
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/{,pnet-}resgen.1

# don't distribute libgc
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/{gc*,leak_detector.h}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/gc
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgc.*

%clean
rm -rf $RPM_BUILD_ROOT

%post	tools -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	tools -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)

%files interpreter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ilrun
%attr(755,root,root) %{_bindir}/clrwrap
%dir %{_libdir}/cscc
%{_mandir}/man1/ilrun.1*
%{_mandir}/man1/clrwrap.1*

%files compiler
%defattr(644,root,root,755)

%files compiler-common
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/cvmdoc
%attr(755,root,root) %{_bindir}/cscc
%attr(755,root,root) %{_bindir}/csant
%attr(755,root,root) %{_bindir}/ilalink
%attr(755,root,root) %{_bindir}/ilheader
%attr(755,root,root) %{_bindir}/ilgac
%attr(755,root,root) %{_bindir}/pnet-resgen
%dir %{_libdir}/cscc/plugins
%{_mandir}/man1/csant.1*
%{_mandir}/man1/cscc.1*
%{_mandir}/man1/ilalink.1*
%{_mandir}/man1/ilheader.1*
%{_mandir}/man1/ilgac.1*
%{_mandir}/man1/pnet-resgen.1*

%files compiler-ilasm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ilasm
%{_mandir}/man1/ilasm.1*

%files compiler-csharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cscc/plugins/cscc-cs
%attr(755,root,root) %{_libdir}/cscc/plugins/cscc-csharp

%files compiler-java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cscc/plugins/cscc-java

%files compiler-bf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cscc/plugins/cscc-b
%attr(755,root,root) %{_libdir}/cscc/plugins/cscc-bf

%files compiler-visualbasic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cscc/plugins/cscc-vb

%files compiler-c
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cscc/plugins/cscc-c-s
%attr(755,root,root) %{_bindir}/cscc-cpp
%{_mandir}/man1/cscc-cpp.1*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ildasm
%attr(755,root,root) %{_bindir}/ildd
%attr(755,root,root) %{_bindir}/ilfind
%attr(755,root,root) %{_bindir}/ilsize
%attr(755,root,root) %{_bindir}/ilnative
%attr(755,root,root) %{_bindir}/ilverify
%attr(755,root,root) %{_bindir}/ilranlib
%attr(755,root,root) %{_bindir}/ilstrip
%attr(755,root,root) %{_bindir}/csdoc
%attr(755,root,root) %{_bindir}/csdoc2html
%attr(755,root,root) %{_bindir}/csdoc2hier
%attr(755,root,root) %{_bindir}/csdoc2texi
%attr(755,root,root) %{_bindir}/cssrc2html
%{_mandir}/man1/csdoc*
%{_mandir}/man1/cssrc2*
%{_mandir}/man1/ildd.1*
%{_mandir}/man1/ildasm.1*
%{_mandir}/man1/ilfind.1*
%{_mandir}/man1/ilnative.1*
%{_mandir}/man1/ilsize.1*
%{_mandir}/man1/ilranlib.1*
%{_mandir}/man1/ilstrip.1*
%{_mandir}/man1/ilverify.1*
%{_infodir}/pnettools.info*

%files devel
%defattr(644,root,root,755)
%{_includedir}/pnet
%{_libdir}/libILAsm.a
%{_libdir}/libILCodeGen.a
%{_libdir}/libILDumpAsm.a
%{_libdir}/libILEngine.a
%{_libdir}/libILImage.a
%{_libdir}/libILLink.a
%{_libdir}/libILSupport.a
