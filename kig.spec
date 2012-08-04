Name:		kig
Summary:	KDE Interactive Geometry
Version: 4.9.0
Release: 1
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://edu.kde.org/kig
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	boost-devel

%description
Kig is a program for use in math classes in high school, to allow
students to interactively explore geometric concepts.

%files
%doc COPYING COPYING.DOC AUTHORS ChangeLog
%doc %{_kde_docdir}/HTML/en/kig
%{_kde_appsdir}/kig
%{_kde_bindir}/kig
%{_kde_bindir}/pykig.py
%{_kde_libdir}/kde4/kigpart.so
%{_kde_iconsdir}/*/*/apps/kig.*
%{_kde_iconsdir}/*/*/mimetypes/application-x-kig.*
%{_kde_applicationsdir}/kig.desktop
%{_kde_services}/kig_part.desktop
%{_kde_appsdir}/katepart/syntax/python-kig.xml
%{_kde_mandir}/man1/kig.1.*

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

