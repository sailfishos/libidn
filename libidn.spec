# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       libidn
Summary:    Internationalized Domain Name support library
Version:    1.21
Release:    1
Group:      System/Libraries
License:    LGPLv2.1+
URL:        http://www.gnu.org/software/libidn/
Source0:    http://ftp.gnu.org/gnu/libidn/libidn-%{version}.tar.gz
Source100:  libidn.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  autoconf


%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.



%package devel
Summary:    Development files for the libidn library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   glibc-devel

%description devel
This package includes header files and libraries necessary for
developing programs which use the GNU libidn library.



%prep
%setup -q -n %{name}-%{version}

# >> setup
%docs_package

%lang_package
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --disable-csharp \
    --disable-java \
    --with-pic

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
rm -f $RPM_BUILD_ROOT/%_infodir/dir
rm -rf $RPM_BUILD_ROOT%{_datadir}/emacs
rm -f  $RPM_BUILD_ROOT%_infodir/libidn-components.png
rm -f %{buildroot}%{_bindir}/idn
# << install post
%find_lang libidn



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files -f libidn.lang
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING.LIB
%{_libdir}/libidn.so.*
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%{_libdir}/libidn.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/libidn.pc
# << files devel

