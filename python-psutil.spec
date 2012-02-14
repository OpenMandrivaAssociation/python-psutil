%global short_name psutil

# Filter Python modules from Provides

Name:		python-psutil
Version:	0.4.1
Release:	1
Summary:	A process utilities module for Python

Group:		Development/Python
License:	BSD
URL:		http://psutil.googlecode.com/
Source0:	http://psutil.googlecode.com/files/%{short_name}-%{version}.tar.gz

BuildRequires:	python-devel

%description
psutil is a module providing an interface for retrieving information on running
processes and system utilization (CPU, memory) in a portable way by using
Python, implementing many functionalities offered by tools like ps, top and
Windows task manager.



%prep
%setup -q -n %{short_name}-%{version}

# Remove shebangs
for file in psutil/*.py; do
  sed -i.orig -e 1d $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done



%build
export CFLAGS=$RPM_OPT_FLAGS
%{__python} setup.py build


%install
%{__python} setup.py install \
  --skip-build \
  --root %buildroot

 
%files
%defattr(-,root,root,-)
%doc CREDITS HISTORY LICENSE README docs/
%{python_sitearch}/%{short_name}/
%{python_sitearch}/*.egg-info
%{python_sitearch}/*.so
