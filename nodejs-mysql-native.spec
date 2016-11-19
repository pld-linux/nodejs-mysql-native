%define		pkg	mysql-native
Summary:	MySQL protocol client for Node.js
Name:		nodejs-%{pkg}
Version:	0.4.7
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/mysql-native/-/%{pkg}-%{version}.tgz
# Source0-md5:	e08a768366196f6a3917ed29038d3f66
URL:		http://github.com/sidorares/nodejs-mysql-native
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs >= 0.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL protocol client for Node.js.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr lib package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog LICENSE README.md
%{nodejs_libdir}/%{pkg}
%{_examplesdir}/%{name}-%{version}
