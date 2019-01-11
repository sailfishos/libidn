Name:       libidn
Summary:    Internationalized Domain Name support library
Version:    1.23
Release:    2
Group:      System/Libraries
License:    LGPLv2.1+
URL:        http://www.gnu.org/software/libidn/
Source0:    http://ftp.gnu.org/gnu/libidn/libidn-%{version}.tar.gz
Patch0:     libidn-aarch64.patch
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

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
Man and info pages for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%lang_package

%build

%configure --disable-static \
    --disable-csharp \
    --disable-java \
    --with-pic

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

rm -f $RPM_BUILD_ROOT/%_infodir/dir
rm -rf $RPM_BUILD_ROOT%{_datadir}/emacs
rm -f  $RPM_BUILD_ROOT%_infodir/libidn-components.png
rm -f %{buildroot}%{_bindir}/idn
%find_lang libidn

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m0644 -t $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
        AUTHORS ChangeLog NEWS README THANKS

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f libidn.lang
%defattr(-,root,root,-)
%license COPYING.LIB
%{_libdir}/libidn.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libidn.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/libidn.pc

%files doc
%defattr(-,root,root,-)
%{_infodir}/%{name}*.*
%{_mandir}/man1/idn.*
%{_mandir}/man3/*.*
%{_docdir}/%{name}-%{version}
