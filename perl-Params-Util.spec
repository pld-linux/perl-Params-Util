#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Params
%define	pnam	Util
Summary:	Params::Util - Simple standalone param-checking functions
Summary(pl):	Params::Util - proste samodzielne funkcje do sprawdzania parametrów
Name:		perl-Params-Util
Version:	0.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Params/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	47ff67318801dbc0aae41f94080cc8af
URL:		http://search.cpan.org/dist/Params-Util/
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl-Test-Simple >= 0.42
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Params::Util provides a basic set of importable functions that makes
checking parameters a hell of a lot easier.

The functions provided by Params::Util check in the most strictly
correct manner, and in should not be fooled by odd cases.

%description -l pl
Params::Util udostêpnia podstawowy zestaw importowalnych funkcji
znacznie u³atwiaj±cych sprawdzanie parametrów.

Funkcje dostarczane przez Params::Util sprawdzaj± poprawno¶æ w
najbardziej ¶cis³y sposób i nie powinny daæ siê og³upiæ przez
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
%{perl_vendorlib}/Params/Util.pm
%{_mandir}/man3/*
