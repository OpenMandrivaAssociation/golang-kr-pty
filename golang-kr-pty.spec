%define prerelease 3b1f6487b7fc649d5f146df04e623bd55ba1bf7f
%define import_path github.com/kr/pty
%define gopath %{_libdir}/golang
%define gosrc %{gopath}/src/pkg/%{import_path}
%define shortcommit %(c=%{prerelease}; echo ${c:0:7})
%define debug_package %nil

Summary:	PTY interface for Go
Name:		golang-kr-pty
Version:	0.1.git%{shortcommit}
Release:	2
License:	MIT
Group:		Development/Other
Url:		https://%{import_path}
Source0:        https://%{import_path}/archive/%{prerelease}.tar.gz
Provides:       golang(%{import_path}) = %{version}-%{release}
BuildArch:	noarch

%description
Pty is a Go package for using UNIX pseudo-terminals.

%prep
%setup -q -n pty-%{prerelease}

%build

%install
mkdir -p %{buildroot}%{gosrc}
cp -av * %{buildroot}%{gosrc}/
rm -f %{buildroot}%{gosrc}/{License,README.md}

%files
%doc License README.md
%{gosrc}/*
