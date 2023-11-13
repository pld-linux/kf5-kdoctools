#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
# - runtime Requires if any
# - package manual pages
%define		kdeframever	5.112
%define		qtver		5.15.2
%define		kfname		kdoctools

Summary:	Create documentation from DocBook
Name:		kf5-%{kfname}
Version:	5.112.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	d10a139c13809198da39a306c25d19d4
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel
BuildRequires:	ninja
BuildRequires:	perl-URI
BuildRequires:	perl-base
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qtver}
Requires:	docbook-style-xsl
Requires:	kf5-dirs
Requires:	kf5-karchive >= %{version}
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
Requires:	cmake >= 3.16

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
%ghost %{_libdir}/libKF5DocTools.so.5
%attr(755,root,root) %{_libdir}/libKF5DocTools.so.*.*
%{_docdir}/HTML/*/kdoctools5-common
%dir %{_datadir}/kf5/kdoctools
%{_datadir}/kf5/kdoctools/customization
%{_mandir}/man1/checkXML5.1*
%{_mandir}/man1/meinproc5.1*
%{_mandir}/man7/kf5options.7*
%{_mandir}/man7/qt5options.7*
%lang(ca) %{_mandir}/ca/man1/checkXML5.1*
%lang(ca) %{_mandir}/ca/man1/meinproc5.1*
%lang(ca) %{_mandir}/ca/man7/kf5options.7*
%lang(ca) %{_mandir}/ca/man7/qt5options.7*
%lang(de) %{_mandir}/de/man1/checkXML5.1*
%lang(de) %{_mandir}/de/man1/meinproc5.1*
%lang(de) %{_mandir}/de/man7/kf5options.7*
%lang(de) %{_mandir}/de/man7/qt5options.7*
%lang(es) %{_mandir}/es/man1/checkXML5.1*
%lang(es) %{_mandir}/es/man1/meinproc5.1*
%lang(es) %{_mandir}/es/man7/kf5options.7*
%lang(es) %{_mandir}/es/man7/qt5options.7*
%lang(it) %{_mandir}/id/man1/checkXML5.1*
%lang(it) %{_mandir}/it/man1/checkXML5.1*
%lang(it) %{_mandir}/it/man1/meinproc5.1*
%lang(it) %{_mandir}/it/man7/kf5options.7*
%lang(it) %{_mandir}/it/man7/qt5options.7*
%lang(nl) %{_mandir}/nl/man1/checkXML5.1*
%lang(nl) %{_mandir}/nl/man1/meinproc5.1*
%lang(nl) %{_mandir}/nl/man7/kf5options.7*
%lang(nl) %{_mandir}/nl/man7/qt5options.7*
%lang(pt) %{_mandir}/pt/man1/checkXML5.1*
%lang(pt) %{_mandir}/pt/man1/meinproc5.1*
%lang(pt) %{_mandir}/pt/man7/kf5options.7*
%lang(pt) %{_mandir}/pt/man7/qt5options.7*
%lang(pt_BR) %{_mandir}/pt_BR/man1/checkXML5.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/meinproc5.1*
%lang(pt_BR) %{_mandir}/pt_BR/man7/kf5options.7*
%lang(pt_BR) %{_mandir}/pt_BR/man7/qt5options.7*
%lang(ru) %{_mandir}/ru/man1/checkXML5.1*
%lang(ru) %{_mandir}/ru/man7/qt5options.7*
%lang(sv) %{_mandir}/sv/man1/checkXML5.1*
%lang(sv) %{_mandir}/sv/man1/meinproc5.1*
%lang(sv) %{_mandir}/sv/man7/kf5options.7*
%lang(sv) %{_mandir}/sv/man7/qt5options.7*
%lang(uk) %{_mandir}/uk/man1/checkXML5.1*
%lang(uk) %{_mandir}/uk/man1/meinproc5.1*
%lang(uk) %{_mandir}/uk/man7/kf5options.7*
%lang(uk) %{_mandir}/uk/man7/qt5options.7*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KDocTools
%{_libdir}/cmake/KF5DocTools
%{_libdir}/libKF5DocTools.so
