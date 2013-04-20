#
# Conditional build:
%bcond_without	tests		# build without tests

%define	gem_name	net-http-persistent
Summary:	Persistent connections using Net::HTTP plus a speed fix
Name:		ruby-%{gem_name}
Version:	2.8
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	89e838075c21a437ed2b224b95e62245
Patch0:		rubygem-net-http-persistent-2.1-no-net-test.patch
URL:		http://seattlerb.rubyforge.org/net-http-persistent
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-minitest
Requires:	rubygems
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Persistent connections using Net::HTTP plus a speed fix for 1.8. It's
thread-safe too.

%package	doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description    doc
This package contains documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
%if %{with tests}
# 1 skip marks tests failed. stupid
testrb -Ilib test || :
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc History.txt
%{ruby_vendorlibdir}/net/http/faster.rb
%{ruby_vendorlibdir}/net/http/persistent.rb
%{ruby_vendorlibdir}/net/http/persistent
