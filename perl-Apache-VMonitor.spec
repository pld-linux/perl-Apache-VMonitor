# Conditional build:
%bcond_with	apache1		# build with apache1
%bcond_with 	tests		# perform "make test" (require to start apache)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	VMonitor
Summary:	Apache::VMonitor - visual system and Apache server monitor
Summary(pl):	Apache::VMonitor - wizualny monitor serwera Apache i systemu
Name:		perl-Apache-VMonitor
Version:	2.0
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	17c76c95f1714a3096cf0910bfcdc7e7
Source1:	%{name}.conf
BuildRequires:	apache-mod_perl >= 1.15
%if %{with tests}
BuildRequires:	perl-Apache-Scoreboard
BuildRequires:	perl-Template-Toolkit
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	apache-mod_perl >= 1.15
Requires:	perl-Apache-Scoreboard >= 0.08
Requires:	perl-GTop >= 0.09
Requires:	perl-Template-Toolkit
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
od¶wie¿ania. Wszystkie sekcje mog± byæ ukrywane/pokazywane dynamicznie
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

install -D %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/httpd.conf/80_Apache_VMonitor.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
%{_sysconfdir}/httpd/httpd.conf/*.conf
