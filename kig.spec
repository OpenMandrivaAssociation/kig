%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	KDE Interactive Geometry
Name:		kig
Version:	25.08.3
Release:	2
License:	GPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/kig
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  gettext
BuildRequires:	boost-devel
BuildRequires:	boost-python-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Test)
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Kig is a program for use in math classes in high school, to allow
students to interactively explore geometric concepts.

%files -f %{name}.lang
%{_bindir}/kig
%{_bindir}/pykig.py
%{_datadir}/kig
%{_datadir}/applications/org.kde.kig.desktop
%{_datadir}/metainfo/*.xml
%{_iconsdir}/hicolor/*/*/*kig.*[gz]
%{_mandir}/man1/kig.1*
%{_qtdir}/plugins/kf6/parts/kigpart.so
%{_datadir}/katepart5/syntax/python-kig.xml
