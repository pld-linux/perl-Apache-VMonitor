%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	VMonitor
Summary:	Apache::VMonitor - Visual System and Apache Server Monitor
Summary(pl):	Apache::VMonitor - wizualny monitor serwera Apache i systemu
Name:		perl-Apache-VMonitor
Version:	0.8
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	88cfba14794b50cb0642931cd19d42da
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	apache-mod_perl >= 1.15
Requires:	perl-Apache-Scoreboard >= 0.08
Requires:	perl-GTop >= 0.09
Requires:	perl-Time-HiRes >= 01.19
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module emulates the reporting functionalities of top(1), extended
for mod_perl processes, mount(1), and df(1) utilities. It has a visual
alerting capabilities and configurable automatic refresh mode. All the
sections can be shown/hidden dynamically through the web interface.

%description -l pl
Ten modu³ emuluje funkcjolano¶æ raportowania oferowan± przez top(1),
rozszerzon± dla procesów mod_perla, oraz narzêdzi mount(1) i df(1).
Ma opcje wizualnego ostrzegania i konfigurowalny tryb automatycznego
od¶wie¿ania.  Wszystkie sekcje mog± byæ ukrywane/pokazywane dynamicznie
przez interfejs WWW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
