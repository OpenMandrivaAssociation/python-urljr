%define module urljr
Name: 		python-%module
Version: 	1.0.0
Release: 	2
License: 	GPL
Summary: 	JanRain's URL Utilities
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-%{version}-build
BuildRequires: 	python-devel
Requires: 	python-curl
Url: 		https://www.openidenabled.com/openid/libraries/python
Source: 	http://www.openidenabled.com/resources/downloads/python-openid/python-urljr-%{version}.tar.gz
Buildarch:	noarch

%description
JanRain's URL Utilities

%prep
%setup

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc README urljr/test/
%{python_sitelib}/*



%changelog
* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 1.0.0-1mdv2011.0
+ Revision: 683272
- import python-urljr


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 1.0.0
- first release for Mandriva 
