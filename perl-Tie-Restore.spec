#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	Restore
Summary:	Tie::Restore - restores ties to an existing object
Summary(pl):	Tie::Restore - odtworzenie powi±zañ do istniej±cego obiektu
Name:		perl-Tie-Restore
Version:	0.11
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1300dfc45d0eb7e4cf0634c81c030230
Patch0:		%{name}-path.patch
URL:		http://search.cpan.org/dist/Tie-Restore/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides the opposite of the 'tied' function. Say you have %%hash that
is tied to $object. Then, it is relatively simple to get $object from
%%hash simply by saying

	$object = tied %%hash;

But, how does one go the other way? Simple, with Tie::Restore

	tie %%hash, 'Tie::Restore', $object;

Works for any kind of tie. (scalar, array, hash, filehandle)

%description -l pl
Ten modu³ dostarcza odwrotno¶æ funkcji 'tied'. Za³ó¿my, ¿e mamy %%hash
przywi±zany do obiektu $object. Wtedy mo¿na stosunkowo prosto otrzymaæ
$object z %%hash poprzez

	$object = tied %%hash;

Ale jak teraz zrobiæ na odwrót? Proste, przy u¿yciu Tie::Restore:

	tie %%hash, 'Tie::Restore', $object;

Dzia³a z dowolnym rodzajem przywi±zania (skalarem, tablic±, tablic±
asocjacyjn±, uchwytem do pliku).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
%{perl_vendorlib}/Tie/*.pm
%{_mandir}/man3/*
