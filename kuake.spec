Summary:	Kuake is a KDE konsole
Summary(pl.UTF-8):	Kuake - konsola KDE
Name:		kuake
Version:	0.4
Release:	1
License:	GPL v2
Group:		Terminals
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	92ccfd9298f969b4aeb78998421770c9
URL:		http://www.kde-apps.org/content/show.php?content=28808
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kuake is a KDE konsole application with the look and feel of that in
the Quake engine.

%description -l pl.UTF-8
Kuake to konsola działająca w środowisku KDE, wyglądem i zachowaniem
przypomina konsole w grach takich jak Quake.

%prep
%setup -q

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/kuake.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/kuake.desktop

mv -f $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/apps/kuake
%{_datadir}/apps/kuake/kuakeui.rc
%{_desktopdir}/kde/kuake.desktop
%{_iconsdir}/hicolor/*/apps/kuake.png
