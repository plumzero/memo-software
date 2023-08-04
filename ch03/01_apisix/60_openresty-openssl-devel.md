
### 添加依赖包

添加依赖包源地址。
```sh
    [openresty]
    name=Official OpenResty Open Source Repository for CentOS
    baseurl=https://openresty.org/package/centos/$releasever/$basearch
    skip_if_unavailable=False
    gpgcheck=1
    repo_gpgcheck=0
    gpgkey=https://openresty.org/package/pubkey.gpg
    enabled=1
    enabled_metadata=1
```


### 查找依赖包

添加依赖源后，在 shell 会话中尝试是否可以查找到依赖包。
```sh
    [root@localhost yum.repos.d]# yum search openresty-openssl-devel
    Last metadata expiration check: 0:00:28 ago on Wed 03 Mar 2021 02:48:28 AM EST.
    =================================================================================================== Name Matched: openresty-openssl-dev ====================================================================================================
    openresty-openssl-devel.x86_64 : Development files for OpenResty's OpenSSL library
    [root@localhost yum.repos.d]# find / -name openssl
    find: ‘/run/user/1000/gvfs’: Permission denied
    /etc/pki/ca-trust/extracted/openssl
    /usr/bin/openssl
    /usr/share/licenses/openssl
    /usr/share/doc/openssl
    /usr/share/bash-completion/completions/openssl
    [root@localhost yum.repos.d]# which openssl
    /usr/bin/openssl
    [root@localhost yum.repos.d]# openssl -v
    Invalid command '-v'; type "help" for a list.
    [root@localhost yum.repos.d]# openssl version
    OpenSSL 1.1.1g FIPS  21 Apr 2020
    [root@localhost yum.repos.d]# which openssl
    /usr/bin/openssl
    [root@localhost yum.repos.d]# ldd /usr/bin/openssl
            linux-vdso.so.1 (0x00007fff589b1000)
            libssl.so.1.1 => /lib64/libssl.so.1.1 (0x00007fe8e81f2000)
            libcrypto.so.1.1 => /lib64/libcrypto.so.1.1 (0x00007fe8e7d0c000)
            libz.so.1 => /lib64/libz.so.1 (0x00007fe8e7af5000)
            libdl.so.2 => /lib64/libdl.so.2 (0x00007fe8e78f1000)
            libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fe8e76d1000)
            libc.so.6 => /lib64/libc.so.6 (0x00007fe8e730e000)
            /lib64/ld-linux-x86-64.so.2 (0x00007fe8e8741000)
    [root@localhost yum.repos.d]# yum install openresty-openssl-dev
    Last metadata expiration check: 0:07:25 ago on Wed 03 Mar 2021 02:48:28 AM EST.
    No match for argument: openresty-openssl-dev
    Error: Unable to find a match: openresty-openssl-dev
```


### 安装依赖包

```sh
    [root@localhost yum.repos.d]# yum install openresty-openssl-devel
    Last metadata expiration check: 0:07:47 ago on Wed 03 Mar 2021 02:48:28 AM EST.
    Dependencies resolved.
    ============================================================================================================================================================================================================================================
     Package                                                            Architecture                                      Version                                                    Repository                                            Size
    ============================================================================================================================================================================================================================================
    Installing:
     openresty-openssl-devel                                            x86_64                                            1.1.0l-2.el8                                               openresty                                            1.5 M
    Installing dependencies:
     openresty-openssl                                                  x86_64                                            1.1.0l-2.el8                                               openresty                                            1.4 M
     openresty-zlib                                                     x86_64                                            1.2.11-3.el8                                               openresty                                             59 k

    Transaction Summary
    ============================================================================================================================================================================================================================================
    Install  3 Packages

    Total download size: 2.9 M
    Installed size: 10 M
    Is this ok [y/N]: y
    Downloading Packages:
    (1/3): openresty-zlib-1.2.11-3.el8.x86_64.rpm                                                                                                                                                               141 kB/s |  59 kB     00:00    
    (2/3): openresty-openssl-1.1.0l-2.el8.x86_64.rpm                                                                                                                                                            2.5 MB/s | 1.4 MB     00:00    
    (3/3): openresty-openssl-devel-1.1.0l-2.el8.x86_64.rpm                                                                                                                                                      2.5 MB/s | 1.5 MB     00:00    
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Total                                                                                                                                                                                                       4.7 MB/s | 2.9 MB     00:00     
    warning: /var/cache/dnf/openresty-9bb47c2efe3dbf62/packages/openresty-openssl-1.1.0l-2.el8.x86_64.rpm: Header V4 RSA/SHA256 Signature, key ID d5edeb74: NOKEY
    Official OpenResty Open Source Repository for CentOS                                                                                                                                                        8.1 kB/s | 1.6 kB     00:00    
    Importing GPG key 0xD5EDEB74:
     Userid     : "OpenResty Admin <admin@openresty.com>"
     Fingerprint: E522 18E7 0878 97DC 6DEA 6D6D 97DB 7443 D5ED EB74
     From       : https://openresty.org/package/pubkey.gpg
    Is this ok [y/N]: y
    Key imported successfully
    Running transaction check
    Transaction check succeeded.
    Running transaction test
    Transaction test succeeded.
    Running transaction
      Preparing        :                                                         1/1
      Installing       : openresty-zlib-1.2.11-3.el8.x86_64                      1/3
      Installing       : openresty-openssl-1.1.0l-2.el8.x86_64                   2/3 
      Installing       : openresty-openssl-devel-1.1.0l-2.el8.x86_64             3/3 
      Running scriptlet: openresty-openssl-devel-1.1.0l-2.el8.x86_64             3/3 
      Verifying        : openresty-openssl-1.1.0l-2.el8.x86_64                   1/3 
      Verifying        : openresty-openssl-devel-1.1.0l-2.el8.x86_64             2/3
      Verifying        : openresty-zlib-1.2.11-3.el8.x86_64                      3/3
    Installed products updated.

    Installed:
      openresty-openssl-1.1.0l-2.el8.x86_64                                        openresty-openssl-devel-1.1.0l-2.el8.x86_64                                        openresty-zlib-1.2.11-3.el8.x86_64                                       

    Complete!
```

从安装打印信息中可以看到依赖包 `openssl` 和 `zlib` 的版本信息。

会安装到 `/usr/local/openresty/` 目录下，在该目录下执行 `tree`，查看其文件结构如下:
```sh
  ├── openssl
  │   ├── bin
  │   │   └── openssl
  │   ├── include
  │   │   └── openssl
  │   │       ├── aes.h
  │   │       ├── asn1.h
  ... ...     ... ...
  │   │       ├── x509v3.h
  │   │       └── x509_vfy.h
  │   └── lib
  │       ├── engines-1.1
  │       │   ├── afalg.so
  │       │   ├── capi.so
  │       │   └── padlock.so
  │       ├── libcrypto.a
  │       ├── libcrypto.so -> libcrypto.so.1.1
  │       ├── libcrypto.so.1.1
  │       ├── libssl.a
  │       ├── libssl.so -> libssl.so.1.1
  │       └── libssl.so.1.1
  └── zlib
      └── lib
          ├── libz.so -> libz.so.1.2.11
          ├── libz.so.1 -> libz.so.1.2.11
          └── libz.so.1.2.11

  8 directories, 86 files
```