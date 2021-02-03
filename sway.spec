Summary:	i3-compatible Wayland compositor
Name:		sway
Version:	1.5.1
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/swaywm/sway/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9a7edc89abfc3f36d47546457e0bc901
Patch0:		x32.patch
URL:		https://swaywm.org/
BuildRequires:	OpenGLESv2-devel
BuildRequires:	bash-completion
BuildRequires:	cairo-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	json-c-devel >= 0.13
BuildRequires:	libevdev-devel
BuildRequires:	libinput-devel >= 1.6.0
BuildRequires:	libxcb-devel
BuildRequires:	meson >= 0.53.0
BuildRequires:	ninja
BuildRequires:	pango-devel
BuildRequires:	pcre-devel
BuildRequires:	pixman-devel
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	scdoc >= 1.9.2
BuildRequires:	systemd-devel >= 239
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.14
BuildRequires:	wlroots-devel >= 0.12.0
BuildRequires:	xorg-lib-libxkbcommon-devel
Requires:	json-c >= 0.13
Requires:	libinput >= 1.6.0
Requires:	systemd-libs >= 239
Requires:	wlroots >= 0.12.0
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
%{?noarchpackage}

%description backgrounds
Background images for sway compositor.

%package -n bash-completion-sway
Summary:	Bash completion for sway
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0
%{?noarchpackage}

%description -n bash-completion-sway
Bash completion for sway.

%package -n fish-completion-sway
Summary:	fish-completion for sway
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	fish
%{?noarchpackage}

%description -n fish-completion-sway
fish-completion for sway.

%package -n zsh-completion-sway
Summary:	ZSH completion for sway
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
%{?noarchpackage}

%description -n zsh-completion-sway
ZSH completion for sway.

%prep
%setup -q
%ifarch x32
%patch0 -p1
%endif

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
