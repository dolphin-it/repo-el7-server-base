Name: dolphinit-server-base
Version: 0.1.0
Release: 1.el7.64
Summary: Metapackage for basic server installs
Group: Applications/System
License: AGPL v3.0

Requires: vim
Requires: nano
Requires: epel-release
Requires: openssh-clients
Requires: openssh-server
Requires: ntp
Requires: ntpdate
Requires: rsync
Requires: wget
Requires: iotop
Requires: virt-top
Requires: htop
Requires: tcpdump
Requires: iftop
Requires: haveged
Requires: net-tools
Requires: curl
Requires: hdparm
Requires: mtr
Requires: nload
Requires: ethtool
Requires: postfix
Requires: python

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

%description
Metapackage for basic server installs

%files

%changelog
