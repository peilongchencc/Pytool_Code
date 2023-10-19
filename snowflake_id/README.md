# SnowflakeID❄️
- [SnowflakeID❄️](#snowflakeid️)
  - [雪花ID简介：](#雪花id简介)
  - [雪花ID为什么由64位组成，而不是更多：](#雪花id为什么由64位组成而不是更多)
  - [雪花ID的位数分配规则：](#雪花id的位数分配规则)
  - [雪花ID的实例：](#雪花id的实例)
  - [使用时间基线生成雪花ID：](#使用时间基线生成雪花id)
    - [部分代码解释：](#部分代码解释)

## 雪花ID简介：

雪花ID（Snowflake ID）是一种分布式唯一标识符生成算法，旨在为分布式系统中生成全局唯一的ID。它由Twitter公司开发，用于解决数据库主键生成的性能瓶颈和冲突问题。<br>

雪花ID由64位二进制数字组成，转换为十进制数字后，可能为17、18或19位数字，雪花ID的组成结构如下：<br>

```txt
1位标志位（始终为0）     41位时间戳（精确到毫秒）     10位工作节点ID       12位序列号
```

雪花ID通常由64位组成，其中标志位始终为0标识为正数，41位时间戳记录了生成ID的时间，10位工作节点ID标识了不同的机器，12位序列号在同一毫秒内自增，以保证同一机器在同一毫秒内生成不同的ID。<br>

通过这种方式，雪花ID生成的ID是有序的，且趋势递增，便于数据库索引的管理。而且它的生成过程是无锁的，可以在高并发环境下快速生成唯一ID。<br>

我们也可以根据自己的需求，手动分配位数，创建不同需求。例如利用 `[时间戳、节点A、节点B、关系]` 组成雪花ID，且为不同需求更改位数的限制，比如降低时间戳所占位数，但降低时间戳所占位数会导致生成ID的范围降低。😲😲😲<br>

## 雪花ID为什么由64位组成，而不是更多：

雪花ID（Snowflake ID）是Twitter开源的分布式ID生成算法。它的ID是一个64位的整数，这样设计有以下几点原因：<br>

1. **硬件与存储因素**：64位整数对大多数现代CPU来说都是原生支持的，这意味着操作64位整数的性能是最优的。相比之下，74位整数在许多平台上都不是原生支持的，操作它们可能需要额外的性能开销。<br>

2. **兼容性**：64位整数在很多编程语言和系统中都有很好的支持。这使得整合和使用雪花ID在各种场景下都变得更加简单。<br>

3. **结构分配**：雪花ID的结构是这样的：1位标志位，41位表示时间戳，10位表示工作节点ID，12位表示序列号。这种分配已经可以满足大多数使用场景的需要，41位的时间戳可以支持约69年的时间，10位工作节点ID可以支持1024个节点，12位序列号可以支持同一毫秒内产生4096个ID。<br>

4. **长度考量**：增加ID的位数不仅会增加存储和处理的复杂性，还可能导致其他系统（例如数据库、缓存等）需要进行额外的调整来适应更长的ID。<br>

综上所述，64位对于雪花ID来说是一个平衡性能、兼容性和功能的选择。如果真的有更大的需求，那么自然可以对算法进行修改，但目前64位已经能满足绝大多数的应用场景。<br>


## 雪花ID的位数分配规则：

在 `SnowflakeID` 中，我们需要决定如何为不同的字段分配位数，分配位数并不是以文字长短分配，而是以可能的不同值分配位数。<br>

例如，如果你知道实体A只可能有4种不同的2字中文词，那么你只需要2位来表示它（因为 \(2^2 = 4\)）。同样，如果实体B可能有16种不同的4字中文词，那么你需要4位来表示它（因为 \(2^4 = 16\)）。<br>

所以，需要注意：位数的占用是可能的不同值的数量，而不是文字的长度。🚨🚨🚨<br>

假设：
- 实体A有4种可能值：需要2位
- 实体B有16种可能值：需要4位
- 关系有64种可能值：需要6位

这样，你总共需要2 + 4 + 6 = 12位来为这些字段编码到 `SnowflakeID` 中。当然，这还不包括时间戳，时间戳将占据其余的位数。<br>

## 雪花ID的实例：

假设你要根据 `data_list` 中的信息为每个元素生成雪花❄️ID，其中 `data_list` 中每个元素由实体A、实体B和关系组成，现在数据量要扩充到超级大的程度，实体A的可能值为1万多种，实体B的可能值也为1万多种，关系的可能值为100多种，尽可能的多设想一些可能值，防止ID的生成限制。<br>

首先，我们将可能性近似转化为2的倍数，1万多种转化为16384种\(2^14 = 16384\)，100多种转化为128种\(2^7 = 128\)，所以此时应该将位数安排如下：<br>

```txt
1. `时间戳`：29位 (约合17年)--最低位
2. `实体A`：14位 (代表 2^{14} = 16384 种)
3. `实体B`：14位 (代表 2^{14} = 16384 种)
4. `关系`：7位 (代表 2^{7} = 128 种)
 
总位数：64位
```

接下来看一下具体的代码实现：<br>

```python
import time

class SnowflakeID:
    def __init__(self):
        self.relation_shift = 57   # relation的可能值为128种(2^7=128)，位数为7，57+7=64
        self.entity_b_shift = 43   # 实体A的可能值为16384种(2^14=16384)，位数为14位，43+14=57
        self.entity_a_shift = 29   # 实体A的可能值为16384种(2^14=16384)，位数为14位，29+14=43
        self.timestamp_shift = 0   # 时间戳定义为0-29位，29位二进制数可以表示的不同值是2^29，这是因为每一位可以是0或1，所以总共有2的 29 次方个不同的组合。这个值等于 536,870,912。
                                   # 由于时间戳的单位是秒，故支持约17年时间转换。由于时间戳的起始是1970年，所以最新时间无法转换，需要添加时间基线。

        self.relation = {}
        self.entity_a = {}
        self.entity_b = {}

    def add_mapping(self, entity_a, entity_b, relation):
        # 添加或更新映射
        if entity_a not in self.entity_a:
            self.entity_a[entity_a] = len(self.entity_a) + 1

        if entity_b not in self.entity_b:
            self.entity_b[entity_b] = len(self.entity_b) + 1

        if relation not in self.relation:
            self.relation[relation] = len(self.relation) + 1

    def generate_id(self, entity_a, entity_b, relation):
        curr_timestamp = int(time.time()) & ((1 << 29) - 1)   # Ensure timestamp is 29 bits
        id = (self.relation[relation] << self.relation_shift) | \
             (self.entity_a[entity_a] << self.entity_a_shift) | \
             (self.entity_b[entity_b] << self.entity_b_shift) | \
             (curr_timestamp << self.timestamp_shift)
        return id

    def parse_id(self, id):
        # Adjusting the masks
        question_value = (id >> self.relation_shift) & ((1 << 7) - 1)
        a_value = (id >> self.entity_a_shift) & ((1 << 14) - 1)
        b_value = (id >> self.entity_b_shift) & ((1 << 14) - 1)
        timestamp = id & ((1 << 29) - 1)

        question_name = list(self.relation.keys())[list(self.relation.values()).index(question_value)]
        a_name = list(self.entity_a.keys())[list(self.entity_a.values()).index(a_value)]
        b_name = list(self.entity_b.keys())[list(self.entity_b.values()).index(b_value)]

        return a_name, b_name, question_name, timestamp

data_list = [['卖出', '钢琴', 'Pat'], 
             ['买入', '黄金', 'Exp'], 
             ['交换', '比特币', 'Clas']]

sf = SnowflakeID()

# 为每个子列表生成和解析雪花 ID
for data in data_list:
    sf.add_mapping(data[0], data[1], data[2])
    id = sf.generate_id(data[0], data[1], data[2])
    print(f"Generated ID: {id}")
    print(f"Generated ID Length: {len(str(id))}")
    # 解析数据
    parsed_data = sf.parse_id(id)
    print(f"Parsed Data: {parsed_data}")    # 注意时间戳移了29位
    print()
```

终端输出效果：<br>

```txt
Generated ID: 144123984789102556
Generated ID Length: 18
Parsed Data: ('卖出', '钢琴', 'Pat', 83353564)

Generated ID: 288247969494851548
Generated ID Length: 18
Parsed Data: ('买入', '黄金', 'Exp', 83353564)

Generated ID: 432371954200600540
Generated ID Length: 18
Parsed Data: ('交换', '比特币', 'Clas', 83353564)
```

> 上述时间戳在转化为 `年-月-日 时-分-秒` 时只能转化为靠近 `1970年` 的时间。

由于将时间戳限制为了29位，时间戳的值实际上只包含了1970年以来的部分秒数，这是不足以表示当前的日期和时间的。如果你希望将其解析为当前日期和时间，那么你需要存储一个基线时间戳，并在解析时将其添加回去。<br>

将时间戳转化为 `年-月-日 时-分-秒` 格式可以参考以下代码，或者直接去笔者所写的 `time` 模块查看更详细内容🥴🥴🥴：<br>

```python
import time

timestamp = 1641009944.0
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
print(formatted_time)   # 2022-01-01 12:05:44
```

## 使用时间基线生成雪花ID：

如果你不关注时间戳的转化，使用上一节的代码没有任何问题，如果你关注时间戳的转化，会发现时间戳只能转化为 `1970年` 左右，这还是很难受的。那么我们要怎样才能让时间正常显示呢？☕️☕️☕️<br>

一个简单的方法是使用 `2023年1月1日` 作为基线时间戳，具体操作如下：<br>

在`SnowflakeID`的`__init__`方法中，添加一个基线时间戳。<br>
在`generate_id`方法中，从当前时间减去这个基线时间戳。<br>
在`parse_id`方法中，将基线时间戳加回来。<br>

具体代码如下：<br>
```python
import time

class SnowflakeID:
    def __init__(self):
        # 基线时间戳：2023年1月1日
        self.baseline_timestamp = int(time.mktime(time.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')))
        self.relation_shift = 57   # relation的可能值为128种(2^7=128)，位数为7，57+7=64
        self.entity_b_shift = 43   # 实体A的可能值为16384种(2^14=16384)，位数为14位，43+14=57
        self.entity_a_shift = 29   # 实体A的可能值为16384种(2^14=16384)，位数为14位，29+14=43
        self.timestamp_shift = 0   # 时间戳定义为0-29位，29位二进制数可以表示的不同值是2^29，这是因为每一位可以是0或1，所以总共有2的 29 次方个不同的组合。这个值等于 536,870,912。
                                   # 由于时间戳的单位是秒，故支持约17年时间转换。由于时间戳的起始是1970年，所以最新时间无法转换，需要添加时间基线。

        self.relation = {}
        self.entity_a = {}
        self.entity_b = {}

    def add_mapping(self, entity_a, entity_b, relation):
        # 添加或更新映射
        if entity_a not in self.entity_a:
            self.entity_a[entity_a] = len(self.entity_a) + 1

        if entity_b not in self.entity_b:
            self.entity_b[entity_b] = len(self.entity_b) + 1

        if relation not in self.relation:
            self.relation[relation] = len(self.relation) + 1

    def generate_id(self, entity_a, entity_b, relation):
        curr_timestamp = (int(time.time()) - self.baseline_timestamp) & ((1 << 29) - 1) 
        id = (self.relation[relation] << self.relation_shift) | \
             (self.entity_a[entity_a] << self.entity_a_shift) | \
             (self.entity_b[entity_b] << self.entity_b_shift) | \
             (curr_timestamp << self.timestamp_shift)
        return id

    def parse_id(self, id):
        question_value = (id >> self.relation_shift) & ((1 << 7) - 1)
        a_value = (id >> self.entity_a_shift) & ((1 << 14) - 1)
        b_value = (id >> self.entity_b_shift) & ((1 << 14) - 1)
        timestamp = id & ((1 << 29) - 1)

        question_name = list(self.relation.keys())[list(self.relation.values()).index(question_value)]
        a_name = list(self.entity_a.keys())[list(self.entity_a.values()).index(a_value)]
        b_name = list(self.entity_b.keys())[list(self.entity_b.values()).index(b_value)]

        timestamp_in_seconds = self.baseline_timestamp + timestamp
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp_in_seconds))
        return a_name, b_name, question_name, formatted_time

if __name__ == '__main__':
    data_list = [['卖出', '钢琴', 'Pat'],
                 ['买入', '黄金', 'Exp'], 
                 ['卖出', '钢琴', 'Pat'], 
                 ['交换', '比特币', 'Clas']]

    snowflakeid = SnowflakeID()

    # 为每个子列表生成和解析雪花 ID
    for data in data_list:
        snowflakeid.add_mapping(data[0], data[1], data[2])
        id = snowflakeid.generate_id(data[0], data[1], data[2])
        print(f"Generated ID: {id}")
        print(f"Generated ID Length: {len(str(id))}")
        # 解析数据
        parsed_data = snowflakeid.parse_id(id)
        print(f"Parsed Data: {parsed_data}")
        print()
```

终端输出效果：<br>

```txt
Generated ID: 144123984727215140
Generated ID Length: 18
Parsed Data: ('卖出', '钢琴', 'Pat', '2023-09-06 10:49:08')

Generated ID: 288247969432964132
Generated ID Length: 18
Parsed Data: ('买入', '黄金', 'Exp', '2023-09-06 10:49:08')

Generated ID: 432371954138713124
Generated ID Length: 18
Parsed Data: ('交换', '比特币', 'Clas', '2023-09-06 10:49:08')
```

现在是不是看着就很舒服了～🤭🤭🤭<br>

### 部分代码解释：

`(1 << 14) - 1` 是一个位运算表达式，它的含义是将二进制数 1 左移 14 位，然后减去 1。

1. `(1 << 14)`：这部分执行了左移位运算，将二进制数 1 左移 14 位。左移操作将 1 的二进制表示向左移动指定的位数，相当于在二进制数的末尾添加了若干个零。在这里，左移 14 位后，得到的结果是 `100000000000000`，它表示了一个二进制数，其中最高位是 1，其余位都是 0。

2. `- 1`：接下来，从左移操作的结果中减去 1。这是一个简单的减法操作。在上一步的基础上减去 1，就得到了 `011111111111111`，这是一个包含 14 个 1 的二进制数。

综合起来，`(1 << 14) - 1` 的结果就是一个包含 14 个连续的 1 的二进制数，它可以用来创建一个位掩码，用于提取一个整数中的低 14 位。这种操作常用于位运算中，用于清除或提取特定位的值。在这个代码中，它被用于提取实体A和实体B的部分值，保留了低 14 位。