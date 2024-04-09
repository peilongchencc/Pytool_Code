from transformers import BertTokenizer, AlbertModel
import torch
import numpy as np

class Convert_Text_2_Vector:
    
    tokenizer = BertTokenizer.from_pretrained("clue/albert_chinese_tiny")
    model = AlbertModel.from_pretrained("clue/albert_chinese_tiny")
    
    def __init__(self):
        pass
    def convert_to_vec(self, user_input):
        inputs = self.tokenizer(user_input, return_tensors='pt')
        with torch.no_grad():
                outputs = self.model(**inputs)
        data = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
        data = data / np.linalg.norm(data, axis=0)
        data = [data.tolist()]  # 数据格式为: [[-0.05411861091852188, 0.048285916447639465, -0.029383817687630653, ...]]
        return data