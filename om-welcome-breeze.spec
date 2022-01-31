Name:		om-welcome-breeze
Version:	2.3.0.11
Release:	1
Summary:	OpenMandriva Lx Welcome Page
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/rugyada/om-welcome-breeze
Source0:	%{name}-%version.tar.gz
Requires:	kdialog
Requires:	htmlscript >= 1.0.1
BuildRequires:	make
BuildArch:	noarch
%rename oma-welcome

%description
Introduce new users to the OpenMandriva Lx.

%prep
%setup -q
%autopatch -p1

%build
# Nothing to do here...

%install
%makeinstall_std

%find_lang om-welcome-breeze

%files -f om-welcome-breeze.lang
%{_sysconfdir}/xdg/autostart/om-welcome-breeze.desktop
%{_bindir}/enable-repo
%{_bindir}/disable-repo
%{_bindir}/om-welcome-breeze
%{_bindir}/om-welcome-breeze-launcher
%{_datadir}/%{name}/*
%{_datadir}/applications/om-welcome-breeze.desktop
