import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer, BertForTokenClassification

# 设定参数
MAX_LEN = 128
BATCH_SIZE = 32
EPOCHS = 3
LEARNING_RATE = 2e-5
MODEL_PATH = "bert-base-chinese"

# 数据路径
train_data_path = "data_cner/train.char.bio.tsv"
test_data_path = "data_cner/test.char.bio.tsv"
# 数据标签列表
labels = ['B-NAME', 'I-NAME', 'O', 'B-CONT', 'I-CONT', 'B-RACE', 'I-RACE', 'B-TITLE', 'I-TITLE', 'B-EDU', 'I-EDU', 'B-ORG', 'I-ORG', 'B-PRO', 'I-PRO', 'B-LOC', 'I-LOC']
NUM_LABELS = len(labels)    # 17

# 数据格式为：
# 常 B-NAME
# 建 I-NAME
# 良 I-NAME
# ， O
# 男 O
# ， O

# 1 O
# 9 O
# 6 O
# 3 O
# 年 O
# 出 O
# 生 O
# ， O
# 工 B-PRO
# 科 I-PRO
# 学 B-EDU
# 士 I-EDU

# 将数据处理为dataloader可接受格式
def process_data_from_txt(filename, has_labels=True):
    processed_data = []
    with open(filename, 'r', encoding='utf-8') as f:
        text = []
        label_list = []
        
        for line in f:
            line = line.strip()
            if line:
                if has_labels:
                    word, label = line.split(' ')
                    label_list.append(labels.index(label))
                else:
                    word, _ = line.split(' ')   # cner数据集对 test 文件也进行了标注，所以此处只使用中文文本，不使用标签。
                text.append(word)
            else:
                if has_labels:
                    processed_data.append({"text": "".join(text), "labels": label_list})
                else:
                    processed_data.append({"text": "".join(text)})  # 不添加标签
                text = []
                label_list = []
        
        if text:
            if has_labels:
                processed_data.append({"text": "".join(text), "labels": label_list})
            else:
                processed_data.append({"text": "".join(text)})
    
    return processed_data

# 加载数据集
class NERDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        text = self.data[index]["text"]
        labels = self.data[index]["labels"]
        
        encoding = tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=MAX_LEN,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )
        
        input_ids = encoding["input_ids"].squeeze()
        attention_mask = encoding["attention_mask"].squeeze()

        # 调整 labels 的长度，labels的长度也要进行填充或截断
        if len(labels) < MAX_LEN:
            labels += [-100] * (MAX_LEN - len(labels))  # padding with -100
        elif len(labels) > MAX_LEN:
            labels = labels[:MAX_LEN]  # truncation

        labels = torch.tensor(labels, dtype=torch.long)

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": labels
        }

# 定义模型
model = BertForTokenClassification.from_pretrained(MODEL_PATH, num_labels=NUM_LABELS)

# 加载分词器
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)

# 定义训练函数
def train(model, dataloader, optimizer):
    model.train()
    total_loss = 0
    for batch in dataloader:
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels = batch["labels"].to(device)
        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        total_loss += loss.item()
        loss.backward()
        optimizer.step()
    avg_loss = total_loss / len(dataloader)
    return avg_loss

# 定义预测函数
def predict(model, dataloader):
    model.eval()
    predictions = []
    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            _, preds = torch.max(logits, dim=2)
            predictions.extend(preds.tolist())
    return predictions

# 将数据转化为Dataloader可接受数据
# 数据格式类似：train_data = [{"text": "我喜欢吃苹果", "labels": [0, 0, 0, 1, 1, 1]}, ...]
processed_train_data = process_data_from_txt(train_data_path, has_labels=True)
processed_test_data = process_data_from_txt(test_data_path, has_labels=False)

# 数据传入dataloader
train_dataset = NERDataset(processed_train_data)
train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)

# 加载测试数据
test_dataset = NERDataset(processed_test_data)
test_dataloader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

optimizer = torch.optim.AdamW(model.parameters(), lr=LEARNING_RATE)

# 训练模型
for epoch in range(EPOCHS):
    train_loss = train(model, train_dataloader, optimizer)
    print(f"Epoch {epoch+1}/{EPOCHS}, Training Loss: {train_loss}")

# 预测
predictions = predict(model, test_dataloader)