Summary:	An ANSI C library for parsing GNU style command line arguments
Summary(pl.UTF-8):	Biblioteka ANSI C do analizy argumentów linii poleceń w stylu GNU
Name:		argtable2
Version:	13
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/argtable/%{name}-%{version}.tar.gz
# Source0-md5:	156773989d0d6406cea36526d3926668
URL:		http://argtable.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Argtable to biblioteka ANSI C do analizy argumentów linii poleceń w
stylu GNU. Pozwala na definiowanie składni linii poleceń programu w
kodzie źródłowym jako tablicy struktur argtable. Linia poleceń jest
potem analizowana zgodnie z tą specyfikacją, a wartości zwracane są
przez te same struktury dostępne dla głównego programu. Obsługiwane
są argumenty zarówno ze znacznikami (-v, --verbose, --foo=bar) jak i
bez znaczników, a także wielokrotne wystąpienia danego argumentu.
Obsługa błędów składni jest automatyczna, a biblioteka udostępnia
także wyświetlanie składni linii poleceń bezpośrednio z tablicy
specyfikacji argumentów.

%package devel
Summary:	Header files for argtable2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki argtable2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for argtable2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki argtable2.

%package static
Summary:	Static argtable2 library
Summary(pl.UTF-8):	Statyczna biblioteka argtable2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static argtable2 library.

%description static -l pl.UTF-8
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

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libargtable2.so.0

%files devel
%defattr(644,root,root,755)
%doc example doc/*.{ps,gif,html,pdf}
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/argtable2.pc
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
