Name:           uxplay
Version:        1.65.3
Release:        1%{?dist}

%global gittag  v%{version}

Summary:        AirPlay-Mirror and AirPlay-Audio server
License:        GPLv3+
URL:            https://github.com/FDH2/UxPlay
Source0:        https://github.com/FDH2/UxPlay/archive/%{gittag}/%{name}-%{version}.tar.gz

Packager:       UxPlay maintainer
 
BuildRequires:  cmake >= 3.4.1
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
Requires:       avahi

#RedHat and clones 
%if %{defined fedora} || %{defined rhel}
BuildRequires:  pkgconf
BuildRequires:  openssl-devel >= 3.0
BuildRequires:  libplist-devel >= 2.0
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
Requires:       openssl-libs >= 3.0
Requires:       libplist >= 2.0
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad-free
Requires:       gstreamer1-libav
%define  cmake_builddir redhat-linux-build
%endif

#SUSE
%if "%{_host_vendor}" == "suse"
BuildRequires:  pkg-config
BuildRequires:  libopenssl-3-devel
BuildRequires:  libplist-2_0-devel
BuildRequires:  avahi-compat-mDNSResponder-devel
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
Requires:       libopenssl3
Requires:       libplist-2_0-3
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-libav
%endif

#Mageia, OpenMandriva, pclinuxos (Mandrake descendents)
%if "%{_host_vendor}" == "mageia" || "%{_host_vendor}" == "OpenMandriva" || "%{_host_vendor}" == "mandriva"
%if "%{_host_vendor}" == "mandriva"
# "mandriva" is pclinuxos.
# as of 07/2023,  pclinuxos does not seem to supply openssl >= 3.0
# Note that UxPlay does not have a "GPL exception" allowing it to be
# distributed in binary form when linked to openssl < 3.0, unless
# openssl < 3.0 can be regarded as a "system library".
BuildRequires:  pkgconfig
BuildRequires:  %{mklibname openssl-devel} >= 1.1.1
Requires:       %{mklibname openssl1.1.0}
%else
BuildRequires:  pkgconf
BuildRequires:  %{mklibname openssl-devel} >= 3.0
Requires:       %{mklibname openssl3}
%endif
BuildRequires:  %{mklibname plist-devel} >= 2.0
Requires:       %{mklibname plist2.0_3}   
BuildRequires:  %{mklibname avahi-compat-libdns_sd-devel}
BuildRequires:  %{mklibname gstreamer1.0-devel}
%if "%{_host_vendor}" == "OpenMandiva" 
BuildRequires:  %{mklibname gst-plugins-base1.0-devel}
%else
BuildRequires:  %{mklibname gstreamer-plugins-base1.0-devel}
%endif
Requires:       gstreamer1.0-plugins-base
Requires:       gstreamer1.0-plugins-good
Requires:       gstreamer1.0-plugins-bad
Requires:       gstreamer1.0-libav
%endif

%description
An AirPlay2 Mirror and AirPlay2 Audio (but not Video) server that provides
screen-mirroring (with audio) of iOS/MacOS clients in a display window on
the server host (which can be shared using a screen-sharing application);
Apple Lossless Audio (ALAC) (e.g.,iTunes) can be streamed from client to
server in non-mirror mode

%prep

%autosetup -n UxPlay-%{version}

%cmake -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}

%build

%if %{defined cmake_builddir}
cd %{cmake_builddir}
%else
cd build
%endif

%make_build

%install

%if %{defined cmake_builddir}
cd %{cmake_builddir}
%else
cd build
%endif

%make_install

%files
%{_bindir}/uxplay
%{_mandir}/man1/uxplay.1*

%doc
%{_docdir}/%{name}/README.txt
%{_docdir}/%{name}/README.html
%{_docdir}/%{name}/README.md

%license
%{_docdir}/%{name}/LICENSE
%{_docdir}/%{name}/llhttp/LICENSE-MIT

%changelog
* Wed Jul 26 2023 UxPlay maintainer <https://github.com/FDH2/UxPlay>
  Initial uxplay.spec: tested on Fedora 38, Rocky Linux 9.2, OpenSUSE
  Leap 15.5, Mageia 9, OpenMandriva ROME, pclinuxos
- 
