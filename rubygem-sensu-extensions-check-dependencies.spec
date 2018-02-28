# Generated from sensu-extensions-check-dependencies-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu-extensions-check-dependencies

Name:               rubygem-%{gem_name}
Version:            1.0.1
Release:            1%{?dist}
Summary:            Filter events when an event already exists for a defined check dependency
License:            MIT
URL:                https://github.com/sensu-extensions/sensu-extensions-check-dependencies
Source0:            https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:      rubygems-devel
BuildRequires:      rubygem(rspec)

Requires:           rubygems
Requires:           rubygem(sensu-extension)

BuildArch: noarch

%if 0%{?rhel}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
Filter events when an event already exists for a defined check dependency.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# Disabled unit tests because working network is required
#rspec spec
popd


%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md


%changelog
* Thu Nov 02 2017 Martin Mágr <mmagr@redhat.com> - 1.0.1-1
- Initial package
