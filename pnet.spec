Summary:	The DotGNU Portable .NET tools
Summary(pl):	Narzêdzia Portable .NET z projektu DotGNU
Summary(pt_BR):	Ferramentas Portable .NET DotGNU
Name:		pnet
Version:	0.5.12
Release:	1.1
License:	GPL
Group:		Development/Languages
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
# Source0-md5:	fe0c29be30212e9e2f8074f0b4a2d617
Patch0:		%{name}-alpha.patch
URL:		http://www.southern-storm.com.au/portable_net.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	treecc >= 0.2.4
Requires:	%{name}-compiler = %{version}
Requires:	%{name}-libgc = %{version}
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

%description -l pl
Celem tego projektu jest stworzenie zestawu Wolnych narzêdzi to
budowania i uruchamiania przeno¶nych plików wykonywalnych (.NET,
JavaTM, Parrot); aplikacji (w³±czaj±c kompilatory, asembler,
disasembler; oraz silnika zdolnego wykonywaæ ró¿ne formaty dla maszyn
stosowych.

Jest to metapakiet zawieraj±cy pnet-compiler, pnet-interpreter i
pnet-tools.

%description -l pt_BR
A meta do projeto é construir um conjunto de ferramentas de software
livre para construit e executar aplicações .NET, incluindo um
compilador C#, assembler, disassembler, e runtime engine.

%package interpreter
Summary:	The DotGNU Portable .NET runtime engine
Summary(pl):	Silnik wykonawczy Portable .NET z projektu DotGNU
Summary(pt_BR):	A engine runtime da Portable .NET
Group:		Applications/Emulators

%description interpreter
The Converted Virtual Machine supports executing multiple kinds of
portable executables, including IL (".NET") and JavaTM classes.

Install it if you want to execute IL executables. You should also
install pnetlib.

%description interpreter -l pl
Konwertowana Maszyna Wirtualna wspiera uruchamiania wielu rodzaji
przeno¶nych plików wykonywalnych w³±czaj±c IL (".NET") oraz klasy
JavaTM.

Zainstaluj je¿eli chcesz uruchamiaæ programy IL. Powiniene¶ tak¿e
zainstalowaæ pnetlib

%description interpreter -l pt_BR
A enfine runtime executa os binários .NET. É uma máquina virtual para
o bytecode .NET

%package compiler
Summary:	The Portable .NET compiler collection
Summary(pl):	Zestaw kompilatorów Portable .NET
Summary(pt_BR):	A coleção de compiladores do Portable .NET
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

%description compiler -l pl
Zestaw kompilatorów cscc t³umaczy wiele jêzyków ¼ród³owych na wiele
jêzyków wynikowych, podobnie jak GCC. W chwili obecnej obs³uguje C#,
JavaTM, Brainf**k, VB i C jako wej¶cie oraz asembler IL (".NET"),
asembler JavaTM, oraz imcc (wysokopoziomowy asembler Parrot (Perl6)).

S± tak¿e za³±czone inne narzêdzia do kompilacji takie jak csant -
zastêpca make.

Jest to wirtualny pakiet który instaluje wszystkie kompilatory
za³±czone z dystrybucj± pnet. Je¿eli chcesz tylko niektóre z nich we¼
pnet-compiler-common i pnet-compiler-<jêzyk>

%description compiler -l pt_BR
Os compiladores para C# e C são incluídos neste pacote. O wrapper cscc
provê uma interface padrão de compilação

%package compiler-common
Summary:	Common files for Portable .NET compilers
Summary(pl):	Pliki wspólne dla kompilatorów Portable .NET
Group:		Development/Languages
Requires:	%{name}-interpreter = %{version}
Requires:	ilasm

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

%description compiler-common -l pl
Zestaw kompilatorów cscc t³umaczy wiele jêzyków ¼ród³owych na wiele
jêzyków wynikowych, podobnie jak GCC. W chwili obecnej obs³uguje C#,
JavaTM, Brainf**k, VB i C jako wej¶cie oraz asembler IL (".NET"),
asembler JavaTM, oraz imcc (wysokopoziomowy asembler Parrot (Perl6)).

S± tak¿e za³±czone inne narzêdzia do kompilacji takie jak csant -
zastêpca make.

Powiniene¶ zainstalowaæ co najmniej jeden z pakietów jêzykowych pnet,
inaczej ten pakiet bêdzie bezu¿yteczny.

%package compiler-ilasm
Summary:	IL Assembler for Portable.NET
Summary(pl):	Assembler IL dla Portable.NET
Group:		Development/Languages
Provides:	ilasm
Obsoletes:	mono-ilasm

%description compiler-ilasm
IL Assembler from Portable.NET package.

%description compiler-ilasm -l pl
Assembler IL z pakietu Portable.NET.

%package compiler-csharp
Summary:	C# backend for cscc
Summary(pl):	Nak³adka do C# na cscc
Group:		Development/Languages
Requires:	%{name}-compiler-common = %{version}

%description compiler-csharp
C# language backend for cscc. Install this if you want to compile C#
programs with cscc. It's pretty useless without package pnetlib,
however.

%description compiler-csharp -l pl
Nak³adka jêzyka C# dla cscc. Zainstaluj j± je¿eli chcesz kompilowaæ
programy w cscc. Zazwyczaj jest bezu¿yteczna bez pnetlib.

%package compiler-java
Summary:	Java backend for cscc
Summary(pl):	Nak³adka do Javy na cscc
Group:		Development/Languages
Requires:	%{name}-compiler-common = %{version}

%description compiler-java
Java language backend for cscc. Install this if you want to compile
Java programs with cscc. It's pretty useless until you manually
install something like classpath, however.

%description compiler-java -l pl
Nak³adka jêzyka Java dla cscc. Zainstaluj j± je¿eli chcesz kompilowaæ
programy Java w cscc. Zazwyczaj jest bezu¿yteczna dopóki nie
zainstalujesz czego¶ jak classpath.

%package compiler-bf
Summary:	Brainf**k backend for cscc
Summary(pl):	Nak³adka do Brainf**k na cscc
Group:		Development/Languages
Requires:	%{name}-compiler-common = %{version}

%description compiler-bf
Brainf**k language backend for cscc. Install this if you want to
compile Brainf**k programs with cscc. Brainf**k is pretty useless,
however.

%description compiler-bf -l pl
Nak³adka jêzyka Brainf**k dla cscc. Zainstaluj j± je¿eli chcesz
kompilowaæ programy Brainf**k w cscc. Zazwyczaj jest bezu¿yteczna.

%package compiler-visualbasic
Summary:	Visual Basic backend for cscc
Summary(pl):	Nak³adka do Visual Basica na cscc
Group:		Development/Languages
Requires:	%{name}-compiler-common = %{version}

%description compiler-visualbasic
Visual Basic language backend for cscc. Install this if you want to
compile Visual Basic programs with cscc. Not as useless as
Brainf**k...probably.

%description compiler-visualbasic -l pl
Nak³adka jêzyka Brainf**k dla cscc. Zainstaluj j± je¿eli chcesz
kompilowaæ programy Visual Basica w cscc. Nie a¿ tak bardzo
bezu¿yteczna jak Brainf**k, ale...

%package compiler-c
Summary:	C backend for cscc
Summary(pl):	Nak³adka do C na cscc
Group:		Development/Languages
Requires:	%{name}-compiler-common = %{version}

%description compiler-c
C language backend for cscc. Install this if you want to compile C
programs with cscc.

C programs require a support library packaged in pnetlib called
`OpenSystem.C.dll'. It's like libgcc. Also, a minimal libc that
compiles with cscc-c-s is in pnetC.

%description compiler-c -l pl
Nak³adka jêzyka C dla cscc. Zainstaluj j± je¿eli chcesz kompilowaæ
programy C w cscc.

%package tools
Summary:	Miscellaneous tools for DotGNU Portable .NET
Summary(pl):	Ró¿ne narzêdzia Portable .NET z projektu DotGNU
Summary(pt_BR):	As ferramentas da Portable .NET
Group:		Development/Tools
Requires:	%{name}-interpreter = %{version}

%description tools
The general toolkit provided along with the pnet compiler and runtime
engines. This includes csant, a replacement for make, and various
tools to deal with IL binaries.

%description tools -l pl
Zestaw ogólnych narzêdzi dostarczanych razem z kompilatorem i
¶rodowiskiem wykonawczym. M. in. csant (zamiennik make) oraz ró¿ne
narzêdzia do obs³ugi binarii IL.

%description tools -l pt_BR
O kit de ferramentas provido junto com o compilador e o runtime. Ele
include o csant, um substituto para make, e várias ferramentas para
lidar com binários IL

%package devel
Summary:	The Portable.Net devel headers
Summary(pl):	Pliki nag³ówkowe Portable.Net
Summary(pt_BR):	Header de desenvolviemnto da Portable.Net
Group:		Development/Libraries

%description devel
The Portable .NET devel headers.

%description devel -l pl
Pliki nag³ówkowe Portable.NET.

%description devel -l pt_BR
Header de desenvolviemnto da Portable .NET.

%package libgc
Summary:	Shared garbage collector built with Portable .NET
Summary(pl):	Dzielony garbage collector zbudowany z Portable .NET
Group:		Libraries

%description libgc
Portable .NET builds and installs a shared garbage-collection library,
supposedly intended for use with embedded CLR.

%description libgc -l pl
Portable .NET buduje i instaluje dzielon± bibliotekê od¶miecacza,
do wykorzystania z wbudowanym CLR.

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
%configure \
%ifarch alpha
	--without-libgc \
%endif
	--enable-threads=pthreads

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# shutup check-files
rm -f $RPM_BUILD_ROOT%{_bindir}/al # just a link
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/pnet/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post tools
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun tools
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
%doc AUTHORS ChangeLog HACKING NEWS README doc/*.html
%attr(755,root,root) %{_bindir}/cscc
%attr(755,root,root) %{_bindir}/csant
%attr(755,root,root) %{_bindir}/ilalink
%attr(755,root,root) %{_bindir}/ilheader
%attr(755,root,root) %{_bindir}/resgen
%dir %{_libdir}/cscc/plugins
%{_mandir}/man1/csant.1*
%{_mandir}/man1/cscc.1*
%{_mandir}/man1/ilalink.1*
%{_mandir}/man1/ilheader.1*
%{_mandir}/man1/resgen.1*

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
%attr(755,root,root) %{_libdir}/cscc/plugins/cscc-bf

%files compiler-visualbasic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cscc/plugins/cscc-vb

%files compiler-c
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cscc/plugins/cscc-c-s

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ildb
%attr(755,root,root) %{_bindir}/ildasm
%attr(755,root,root) %{_bindir}/ildiff
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
%{_mandir}/man1/ildb.1*
%{_mandir}/man1/ildd.1*
%{_mandir}/man1/ildiff.1*
%{_mandir}/man1/ildasm.1*
%{_mandir}/man1/ilfind.1*
%{_mandir}/man1/ilnative.1*
%{_mandir}/man1/ilsize.1*
%{_mandir}/man1/ilranlib.1*
%{_mandir}/man1/ilstrip.1*
%{_infodir}/pnettools.info*

%files devel
%defattr(644,root,root,755)
%{_includedir}/pnet

%ifnarch alpha
%files libgc
%defattr(644,root,root,755)
%dir %{_libdir}/pnet
%{_libdir}/pnet/libgc.so.*
%{_libdir}/pnet/libffi.la
%{_libdir}/pnet/libgc.la
%endif
