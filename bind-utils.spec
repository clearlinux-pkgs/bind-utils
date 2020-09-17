#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9521A7ED5DACE918 (codesign@isc.org)
#
%define keepstatic 1
Name     : bind-utils
Version  : 9.16.7
Release  : 79
URL      : https://downloads.isc.org/isc/bind9/9.16.7/bind-9.16.7.tar.xz
Source0  : https://downloads.isc.org/isc/bind9/9.16.7/bind-9.16.7.tar.xz
Source1  : https://downloads.isc.org/isc/bind9/9.16.7/bind-9.16.7.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause ISC MPL-2.0
Requires: bind-utils-bin = %{version}-%{release}
Requires: bind-utils-lib = %{version}-%{release}
Requires: bind-utils-license = %{version}-%{release}
Requires: bind-utils-man = %{version}-%{release}
Requires: bind-utils-python = %{version}-%{release}
Requires: bind-utils-python3 = %{version}-%{release}
Requires: ply
BuildRequires : buildreq-distutils3
BuildRequires : doxygen
BuildRequires : e2fsprogs-dev
BuildRequires : krb5-dev
BuildRequires : libcap-dev
BuildRequires : libxml2-dev
BuildRequires : openssl-dev
BuildRequires : perl
BuildRequires : pkgconfig(cmocka)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libidn2)
BuildRequires : pkgconfig(libmaxminddb)
BuildRequires : pkgconfig(libuv)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(zlib)
BuildRequires : ply
BuildRequires : pytest
BuildRequires : readline-dev

%description
BIND 9
Contents
1. Introduction
2. Reporting bugs and getting help
3. Contributing to BIND
4. BIND 9.16 features
5. Building BIND
6. macOS
7. Dependencies
8. Compile-time options
9. Automated testing
10. Documentation
11. Change log
12. Acknowledgments

%package bin
Summary: bin components for the bind-utils package.
Group: Binaries
Requires: bind-utils-license = %{version}-%{release}

%description bin
bin components for the bind-utils package.


%package dev
Summary: dev components for the bind-utils package.
Group: Development
Requires: bind-utils-lib = %{version}-%{release}
Requires: bind-utils-bin = %{version}-%{release}
Provides: bind-utils-devel = %{version}-%{release}
Requires: bind-utils = %{version}-%{release}

%description dev
dev components for the bind-utils package.


%package extras-dnssec
Summary: extras-dnssec components for the bind-utils package.
Group: Default

%description extras-dnssec
extras-dnssec components for the bind-utils package.


%package lib
Summary: lib components for the bind-utils package.
Group: Libraries
Requires: bind-utils-license = %{version}-%{release}

%description lib
lib components for the bind-utils package.


%package license
Summary: license components for the bind-utils package.
Group: Default

%description license
license components for the bind-utils package.


%package man
Summary: man components for the bind-utils package.
Group: Default

%description man
man components for the bind-utils package.


%package python
Summary: python components for the bind-utils package.
Group: Default
Requires: bind-utils-python3 = %{version}-%{release}

%description python
python components for the bind-utils package.


%package python3
Summary: python3 components for the bind-utils package.
Group: Default
Requires: python3-core

%description python3
python3 components for the bind-utils package.


%package staticdev
Summary: staticdev components for the bind-utils package.
Group: Default
Requires: bind-utils-dev = %{version}-%{release}

%description staticdev
staticdev components for the bind-utils package.


%prep
%setup -q -n bind-9.16.7
cd %{_builddir}/bind-9.16.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600361913
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure  --without-libxml2 \
--with-libtool \
--with-gssapi=krb5-config
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1600361913
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bind-utils
cp %{_builddir}/bind-9.16.7/LICENSE %{buildroot}/usr/share/package-licenses/bind-utils/ece3df1263c100f93c427face535a292723d38e7
cp %{_builddir}/bind-9.16.7/bin/tests/system/dyndb/driver/COPYING %{buildroot}/usr/share/package-licenses/bind-utils/39f18898eca8d182f9386279eae016ca016a8c84
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/bind9-config
rm -f %{buildroot}/usr/bin/delv
rm -f %{buildroot}/usr/bin/isc-config.sh
rm -f %{buildroot}/usr/bin/lwresd
rm -f %{buildroot}/usr/bin/named
rm -f %{buildroot}/usr/bin/named-checkconf
rm -f %{buildroot}/usr/bin/named-journalprint
rm -f %{buildroot}/usr/bin/named-rrchecker
rm -f %{buildroot}/usr/bin/rndc
rm -f %{buildroot}/usr/bin/rndc-confgen
rm -f %{buildroot}/usr/bin/tsig-keygen
rm -f %{buildroot}/etc/bind.keys

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/arpaname
/usr/bin/ddns-confgen
/usr/bin/dig
/usr/bin/host
/usr/bin/mdig
/usr/bin/named-checkzone
/usr/bin/named-compilezone
/usr/bin/nsec3hash
/usr/bin/nslookup
/usr/bin/nsupdate

