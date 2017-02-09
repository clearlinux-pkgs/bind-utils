#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF1B11BF05CF02E57 (codesign@isc.org)
#
%define keepstatic 1
Name     : bind-utils
Version  : 9.11.0
Release  : 43
URL      : https://ftp.isc.org/isc/bind9/9.11.0-P2/bind-9.11.0-P2.tar.gz
Source0  : https://ftp.isc.org/isc/bind9/9.11.0-P2/bind-9.11.0-P2.tar.gz
Source99 : https://ftp.isc.org/isc/bind9/9.11.0-P2/bind-9.11.0-P2.tar.gz.asc
Summary  : Internationalized Domain Name kit (idnkit/JPNIC)
Group    : Development/Tools
License  : BSD-3-Clause ISC MPL-2.0-no-copyleft-exception
Requires: bind-utils-bin
Requires: bind-utils-lib
Requires: bind-utils-doc
BuildRequires : libcap-dev
BuildRequires : libxml2-dev
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : readline-dev
BuildRequires : setuptools
Patch1: cve-2010-0290.nopatch
Patch2: cve-2010-0382.nopatch
Patch3: cve-2015-1349.nopatch
Patch4: cve-2015-4620.nopatch
Patch5: cve-2015-5477.nopatch
Patch6: cve-2015-5722.nopatch
Patch7: cve-2015-5986.nopatch
Patch8: cve-2015-8000.nopatch
Patch9: cve-2015-8461.nopatch
Patch10: cve-2015-8704.nopatch
Patch11: cve-2015-8705.nopatch
Patch12: cve-2016-1285.nopatch
Patch13: cve-2016-1286.nopatch
Patch14: cve-2016-2088.nopatch
Patch15: cve-2016-6170.nopatch
Patch16: cve-2016-2775.nopatch
Patch17: cve-2016-2776.nopatch
Patch18: cve-2016-8864.nopatch
Patch19: cve-2016-9131.nopatch
Patch20: cve-2016-9147.nopatch
Patch21: cve-2016-9444.nopatch

%description
idnkit is a kit for handling Internationalized Domain Name.

%package bin
Summary: bin components for the bind-utils package.
Group: Binaries

%description bin
bin components for the bind-utils package.


%package dev
Summary: dev components for the bind-utils package.
Group: Development
Requires: bind-utils-lib
Requires: bind-utils-bin
Provides: bind-utils-devel

%description dev
dev components for the bind-utils package.


%package doc
Summary: doc components for the bind-utils package.
Group: Documentation

%description doc
doc components for the bind-utils package.


%package lib
Summary: lib components for the bind-utils package.
Group: Libraries

%description lib
lib components for the bind-utils package.


