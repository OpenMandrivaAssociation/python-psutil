%define module psutil

Name:		python-psutil
Version:	7.2.2
Release:	1
Summary:	Interface for retrieving information on all running processes
Group:		Development/Python
License:	MIT
URL:		https://github.com/giampaolo/psutil
Source0:	https://github.com/giampaolo/psutil/archive/release-%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	procps-ng
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	gettext-devel
Requires:	procps-ng
%rename python3-psutil

%description
psutil is a module providing an interface for retrieving information
on all running processes and system utilization (CPU, memory, disks,
network, users) in a portable way by using Python, implementing many
functionalities offered by command line tools.

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{pyver}"
%py_build

%files
%{py_platsitedir}/%{module}/
%{py_platsitedir}/%{module}-%{version}.dist-info