%files dev
%defattr(-,root,root,-)
/usr/include/bind9/check.h
/usr/include/bind9/getaddresses.h
/usr/include/bind9/version.h
/usr/include/dns/acl.h
/usr/include/dns/adb.h
/usr/include/dns/badcache.h
/usr/include/dns/bit.h
/usr/include/dns/byaddr.h
/usr/include/dns/cache.h
/usr/include/dns/callbacks.h
/usr/include/dns/catz.h
/usr/include/dns/cert.h
/usr/include/dns/client.h
/usr/include/dns/clientinfo.h
/usr/include/dns/compress.h
/usr/include/dns/db.h
/usr/include/dns/dbiterator.h
/usr/include/dns/dbtable.h
/usr/include/dns/diff.h
/usr/include/dns/dispatch.h
/usr/include/dns/dlz.h
/usr/include/dns/dlz_dlopen.h
/usr/include/dns/dns64.h
/usr/include/dns/dnsrps.h
/usr/include/dns/dnssec.h
/usr/include/dns/dnstap.h
/usr/include/dns/ds.h
/usr/include/dns/dsdigest.h
/usr/include/dns/dyndb.h
/usr/include/dns/ecdb.h
/usr/include/dns/ecs.h
/usr/include/dns/edns.h
/usr/include/dns/enumclass.h
/usr/include/dns/enumtype.h
/usr/include/dns/events.h
/usr/include/dns/fixedname.h
/usr/include/dns/forward.h
/usr/include/dns/geoip.h
/usr/include/dns/ipkeylist.h
/usr/include/dns/iptable.h
/usr/include/dns/journal.h
/usr/include/dns/kasp.h
/usr/include/dns/keydata.h
/usr/include/dns/keyflags.h
/usr/include/dns/keymgr.h
/usr/include/dns/keytable.h
/usr/include/dns/keyvalues.h
/usr/include/dns/lib.h
/usr/include/dns/librpz.h
/usr/include/dns/lmdb.h
/usr/include/dns/log.h
/usr/include/dns/lookup.h
/usr/include/dns/master.h
/usr/include/dns/masterdump.h
/usr/include/dns/message.h
/usr/include/dns/name.h
/usr/include/dns/ncache.h
/usr/include/dns/nsec.h
/usr/include/dns/nsec3.h
/usr/include/dns/nta.h
/usr/include/dns/opcode.h
/usr/include/dns/order.h
/usr/include/dns/peer.h
/usr/include/dns/portlist.h
/usr/include/dns/private.h
/usr/include/dns/rbt.h
/usr/include/dns/rcode.h
/usr/include/dns/rdata.h
/usr/include/dns/rdataclass.h
/usr/include/dns/rdatalist.h
/usr/include/dns/rdataset.h
/usr/include/dns/rdatasetiter.h
/usr/include/dns/rdataslab.h
/usr/include/dns/rdatastruct.h
/usr/include/dns/rdatatype.h
/usr/include/dns/request.h
/usr/include/dns/resolver.h
/usr/include/dns/result.h
/usr/include/dns/rootns.h
/usr/include/dns/rpz.h
/usr/include/dns/rriterator.h
/usr/include/dns/rrl.h
/usr/include/dns/sdb.h
/usr/include/dns/sdlz.h
/usr/include/dns/secalg.h
/usr/include/dns/secproto.h
/usr/include/dns/soa.h
/usr/include/dns/ssu.h
/usr/include/dns/stats.h
/usr/include/dns/tcpmsg.h
/usr/include/dns/time.h
/usr/include/dns/timer.h
/usr/include/dns/tkey.h
/usr/include/dns/tsec.h
/usr/include/dns/tsig.h
/usr/include/dns/ttl.h
/usr/include/dns/types.h
/usr/include/dns/update.h
/usr/include/dns/validator.h
/usr/include/dns/version.h
/usr/include/dns/view.h
/usr/include/dns/xfrin.h
/usr/include/dns/zone.h
/usr/include/dns/zonekey.h
/usr/include/dns/zoneverify.h
/usr/include/dns/zt.h
/usr/include/dst/dst.h
/usr/include/dst/gssapi.h
/usr/include/dst/result.h
/usr/include/irs/context.h
/usr/include/irs/dnsconf.h
/usr/include/irs/netdb.h
/usr/include/irs/platform.h
/usr/include/irs/resconf.h
/usr/include/irs/types.h
/usr/include/irs/version.h
/usr/include/isc/aes.h
/usr/include/isc/align.h
/usr/include/isc/app.h
/usr/include/isc/assertions.h
/usr/include/isc/astack.h
/usr/include/isc/atomic.h
/usr/include/isc/backtrace.h
/usr/include/isc/base32.h
/usr/include/isc/base64.h
/usr/include/isc/bind9.h
/usr/include/isc/buffer.h
/usr/include/isc/bufferlist.h
/usr/include/isc/commandline.h
/usr/include/isc/condition.h
/usr/include/isc/counter.h
/usr/include/isc/crc64.h
/usr/include/isc/deprecated.h
/usr/include/isc/dir.h
/usr/include/isc/endian.h
/usr/include/isc/errno.h
/usr/include/isc/error.h
/usr/include/isc/event.h
/usr/include/isc/eventclass.h
/usr/include/isc/file.h
/usr/include/isc/formatcheck.h
/usr/include/isc/fsaccess.h
/usr/include/isc/fuzz.h
/usr/include/isc/hash.h
/usr/include/isc/heap.h
/usr/include/isc/hex.h
/usr/include/isc/hmac.h
/usr/include/isc/hp.h
/usr/include/isc/ht.h
/usr/include/isc/httpd.h
/usr/include/isc/interfaceiter.h
/usr/include/isc/iterated_hash.h
/usr/include/isc/lang.h
/usr/include/isc/lex.h
/usr/include/isc/lfsr.h
/usr/include/isc/lib.h
/usr/include/isc/likely.h
/usr/include/isc/list.h
/usr/include/isc/log.h
/usr/include/isc/magic.h
/usr/include/isc/md.h
/usr/include/isc/mem.h
/usr/include/isc/meminfo.h
/usr/include/isc/mutex.h
/usr/include/isc/mutexatomic.h
/usr/include/isc/mutexblock.h
/usr/include/isc/net.h
/usr/include/isc/netaddr.h
/usr/include/isc/netdb.h
/usr/include/isc/netmgr.h
/usr/include/isc/netscope.h
/usr/include/isc/nonce.h
/usr/include/isc/offset.h
/usr/include/isc/once.h
/usr/include/isc/os.h
/usr/include/isc/parseint.h
/usr/include/isc/platform.h
/usr/include/isc/pool.h
/usr/include/isc/portset.h
/usr/include/isc/print.h
/usr/include/isc/queue.h
/usr/include/isc/quota.h
/usr/include/isc/radix.h
/usr/include/isc/random.h
/usr/include/isc/ratelimiter.h
/usr/include/isc/refcount.h
/usr/include/isc/regex.h
/usr/include/isc/region.h
/usr/include/isc/resource.h
/usr/include/isc/result.h
/usr/include/isc/resultclass.h
/usr/include/isc/rwlock.h
/usr/include/isc/safe.h
/usr/include/isc/serial.h
/usr/include/isc/siphash.h
/usr/include/isc/sockaddr.h
/usr/include/isc/socket.h
/usr/include/isc/stat.h
/usr/include/isc/stats.h
/usr/include/isc/stdatomic.h
/usr/include/isc/stdio.h
/usr/include/isc/stdtime.h
/usr/include/isc/strerr.h
/usr/include/isc/string.h
/usr/include/isc/symtab.h
/usr/include/isc/syslog.h
/usr/include/isc/task.h
/usr/include/isc/taskpool.h
/usr/include/isc/thread.h
/usr/include/isc/time.h
/usr/include/isc/timer.h
/usr/include/isc/tm.h
/usr/include/isc/types.h
/usr/include/isc/utf8.h
/usr/include/isc/util.h
/usr/include/isc/version.h
/usr/include/isccc/alist.h
/usr/include/isccc/base64.h
/usr/include/isccc/cc.h
/usr/include/isccc/ccmsg.h
/usr/include/isccc/events.h
/usr/include/isccc/result.h
/usr/include/isccc/sexpr.h
/usr/include/isccc/symtab.h
/usr/include/isccc/symtype.h
/usr/include/isccc/types.h
/usr/include/isccc/util.h
/usr/include/isccc/version.h
/usr/include/isccfg/aclconf.h
/usr/include/isccfg/cfg.h
/usr/include/isccfg/dnsconf.h
/usr/include/isccfg/grammar.h
/usr/include/isccfg/kaspconf.h
/usr/include/isccfg/log.h
/usr/include/isccfg/namedconf.h
/usr/include/isccfg/version.h
/usr/include/ns/client.h
/usr/include/ns/hooks.h
/usr/include/ns/interfacemgr.h
/usr/include/ns/lib.h
/usr/include/ns/listenlist.h
/usr/include/ns/log.h
/usr/include/ns/notify.h
/usr/include/ns/query.h
/usr/include/ns/server.h
/usr/include/ns/sortlist.h
/usr/include/ns/stats.h
/usr/include/ns/types.h
/usr/include/ns/update.h
/usr/include/ns/version.h
/usr/include/ns/xfrout.h
/usr/include/pk11/constants.h
/usr/include/pk11/internal.h
/usr/include/pk11/pk11.h
/usr/include/pk11/result.h
/usr/include/pk11/site.h
/usr/include/pkcs11/pkcs11.h
/usr/lib64/libbind9.so
/usr/lib64/libdns.so
/usr/lib64/libirs.so
/usr/lib64/libisc.so
/usr/lib64/libisccc.so
/usr/lib64/libisccfg.so
/usr/lib64/libns.so

