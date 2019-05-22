Name:    keepassxc-rofi
Version: 1
Release: 1%{?dist}
Summary: Rofi pop-up for KeePassXC

License: Public Domain
Source0: keepassxc-rofi

Requires: rofi
Requires: keepassxc
Requires: keyutils
Requires: libnotify
Requires: /bin/awk
Requires: /bin/sh

BuildRequires: asciidoc
BuildArch: noarch

%description

%prep
%setup -q

%build
a2x -d manpage -f manpage doc/keepassxc-rofi.1.adoc

%description
A Rofi driven user interface to KeePassXC's copy-to-clipboard functionality.

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p ${buildroot}/${_mandir}/man1
install -p -m 755 src/%{name} %{buildroot}/%{_bindir}
install -p -m 755 doc/keepassxc-rofi.1 ${buildroot}/${_mandir}/man1

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
* Wed May 22 2018 Gary Tierney <gary.tierney@fastmail.com> - 0.1-1
- Created package for keepassxc-rofi supporting a single password database locked with a password.