%prep
%setup -q -n bind-9.11.0-P2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1486663368
%configure  --without-libxml2 ; libtoolize -c -f; aclocal -I libtool.m4 --force; autoconf -f ; %configure --without-libxml2 --with-libtool
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1486663368
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/bind9-config
%exclude /usr/bin/delv
%exclude /usr/bin/isc-config.sh
%exclude /usr/bin/lwresd
%exclude /usr/bin/named
%exclude /usr/bin/named-checkconf
%exclude /usr/bin/named-journalprint
%exclude /usr/bin/named-rrchecker
%exclude /usr/bin/rndc
%exclude /usr/bin/rndc-confgen
%exclude /usr/bin/tsig-keygen
/usr/bin/arpaname
/usr/bin/ddns-confgen
/usr/bin/dig
/usr/bin/dnssec-dsfromkey
/usr/bin/dnssec-importkey
/usr/bin/dnssec-keyfromlabel
/usr/bin/dnssec-keygen
/usr/bin/dnssec-revoke
/usr/bin/dnssec-settime
/usr/bin/dnssec-signzone
/usr/bin/dnssec-verify
/usr/bin/genrandom
/usr/bin/host
/usr/bin/isc-hmac-fixup
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
/usr/include/dns/acache.h
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
/usr/include/dns/dnssec.h
/usr/include/dns/dnstap.h
/usr/include/dns/ds.h
/usr/include/dns/dsdigest.h
/usr/include/dns/dyndb.h
/usr/include/dns/ecdb.h
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
/usr/include/dns/keydata.h
/usr/include/dns/keyflags.h
/usr/include/dns/keytable.h
/usr/include/dns/keyvalues.h
/usr/include/dns/lib.h
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
/usr/include/dns/zt.h
/usr/include/dst/dst.h
/usr/include/dst/gssapi.h
/usr/include/dst/lib.h
/usr/include/dst/result.h
/usr/include/irs/context.h
/usr/include/irs/dnsconf.h
/usr/include/irs/netdb.h
/usr/include/irs/platform.h
/usr/include/irs/resconf.h
/usr/include/irs/types.h
/usr/include/irs/version.h
/usr/include/isc/aes.h
/usr/include/isc/app.h
/usr/include/isc/assertions.h
/usr/include/isc/atomic.h
/usr/include/isc/backtrace.h
/usr/include/isc/base32.h
/usr/include/isc/base64.h
/usr/include/isc/bind9.h
/usr/include/isc/boolean.h
/usr/include/isc/buffer.h
/usr/include/isc/bufferlist.h
/usr/include/isc/commandline.h
/usr/include/isc/condition.h
/usr/include/isc/counter.h
/usr/include/isc/crc64.h
/usr/include/isc/dir.h
/usr/include/isc/entropy.h
/usr/include/isc/errno.h
/usr/include/isc/error.h
/usr/include/isc/event.h
/usr/include/isc/eventclass.h
/usr/include/isc/file.h
/usr/include/isc/formatcheck.h
/usr/include/isc/fsaccess.h
/usr/include/isc/hash.h
/usr/include/isc/heap.h
/usr/include/isc/hex.h
/usr/include/isc/hmacmd5.h
/usr/include/isc/hmacsha.h
/usr/include/isc/ht.h
/usr/include/isc/httpd.h
/usr/include/isc/int.h
/usr/include/isc/interfaceiter.h
/usr/include/isc/iterated_hash.h
/usr/include/isc/json.h
/usr/include/isc/keyboard.h
/usr/include/isc/lang.h
/usr/include/isc/lex.h
/usr/include/isc/lfsr.h
/usr/include/isc/lib.h
/usr/include/isc/list.h
/usr/include/isc/log.h
/usr/include/isc/magic.h
/usr/include/isc/md5.h
/usr/include/isc/mem.h
/usr/include/isc/meminfo.h
/usr/include/isc/msgcat.h
/usr/include/isc/msgs.h
/usr/include/isc/mutex.h
/usr/include/isc/mutexblock.h
/usr/include/isc/net.h
/usr/include/isc/netaddr.h
/usr/include/isc/netdb.h
/usr/include/isc/netscope.h
/usr/include/isc/offset.h
/usr/include/isc/once.h
/usr/include/isc/ondestroy.h
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
/usr/include/isc/sha1.h
/usr/include/isc/sha2.h
/usr/include/isc/sockaddr.h
/usr/include/isc/socket.h
/usr/include/isc/stat.h
/usr/include/isc/stats.h
/usr/include/isc/stdio.h
/usr/include/isc/stdlib.h
/usr/include/isc/stdtime.h
/usr/include/isc/strerror.h
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
/usr/include/isc/util.h
/usr/include/isc/version.h
/usr/include/isc/xml.h
/usr/include/isccc/alist.h
/usr/include/isccc/base64.h
/usr/include/isccc/cc.h
/usr/include/isccc/ccmsg.h
/usr/include/isccc/events.h
/usr/include/isccc/lib.h
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
/usr/include/isccfg/log.h
/usr/include/isccfg/namedconf.h
/usr/include/isccfg/version.h
/usr/include/lwres/context.h
/usr/include/lwres/int.h
/usr/include/lwres/ipv6.h
/usr/include/lwres/lang.h
/usr/include/lwres/list.h
/usr/include/lwres/lwbuffer.h
/usr/include/lwres/lwpacket.h
/usr/include/lwres/lwres.h
/usr/include/lwres/net.h
/usr/include/lwres/netdb.h
/usr/include/lwres/platform.h
/usr/include/lwres/result.h
/usr/include/lwres/stdlib.h
/usr/include/lwres/string.h
/usr/include/lwres/version.h
/usr/include/pk11/constants.h
/usr/include/pk11/internal.h
/usr/include/pk11/pk11.h
/usr/include/pk11/result.h
/usr/include/pk11/site.h
/usr/include/pkcs11/cryptoki.h
/usr/include/pkcs11/pkcs11.h
/usr/include/pkcs11/pkcs11f.h
/usr/include/pkcs11/pkcs11t.h
/usr/lib64/*.a
/usr/lib64/libbind9.so
/usr/lib64/libdns.so
/usr/lib64/libirs.so
/usr/lib64/libisc.so
/usr/lib64/libisccc.so
/usr/lib64/libisccfg.so
/usr/lib64/liblwres.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbind9.so.160
/usr/lib64/libbind9.so.160.0.2
/usr/lib64/libdns.so.166
/usr/lib64/libdns.so.166.0.4
/usr/lib64/libirs.so.160
/usr/lib64/libirs.so.160.0.1
/usr/lib64/libisc.so.160
/usr/lib64/libisc.so.160.5.2
/usr/lib64/libisccc.so.160
/usr/lib64/libisccc.so.160.0.2
/usr/lib64/libisccfg.so.160
/usr/lib64/libisccfg.so.160.0.5
/usr/lib64/liblwres.so.160
/usr/lib64/liblwres.so.160.0.0
