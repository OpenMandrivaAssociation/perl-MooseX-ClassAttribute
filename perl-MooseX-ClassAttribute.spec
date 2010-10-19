%define upstream_name    MooseX-ClassAttribute
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Declare class attributes Moose-style
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(B)
BuildRequires: perl(Exporter)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::AttributeHelpers)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Name)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/MooseX
