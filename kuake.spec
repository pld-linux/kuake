Summary:	Kuake is a KDE konsole
Summary(pl):	Kuake to konsola KDE
Name:		kuake
Version:	0.2.1
Release:	1
License:	GPL v2
Vendor:		Martin Galpin <martin@nemohackers.org>
Group:		Terminals
Source0:	http://216.26.131.89/software/kuake/%{name}-%{version}.tar.gz
URL:		http://www.nemohackers.org/index.php?p=kuake
BuildRequires:	qt-devel
Requires:	qt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kuake is a KDE konsole application with the look and feel of that in
the Quake engine.

%description -l pl
Kuake to kosola dzia³aj±ca w ¶rodowisku KDE, wygl±dem i zachowaniem
przypomina konsole w grach takich jak Quake.

%prep
%setup -q

%build
%configure

%{__make}

%install

rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applnk/Utilities/kuake.desktop
%{_datadir}/apps/kuake/kuakeui.rc
%{_datadir}/icons/locolor/16x16/apps/kuake.png
%{_datadir}/icons/locolor/32x32/apps/kuake.png
