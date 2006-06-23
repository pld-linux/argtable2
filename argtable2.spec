Summary:	An ANSI C library for parsing GNU style command line arguments
Summary(pl):	Biblioteka ANSI C do analizy argumentów linii poleceñ w stylu GNU
Name:		argtable2
Version:	6
Release:	0.9
License:	LGPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/argtable/%{name}-%{version}.tar.gz
# Source0-md5:	e1d5035992b29b45c5abad2b3487e096
URL:		http://argtable.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Argtable is an ANSI C library for parsing GNU style command line
arguments. It enables a program's command line syntax to be defined in
the source code as an array of argtable structs. The command line is
then parsed according to that specification and the resulting values
are returned in those same structs where they are accessible to the
main program. Both tagged (-v, --verbose, --foo=bar) and untagged
arguments are supported, as are multiple instances of each argument.
Syntax error handling is automatic and the library also provides the
means for displaying the command line syntax directly from the array
of argument specifications.

%description -l pl
Argtable to biblioteka ANSI C do analizy argumentów linii poleceñ w
stylu GNU. Pozwala na definiowanie sk³adni linii poleceñ programu w
kodzie ¼ród³owym jako tablicy struktur argtable. Linia poleceñ jest
potem analizowana zgodnie z t± specyfikacj±, a warto¶ci zwracane s±
przez te same struktury dostêpne dla g³ównego programu. Obs³ugiwane
s± argumenty zarówno ze znacznikami (-v, --verbose, --foo=bar) jak i
bez znaczników, a tak¿e wielokrotne wyst±pienia danego argumentu.
Obs³uga b³êdów sk³adni jest automatyczna, a biblioteka udostêpnia
tak¿e wy¶wietlanie sk³adni linii poleceñ bezpo¶rednio z tablicy
specyfikacji argumentów.

%package devel
Summary:	Header files for argtable2 library
Summary(pl):	Pliki nag³ówkowe biblioteki argtable2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for argtable2 library.

%description devel -l pl
Pliki nag³ówkowe biblioteki argtable2.

%package static
Summary:	Static argtable2 library
Summary(pl):	Statyczna biblioteka argtable2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static argtable2 library.

%description static -l pl
Statyczna biblioteka argtable2.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc example doc/*.{ps,gif,html,pdf}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_datadir}/%{name}.def
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
