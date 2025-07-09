#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Rich help formatters for argparse and optparse
Summary(pl.UTF-8):	Bogate funkcje formatujące pomoc dla argparse i optparse
Name:		python3-rich_argparse
Version:	1.7.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/rich-argparse/
Source0:	https://files.pythonhosted.org/packages/source/r/rich-argparse/rich_argparse-%{version}.tar.gz
# Source0-md5:	7b2f1bcac3742d37fe4ae967ae65609e
URL:		https://pypi.org/project/rich-argparse/
BuildRequires:	python3-build
BuildRequires:	python3-hatchling >= 1.11.0
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-rich >= 11.0.0
%if "%{_ver_lt %{py3_ver} 3.10}" == "1"
BuildRequires:	python3-typing_extensions
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rich_argparse allows to format argparse and optparse help using rich
(<https://pypi.org/project/rich/>). It improves the look and
readability of argparse's help while requiring minimal changes to the
code.

%description -l pl.UTF-8
rich_argparse pozwala formatować pomoc argparse i optparse przy użyciu
richa (<https://pypi.org/project/rich/>). Poprawia wygląd i czytelność
pomocy argparse, wymagając minimalnych zmian w kodzie.

%prep
%setup -q -n rich_argparse-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/rich_argparse
%{py3_sitescriptdir}/rich_argparse-%{version}.dist-info
