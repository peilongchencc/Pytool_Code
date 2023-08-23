####################################################
# 计算字典型数据中 values 的唯一值数量和不同值出现的次数。
####################################################
data = {
    '美': 'B-LOC',
    '国': 'I-LOC',
    '的': 'O',
    '华': 'B-PER',
    '莱': 'I-PER',
    '士': 'I-PER',
    '我': 'O',
    '跟': 'O',
    '他': 'O'
}

label_counts = {}

for label in data.values():
    if label not in label_counts:
        label_counts[label] = 1
    else:
        label_counts[label] += 1

print("标签种类数量：", len(label_counts))
print("各标签数量：", label_counts)