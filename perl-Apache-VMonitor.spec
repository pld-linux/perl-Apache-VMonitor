# TODO
# - webapps?
# Conditional build:
%bcond_with	apache1		# build with apache1
%bcond_with	tests		# perform "make test" (require to start apache)

%define		pdir	Apache
%define		pnam	VMonitor
Summary:	Apache::VMonitor - visual system and Apache server monitor
Summary(pl.UTF-8):	Apache::VMonitor - wizualny monitor serwera Apache i systemu
Name:		perl-Apache-VMonitor
Version:	2.07
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	decb0649220019a109acfa49d35b8f92
Source1:	%{name}.conf
URL:		http://search.cpan.org/dist/Apache-VMonitor/
BuildRequires:	apache-mod_perl-devel >= 1.15
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildConflicts:	apache1-mod_perl
%if %{with tests}
BuildRequires:	perl-Apache-Scoreboard
BuildRequires:	perl-Template-Toolkit
%endif
Requires:	apache-mod_perl >= 1.15
Requires:	perl-Apache-Scoreboard >= 2.08
Requires:	perl-GTop >= 0.12
Requires:	perl-Template-Toolkit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module emulates the reporting functionalities of top(1), extended
for mod_perl processes, mount(1), and df(1) utilities. It has a visual
alerting capabilities and configurable automatic refresh mode. All the
sections can be shown/hidden dynamically through the web interface.

%description -l pl.UTF-8
Ten moduł emuluje funkcjolaność raportowania oferowaną przez top(1),
rozszerzoną dla procesów mod_perla, oraz narzędzi mount(1) i df(1). Ma
opcje wizualnego ostrzegania i konfigurowalny tryb automatycznego
odświeżania. Wszystkie sekcje mogą być ukrywane/pokazywane dynamicznie
przez interfejs WWW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	MOD_PERL=%{?with_apache1:1}%{!?with_apache1:2}
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/80_Apache_VMonitor.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd/conf.d/80_Apache_VMonitor.conf
