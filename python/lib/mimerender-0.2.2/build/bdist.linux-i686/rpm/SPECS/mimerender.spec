%define name mimerender
%define version 0.2.2
%define unmangled_version 0.2.2
%define release 1

Summary: RESTful resource variant rendering using MIME Media-Types
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Martin Blech <mblech@bmat.com>
Url: http://code.google.com/p/mimerender/

%description

    This module allows, with the use of python decorators, to transparently select a render function for an HTTP request handler's result. It uses mimeparse to parse the HTTP Accept header and select the best available representation. Currently it only supports (web.py), but other web frameworks can be considered.
    

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
