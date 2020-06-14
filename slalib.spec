%define _prefix __auto__
%define gemopt opt
%define name slalib
%define version 3.15.8
%define release 1.9.11
%define repository gemdev
%define debug_package %{nil}
%define arch %(uname -m)
%define checkout %(git log --pretty=format:'%h' -n 1) 

#These global defines are added to prevent stripping
# symbols on vxWorks cross-compiled code
# Getting 'strip' to work is probably only needed for
# building a related debug sub-package
#
# But this prevents all the strip warnings
# mrippa 20120202
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Summary: %{name} Package, an application for EPICS base
Name: %{name}
Version: %{version}
Release: %release.%(date +"%Y%m%d")git%{checkout}%{?dist}
License: EPICS Open License
Group: Applications/Engineering
Source0: %{name}-%{version}.tar.gz
ExclusiveArch: %{arch}
Prefix: %{_prefix}
## You may specify dependencies here
#BuildRequires: epics-base-devel
#Requires: epics-base-devel 
## Switch dependency checking off
# AutoReqProv: no

%description
EPICS is a set of Open Source software tools, libraries and applications developed collaboratively and used worldwide to create distributed soft real-time control systems for scientific instruments such as a particle accelerators, telescopes and other large scientific experiments.
This is the application %{name}.

%prep
%setup -q 

%build
make distclean uninstall
make

%install
## Write install instructions here, e.g
## install -D zzz/zzz  $RPM_BUILD_ROOT/%{_prefix}/zzz/zzz
export DONT_STRIP=1
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/%{gemopt}/epics/modules/slalib
cp -r lib $RPM_BUILD_ROOT/%{_prefix}/%{gemopt}/epics/modules/slalib/
cp -r include $RPM_BUILD_ROOT/%{_prefix}/%{gemopt}/epics/modules/slalib/

## if you want to do something after installation uncomment the following
## and list the actions to perform:
# %post
## actions, e.g. /sbin/ldconfig

## If you want to have a devel-package to be generated and do some
## %post-stuff regarding it uncomment the following:
# %post devel

## if you want to do something after uninstallation uncomment the following
## and list the actions to perform. But be aware of e.g. deleting directories,
## see the example below how to do it:
# %postun
if [ "$1" = "0" ]; then
	rm -rf/%{_prefix}/%{gemopt}/epics/modules/slalib
fi

## If you want to have a devel-package to be generated and do some
## %postun-stuff regarding it uncomment the following:
# %postun devel

## Its similar for %pre, %preun, %pre devel, %preun devel.

%clean
## Usually you won't do much more here than
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
## list files that are installed here, e.g
/%{_prefix}/%{gemopt}/epics/modules/slalib

%changelog
* Sat Jun 13 2020 Matt Rippa <mrippa@gemini.edu> 3.15.8-1.9.11.20200613git89d2d84
- Simplified setup prep (mrippa@gemini.edu)

* Sat Jun 13 2020 Matt Rippa <mrippa@gemini.edu> 3.15.8-1.9.11.20200613git2244484
- new package built with tito

## Write changes here, e.g.
* Fri Mar 9 2012 Mathew Rippa <mrippa@gemini.edu> 3.14.12.2-0
 - r3.14.12.2, rpmlint compliant
* Mon Feb 11 2008 Matt Rippa <mrippa@gemini.edu>, Felix Kraemer <fkraemer@gemini.edu> 2.0.11-3
- upgrade to work with EPICS framework
* Wed Dec 19 2007 Felix Kraemer <fkraemer@gemini.edu> 2.0.11-0
- initial release
