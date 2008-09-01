
%define realname   Padre-Plugin-PAR
%define version    0.02
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl Application Development and Refactoring Environment
Source:     http://www.cpan.org/modules/by-module//%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Padre)
BuildRequires: perl(Module::Build)
Requires:  perl(Padre)

BuildArch: noarch

%description
The application maintains its configuration information in a directory
called .padre

On Strawberry Perl you can associate .pl file extension with
c:\strawberry\perl\bin\wxperl and then you can start double clicking on the
application. It should work.

 Run This (F5) - run the current buffer with the current perl
 this currently only works with files with .pl  extensions.

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
