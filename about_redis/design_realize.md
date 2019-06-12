### 一、数据结构与对象

---

#### 1、简单动态字符串 (Simple Dynamic String)

---
- **数据结构**
```C
// sds.h/sdshdr redis默认字符串结构定义
struct sdshdr {
    // 记录buf数组中已使用字节的数量， 等于SDS所保存字符串长度
    int len;
    // 记录buf数组中未使用字节的数量
    int free;
    // 字节数组，用于保存字符串
    char buf[];
}
```
- **特性**
1、常数复杂度获取字符串长度
2、API是安全的，不会造成缓冲区溢出
3、减少修改字符串长度时内存重新分配的次数
4、二进制安全，可以保存文本和二进制
5、兼容部分C字符串函数

#### 2、链表
---
- **数据结构**
```C
// adlist.h/listNode 链表节点结构
typedef struct listNode {
    // 前置节点
    struct listNode *prev;
    // 后置节点
    struct listNode *next;
    // 节点的值
    void *value;
};

// adlist.h/list 链表结构
typedef struct list {
    // 表头节点
    listNode *head;
    // 表尾节点
    listNode *tail;
    // 链表所包含节点数量
    unsigned long len;
    // 节点复制函数
    void *(*dup)(void *ptr);
    // 节点值释放函数
    void (*free)(void *ptr);
    // 节点值对比函数
    int (*match)(void *ptr, void *key);
} list;
```
- **特性**
1、广泛用于Redis各种功能，列表建、发布与订阅、慢查询、监视器等
2、Redis链表实现是双端链表
3、每个链表都用一个list结构来表示，有头、尾、长度信息
4、Redis的链表实现是无环链表
5、通过为链表设置不同类的类型特定函数，Redis链表可以保存各种不同类型的值

#### 3、字典
---
- **简介**
    又称符号表（symbol table）、关联数组（associative array）、映射（map）,保存键值对的抽象数据结构

- **数据结构**
```C
// dict.h/dictEntry 哈希表节点dictEntry 结构
typedef struct dictEntry {
    // 键
    void *key;
    // 值
    union{
        void *val;
        uint64_tu64;
        int64_ts64;
    } v;
    // 指向下一个哈希表节点，形成链表
    struct dictEntry *next;
} dictEntry;

// dict.h/dictht redis 哈希表结构
typedef struct dictht {
    // 哈希表数组
    dictEntry **table;
    // 哈希表大小
    unsigned long size;
    // 哈希表大小掩码，用于计算索引值，总是等于size-1
    unsigned long sizemask;
    // 该哈希表已有节点数量
    unsigned long used;
} dictht;

// dict.h/dict redis字典结构
typedef struct dict {
    // 类型特定函数
    dictType *type;
    // 私有数据
    void *privdata;
    // 哈希表
    dictht ht[2];
    // rehash索引，当rehash值不存在是，值为-1
    int rehashidx;
} dict;

// dict.h/dictType

typedef struct dictType {
    // 计算哈希值的函数
    unsigned int (*hashFunction)(const void *key);
    // 复制键的函数
    void *(*keyDup)(void *privdata, const void *key);
    // 复制值的函数
    void *(*valDup)(void *privdata, const void *obj);
    // 对比键的函数
    int (*keyCompare)(void *privdata, const void *key1, const void *key2);
    // 销毁键的函数
    void (*keyDestructor)(void *privdata, void *key);
    // 销毁值的函数
    void (*valDestructor)(void *privdata, void *obj)；
} dictType;

```
- **rehash**
1. 为ht[1]分配空间：
    * 扩展操作：ht[1]的大小为第一个大于等于ht[0].used*2的2的n次幂；
    * 收缩操作：ht[1]的大小为第一个大于等于ht[0].used的2的n次幂；
2. 将保存在ht[0]的所有键值对rehash到ht[1]上面，需要重新计算键的哈希值和索引值，然后放置在ht[1]的指定位置上；
3. 当ht[0]的所有键值对都迁移到ht[1]之后（ht[0]变为空表），释放ht[0]，将ht[1]置为ht[0], 并在ht[1]新创建一个空白的哈希表，为下一次rehash做准备。

