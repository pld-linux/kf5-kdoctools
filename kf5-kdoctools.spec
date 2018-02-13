# TODO:
# - runtime Requires if any
# - package manual pages
%define		kdeframever	5.43
%define		qtver		5.4.0
%define		kfname		kdoctools

Summary:	Create documentation from DocBook
Name:		kf5-%{kfname}
Version:	5.43.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	aec9d49e1bef4aa20151ec06c2fcffe5
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	docbook-dtd45-xml
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	perl-URI
BuildRequires:	polkit-qt-1-devel
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Provides tools to generate documentation in various format from
DocBook files.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtver}
Requires:	cmake >= 2.6.0

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/checkXML5
%attr(755,root,root) %{_bindir}/meinproc5
%attr(755,root,root) %ghost %{_libdir}/libKF5DocTools.so.5
%attr(755,root,root) %{_libdir}/libKF5DocTools.so.*.*
%{_docdir}/HTML/*/kdoctools5-common
%dir %{_datadir}/kf5/kdoctools
%{_datadir}/kf5/kdoctools/customization
%{_mandir}/man1/checkXML5.1*
%{_mandir}/man1/meinproc5.1*
%{_mandir}/man7/kf5options.7*
%{_mandir}/man7/qt5options.7*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KDocTools
%{_libdir}/cmake/KF5DocTools
%attr(755,root,root) %{_libdir}/libKF5DocTools.so
