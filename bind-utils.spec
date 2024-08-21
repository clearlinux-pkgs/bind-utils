#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0x182E23579462EFAA (mnowak@isc.org)
#
%define keepstatic 1
Name     : bind-utils
Version  : 9.20.1
Release  : 133
URL      : https://downloads.isc.org/isc/bind9/9.20.1/bind-9.20.1.tar.xz
Source0  : https://downloads.isc.org/isc/bind9/9.20.1/bind-9.20.1.tar.xz
Source1  : https://downloads.isc.org/isc/bind9/9.20.1/bind-9.20.1.tar.xz.asc
Source2  : 182E23579462EFAA.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC MPL-2.0
Requires: bind-utils-bin = %{version}-%{release}
Requires: bind-utils-lib = %{version}-%{release}
Requires: bind-utils-license = %{version}-%{release}
Requires: bind-utils-man = %{version}-%{release}
Requires: pypi(ply)
BuildRequires : buildreq-configure
BuildRequires : doxygen
BuildRequires : e2fsprogs-dev
BuildRequires : file
BuildRequires : gnupg
BuildRequires : krb5-dev
BuildRequires : libcap-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : nmap-extras
BuildRequires : openssl-dev
BuildRequires : perl
BuildRequires : pkgconfig(cmocka)
BuildRequires : pkgconfig(libcap)
BuildRequires : pkgconfig(libidn2)
BuildRequires : pkgconfig(libmaxminddb)
BuildRequires : pkgconfig(libnghttp2)
BuildRequires : pkgconfig(libprotobuf-c)
BuildRequires : pkgconfig(liburcu-cds)
BuildRequires : pkgconfig(libuv)
BuildRequires : pkgconfig(systemd)
BuildRequires : pypi(ply)
BuildRequires : pypi-pytest
BuildRequires : pypi-sphinx
BuildRequires : readline-dev
BuildRequires : tzdata
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!--
SPDX-License-Identifier: MPL-2.0
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0.  If a copy of the MPL was not distributed with this
file, you can obtain one at https://mozilla.org/MPL/2.0/.

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


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 182E23579462EFAA' gpg.status
%setup -q -n bind-9.20.1
cd %{_builddir}/bind-9.20.1
pushd ..
cp -a bind-9.20.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724277217
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure  --without-libxml2 \
--with-libtool \
--with-gssapi=krb5-config
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure  --without-libxml2 \
--with-libtool \
--with-gssapi=krb5-config
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724277217
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bind-utils
cp %{_builddir}/bind-%{version}/COPYING %{buildroot}/usr/share/package-licenses/bind-utils/4fa8d983d44984c7a1d7bbca6971242b10155776 || :
cp %{_builddir}/bind-%{version}/COPYRIGHT %{buildroot}/usr/share/package-licenses/bind-utils/99e1411b8c4ea09c7847a93fa9fcdc275f39bdc5 || :
cp %{_builddir}/bind-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/bind-utils/4fa8d983d44984c7a1d7bbca6971242b10155776 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/bind9-config
rm -f %{buildroot}*/usr/bin/delv
rm -f %{buildroot}*/usr/bin/isc-config.sh
rm -f %{buildroot}*/usr/bin/lwresd
rm -f %{buildroot}*/usr/bin/named
rm -f %{buildroot}*/usr/bin/named-checkconf
rm -f %{buildroot}*/usr/bin/named-journalprint
rm -f %{buildroot}*/usr/bin/named-rrchecker
rm -f %{buildroot}*/usr/bin/rndc
rm -f %{buildroot}*/usr/bin/rndc-confgen
rm -f %{buildroot}*/usr/bin/tsig-keygen
rm -f %{buildroot}*/etc/bind.keys
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/arpaname
/V3/usr/bin/ddns-confgen
/V3/usr/bin/dig
/V3/usr/bin/dnssec-ksr
/V3/usr/bin/host
/V3/usr/bin/mdig
/V3/usr/bin/named-checkzone
/V3/usr/bin/named-compilezone
/V3/usr/bin/nsec3hash
/V3/usr/bin/nslookup
/V3/usr/bin/nsupdate
/usr/bin/arpaname
/usr/bin/ddns-confgen
/usr/bin/dig
/usr/bin/dnssec-ksr
/usr/bin/host
/usr/bin/mdig
/usr/bin/named-checkzone
/usr/bin/named-compilezone
/usr/bin/nsec3hash
/usr/bin/nslookup
/usr/bin/nsupdate

