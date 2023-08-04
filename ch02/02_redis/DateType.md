
[快速参考](https://redis.io/topics/data-types-intro)

Redis 不是传统意义上的键值对数据库，它的值可以有复杂的数据结构，是一种可以存储各类数据结构的服务器。Redis 支持的数据结构类型如下:
* 字符串。二进制安全的字符串
* 列表。按插入顺序排序的字符串列表
* 集合。无重复的无序字符串元素集合
* 有序集合。与无序集合相似，但每个字符串元素关联一个称为评分(score)的浮点值，各元素按这个评分排序。因为是有序的，所以它可以获取范围内元素，这点也与普通集合不一样。
* 哈希。其映射的对象可以是多种字段名及其关联值的组合。字段名与关联值均是字符串。
* 比特数组。通过特殊的命令，将字符串值处理成一段比特序列。你可以设置或者清除某个比特、统计值为 1 的比特数量、找到第一个设置或未设置的比特等。
* HyperLogLogs。
* 流。


### Redis Keys

Redis 的键是二进制安全的，使用者可以将任何二进制序列作为键，简单如"foo"、复杂到一个 JPEG 文件内容都可以，甚至一个空字符串也是一个有效的键。

关于 Redis 的键，这里有一些规则要注意:
* 不推荐使用长字符串作为键。否则会在内存及计算比较上占用较大消耗。
* 也不推荐使用较短的字符串作为键。还要保证键的直观可读性。
* 可以对键名进行概要性的命名设计。如按照 "object-type:id" 方式命名出的 "user:1000" 就是很好的命名方式。适当的话也可以加上圆点符号(.)或破折号(-)等进行分隔。
* 最大键大小为 512 MB。


### Redis Strings

Redis 字符串是 Redis 键可以关联到的最简单的数据类型，也是内存缓存中唯一的数据表现类型。

由于 Redis 键也是字符串，当值也是字符串时，就是字符串到字符串的映射。

字符串类型是一些场景下很有用，比如缓存 HTML 分片或页面等。

字符串值最大为 512 MB。

关于值类型为字符串的操作演示:
```sh
    > set mykey somevalue
    OK
    > get mykey
    "somevalue" 
```
如上所示，使用者可以通过`SET`和`GET`命令设置和获取字符串。当某个键已经存在时，`SET`命令会替代旧的映射值，即使映射值未必是字符串类型。

通过为 `SET` 命令添加一些参数，可以实现相应的选项操作:
```sh
    > set mykey newval nx
    (nil)
    > get mykey
    "somevalue"
```
mykey 已经存在，通过 `nx` 选项可以使旧键不被覆盖，同时返回 nil。

当字符串表现为基础数值时(如 100, -201 等)，通过一些命令也可以进行一些数值操作。如原子自增操作:
```sh
    > set counter 100
    OK
    > incr counter
    (integer) 101
    > incr counter
    (integer) 102
    > incrby counter 50
    (integer) 152
```
* `INCR` 命令将字符串解析为一个整型，之后将加上相应的数值，将得到的结果替换原来的值。相似的命令还有 `INCRBY`、`DECR`、`DECRBY`，本质上它们都是同样的命令，只是执行上有些不同。
* `INCR` 类命令是原子性的，多客户端同时对同一个对象操作不会触发竞态操作。

其他关于字符串操作的命令。
* `GETSET`: 如果键不存在，设置键值并返回 nil。如果键已经存在，设置新值，同时返回旧值。这个命令在时段统计操作时很有用。
* `MSET` 和 `MGET`: 一次设置或获取多个键值对。
```sh
    > mset a 10 b 20 c 30
    OK
    > get a
    "10"
    > mget a b mykey
    1) "10"
    2) "20"
    3) "somevalue"
```
`MGET` 在使用时，Redis 会返回一个数组。


### 改变和查询键

有些命令并未指定适用于特定数据类型，它的操作目标对象是键字符串。这样看来，这些命令也就可以适用于各种数据类型。比如 `EXISTS` 和 `DEL`:
```sh
    > set mykey hello
    OK
    > exists mykey
    (integer) 1
    > del mykey
    (integer) 1
    > exists mykey
    (integer) 0
```

通过 `TYPE` 命令查询键所对应的值的数据类型:
```sh
    > set mykey x
    OK
    > type mykey
    string
    > del mykey
    (integer) 1
    > type mykey
    none
```

### 键的有效期: Redis expires

键的有效期特性不依赖具体对应的数据类型。最简单的，用户可以设置一个超时作为这个键的有效期，过了有效期后键值将会自动销毁，就像执行了 `DEL` 命令一样。

关于有效期，有些信息需要了解一下:
* 有效期精度可以设置为秒或毫秒
* 最小精度为 1 毫秒
* 有效期信息会反复、持续的永久化到磁盘上。此时 Redis 如果停止服务，但实际上时间却在流逝，这就意味着 Redis 仍然保存着过期数据。

```sh
    > set key some-value
    OK
    > expire key 5
    (integer) 1
    > get key
    "some-value"
    > get key
    (nil)
```
使用 `EXPIRE` 为一个键设置一个有效期(如上示例为 5 秒)，也可以为一个已经存在有效的键设置一个新的有效期。`PERSIST`可以消除一个键的有效期(如果有的话)，使其永远有效。

也可以在使用 `SET` 命令的时候设置有效期:
```sh
    > set key 10 ex 10
    OK
    > ttl key
    (integer) 7
```
`TTL` 命令用于查询一个键的剩余有效期时间，当返回值为 -1 时表示永远有效。

`PEXPIRE` 和 `PTTL` 可以为一个键设置和查询毫秒级的有效期。


### Redis Lists

Redis 列表的底层数据结构为链表，这意味着在头部和尾部的插入是常量级操作。也就是说，通过 `LPUSH` 命令将一个元素插入到只含有 10 个元素的列表的头部，与按照同样方法将一个元素插入到有 1000 万个元素的列表的头部，是一样快的。

Redis 列表的缺点是通过索引访问较慢。如果你需要快速访问数据，可以使用其他数据类型，如有序集合。

`LPUSH` 命令可以将一个元素添加到列表头，`RPUSH` 则相反，二者均支持多参数操作。`LRANGE` 用于获取列表范围数据:
```sh
    > rpush mylist A
    (integer) 1
    > rpush mylist B
    (integer) 2
    > lpush mylist first
    (integer) 3
    > lrange mylist 0 -1
    1) "first"
    2) "A"
    3) "B"
```

列表支持 pop 操作，具体命令为 `LPOP` 和 `RPOP`，分别表示左弹出和右弹出:
```sh
    > rpush mylist a b c
    (integer) 3
    > rpop mylist
    "c"
    > lpop mylist
    "a"
    > lrange mylist 0 -1
    1) "b"
```

列表的一些通用应用场景:
* 记录一些最新的更新操作(如社交网络)
* 生产者-消费者模型

多数场景中，我们只想要获取列表中最近的某个列表片段，而不是全部。这可以通过 `LTRIM` 做到:
```sh
    > rpush mylist 1 2 3 4 5
    (integer) 5
    > ltrim mylist 0 2
    OK
    > lrange mylist 0 -1
    1) "1"
    2) "2"
    3) "3" 
```

### 对列表的阻塞操作

列表可用于实现一个队列，以常见的生产者-消费者模型为示例，其作业方式如下:
* 生产者通过 `LPUSH` 生产数据
* 消费者通过 `RPOP` 消息数据

一般情况下是没有问题的，但当列表为空时，`RPOP` 就会返回 NULL。这种情况下，消费者可以等待一段时间后再执行 `RPOP`，这称为轮询(polling)。但这种方式有两个明显缺点:
* 1.Redis 及其客户端无效地执行一些操作
* 2.也可以添加一个延迟操作，即返回数据为空后等待一点时间。但同时为了能够及时的获取数据，这个时间要设置的够小，实际上也是无效地执行了一些操作。

为此，Redis 提供了对应的阻塞版操作，`BRPOP` 和 `BLPOP` 是分别对应于 `RPOP` 和 `LPOP` 的阻塞版本: 它们只在从列表中成功获取数据后或者到达用户指定超时后才会返回。

```sh
    > rpush mylist 1 2 3 4 5
    (integer) 5
    > brpop mylist 10
    1) "mylist"
    2) "5"
```
`brpop mylist 10` 表示从 mylist 列表中阻塞获取数据，到达 10 秒超时后仍未有数据就返回。当超时时间为 0 时表示永久等待。

使用者甚至可以通过 `BRPOP` 命令同时阻塞等待获取多个列表的数据:
```sh
    > BRPOP yrlist mylist 10
    1) "yrlist"
    2) "1"
    (1.78s)
```

关于 `BRPOP` 命令，有些事情需要注意:
* 多个客户端会有序地执行 `BRPOP` 获取数据，不会发生竞争操作(比如说后来的反而先获得数据，这种情况是不会发生的)。
* `BRPOP` 的返回值不同于 `RPOP`，前者返回的是一个二值数组，除了获取到的值之外，还有列表的名称。因为 `BRPOP` 可以同时操作多个列表，所以有必要说明是从哪个列表中获取到的。
* 到达超时后，依旧返回 NULL 。

关于列表及其阻塞操作的，还有 `LMOVE` 和 `BLMOVE`。


### Redis Hashes

Redis 的哈希是由 字段-值(field-value) 对组成的。
```sh
    > hmset user:1000 username Antirez birthyear 1977 verified 1
    OK
    > hget user:1000 username
    "Antirez"
    > hget user:1000 birthyear
    "1977"
    > hgetall user:1000
    1) "username"
    2) "Antirez"
    3) "birthyear"
    4) "1977"
    5) "verified"
    6) "1"
```
如上示例，`HMSET` 在一个哈希中设置多个字段-值对，利用 `HGET` 可以获取哈希某个字段的值，`HGETALL` 则是获取所有。

使用哈希表示一个结构体对象很是方便，且实用上没有多少限制，也因此这种类型在应用上很常用。

可以使用某些命令来单独对哈希中的某个字段进行操作，如`HINCRBY`:
```sh
    > hincrby user:1000 birthyear 10
    (integer) 1987
```


### Redis Sets

Redis Sets 是一种无序字符串集合。`SADD` 用于将新元素添加到集合中，`SISMEMBER` 用来测试某个元素在集合中是否存在:
```sh
    > sadd myset 1 2 3
    (integer) 3
    > sismember myset 3
    (integer) 1
    > sismember myset 30
    (integer) 0
    > smembers myset
    1) "1"
    2) "2"
    3) "3"
```
通过 `SMEMBERS` 命令可以返回集合中的所有元素。不过需要注意的是，集合是无序的，下次执行同样的命令未必返回是按同样的顺序返回。

集合可以很好的表述两个对象之间的关系。

Redis 集合也提供了传统意义上关于集合的交、并、差的操作:
```sh
    > sinter tag:1:news tag:2:news tag:10:news tags:27:news
    (empty array)
```

`SPOP` 用于随机从集合中移除一个元素，并将该元素返回。

`SUNIONSTORE` 与 `SUNION` 执行结果相同，不同的是后者将结果保存到其命令中的第一个集合(如果已存在则覆盖)中。

`SCARD` 用于获取某个集合中的元素数量。

`SRANDMEMBER` 用于随机从集合中获取指定数量的元素，并且这些元素不会从原集合中移除。


### Redis Sorted sets

有序集合中的元素是按照如下规则进行排序的:
* 如果 A 和 B 有不同的评分，如果 A.score > B.score，那么 A > B
* 如果 A 和 B 有同样的评分，如果 A 的字典序比 B 大，那么 A > B

```sh
    > zadd hackers 1940 "Alan Kay"
    (integer) 1
    > zadd hackers 1957 "Sophie Wilson"
    (integer) 1
    > zadd hackers 1953 "Richard Stallman"
    (integer) 1
    > zadd hackers 1949 "Anita Borg"
    (integer) 1
    > zadd hackers 1965 "Yukihiro Matsumoto"
    (integer) 1
    > zadd hackers 1914 "Hedy Lamarr"
    (integer) 1
    > zadd hackers 1916 "Claude Shannon"
    (integer) 1
    > zadd hackers 1969 "Linus Torvalds"
    (integer) 1
    > zadd hackers 1912 "Alan Turing"
    (integer) 1
```
`ZADD` 命令与 `SADD` 相似，不过多了一个额外参数(置于要插入的元素之前)，称为评分。`ZADD` 可以跟多个 `评分-值` 对。

有序列表的底层采用双数据结构实现，具体就是一个跳表和一个哈希，向有序列表中添加元素是 O(log(N)) 操作，但是从有序列表是获取元素则不需要太多消耗，因为已经排好序了。

按评分升序遍历:
```sh
    > zrange hackers 0 -1
    1) "Alan Turing"
    2) "Hedy Lamarr"
    3) "Claude Shannon"
    4) "Alan Kay"
    5) "Anita Borg"
    6) "Richard Stallman"
    7) "Sophie Wilson"
    8) "Yukihiro Matsumoto"
    9) "Linus Torvalds"
```
按评分降序遍历:
```sh
    > zrevrange hackers 0 -1
    1) "Linus Torvalds"
    2) "Yukihiro Matsumoto"
    3) "Sophie Wilson"
    4) "Richard Stallman"
    5) "Anita Borg"
    6) "Alan Kay"
    7) "Claude Shannon"
    8) "Hedy Lamarr"
    9) "Alan Turing"
```
按评分升序遍历(带评分):
```sh
    > zrange hackers 0 -1 withscores
    1) "Alan Turing"
    2) "1912"
    3) "Hedy Lamarr"
    4) "1914"
    5) "Claude Shannon"
    6) "1916"
    7) "Alan Kay"
    8) "1940"
    9) "Anita Borg"
    10) "1949"
    11) "Richard Stallman"
    12) "1953"
    13) "Sophie Wilson"
    14) "1957"
    15) "Yukihiro Matsumoto"
    16) "1965"
    17) "Linus Torvalds"
    18) "1969"
```
评分值小于等于1950的元素按升序遍历:
```sh
    > zrangebyscore hackers -inf 1950
    1) "Alan Turing"
    2) "Hedy Lamarr"
    3) "Claude Shannon"
    4) "Alan Kay"
    5) "Anita Borg"
```

删除排序后指定范围内的元素，返回删除的元素数量:
```sh
    > zremrangebyscore hackers 1940 1960
    (integer) 4
```

获取某个元素在有序列表中的位置:
```sh
    > zrank hackers "Linus Torvalds"
    (integer) 4
```