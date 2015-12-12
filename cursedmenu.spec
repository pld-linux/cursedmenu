Summary:	ncurses based menu system for character based sessions
Summary(pl.UTF-8):	oparty o ncurses system menu dla sesji terminalowych
Name:		cursedmenu
Version:	1.0.4
Release:	6
License:	GPL v3
Group:		Applications
Source0:	http://dl.sourceforge.net/cursedmenu/%{name}-%{version}.tar.bz2
# Source0-md5:	31e9353ba603b95df3b742bfa3a0ed87
Patch0:		%{name}-gcc43.patch
Patch1:		%{name}-build.patch
URL:		http://cursedmenu.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cursed Menu aims to create an ncurses based menu system for character
based sessions. This menu program could be used to create user, system
administration, or utility menus for clients connecting with text
based clients such as telnet, ssh, or rlogin.

%description -l pl.UTF-8
Cursed Menu ma na celus tworzenie opartego o ncurses systemu menu dla
sesji tekstowych. Program ten pozwala na stworzenie menu uzytkownika,
administratora lub innych dla klientów korzystających z sesji
tekstowych, takich jak telnet, ssh czy rlogin.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CPPFLAGS="%{rpmcflags} -I/usr/include/ncurses"
export CPPFLAGS
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog src/{default.cmd,sub.cmd,sub2.cmd}
%attr(755,root,root) %{_bindir}/*
