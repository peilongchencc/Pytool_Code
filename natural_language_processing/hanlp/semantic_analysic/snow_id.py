import time

class SnowflakeID:
    def __init__(self):
        # 基线时间戳：2023年1月1日
        self.baseline_timestamp = int(time.mktime(time.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')))
        self.relation_shift = 57   # 14(A) + 14(B) + 7(relation) + 29(timestamp) = 64
        self.entity_b_shift = 43   # 14(B) + 7(relation) + 29(timestamp) = 50
        self.entity_a_shift = 29   # 7(relation) + 29(timestamp) = 36
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
        curr_timestamp = (int(time.time()) - self.baseline_timestamp) & ((1 << 29) - 1)   # Ensure timestamp is 29 bits
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

        timestamp_in_seconds = self.baseline_timestamp + timestamp
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp_in_seconds))
        return a_name, b_name, question_name, formatted_time