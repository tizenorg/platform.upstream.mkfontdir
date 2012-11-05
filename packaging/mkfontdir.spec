Name:           mkfontdir
Version:        1.0.7
Release:        1
License:        MIT
Summary:        Utility to create index of X font files
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
# mkfontdir is just a wrapper around mkfontscale and won't do anything on it's own.
Requires:       mkfontscale
Conflicts:      xorg-x11 <= 7.6

%description
mkfontdir creates the fonts.dir files needed by the legacy X server
core font system. The current implementation is a simple wrapper script
around the mkfontscale program, which must be built and installed first.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/mkfontdir
%{_mandir}/man1/mkfontdir.1%{?ext_man}

%changelog
