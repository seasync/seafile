%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:		seafile
Version:	7.0.7
Release:	1%{?dist}
Summary:	seafile core

Group:		Libraries
License:	GPLv2
URL:		https://github.com/seasync/seafile
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot)

BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	sqlite-devel
BuildRequires:  libsearpc
BuildRequires:  libevent
BuildRequires:	vala
BuildRequires:	intltool

Requires:	libsearpc
Requires:	sqlite
Requires:	libevent

%description
The RPC framework for Seafile

%prep
%setup -q -n %{name}-%{version}


%build
%autogen.sh
%configure --enable-console \
	--prefix=/usr \
	PYTHON='/usr/bin/python3'
make %{?_smp_mflags}

%install
%makeinstall

%clean
rm -rf %{buildroot}

%post -n %name -p /sbin/ldconfig

%postun -n %name -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/seaf-cli
%{_bindir}/seaf-daemon
%{python3_sitearch}
%{_includedir}/seafile/*
