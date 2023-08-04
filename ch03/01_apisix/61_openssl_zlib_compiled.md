

### openssl

```sh
    ./config --prefix=/usr/local/openssl
    make
    make install    
```

附: `/usr/local/openssl` 的二级目录树结构为:
```sh
  ├── bin
  │   ├── c_rehash
  │   └── openssl
  ├── include
  │   └── openssl
  ├── lib
  │   ├── engines-1.1
  │   ├── libcrypto.a
  │   ├── libcrypto.so -> libcrypto.so.1.1
  │   ├── libcrypto.so.1.1
  │   ├── libssl.a
  │   ├── libssl.so -> libssl.so.1.1
  │   ├── libssl.so.1.1
  │   └── pkgconfig
  ├── share
  │   ├── doc
  │   └── man
  └── ssl
      ├── certs
      ├── misc
      ├── openssl.cnf
      ├── openssl.cnf.dist
      └── private
```


### zlib

```sh
    ./configure --prefix=/usr/local/zlib
    make
    make install
```