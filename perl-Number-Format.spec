#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Number
%define		pnam	Format
Summary:	Number::Format - Perl extension for formatting numbers
Summary(pl):	Number::Format - modu� do formatowania liczb
Name:		perl-Number-Format
Version:	1.51
Release:	0.1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0191de22501fa4df10a58a400bd79977
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Number::Format is a library for formatting numbers.  Functions are
provided for converting numbers to strings in a variety of ways, and to
convert strings that contain numbers back into numeric form.  The output
formats may include thousands separators - characters inserted between
each group of three characters counting right to left from the decimal
point.  The characters used for the decimal point and the thousands
separator come from the locale information or can be specified by
the user.

%description -l pl
Number::Format jest bibliotek�, s�u��c� do formatowania liczb.
Dostarcza funkcji do konwersji liczb na ci�gi znak�w w r�ny spos�b,
oraz do konwersji ci�g�w zawieraj�cych liczby z powrotem na ich posta�
numeryczn�.  Formaty wynikowe mog� zawiera� separatory tysi�czne --
znaki, wstawiane pomi�dzy ka�d� grup� trzech znak�w licz�c od prawej do
lewej od kropki dziesi�tnej.  Znaki, u�ywane jako kropka dziesi�tna i
separator tysi�czny pochodz� z informacji o locale; mog� te� by� podane
przez u�ytkownika.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%{perl_vendorlib}/Number/Format.pm
%{_mandir}/man3/*
