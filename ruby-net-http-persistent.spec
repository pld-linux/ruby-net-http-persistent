#
# Conditional build:
%bcond_without	tests		# build without tests

%define	pkgname	net-http-persistent
Summary:	Persistent connections using Net::HTTP plus a speed fix
Summary(pl.UTF-8):	Trwałe połączenia przy użyciu Net::HTTP z poprawą szybkości
Name:		ruby-%{pkgname}
Version:	2.9.4
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	61cb21cccc85ddca77ee58af25bcf51f
Patch0:		rubygem-net-http-persistent-2.1-no-net-test.patch
URL:		http://seattlerb.rubyforge.org/net-http-persistent
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-minitest
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Persistent connections using Net::HTTP plus a speed fix for Ruby 1.8.
It's thread-safe too.

%description -l pl.UTF-8
Trwałe połączenia przy użyciu Net::HTTP z poprawą szybkości dla
Ruby'ego 1.8. Moduł jest bezpieczny względem wątków.

%package doc
Summary:	Documentation for Net::HTTP::Persistent module
Summary(pl.UTF-8):	Dokumentacja do modułu Net::HTTP::Persistent
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for Net::HTTP::Persistent module.

%description doc -l pl.UTF-8
Dokumentacja do modułu Net::HTTP::Persistent.

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