%files dev
%defattr(-,root,root,-)
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
/usr/include/dns/ecs.h
/usr/include/dns/edns.h
/usr/include/dns/enumclass.h
/usr/include/dns/enumtype.h
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
/usr/include/dns/keystore.h
/usr/include/dns/keytable.h
/usr/include/dns/keyvalues.h
/usr/include/dns/librpz.h
/usr/include/dns/log.h
/usr/include/dns/master.h
/usr/include/dns/masterdump.h
/usr/include/dns/message.h
/usr/include/dns/name.h
/usr/include/dns/nametree.h
/usr/include/dns/ncache.h
/usr/include/dns/nsec.h
/usr/include/dns/nsec3.h
/usr/include/dns/nta.h
/usr/include/dns/opcode.h
/usr/include/dns/order.h
/usr/include/dns/peer.h
/usr/include/dns/private.h
/usr/include/dns/qp.h
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
/usr/include/dns/remote.h
/usr/include/dns/request.h
/usr/include/dns/resolver.h
/usr/include/dns/result.h
/usr/include/dns/rootns.h
/usr/include/dns/rpz.h
/usr/include/dns/rriterator.h
/usr/include/dns/rrl.h
/usr/include/dns/sdlz.h
/usr/include/dns/secalg.h
/usr/include/dns/secproto.h
/usr/include/dns/soa.h
/usr/include/dns/ssu.h
/usr/include/dns/stats.h
/usr/include/dns/time.h
/usr/include/dns/tkey.h
/usr/include/dns/trace.h
/usr/include/dns/transport.h
/usr/include/dns/tsig.h
/usr/include/dns/ttl.h
/usr/include/dns/types.h
/usr/include/dns/update.h
/usr/include/dns/validator.h
/usr/include/dns/view.h
/usr/include/dns/xfrin.h
/usr/include/dns/zone.h
/usr/include/dns/zonekey.h
/usr/include/dns/zoneverify.h
/usr/include/dns/zt.h
/usr/include/dst/dst.h
/usr/include/dst/gssapi.h
/usr/include/irs/resconf.h
/usr/include/isc/ascii.h
/usr/include/isc/assertions.h
/usr/include/isc/async.h
/usr/include/isc/atomic.h
/usr/include/isc/attributes.h
/usr/include/isc/backtrace.h
/usr/include/isc/barrier.h
/usr/include/isc/base32.h
/usr/include/isc/base64.h
/usr/include/isc/buffer.h
/usr/include/isc/commandline.h
/usr/include/isc/condition.h
/usr/include/isc/counter.h
/usr/include/isc/crc64.h
/usr/include/isc/dir.h
/usr/include/isc/dnsstream.h
/usr/include/isc/endian.h
/usr/include/isc/entropy.h
/usr/include/isc/errno.h
/usr/include/isc/error.h
/usr/include/isc/file.h
/usr/include/isc/fips.h
/usr/include/isc/formatcheck.h
/usr/include/isc/fuzz.h
/usr/include/isc/getaddresses.h
/usr/include/isc/hash.h
/usr/include/isc/hashmap.h
/usr/include/isc/heap.h
/usr/include/isc/hex.h
/usr/include/isc/histo.h
/usr/include/isc/hmac.h
/usr/include/isc/ht.h
/usr/include/isc/httpd.h
/usr/include/isc/interfaceiter.h
/usr/include/isc/iterated_hash.h
/usr/include/isc/job.h
/usr/include/isc/lang.h
/usr/include/isc/lex.h
/usr/include/isc/list.h
/usr/include/isc/log.h
/usr/include/isc/loop.h
/usr/include/isc/magic.h
/usr/include/isc/managers.h
/usr/include/isc/md.h
/usr/include/isc/mem.h
/usr/include/isc/meminfo.h
/usr/include/isc/mutex.h
/usr/include/isc/mutexblock.h
/usr/include/isc/net.h
/usr/include/isc/netaddr.h
/usr/include/isc/netmgr.h
/usr/include/isc/netscope.h
/usr/include/isc/nonce.h
/usr/include/isc/once.h
/usr/include/isc/os.h
/usr/include/isc/overflow.h
/usr/include/isc/parseint.h
/usr/include/isc/pause.h
/usr/include/isc/portset.h
/usr/include/isc/proxy2.h
/usr/include/isc/queue.h
/usr/include/isc/quota.h
/usr/include/isc/radix.h
/usr/include/isc/random.h
/usr/include/isc/ratelimiter.h
/usr/include/isc/refcount.h
/usr/include/isc/regex.h
/usr/include/isc/region.h
/usr/include/isc/result.h
/usr/include/isc/rwlock.h
/usr/include/isc/safe.h
/usr/include/isc/serial.h
/usr/include/isc/signal.h
/usr/include/isc/siphash.h
/usr/include/isc/sockaddr.h
/usr/include/isc/spinlock.h
/usr/include/isc/stats.h
/usr/include/isc/stdio.h
/usr/include/isc/stdtime.h
/usr/include/isc/strerr.h
/usr/include/isc/string.h
/usr/include/isc/symtab.h
/usr/include/isc/syslog.h
/usr/include/isc/thread.h
/usr/include/isc/tid.h
/usr/include/isc/time.h
/usr/include/isc/timer.h
/usr/include/isc/tls.h
/usr/include/isc/tm.h
/usr/include/isc/types.h
/usr/include/isc/urcu.h
/usr/include/isc/url.h
/usr/include/isc/utf8.h
/usr/include/isc/util.h
/usr/include/isc/uv.h
/usr/include/isc/work.h
/usr/include/isc/xml.h
/usr/include/isccc/alist.h
/usr/include/isccc/base64.h
/usr/include/isccc/cc.h
/usr/include/isccc/ccmsg.h
/usr/include/isccc/sexpr.h
/usr/include/isccc/symtab.h
/usr/include/isccc/symtype.h
/usr/include/isccc/types.h
/usr/include/isccc/util.h
/usr/include/isccfg/aclconf.h
/usr/include/isccfg/cfg.h
/usr/include/isccfg/check.h
/usr/include/isccfg/duration.h
/usr/include/isccfg/grammar.h
/usr/include/isccfg/kaspconf.h
/usr/include/isccfg/log.h
/usr/include/isccfg/namedconf.h
/usr/include/ns/client.h
/usr/include/ns/hooks.h
/usr/include/ns/interfacemgr.h
/usr/include/ns/listenlist.h
/usr/include/ns/log.h
/usr/include/ns/notify.h
/usr/include/ns/query.h
/usr/include/ns/server.h
/usr/include/ns/sortlist.h
/usr/include/ns/stats.h
/usr/include/ns/types.h
/usr/include/ns/update.h
/usr/include/ns/xfrout.h