- **渐进式rehash**
1. 为ht[1]分配空间，让字典同时拥有两个哈希表，ht[0]和ht[1]；
2. 字典中维持一个索引计数器变量rehashidx，将它的值设置为0，标示rehash正式开始；
3. 在rehash同时，每次字典进行增删改查操作时候，程序除了执行指定操作外，还会顺带将ht[0]哈希表在rehashidx索引上的所有键值对rehash到ht[1], 当rehash完成后，程序将rehashidx的值增一；
4. 当ht[0]所有的键值对都rehash到ht[1]，程序会将rehashidx设置为-1，表示rehash结束。

- **特性**
1. 字典被广泛用于Redis各种功能，包括数据库和哈希键；
2. Redis中的字典使用哈希键作为底层实现，每个字典都有两个哈希表ht[0]和ht[1],一个平时使用，另外一个仅在rehash时候使用
3. 当字典用作数据库底层或者哈希键底层底层实现，Redis使用MurMurHash2算法来计算键的哈希值
4. 哈希表使用链地址法来解决键冲突，被分配到同一个索引上的多个键值对会连接成一个单项链表
5. 在对哈希表进行扩展或者收缩操作时候，程序需要将现有哈希表包含的所有键值对rehash到新哈希表里面，这个rehash过程是渐进式完成的。


#### 4、跳跃表（skiplist）
---

- 简介
    1、跳跃表是一种有序数据结构，它通过在每个节点中维持多个指向其他节点的指针，从而达到快速访问的目的。节点查找的平均复杂度O(logN)、最坏O(N)，还可以通过顺序性操作来批量处理节点。
    2、Redis使用跳跃表作为有序集合键的底层实现之一。如果一个有序集合包含的元素数量比较多或者元素的成员是比较长的字符串时，Redis就会使用跳跃表作为有序集合键的底层实现。
    3、Redis里面只有有序集合键和集群节点中内部数据额结构使用到了跳跃表。

- **数据结构**
```C
// redis.h/zskiplistNode
typedef struct zskiplistNode {
    // 层
    struct {
        // 前进指针
        struct zskiplistNode *forward;
        // 跨度
        unsigned int span;
    } level[];

    // 后退指针
    struct zskiplistNode *backward;
    // 分值
    double score;
    // 成员对象
    robj *obj;

} zskiplistNode；

// redis.h/zskiplist

typedef struct zskiplist {
    // 表头节点和表尾节点
    struct zskiplistNode *header, *tail;
    // 表中节点数量
    unsigned long length;
    // 表中层数最大节点的层数
    int level;
} zskiplist;

```
- **特性**

1. 跳跃表是有序集合的底层实现之一；
2. Redis跳跃表实现由zskiplist和zskiplistNode两个结构组成，其中zskiplist用来保存跳跃表信息，zskiplistNode用来表示跳跃表节点；
3. 每个跳跃表节点的层高都是1~32之间；
4. 在同一个跳跃表中，多个节点可以包含相同的分值，但是每个节点的成员对象必须是唯一的；
5. 跳跃表中的节点顺序按照分值大小排序，当分值相同时，节点按照成员对象的大小进行排序


#### 5、整数集合(intset)
---
- **简介**
    用于保存整数值的集合，一个抽象的数据结构，它可以保存类型为int16_t、int32_t、int64_t的整数值，并且保证集合中不会出现重复元素。

- **数据结构**
```C
// intset.h/intset

typedef struct intset {
    // 编码方式
    uint32_t encoding;
    // 集合包含的元素数量
    uint32_t length;
    // 保存元素的数组
    int8_t contents[];
} intset;

// contents 数组是整数集合的底层实现： 整数集合的每个元素都是contents数组的一个数据项（item），每个项在数组中按照值的大小从小到大的有序排列，并且数组中不包含重复项， contents数组真正的类型取决于encoding属性的值
```

- **特性**
1. 整数集合是集合键的底层实现之一；
2. 整数集合的底层实现是数组，这个数组以有序、无重复的方式保存集合元素，在有需要时，程序会根据新添加的元素的类型，改变这个数组的类型。
3. 升级操作为整数集合带来了操作上的灵活性，并且尽可能的节约了内存；
4. 整数集合只支持升级操作，不支持降级操作。

#### 6、压缩列表（ziplist）
---
- **简介**
    1、压缩列表是列表键和哈希键的底层实现之一。当一个列表键只含有少量列表项，并且每个列表项要么是小整数值，要么是长度较短的字符串，那么Redis就会使用压缩列表来做列表键的底层实现。
    2、压缩列表由一系列特殊编码的连续内存块组成的顺序形数据结构。一个压缩列表可以包含任意多个节点（Entry），每个节点可以保存一个字节数组或者一个整数值。

