"""
文件解释：利用`特殊词.txt`进行分词，将分词后的基本问句灌入hanlp语义分析模型，根据预设的关系进行语义分析结果的提取。

现将结果存为xlsx文件，便于观察。(后续会直接存入neo4j)

备注：xlsx文件中雪花id显示不正常是excel的原因(默认单元格格式为"常规")，后续需要测试雪花id写入neo4j是否正常。
"""

import hanlp
from openpyxl import Workbook
from snow_id import SnowflakeID

# 构建分词库：
segment_words_file_path = './特殊词.txt'
# 打开文件并读取内容
with open(segment_words_file_path, 'r', encoding='utf-8') as file:
    # 使用set()构建一个空集合
    segment_dict = set()

    # 逐行读取文件并添加到集合中
    for line in file:
        # 使用strip()方法去除每行的换行符和空白字符
        word = line.strip()
        segment_dict.add(word)
    # 现在，segment_dict 包含了文件中的所有唯一单词

# 加载基本问句
standard_question_file_path = './基本问句模板.txt'
# 打开文件并读取内容
with open(standard_question_file_path, 'r', encoding='utf-8') as file:
    # 使用list()构建一个空列表
    standard_question_data = list()

    # 逐行读取文件并添加到列表中
    for line in file:
        # 使用strip()方法去除每行的换行符和空白字符
        word = line.strip()
        standard_question_data.append(word)
    # 现在，standard_question_data 包含了文件中的所有标准问句


def segment(input_list,seg_dict):
    """
    结合hanlp的分词，构建自定义分词函数
    """
    Segment = hanlp.load('CTB9_TOK_ELECTRA_SMALL')
    Segment.dict_force = None
    Segment.dict_combine = seg_dict
    res = Segment(input_list)
    return res

# pipeline组成为：分词、语义依存分析
HanLP = hanlp.pipeline() \
    .append(segment, output_key='tok', seg_dict=segment_dict) \
    .append(hanlp.load('SEMEVAL16_ALL_ELECTRA_SMALL_ZH'), output_key='sdp')

# 加载标准问句
doc = HanLP(standard_question_data)
# 提取出我们需要的语义依存分析结果
# print(doc)
need_data = doc['sdp']

# 需要提取的关系
needed_semantic_relation = {
    "Pat": {"mean_zh": "受事", "subject_role": "受事主体", "object_role": "受事客体"},
    "Exp": {"mean_zh": "当事", "subject_role": "当事主体", "object_role": "当事客体"},
    "Belg": {"mean_zh": "属事", "subject_role": "属事主体", "object_role": "属事客体"},
    "Clas": {"mean_zh": "类事", "subject_role": "类事主体", "object_role": "类事客体"},
    "Cont": {"mean_zh": "客事", "subject_role": "客事主体", "object_role": "客事客体"},
    "Poss": {"mean_zh": "领事", "subject_role": "领事主体", "object_role": "领事客体"},
    "Desc": {"mean_zh": "描写角色", "subject_role": "描写主体", "object_role": "描写客体"},
    "Comp": {"mean_zh": "比较角色", "subject_role": "比较主体", "object_role": "比较客体"},
    "Mann": {"mean_zh": "方式角色", "subject_role": "方式主体", "object_role": "方式客体"},
    "eCoo": {"mean_zh": "并列角色", "subject_role": "并列主体", "object_role": "并列客体"},
    "Quan": {"mean_zh": "数量角色", "subject_role": "数量主体", "object_role": "数量客体"},
    "Qp": {"mean_zh": "数量组合", "subject_role": "数量组合主体", "object_role": "数量组合客体"},
    "Host": {"mean_zh": "宿主角色", "subject_role": "宿主主体", "object_role": "宿主客体"},
    "Time": {"mean_zh": "时间角色", "subject_role": "时间主体", "object_role": "时间客体"},
    "Loc": {"mean_zh": "空间角色", "subject_role": "空间主体", "object_role": "空间客体"},
    "Lini":{"mean_zh": "原处所", "subject_role": "原处所主体", "object_role": "原处所客体"},
    "Lfin":{"mean_zh": "终处所", "subject_role": "终处所主体", "object_role": "终处所客体"},
    "Accd": {"mean_zh": "依据角色", "subject_role": "依据主体", "object_role": "依据客体"},
    "Reas": {"mean_zh": "缘故角色", "subject_role": "缘故主体", "object_role": "缘故客体"},
    "rReas": {"mean_zh": "反缘故角色", "subject_role": "反缘故主体", "object_role": "反缘故客体"},
    "mNeg": {"mean_zh": "否定标记", "subject_role": "否定标记主体", "object_role": "否定标记客体"},
    "Tmod": {"mean_zh": "时间修饰角色", "subject_role": "时间修饰主体", "object_role": "时间修饰客体"},
    "mTime": {"mean_zh": "时间标记", "subject_role": "时间标记主体", "object_role": "时间标记客体"},
    "Freq": {"mean_zh": "频率角色", "subject_role": "频率主体", "object_role": "频率客体"},
    "dExp": {"mean_zh": "嵌套当事", "subject_role": "嵌套当事主体", "object_role": "嵌套当事客体"},
    "dPat": {"mean_zh": "嵌套受事", "subject_role": "嵌套受事主体", "object_role": "嵌套受事客体"},
    "dCont": {"mean_zh": "嵌套客事", "subject_role": "嵌套客事主体", "object_role": "嵌套客事客体"},
    "dClas": {"mean_zh": "嵌套类事", "subject_role": "嵌套类事主体", "object_role": "嵌套类事客体"},
    "dBelg": {"mean_zh": "嵌套属事", "subject_role": "嵌套属事主体", "object_role": "嵌套属事客体"},
    "rPat": {"mean_zh": "反受事", "subject_role": "反受事主体", "object_role": "反受事客体"},
    "rExp": {"mean_zh": "反当事", "subject_role": "反当事主体", "object_role": "反当事客体"},
    "rCont": {"mean_zh": "反客事", "subject_role": "反客事主体", "object_role": "反客事客体"},
    "eSelt": {"mean_zh": "选择关系", "subject_role": "选择关系主体", "object_role": "选择关系客体"},
    "Prod": {"mean_zh": "成事", "subject_role": "成事主体", "object_role": "成事客体"},
    "Cons": {"mean_zh": "结局角色", "subject_role": "结局角色主体", "object_role": "结局角色客体"}
}

