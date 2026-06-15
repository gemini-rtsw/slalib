%define _prefix /gem_base/epics/support
%define name slalib
%define repository gemdev
%define debug_package %{nil}
%define arch %(uname -m)
%define checkout %(if [ -n "$GIT_HASH" ]; then echo "$GIT_HASH"; else git rev-parse --short HEAD 2>/dev/null || echo nogit; fi)

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

Summary: %{name} Package, a module for EPICS base
Name: %{name}
Version: 1.9.7
Release: 6.git.%{checkout}%{?dist}
License: EPICS Open License
Group: Applications/Engineering
Source0: %{name}-%{version}.tar.gz
ExclusiveArch: %{arch}
Prefix: %{_prefix}
## You may specify dependencies here
BuildRequires: epics-base-devel = 7.0.7-0.gitd18bee6.el8 re2c gemini-ade
Requires: epics-base = 7.0.7-0.gitd18bee6.el8
## Switch dependency checking off
## AutoReqProv: no

%description
This is the module %{name}.

## If you want to have a devel-package to be generated uncomment the following:
%package devel
Summary: %{name}-devel Package
Group: Development/Gemini
Requires: %{name}
%description devel
This is the module %{name}.

%prep
%setup -q 

%build
make distclean uninstall
make

%install
export DONT_STRIP=1
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/%{name}
cp -r dbd $RPM_BUILD_ROOT/%{_prefix}/%{name}
#cp -r bin $RPM_BUILD_ROOT/%{_prefix}/%{name}
cp -r lib $RPM_BUILD_ROOT/%{_prefix}/%{name}
cp -r include $RPM_BUILD_ROOT/%{_prefix}/%{name}
cp -r configure $RPM_BUILD_ROOT/%{_prefix}/%{name}
# find $RPM_BUILD_ROOT/%{_prefix}/%{name}/configure -name ".git" -exec rm -rf {} \;


%postun
if [ "$1" = "0" ]; then
	rm -rf %{_prefix}/%{name}
fi


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#   /%{_prefix}/%{name}/bin
   /%{_prefix}/%{name}/lib

%files devel
%defattr(-,root,root)
   /%{_prefix}/%{name}/dbd
   /%{_prefix}/%{name}/include
   /%{_prefix}/%{name}/configure

%changelog
* Wed Jul 07 2021 Emma Kurz <emma.kurz@noirlab.edu> 1.9.7-5
- Closes issue #1
- New branch for EPICS 7 RTEMS 5

* Wed Dec 30 2020 Roberto Rojas <rrojas@gemini.edu> 1.9.7-4
- 

* Wed Dec 30 2020 Roberto Rojas <rrojas@gemini.edu> 1.9.7-3
- save everything

* Thu Oct 08 2020 fkraemer <fkraemer@gemini.edu> 1.9.7-2
- applied new version/release scheme and new yum repository structure
- Automatic commit of package [slalib] release
  [3.15.8-1.9.7.202008050433c130223].

* Fri Aug 28 2020 Felix Kraemer <fkraemer@gemini.edu> 3.15.8-1.9.7.2020082821310acb1b4
- Adjustments to include configuration from configure/RELEASE.local for testing
  purposes (fkraemer@gemini.edu)

* Wed Aug 05 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-1.9.7.202008050433c130223
- Release tag enriched with hour and minute (%%H%%M) to be able to build
  several RPMs a day without messing up the repo (fkraemer@gemini.edu)
- very small change to test merge request (fkraemer@gemini.edu)

* Sun Jul 26 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-1.9.7.202007265260771
- new package built with tito

* Sun Jul 26 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-1.9.7.20200726643cc78
- new package built with tito

* Sun Jul 26 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-4.1.13.20200726ff76345
- RPM build possible
- no bin dir, so removed from specfile (fkraemer@gemini.edu)
- added gemini-ade dependency (fkraemer@gemini.edu)

* Wed Jul 22 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-4.1.13.20200722b932e58
- fixed a merge conflict (fkraemer@gemini.edu)

* Wed Jul 22 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-4.1.13.202007220c32b86
- new package built with tito

* Wed Jul 22 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-4.1.13.20200722a1645a1
- new package built with tito

* Wed Jul 22 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-4.1.13.2020072238eb7bd
- new package built with tito

* Wed Jul 22 2020 fkraemer <fkraemer@gemini.edu> 3.15.8-4.1.13.2020072286a4352
- new package built with tito

