%include	/usr/lib/rpm/macros.perl
Summary:	Number-Format perl module
Summary(pl):	Modu³ perla Number-Format
Name:		perl-Number-Format
Version:	1.42
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Number/Number-Format-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Number-Format - Perl extension for formatting numbers.

%description -l pl
Number-Format - modu³ do formatowania liczb.

%prep
%setup -q -n Number-Format-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Number/Format.pm
%{_mandir}/man3/*
