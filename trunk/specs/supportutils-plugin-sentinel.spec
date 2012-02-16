#
# spec file for package supportutils-plugin-netiq-sentinel (Version 1.0-1)
#
# Copyright (C) 2012 NetIQ, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild  

Name:         supportutils-plugin-netiq-sentinel
License:      GPLv2
Group:        Productivity/Security
Autoreqprov:  on
Version:      1.0.1
Release:      1.1.20120216.PTF.1
Source:       %{name}-%{version}.tar.gz
Summary:      Supportconfig Plugin for NetIQ Sentinel
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Vendor:       NetIQ
Requires:     supportutils

%description
Sentinel plugin for the supportconfig command (part of the supportutils package) to gather Sentinel-specific information during execution of supportconfig.

Authors:
Aaron Burgemeister, ab@novell.com, dajoker@gmail.com

%prep
%setup -q

%build
gzip -9f sentplugin.8
gzip -9f sentplugin.properties.5

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -d $RPM_BUILD_ROOT/usr/share/man/man5
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0544 sentplugin $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -m 0644 sentplugin.properties $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -m 0644 sentplugin.properties.5.gz $RPM_BUILD_ROOT/usr/share/man/man5/sentplugin.properties.5.gz
install -m 0644 sentplugin.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/sentplugin.8.gz

%files
%defattr(0755,root,root)
%dir /usr/lib/supportconfig
%dir /usr/lib/supportconfig/plugins
/usr/lib/supportconfig/plugins/sentplugin
%config /usr/lib/supportconfig/plugins/sentplugin.properties
/usr/share/man/man5/sentplugin.properties.5.gz
/usr/share/man/man8/sentplugin.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Jan 27 2012 ab@novell.com
-Fixing issue with psql command in script
-Fixing spec file to treat sentplugin.properties as config file
-Excluding gathering of last 500 lines of files ending in .hprof (memory dumps) from log directory.

* Fri Jan 20 2012 ab@novell.com
-Adding ability to pick up Jetty configuration files in Sentinel 7.

* Mon Jan 16 2012 ab@novell.com
-Adding support for alternate Sentinel/LogManager install base locations via sentplugin.properties file