- **数据结构**
```C
[zlbytes, zltail, zllen, ... entryX, zlend]
// zlbytes: uint32_t, 4字节，整个压缩列表占用的内存字节数
// zltail: uint32_t, 4字节，记录压缩列表尾节点距离起始节点有多少字节
// zllen： uint16_t, 2字节，记录压缩列表含有的节点数量，当节点数据大于UINT16_MAX 时候需要遍历整个压缩列表才能算出
// entryX: 列表节点，不确定，压缩列表的各个节点，节点的长度由节点保存的内容决定
// zlend: uint8_t, 1字节，特殊值0xFF，标记压缩列表的尾端
```

- **特性**


#### 7、对象
---
- **简介**
    1、Redis并没有直接使用以上数据结构来实现键值数据库，而是基于上面这些数据结构实现了一个对象系统。包含：字符串对象、列表对象、哈希对象、集合对象、有序集合对象。Redis在执行命令之前，根据对象类型来判断一个对象是否可以执行给定的命令。
    2、Redis对象系统还实现了基于引用计数计数的内存回收机制，当程序不在使用某个对象的时候，这个对象所对应的内存就会被自动释放；另外，Redis通过引用计数计数实现了对象共享机制，这一机制可以在适当的条件下，通过让多个数据库键共享同一个对象来节约内存。

- **数据结构**
```C
typedef struct redisObject {
    // 类型
    unsigned type:4;
    // 编码
    unsigned encoding:4;
    // 指向底层实现数据结构的指针
    void *ptr;
    unsigned lru:32;
    // ...
} robj;

```

###### 1.类型

|类型常量|对象名称|TYPE命令输出|
|---|---|---|
REDIS_STRING|字符串对象|string|
REDIS_LIST|列表对象|list|
REDIS_HASH|哈希对象|hash|
REDIS_SET|集合对象|set|
REDIS_ZSET|有序集合对象|zset|

###### 2.类型和编码

| 类型 | 编码 | 对象 |
| --- | --- | --- |
| REDIS_STRING | REDIS_ENCODING_INT | 使用整数值实现的字符串对象 |
| REDIS_STRING | REDIS_ENCODING_EMBSTR | 使用embstr编码的简单动态字符串实现的字符串对象 |
| REDIS_STRING | REDIS_ENCODING_RAW | 使用SDS实现的字符串对象 |
| REDIS_LIST | REDIS_ENCODING_ZIPLIST | 使用压缩列表实现的列表对象 |
| REDIS_LIST | REDIS_ENCODING_LINKEDLIST | 使用双端链表实现的列表对象 |
| REDIS_HASH | REDIS_ENCODING_ZIPLIST | 使用压缩列表实现的哈希对象 |
| REDIS_HASH | REDIS_ENCODING_HT | 使用字典实现的哈希对象 |
| REDIS_SET | REDIS_ENCODING_INTSET | 使用整数集合实现的集合对象 |
| REDIS_SET | REDIS_ENCODING_HT | 使用字典实现的集合对象 |
| REDIS_ZSET | REDIS_ENCODING_ZIPLIST | 使用压缩列表实现的有序集合对象 |
| REDIS_ZSET | REDIS_ENCODING_SKIPLIST | 使用跳跃表和字典实现的有序集合对象 |


- **特性**
1. Redis数据库中的每个键值对的键和值都是一个对象
2. Redis共有字符串、列表、哈希、集合、有序集合五种类型的对象，每种类型都有两种或者两种以上的编码方式，不同的编码可以在不同的场景上优化对象的使用效率
3. 服务器在执行某些命令之前，会先检查给定键的类型能否执行指定的命令，而检查一个键的类型就是检查键的值对象的类型
4. Redis的对象系统带有引用计数实现的内存回收机制，当一个对象不再被使用时候，该对象被占用的内存就会被自动释放
5. Redis的共享值为0-9999的字符串对象
6. 对象会记录自己的最后一次被访问的时间，这个时间可以用于计算对象的空转时间


### 二、单机数据库的实现

#### 1、数据库

```C
// redis.h/redisServer
struct redisServer {
    //...

    // 一个数组，保存着服务器中所有的数据库
    redisDb *db;

    // 服务器中的数据库数量, 默认为16
    int dbnum;

    //...
};


// redis.h/redisClient
typedef struct redisClient {
    // ...
    // 记录客户端当前正在使用的数据库
    redisDb *db;
    // ...
} redisClient;


// redis.h/redisDb
typedef struct redisDb {
    // ...
    // 数据库键空间，保存在数据库中所有的键值对
    dict *dict;
    // 过期字典，保存着键的过期时间
    dict *expires;
    // ...
} redisDb;

```

