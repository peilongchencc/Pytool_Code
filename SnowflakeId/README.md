# SnowflakeId
基本情况：
假设要根据 `data_list` 中的信息为每个元素生成雪花❄️ID，其中 `data_list` 中每个元素由实体A、实体B和关系组成，现在数据量要扩充到超级大的程度，实体A的可能值为16384种，实体B的可能值为16384种，关系的可能值为128种<br>

此时应该将位数安排如下：<br>
```txt
1. `时间戳`：29位 (约合17年)--最低位
2. `实体B`：14位 (代表 2^{14} = 16384 种)
3. `实体A`：14位 (代表 2^{14} = 16384 种)
4. `关系`：7位 (代表 2^{7} = 128 种)
 
总位数：64位
```

```python
import time

class SnowflakeID:
    def __init__(self):
        # Adjusting the shifts
        self.relation_shift = 57   # 14(A) + 14(B) + 7(relation) + 29(timestamp) = 64
        self.entity_a_shift = 43   # 14(B) + 7(relation) + 29(timestamp) = 50
        self.entity_b_shift = 29   # 7(relation) + 29(timestamp) = 36
        self.timestamp_shift = 0   # Timestamp stays at the least significant position

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