%files extras-dnssec
%defattr(-,root,root,-)
/usr/bin/dnssec-cds
/usr/bin/dnssec-checkds
/usr/bin/dnssec-coverage
/usr/bin/dnssec-dsfromkey
/usr/bin/dnssec-importkey
/usr/bin/dnssec-keyfromlabel
/usr/bin/dnssec-keygen
/usr/bin/dnssec-keymgr
/usr/bin/dnssec-revoke
/usr/bin/dnssec-settime
/usr/bin/dnssec-signzone
/usr/bin/dnssec-verify

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbind9.so.1600
/usr/lib64/libbind9.so.1600.0.5
/usr/lib64/libdns.so.1607
/usr/lib64/libdns.so.1607.0.0
/usr/lib64/libirs.so.1601
/usr/lib64/libirs.so.1601.0.0
/usr/lib64/libisc.so.1606
/usr/lib64/libisc.so.1606.0.1
/usr/lib64/libisccc.so.1600
/usr/lib64/libisccc.so.1600.0.2
/usr/lib64/libisccfg.so.1601
/usr/lib64/libisccfg.so.1601.0.0
/usr/lib64/libns.so.1604
/usr/lib64/libns.so.1604.0.1
/usr/lib64/named/filter-aaaa.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bind-utils/39f18898eca8d182f9386279eae016ca016a8c84
/usr/share/package-licenses/bind-utils/ece3df1263c100f93c427face535a292723d38e7

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/arpaname.1
/usr/share/man/man1/delv.1
/usr/share/man/man1/dig.1
/usr/share/man/man1/host.1
/usr/share/man/man1/mdig.1
/usr/share/man/man1/named-rrchecker.1
/usr/share/man/man1/nslookup.1
/usr/share/man/man1/nsupdate.1
/usr/share/man/man5/named.conf.5
/usr/share/man/man5/rndc.conf.5
/usr/share/man/man8/ddns-confgen.8
/usr/share/man/man8/dnssec-cds.8
/usr/share/man/man8/dnssec-checkds.8
/usr/share/man/man8/dnssec-coverage.8
/usr/share/man/man8/dnssec-dsfromkey.8
/usr/share/man/man8/dnssec-importkey.8
/usr/share/man/man8/dnssec-keyfromlabel.8
/usr/share/man/man8/dnssec-keygen.8
/usr/share/man/man8/dnssec-keymgr.8
/usr/share/man/man8/dnssec-revoke.8
/usr/share/man/man8/dnssec-settime.8
/usr/share/man/man8/dnssec-signzone.8
/usr/share/man/man8/dnssec-verify.8
/usr/share/man/man8/filter-aaaa.8
/usr/share/man/man8/named-checkconf.8
/usr/share/man/man8/named-checkzone.8
/usr/share/man/man8/named-compilezone.8
/usr/share/man/man8/named-journalprint.8
/usr/share/man/man8/named.8
/usr/share/man/man8/nsec3hash.8
/usr/share/man/man8/rndc-confgen.8
/usr/share/man/man8/rndc.8
/usr/share/man/man8/tsig-keygen.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libbind9.a
/usr/lib64/libdns.a
/usr/lib64/libirs.a
/usr/lib64/libisc.a
/usr/lib64/libisccc.a
/usr/lib64/libisccfg.a
/usr/lib64/libns.a
