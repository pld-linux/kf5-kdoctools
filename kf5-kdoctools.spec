# TODO:
# - proper place for *.pri,
# - set ECM_MKSPECS_INSTALL_DIR in kde5-extra-cmake-modules
# - _IMPORT_PREFIX also must be set somewhere
# - runtime Requires if any
# - these dirs are not own by any package
#  /usr/include/KF5
#  /usr/lib/libexec
#  /usr/lib/plugins
#  /usr/share/kf5
# /usr/share/doc/HTML/*/
%define         _state          stable
%define		orgname		kdoctools

Summary:	Create documentation from DocBook
Name:		kf5-%{orgname}
Version:	5.0.0
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/frameworks/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	7048b70497c07e65c5f36842fd074850
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	polkit-qt-1-devel
BuildRequires:	qt5-linguist
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Provides tools to generate documentation in various format from
DocBook files.

%package devel
Summary:	Header files for %{orgname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{orgname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{orgname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{orgname}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DBIN_INSTALL_DIR=%{_bindir} \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DPLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQT_PLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQML_INSTALL_DIR=%{qt5dir}/qml \
	-DIMPORTS_INSTALL_DIR=%{qt5dirs}/imports \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_LIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_INCLUDE_INSTALL_DIR=%{_includedir} \
	-DECM_MKSPECS_INSTALL_DIR=%{qt5dir}/mkspecs/modules \
	-D_IMPORT_PREFIX=%{_prefix} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/checkXML5
%attr(755,root,root) %{_bindir}/meinproc5
%{_libdir}/libKF5XsltKde.a
%{_docdir}/HTML/*/kdoctools5-common
%dir %{_datadir}/kf5/kdoctools
%{_datadir}/kf5/kdoctools/customization
%{_mandir}/man1/checkXML5.1*
%{_mandir}/man7/kf5options.7*
%{_mandir}/man7/qt5options.7*
%{_mandir}/man8/meinproc5.8*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/XsltKde
%{_libdir}/cmake/KF5DocTools
