%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	VMonitor
Summary:	Apache::VMonitor - Visual System and Apache Server Monitor
Summary(pl):	Apache::VMonitor - Wizualny monitor serwera Apache i systemu
Name:		perl-Apache-VMonitor
Version:	0.7
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
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
Ten modu� emuluje funkcjolano�� raportowania oferowan� przez top(1),
rozszerzon� dla proces�w mod_perla, oraz narz�dzi mount(1) i df(1).
Ma opcje wizualnego ostrzegania i konfigurowalny tryb automatycznego
od�wie�ania.  Wszystkie sekcje mog� by� ukrywane/pokazywane dynamicznie
przez interfejs WWW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
