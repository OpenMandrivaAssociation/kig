Summary:	KDE Interactive Geometry
Name:		kig
Version:	15.04.1
Release:	1
License:	GPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kig
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(python)
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

%description
Kig is a program for use in math classes in high school, to allow
students to interactively explore geometric concepts.

%files
%doc COPYING COPYING.DOC AUTHORS ChangeLog
%doc %{_docdir}/HTML/en/kig
%{_bindir}/kig
%{_bindir}/pykig.py
%{_datadir}/appdata/kig.appdata.xml
%{_iconsdir}/hicolor/*/*/*kig.*[gz]
%{_mandir}/man1/kig.1.*

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
