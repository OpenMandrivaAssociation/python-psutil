%define srcname psutil

Name:           python-%{srcname}
Version:	5.8.0
Release:	1
Summary:        Interface for retrieving information on all running processes
Group:          Development/Python
License:        MIT
URL:            http://code.google.com/p/psutil/
Source0:	https://github.com/giampaolo/psutil/archive/release-%{version}.tar.gz
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
BuildRequires:	python3-devel
BuildRequires:  python3-distribute
%rename python3-psutil

%description
psutil is a module providing an interface for retrieving information
on all running processes and system utilization (CPU, memory, disks,
network, users) in a portable way by using Python, implementing many
functionalities offered by command line tools.

%files
%{py3_platsitedir}/%{srcname}/
%{py3_platsitedir}/*.egg-info/

%package -n python2-%{srcname}
Summary:	%{summary}
Group:		Development/Python

%description -n python2-%{srcname}
psutil is a module providing an interface for retrieving information
on all running processes and system utilization (CPU, memory, disks,
network, users) in a portable way by using Python, implementing many
functionalities offered by command line tools.

%files -n python2-%{srcname}
%{py2_platsitedir}/%{srcname}/
%{py2_platsitedir}/*.egg-info/

#--------------------------------------------------------------------

%prep
%setup -q -n %{srcname}-release-%{version}
# Remove shebangs
for file in psutil/*.py; do
  sed -i.orig -e 1d $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done

rm -rf %{py3dir}
cp -a . %{py3dir}

%build
CFLAGS="%{optflags}" %{__python2} setup.py build

pushd %{py3dir}
	CFLAGS="%{optflags} `python3-config --libs`" %{__python3} setup.py build
popd

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

pushd %{py3dir}
	%{__python3} setup.py install --skip-build --root=%{buildroot}
popd
