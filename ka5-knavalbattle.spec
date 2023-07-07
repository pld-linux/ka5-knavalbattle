#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.04.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		knavalbattle
Summary:	knavalbattle
Name:		ka5-%{kaname}
Version:	23.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	f442c98f1ba81a6b5d48ab75e8780f48
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdnssd-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Naval Battle is a ship sinking game by KDE. Ships are placed on a
board which represents the sea. Players try to hit each others ships
in turns without knowing where they are placed. The first player to
destroy all ships wins the game.

%description -l pl.UTF-8
Naval Battle to gra w statki dla KDE. Okręty są umieszczone na
planszy, która reprezentuje morze. Gracze próbują trafić statki
przeciwnika, nie wiedząc, gdzie się one znajdują, wykonując strzały
na przemian. Gracz, który pierwszy zatopi wszystkie okręty
przeciwnika wygrywa.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knavalbattle
%{_desktopdir}/org.kde.knavalbattle.desktop
%{_iconsdir}/hicolor/128x128/apps/knavalbattle.png
%{_iconsdir}/hicolor/16x16/apps/knavalbattle.png
%{_iconsdir}/hicolor/22x22/apps/knavalbattle.png
%{_iconsdir}/hicolor/32x32/apps/knavalbattle.png
%{_iconsdir}/hicolor/48x48/apps/knavalbattle.png
%{_iconsdir}/hicolor/64x64/apps/knavalbattle.png
%{_datadir}/knavalbattle
%{_datadir}/metainfo/org.kde.knavalbattle.appdata.xml
%{_datadir}/qlogging-categories5/knavalbattle.categories
