Summary:	i3-compatible Wayland compositor
Name:		sway
Version:	1.10.1
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/swaywm/sway/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	613475773afc3a3def1380f1ff214942
Patch0:		x32.patch
URL:		https://swaywm.org/
BuildRequires:	bash-completion-devel
BuildRequires:	cairo-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	json-c-devel >= 0.13
BuildRequires:	libdrm-devel
BuildRequires:	libevdev-devel
BuildRequires:	libinput-devel >= 1.26.0
BuildRequires:	libxcb-devel
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja
BuildRequires:	pango-devel
BuildRequires:	pcre2-8-devel
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	scdoc >= 1.9.2
BuildRequires:	systemd-devel >= 1:239
BuildRequires:	udev-devel
BuildRequires:	wayland-devel >= 1.21.0
BuildRequires:	wayland-protocols >= 1.24
BuildRequires:	wlroots0.18-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 1.5.0
Requires:	json-c >= 0.13
Requires:	libinput >= 1.26.0
Requires:	systemd-libs >= 1:239
Requires:	wayland >= 1.21.0
Requires:	xorg-lib-libxkbcommon >= 1.5.0
Suggests:	xorg-xserver-Xwayland
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sway is a tiling Wayland compositor and a drop-in replacement for the
i3 window manager for X11. It works with your existing i3
configuration and supports most of i3's features, plus a few extras.

Sway allows you to arrange your application windows logically, rather
than spatially. Windows are arranged into a grid by default which
maximizes the efficiency of your screen and can be quickly manipulated
using only the keyboard.

%package backgrounds
Summary:	Background images for sway compositor
Group:		Themes
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description backgrounds
Background images for sway compositor.

%package -n bash-completion-sway
Summary:	Bash completion for sway
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-sway
Bash completion for sway.

%package -n fish-completion-sway
Summary:	fish-completion for sway
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	fish
BuildArch:	noarch

%description -n fish-completion-sway
fish-completion for sway.

%package -n zsh-completion-sway
Summary:	ZSH completion for sway
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-sway
ZSH completion for sway.

%prep
%setup -q
%patch -P0 -p1

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING.md README.md
%dir %{_sysconfdir}/sway
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sway/config
%attr(755,root,root) %{_bindir}/sway
%attr(755,root,root) %{_bindir}/swaybar
%attr(755,root,root) %{_bindir}/swaymsg
%attr(755,root,root) %{_bindir}/swaynag
%{_datadir}/wayland-sessions/sway.desktop
%{_mandir}/man1/sway.1*
%{_mandir}/man1/swaymsg.1*
%{_mandir}/man1/swaynag.1*
%{_mandir}/man5/sway-bar.5*
%{_mandir}/man5/sway-input.5*
%{_mandir}/man5/sway-output.5*
%{_mandir}/man5/sway.5*
%{_mandir}/man5/swaynag.5*
%{_mandir}/man7/sway-ipc.7*
%{_mandir}/man7/swaybar-protocol.7*

%files backgrounds
%defattr(644,root,root,755)
%dir %{_datadir}/backgrounds/sway
%{_datadir}/backgrounds/sway/Sway_Wallpaper_Blue_*.png

%files -n bash-completion-sway
%defattr(644,root,root,755)
%{bash_compdir}/sway
%{bash_compdir}/swaybar
%{bash_compdir}/swaymsg

%files -n fish-completion-sway
%defattr(644,root,root,755)
%{fish_compdir}/sway.fish
%{fish_compdir}/swaymsg.fish
%{fish_compdir}/swaynag.fish

%files -n zsh-completion-sway
%defattr(644,root,root,755)
%{zsh_compdir}/_sway
%{zsh_compdir}/_swaymsg