- 数据库键空间
    - 键空间的键也就是数据库的键，每个键都是一个字符串对象
    - 键空间的值也就是数据库的值，每个值可以是字符串对象、列表对象、哈希对象、集合对象、有序集合对象中的任意一种Redis对象
- 过期键删除策略
    - 定时删除：在设置过期时间同时，创建一个定时器，让定时器在过期时间来临时，立即执行对键的删除
    - 惰性删除：放任键不管，在每次获取键的时候，判断是否过期，如果过期则删除，没过期就返回
    - 定期删除：每隔一段时间程序对数据库里面过期的键进行删除
- redis使用了惰性删除+定期删除两种结合的键删除策略。


#### 2、RDB持久化
**RDB文件结构：**

```yaml
RDB 文件：
    REDIS | db_version | databases | EOF | check_num

database 部分：
    SELECTDB | db_number | key_value_pairs

key_value_pairs 部分：
    TYPE | key | value

key_value_pairs 部分 (有过期时间)：
    EXPIRETIME_MS | MS | TYPE | key | value

```

```C
struct redisServer {
    // ...
    // 修改计数器
    long dirty;
    // 上一次执行保存的时间
    time_t lastsave;
    // ...
};
```

**重点回顾：**

1. RDB文件用于保存和还原Redis服务器所有数据库中的所有键值对数据
2. SAVE命令由服务器进程直接执行保存操作，所以该命令会阻塞服务器
3. BGSAVE命令由子进程执行保存操作，所以该命令不会阻塞服务器
4. 服务器状态中会保存所有有用SAVE选项设置的保存条件，当任意一个保存条件被满足时候，服务器会自动执行BGSAVE命令，（900s 1次修改；300s 10次修改；60s 10000次修改）
5. RDB文件是一个经过压缩的二进制文件，由多个部分组成
6. 对于不同类型的键值对，RDB文件会用不同的方式来保存它们

#### 3、AOF持久化

**重点回顾**

1. AOF文件通过保存所有修改数据库的写命令请求来记录服务器的数据库状态
2. AOF文件中的所有命令都已REDIS命令请求协议的格式保存
3. 命令请求会先保存到AOF缓冲区里面，之后再定期写入并同步到AOF文件
4. appendfsync选项的不同值对AOF持久化功能的安全性以及Redis服务器的性能有很大的影响（alway，everysec，no）
5. 服务器只要载入并重新执行保存在AOF文件中的命令，就可以还原数据库本来的状态
6. AOF重写可以产生一个新的AOF文件，这个心的AOF文件和原有的AOF文件所保存的数据库状态一样，但是体积更小
7. AOF重写是通过读取数据库中的键值对来实现的，程序无需对现有的AOF文件进行任何读、分析和写操作
8. 在执行BGREWRITEAOF命令时，Redis服务器会维护一个AOF重写缓冲区，该缓冲区会在子进程创建新的AOF文件期间，记录服务器所有执行的写命令。当子进程完成创建新的AOF文件工作之后，服务器会重写缓冲区中的所有内容到新的AOF文件末尾，使得新旧两个AOF文件所保持的数据是一致的。最后，服务器会用新的AOF文件替换旧的AOF文件，以此来完成AOF文件的重写操作。

#### 4、事件

**文件事件**
Redis基于Reactor模式开发了自己的网络时间处理器
- 文件事件处理器使用I/O多路复用程序来同时监听多个套接字，并根据套接字目前执行的任务来为套接字关联不同的时间处理器
- 当被监听的套接字准备好执行连接应答（accept）、读取（read）、写入、关闭（）等操作时，与操作相对应的文件事件就会产生，这时文件事件处理器就会调用套接字之前关联好的时间处理器来处理这些事件
- 文件事件处理器的四个组成部分：套接字、I/O多路复用程序、文件事件分派器（dispatcher）、以及事件处理器

**时间事件**
- 分为定时事件和周期性事件
- 一个时间事件主要有三部分：id 全局唯一标示；when 时间事件的到达时间，毫秒的unix时间戳；timeProc 时间事件处理器，一个函数
- 目前Redis只使用了周期性事件


