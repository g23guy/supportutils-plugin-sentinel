#
# spec file for package supportutils-plugin-sentinel (Version 1.0-0)
#
# Copyright (C) 2010 Novell, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild  

Name:         supportutils-plugin-sentinel
URL:          http://www.novell.com/products/sentinel/overview.html
License:      GPLv2
Group:        Documentation/SuSE
Autoreqprov:  on
Version:      1.0
Release:      DEV_20100929.1
Source:       %{name}-%{version}.tar.gz
Summary:      Supportconfig Plugin for Novell Sentinel
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     supportconfig-plugin-resource
Requires:     sentinel

%description
Supportconfig plugin for Novell Sentinel. Gathers information directly 
related to Sentinel. Plugins extend supportconfig functionality and 
include the output in the supportconfig tar ball. Supportconfig saves 
the plugin output as plugin-sentinel.txt.

Please submit bug fixes or comments via:
    https://code.google.com/p/supportutils-plugin-sentinel/issues/list

Authors:
--------
    Jason Record <jrecord@novell.com>

%prep
%setup -q
%build
gzip -9f sentinel-plugin.8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/opt/supportconfig/plugins
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0500 sentinel $RPM_BUILD_ROOT/opt/supportconfig/plugins
install -m 0644 sentinel-plugin.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/sentinel-plugin.8.gz

%files
%defattr(-,root,root)
/opt/supportconfig/plugins/*
/usr/share/man/man8/sentinel-plugin.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog -n supportutils-plugin-sentinel

