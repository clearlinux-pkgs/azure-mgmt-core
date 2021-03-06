#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-mgmt-core
Version  : 1.2.2
Release  : 9
URL      : https://files.pythonhosted.org/packages/fc/f5/ed6e7dacd1140699bcc74f519d8461dc06425adbaf97629098fef58255ae/azure-mgmt-core-1.2.2.zip
Source0  : https://files.pythonhosted.org/packages/fc/f5/ed6e7dacd1140699bcc74f519d8461dc06425adbaf97629098fef58255ae/azure-mgmt-core-1.2.2.zip
Summary  : Microsoft Azure Management Core Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-mgmt-core-license = %{version}-%{release}
Requires: azure-mgmt-core-python = %{version}-%{release}
Requires: azure-mgmt-core-python3 = %{version}-%{release}
Requires: azure-core
Requires: azure-mgmt-nspkg
BuildRequires : azure-core
BuildRequires : azure-mgmt-nspkg
BuildRequires : buildreq-distutils3

%description
# Azure Management Core Library
        
        Azure management core library defines extensions to Azure Core that are specific to ARM (Azure Resource Management) needed when you use client libraries.
        
        As an end user, you don't need to manually install azure-mgmt-core because it will be installed automatically when you install other SDKs.

%package license
Summary: license components for the azure-mgmt-core package.
Group: Default

%description license
license components for the azure-mgmt-core package.


%package python
Summary: python components for the azure-mgmt-core package.
Group: Default
Requires: azure-mgmt-core-python3 = %{version}-%{release}

%description python
python components for the azure-mgmt-core package.


%package python3
Summary: python3 components for the azure-mgmt-core package.
Group: Default
Requires: python3-core
Provides: pypi(azure_mgmt_core)
Requires: pypi(azure_core)

%description python3
python3 components for the azure-mgmt-core package.


%prep
%setup -q -n azure-mgmt-core-1.2.2
cd %{_builddir}/azure-mgmt-core-1.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608046085
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/azure-mgmt-core
cp %{_builddir}/azure-mgmt-core-1.2.2/LICENSE.md %{buildroot}/usr/share/package-licenses/azure-mgmt-core/579cbb785bfbb1c60b923fc50948313e74cb168c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/azure-mgmt-core/579cbb785bfbb1c60b923fc50948313e74cb168c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
