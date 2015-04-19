Summary:	xcmsdb - Device Color Characterization utility for X Color Management System
Summary(pl.UTF-8):	xcmsdb - charakterystyka kolorów urządzeń dla systemu zarządzania kolorami X
Name:		xorg-app-xcmsdb
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xcmsdb-%{version}.tar.bz2
# Source0-md5:	9956d751ea3ae4538c3ebd07f70736a0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xcmsdb application is used to load, query, or remove Device Color
Characterization data stored in properties on the root window of the
screen as specified in section 7, Device Color Characterization, of
the X11 Inter-Client Communication Conventions Manual (ICCCM).

%description -l pl.UTF-8
Aplikacja xcmsdb służy do wczytywania, pobierania i usuwania danych
o charakterystyce kolorów urządzeń (Device Color Characterization) we
właściwościach głównego okna ekranu, zgodnie z opisem w sekcji 7
(Device Color Characterization) podręcznika konwencji komunikacji
między klientami X11 (ICCCM - X11 Inter-Client Communication
Conventions Manual).

%prep
%setup -q -n xcmsdb-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xcmsdb
%{_mandir}/man1/xcmsdb.1*
