#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBIx-Class-OptimisticLocking
Version  : 0.02
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/B/BP/BPHILLIPS/DBIx-Class-OptimisticLocking-0.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BP/BPHILLIPS/DBIx-Class-OptimisticLocking-0.02.tar.gz
Summary  : 'Optimistic locking support for DBIx::Class'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-DBIx-Class-OptimisticLocking-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DBIx::Class)
BuildRequires : perl(DBIx::Class::Schema)

%description
NAME
DBIx::Class::OptimisticLocking - Optimistic locking support for
DBIx::Class

%package dev
Summary: dev components for the perl-DBIx-Class-OptimisticLocking package.
Group: Development
Provides: perl-DBIx-Class-OptimisticLocking-devel = %{version}-%{release}
Requires: perl-DBIx-Class-OptimisticLocking = %{version}-%{release}

%description dev
dev components for the perl-DBIx-Class-OptimisticLocking package.


%package license
Summary: license components for the perl-DBIx-Class-OptimisticLocking package.
Group: Default

%description license
license components for the perl-DBIx-Class-OptimisticLocking package.


%prep
%setup -q -n DBIx-Class-OptimisticLocking-0.02

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DBIx-Class-OptimisticLocking
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-DBIx-Class-OptimisticLocking/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/DBIx/Class/OptimisticLocking.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DBIx::Class::OptimisticLocking.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DBIx-Class-OptimisticLocking/LICENSE
