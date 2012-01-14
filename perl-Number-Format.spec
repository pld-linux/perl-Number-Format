#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Number
%define		pnam	Format
%define		major_ver	1.73
%define		minor_ver	%{nil}
Summary:	Number::Format - Perl extension for formatting numbers
Summary(pl.UTF-8):	Number::Format - moduł do formatowania liczb
Name:		perl-Number-Format
Version:	%{major_ver}%{minor_ver}
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3a4188de6e84b04361def285b93dc240
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

%description -l pl.UTF-8
Number::Format jest biblioteką, służącą do formatowania liczb.
Dostarcza funkcji do konwersji liczb na ciągi znaków w różny sposób,
oraz do konwersji ciągów zawierających liczby z powrotem na ich postać
numeryczną.  Formaty wynikowe mogą zawierać separatory tysięczne --
znaki, wstawiane pomiędzy każdą grupę trzech znaków licząc od prawej do
lewej od kropki dziesiętnej.  Znaki, używane jako kropka dziesiętna i
separator tysięczny pochodzą z informacji o locale; mogą też być podane
przez użytkownika.

%prep
%setup -q -n %{pdir}-%{pnam}-%{major_ver}

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
