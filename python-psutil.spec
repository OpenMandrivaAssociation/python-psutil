%define srcname psutil

Name:           python-%{srcname}
Version:        2.0.0
Release:        1
Summary:        Interface for retrieving information on all running processes
Group:          Development/Python
License:        MIT
URL:            http://code.google.com/p/psutil/
Source0:        https://pypi.python.org/packages/source/p/psutil/%{srcname}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-distribute
BuildRequires:	python3-devel
BuildRequires:  python3-distribute

%description
psutil is a module providing an interface for retrieving information
on all running processes and system utilization (CPU, memory, disks,
network, users) in a portable way by using Python, implementing many
functionalities offered by command line tools.

%files
%{python_sitearch}/%{srcname}/
%{python_sitearch}/*.egg-info/
%{python_sitearch}/*.so

%package -n python3-%{srcname}
Summary:	%{summary}
Group:		Development/Python

%description -n python3-%{srcname}
psutil is a module providing an interface for retrieving information
on all running processes and system utilization (CPU, memory, disks,
network, users) in a portable way by using Python, implementing many
functionalities offered by command line tools.

%files -n python3-%{srcname}
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/*.egg-info/
%{python3_sitearch}/*.so

#--------------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}
# Remove shebangs
for file in psutil/*.py; do
  sed -i.orig -e 1d $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done

rm -rf %{py3dir}
cp -a . %{py3dir}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

pushd %{py3dir}
	CFLAGS="%{optflags} -lpython3.3m" %{__python3} setup.py build
popd

%install
%{__python} setup.py install --skip-build --root %{buildroot}

pushd %{py3dir}
	%{__python3} setup.py install --skip-build --root=%{buildroot}
popd
