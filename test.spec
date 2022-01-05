Name:           test-upstream
Version:        1.0.0
Release:        1%{?dist}
Summary:        A test SPEC for soot

License:        Public-Domain
URL:     https://github.com/sparticvs/test-upstream       
Source0: https://github.com/sparticvs/test-upstream/archive/refs/tags/v%{version}.tar.gz 

BuildRequires:  
Requires:       

%description


%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Wed Jan  5 2022 Charles Timko <ctimko@redhat.com>
- 
