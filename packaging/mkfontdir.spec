#
# spec file for package mkfontdir
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# This was part of the xorg-x11 package up to version 7.6
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
