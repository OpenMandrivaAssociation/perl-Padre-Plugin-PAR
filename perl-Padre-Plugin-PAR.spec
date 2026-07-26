%define upstream_name    Padre-Plugin-PAR
Name:		perl-%{upstream_name}
Version:	0.06
Release:	7

Summary:	PAR generation from Padre
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://padre.perlide.org
Source0:	https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Padre-Plugin-PAR-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Padre)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch
Requires:	perl(Padre)

%description
Padre plugin to seamlessly generate a standalone exuctable.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
#Disable tests because they need to export display
#./Build test

%install
./Build install

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 655606
- rebuild for updated spec-helper

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 569949
- update to 0.06

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 401623
- rebuild using %0.06 fixed license field

* Mon May 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.05-2mdv2010.0
+ Revision: 371826
- bumping mkrel to force re-submission

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2010.0
+ Revision: 371728
- update to new version 0.05

* Wed Jan 14 2009 Jérôme Quelin <jquelin@mandriva.org> 0.04-1mdv2009.1
+ Revision: 329376
- update to new version 0.04
- update url, summary & description

* Mon Sep 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.02-1mdv2009.0
+ Revision: 278213
- import perl-Padre-Plugin-PAR


