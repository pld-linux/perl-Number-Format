%include	/usr/lib/rpm/macros.perl
%define	pdir	Number
%define	pnam	Format
Summary:	Number::Format perl module
Summary(pl):	Modu³ perla Number::Format
Name:		perl-Number-Format
Version:	1.44
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Number::Format - Perl extension for formatting numbers.

%description -l pl
Number::Format - modu³ do formatowania liczb.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%{perl_sitelib}/Number/Format.pm
%{_mandir}/man3/*
