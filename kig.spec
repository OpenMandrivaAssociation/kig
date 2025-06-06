%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	KDE Interactive Geometry
Name:		kig
Version:	23.08.5
Release:	6
License:	GPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/kig
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  gettext
BuildRequires:	boost-devel
BuildRequires:	boost-python-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Emoticons)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5XmlPatterns)

%description
Kig is a program for use in math classes in high school, to allow
students to interactively explore geometric concepts.

%files -f kig.lang
%{_bindir}/kig
%{_bindir}/pykig.py
%{_libdir}/qt5/plugins/kf5/parts/kigpart.so
%{_datadir}/kig
%{_datadir}/applications/org.kde.kig.desktop
%{_datadir}/metainfo/*.xml
%optional %{_datadir}/katepart5/syntax/python-kig.xml
%{_datadir}/kxmlgui5/kig/*.rc
%{_iconsdir}/hicolor/*/*/*kig.*[gz]
%{_mandir}/man1/kig.1.*

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 \
	-DPYTHON_INCLUDE_DIR=%(python -c "from distutils.sysconfig import get_python_inc; print (get_python_inc());") \
	-DPYTHON_LIBRARY=%{_libdir}/libpython%(python --version |cut -d' ' -f2 |cut -d. -f1-2).so

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kig --with-html --with-man --all-name
