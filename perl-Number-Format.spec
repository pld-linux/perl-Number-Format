%include	/usr/lib/rpm/macros.perl
Summary:	Number-Format perl module
Summary(pl):	Modu³ perla Number-Format
Name:		perl-Number-Format
Version:	1.41
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Number/Number-Format-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Number-Format - Perl extension for formatting numbers. 

%description -l pl
Number-Format - modu³ do formatowania liczb.

%prep
%setup -q -n Number-Format-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Number/Format
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        CHANGES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README,TODO}.gz

%{perl_sitelib}/Number/Format.pm
%{perl_sitearch}/auto/Number/Format

%{_mandir}/man3/*
