#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Params
%define	pnam	Util
Summary:	Params::Util - Simple standalone param-checking functions
Summary(pl.UTF-8):	Params::Util - proste samodzielne funkcje do sprawdzania parametrów
Name:		perl-Params-Util
Version:	1.07
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Params/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	02db120c0eef87aae1830cc62bdec37b
URL:		http://search.cpan.org/dist/Params-Util/
BuildRequires:	perl-ExtUtils-CBuilder >= 0.27
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.52
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl(Scalar::Util) >= 1.18
BuildRequires:	perl-Test-Simple >= 0.42
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Params::Util provides a basic set of importable functions that makes
checking parameters a hell of a lot easier.

The functions provided by Params::Util check in the most strictly
correct manner, and in should not be fooled by odd cases.

%description -l pl.UTF-8
Params::Util udostępnia podstawowy zestaw importowalnych funkcji
znacznie ułatwiających sprawdzanie parametrów.

Funkcje dostarczane przez Params::Util sprawdzają poprawność w
najbardziej ścisły sposób i nie powinny dać się ogłupić przez
nietypowe przypadki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README
%{perl_vendorarch}/Params/Util.pm
%attr(755,root,root) %{perl_vendorarch}/auto/Params/Util/Util.so
%{_mandir}/man3/Params::Util.3pm*
