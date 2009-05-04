
%define realname   Padre-Plugin-PAR
%define version    0.05
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    PAR generation from Padre
Source:     http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Padre)
BuildRequires: perl(Module::Build)
Requires:  perl(Padre)

BuildArch: noarch

%description
Padre plugin to seamlessly generate a standalone exuctable.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
#Disable tests because they need to export display
#./Build test

%install
rm -rf %{buildroot}
./Build install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