**重点回顾**

1. Redis服务器是一个事件驱动程序，服务器处理的事件分为时间事件和文件事件两类
2. 文件事件处理器是基于Reactor模式实现的网络通信程序
3. 文件事件是对套接字操作的抽象：每次套接字变为：可应答、可读、可写时候相应的文件事件就会产生
4. 文件事件分为AE_READABLE事件（读）和AE_ARITABLE事件（写）两类
5. 时间事件分为定时事件和周期事件：定时事件只在指定的时间到达一次，周期性事件每隔一段时间到达一次
6. 服务器在一般情况下只执行serverCron函数一个时间事件，并且这个事件是周期性事件
7. 文件事件和时间事件之间和合作关系，服务器会轮流处理这两种事件，并且处理事件的过程中也不会进行抢占
8. 时间事件的实际处理时间通常会比设定的到达时间晚一些


#### 5、客户端

```C

struct redisServer {
    // ...

    // 一个链表，保存了所有客户端的状态
    list *clients;

    // ...

};

typedef struct redisClient {
    // ...

    // 客户端状态的fd属性记录了 客户端正在使用的套接字描述符
    int fd;

    // 客户端名称
    robj *name;

    // 客户端目前状态
    int flags;

    // 输入缓冲区
    sds querybuf;

    // 命令和命令参数
    robj **argv;
    int argc;

    // 命令的实现函数
    struct redisCommand *cmd;

    // 输出缓冲区
    char buf[REDIS_REPLY_CHUNK_BYTES];
    int bufpos;

    // 可变大小缓冲区
    list *replay;

    // 身份验证
    list authenticated;

    // 客户端创建时间
    time_t ctime;
    // 客户端与服务器最后一次互动时间
    time_t lastinteraction;
    // 缓冲区第一次到达软性限制的时间
    time_t obuf_soft_limit_reached_time;

    // ...

} redisClient;

```

**redisClient**
根据客户端类型的不同，fd属性的值可以是-1 或者是大于-1的整数：

1. 伪客户端（fake client）：fd的属性为-1，伪客户端的命令请求来源于AOF文件或者LUA脚本，而不是网络，所以这种客户端不需要套接字连接，自然也就不需要记录套接字描述符。
2. 普通客户端：fd的属性是一个大于-1的整数，普通客户端使用套接字来和服务器进行通信，所以服务器会用fd属性来记录客户端套接字的描述符。


**重点回顾**

1. 服务器状态结构使用clients链表连接起多个客户端状态，新添加的客户端状态会被放到链表的末尾
2. 客户端状态的flags属性使用不同标志来表示客户端的角色，以及客户端当前所处的状态
3. 输入缓冲区记录了客户端发送的命令请求，这个缓冲区的大小不能超过1GB
4. 命令的参数和参数的个数会记录在客户端状态的argv和argc属性里面，而cmd属性记录了客户端要执行命令的实现函数
5. 客户端有固定大小缓冲区和可变大小缓冲区，固定大小缓冲区的大小为16KB,而可变大小缓冲区的大小不能超过服务器设置的硬性限制值
6. 输出缓冲区限制有两种，如果输出缓冲区大小超过了服务器设置的硬性限制，那么客户端会被立即关闭；如果客户端在一定时间内，一直超过服务器的软性限制，那么客户端也会被关闭
7. 当客户端通过网络连接到服务器，服务器会给客户端创建响应的状态
8. 处理LUA脚本的伪客户端在服务器初始化时创建，这个客户端会一直存在，知道服务器关闭
9. 载入AOF文件使用的伪客户端在载入工作开始时动态创建，载入工作完毕之后关闭

#### 6、服务端

```C

struct redisServer {
    // ...

    // 一个链表，保存了所有客户端的状态
    list *clients;

    // 默认每10秒更新一次的时钟缓存
    // 用于计算键的空转时长（idle）
    unsigned lruclock:22;
    // ...
};


tyoedef struct redisObject {
    // ...

    // 最后一次被命令访问的时间
    unsigned lru:22;

    // ...

}robj;

```


### 三、多机数据库的实现

#### 1、复制
#### 2、Sentinel


### 四、独立功能的实现



##### Redis 管道（Pipelining）
    一次请求/响应服务器能实现处理新的请求即使旧的请求还未被响应。这样就可以将多个命令发送到服务器，而不用等待回复，最后在一个步骤中读取该答复。

##### Pub/Sub
