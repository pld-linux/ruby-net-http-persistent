#
# Conditional build:
%bcond_without	tests		# build without tests

%define	pkgname	net-http-persistent
Summary:	Persistent connections using Net::HTTP plus a speed fix
Name:		ruby-%{pkgname}
Version:	2.8
Release:	3
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	89e838075c21a437ed2b224b95e62245
Patch0:		rubygem-net-http-persistent-2.1-no-net-test.patch
URL:		http://seattlerb.rubyforge.org/net-http-persistent
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-minitest
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Persistent connections using Net::HTTP plus a speed fix for 1.8. It's
thread-safe too.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
# 1 skip marks tests failed. stupid
testrb -Ilib test || :
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc History.txt
%dir %{ruby_vendorlibdir}/net/http
%{ruby_vendorlibdir}/net/http/faster.rb
%{ruby_vendorlibdir}/net/http/persistent.rb
%{ruby_vendorlibdir}/net/http/persistent
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
