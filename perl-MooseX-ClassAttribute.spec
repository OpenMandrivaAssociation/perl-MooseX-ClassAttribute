%define upstream_name    MooseX-ClassAttribute
%define upstream_version 0.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Declare class attributes Moose-style
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/MooseX-ClassAttribute-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(B)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::AttributeHelpers)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(namespace::autoclean)

BuildArch:	noarch

%description
This module allows you to declare class attributes in exactly the same way
as you declare object attributes, except using 'class_has()' instead of
'has()'. It is also possible to make these attributes immutable (and
faster) just as you can with normal Moose attributes.

You can use any feature of Moose's attribute declarations, including
overriding a parent's attributes, delegation ('handles'), and attribute
metaclasses, and it should just work.

The accessors methods for class attribute may be called on the class
directly, or on objects of that class. Passing a class attribute to the
constructor will not set it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/MooseX


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.260.0-1mdv2011.0
+ Revision: 684776
- update to new version 0.26

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.240.0-1
+ Revision: 662126
- update to new version 0.24

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.220.0-1
+ Revision: 635536
- update to new version 0.22

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.210.0-1mdv2011.0
+ Revision: 594880
- update to new version 0.21

* Tue Oct 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 586831
- new version

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 553961
- update to 0.16

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.1
+ Revision: 504490
- update to 0.13

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.1
+ Revision: 503783
- update to 0.11

* Thu Aug 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 421623
- update to 0.10

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 405944
- rebuild using %%perl_convert_version

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2010.0
+ Revision: 394087
- update to new version 0.09

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2010.0
+ Revision: 371864
- new version

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2009.1
+ Revision: 302851
- update to new version 0.07

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.1
+ Revision: 292558
- update to new version 0.06

* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.0
+ Revision: 236406
- import perl-MooseX-ClassAttribute


* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.0
- initial mdv release, generated with cpan2dist