%files extras-dnssec
%defattr(-,root,root,-)
/V3/usr/bin/dnssec-cds
/V3/usr/bin/dnssec-dsfromkey
/V3/usr/bin/dnssec-importkey
/V3/usr/bin/dnssec-keyfromlabel
/V3/usr/bin/dnssec-keygen
/V3/usr/bin/dnssec-revoke
/V3/usr/bin/dnssec-settime
/V3/usr/bin/dnssec-signzone
/V3/usr/bin/dnssec-verify
/usr/bin/dnssec-cds
/usr/bin/dnssec-dsfromkey
/usr/bin/dnssec-importkey
/usr/bin/dnssec-keyfromlabel
/usr/bin/dnssec-keygen
/usr/bin/dnssec-revoke
/usr/bin/dnssec-settime
/usr/bin/dnssec-signzone
/usr/bin/dnssec-verify

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/bind/filter-a.so
/V3/usr/lib64/bind/filter-aaaa.so
/V3/usr/lib64/libdns-9.20.1.so
/V3/usr/lib64/libisc-9.20.1.so
/V3/usr/lib64/libisccc-9.20.1.so
/V3/usr/lib64/libisccfg-9.20.1.so
/V3/usr/lib64/libns-9.20.1.so
/usr/lib64/bind/filter-a.so
/usr/lib64/bind/filter-aaaa.so
/usr/lib64/libdns-9.20.1.so
/usr/lib64/libdns.so
/usr/lib64/libisc-9.20.1.so
/usr/lib64/libisc.so
/usr/lib64/libisccc-9.20.1.so
/usr/lib64/libisccc.so
/usr/lib64/libisccfg-9.20.1.so
/usr/lib64/libisccfg.so
/usr/lib64/libns-9.20.1.so
/usr/lib64/libns.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bind-utils/4fa8d983d44984c7a1d7bbca6971242b10155776
/usr/share/package-licenses/bind-utils/99e1411b8c4ea09c7847a93fa9fcdc275f39bdc5

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/arpaname.1
/usr/share/man/man1/delv.1
/usr/share/man/man1/dig.1
/usr/share/man/man1/dnssec-cds.1
/usr/share/man/man1/dnssec-dsfromkey.1
/usr/share/man/man1/dnssec-importkey.1
/usr/share/man/man1/dnssec-keyfromlabel.1
/usr/share/man/man1/dnssec-keygen.1
/usr/share/man/man1/dnssec-ksr.1
/usr/share/man/man1/dnssec-revoke.1
/usr/share/man/man1/dnssec-settime.1
/usr/share/man/man1/dnssec-signzone.1
/usr/share/man/man1/dnssec-verify.1
/usr/share/man/man1/host.1
/usr/share/man/man1/mdig.1
/usr/share/man/man1/named-checkconf.1
/usr/share/man/man1/named-checkzone.1
/usr/share/man/man1/named-compilezone.1
/usr/share/man/man1/named-journalprint.1
/usr/share/man/man1/named-rrchecker.1
/usr/share/man/man1/nsec3hash.1
/usr/share/man/man1/nslookup.1
/usr/share/man/man1/nsupdate.1
/usr/share/man/man5/named.conf.5
/usr/share/man/man5/rndc.conf.5
/usr/share/man/man8/ddns-confgen.8
/usr/share/man/man8/filter-a.8
/usr/share/man/man8/filter-aaaa.8
/usr/share/man/man8/named.8
/usr/share/man/man8/rndc-confgen.8
/usr/share/man/man8/rndc.8
/usr/share/man/man8/tsig-keygen.8