# 计数器，用于生成唯一ID
id_counter = 1001

# 遍历字典并为每个元素添加新的字段
for key, value in needed_semantic_relation.items():
    value["subject_role_id"] = id_counter
    id_counter += 1
    value["object_role_id"] = id_counter
    id_counter += 1

"""
修改后字典类似于：
needed_semantic_relation = {
    "Pat": {"mean_zh": "受事", "subject_role": "受事主体", "object_role": "受事客体", "subject_role_id": 1001, "object_role_id": 1002},
    "Exp": {"mean_zh": "当事", "subject_role": "当事主体", "object_role": "当事客体", "subject_role_id": 1003, "object_role_id": 1004},
    "Belg": {"mean_zh": "属事", "subject_role": "属事主体", "object_role": "属事客体", "subject_role_id": 1005, "object_role_id": 1006}
}
"""

# 实例化雪花id类
snowflakeid = SnowflakeID()

semantic_triples = []
# 按句子获取不同输入的分析结果
for idx, element in enumerate(need_data):
    # 按分词获取每个分词与其他分词的关系与关系词索引
    for  i in element:
        entity_b = i.form                 # 当前词的名称
        # 一个分词可能和多个分词组成关系，i.deps的结果为：[(4, 'Pat'), [6, "Agt"]]
        for each_dep in i.deps:
            entity_a_idx = each_dep[0]-1     # 因HanLP序列后的结果从1开始编号，所以需要-1。
            entity_a = element[entity_a_idx].form
            relation = each_dep[1]
            if relation in needed_semantic_relation:
                mean_zh = needed_semantic_relation[relation]["mean_zh"]
                subject_role = needed_semantic_relation[relation]["subject_role"]
                object_role = needed_semantic_relation[relation]["object_role"]
                subject_role_id = needed_semantic_relation[relation]["subject_role_id"]
                object_role_id = needed_semantic_relation[relation]["object_role_id"]
                
                # 将实体A，实体B，关系(英文缩写)存入SnowflakeID()类，当将雪花id解析为文本时会用到。
                snowflakeid.add_mapping(entity_a, entity_b, relation)
                # 根据实体A，实体B，关系(英文缩写)生成雪花id
                snowflake_id = snowflakeid.generate_id(entity_a, entity_b, relation)
                
                # 存入的信息分别为：[原句, 实体A，实体B，关系(英文缩写)，关系(中文)，实体A的角色，实体B的角色，实体A的角色对应的id，实体B的角色对应的id，雪花id]
                triple = [standard_question_data[idx], entity_a, entity_b, relation, mean_zh, subject_role, object_role, subject_role_id, object_role_id, snowflake_id]
                semantic_triples.append(triple)


# 创建一个新的Excel工作簿和工作表
workbook = Workbook()
worksheet = workbook.active # 默认选择第一个工作表

# 修改工作表的名称
worksheet.title = "基本问句_语义分析"

# 添加表头行
header = ["原句", "实体A", "实体B", "关系(英文缩写)", "关系(中文)", "实体A的角色", "实体B的角色", "实体A的角色对应的id", "实体B的角色对应的id", "雪花id"]
worksheet.append(header)

# 将数据写入工作表
for item in semantic_triples:
    worksheet.append(item)

# 待保存的文件路径
result_output_file_path = "基本问句语义_句法分析.xlsx"

# 保存Excel文件
workbook.save(result_output_file_path)

print(f"数据已写入{result_output_file_path}文件")