%global sum     Backport of functools.lru_cache from Python 3.3 as published at ActiveState.
%global uname   backports.functools_lru_cache

Name:           python-backports-functools-lru-cache
Version:        1.3
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/jaraco/%{uname}
Source0:        https://github.com/jaraco/%{uname}/archive/%{version}.tar.gz

BuildArch:      noarch


%description
%{sum}

%package -n python2-backports-functools-lru-cache
Summary:        %sum

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools_scm

Requires:       python-setuptools
Requires:       python-backports


%description -n python2-backports-functools-lru-cache
%{sum}


%prep
%autosetup -n %{uname}-%{version}

# Remove setuptools_scm min version requirements
sed -i "s|setuptools_scm>=.*|setuptools_scm',|" setup.py


%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %{__python2} setup.py build


%install
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %{__python2} setup.py install --skip-build --root %{buildroot}
rm %{buildroot}%{python2_sitelib}/*-nspkg.pth


%files
%doc CHANGES.rst


%files -n python2-backports-functools-lru-cache
%{python2_sitelib}/%{uname}-%{version}-py*.egg-info
%{python2_sitelib}/backports/functools_lru_cache.py*


%changelog
* Thu Mar 16 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 1.3-1
- Initial packaging
