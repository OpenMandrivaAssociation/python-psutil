%define srcname psutil

Name:           python-%{srcname}
Version:	7.1.3
Release:	1
Summary:        Interface for retrieving information on all running processes
Group:          Development/Python
License:        MIT
URL:            https://code.google.com/p/psutil/
Source0:	https://github.com/giampaolo/psutil/archive/release-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	python3-devel
BuildRequires:	gettext-devel
%rename python3-psutil

%description
psutil is a module providing an interface for retrieving information
on all running processes and system utilization (CPU, memory, disks,
network, users) in a portable way by using Python, implementing many
functionalities offered by command line tools.

%files
%{py_platsitedir}/%{srcname}/
%{py_platsitedir}/psutil-%{version}.dist-info
