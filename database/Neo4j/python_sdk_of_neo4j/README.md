# python_sdk_of_neo4j

介绍python连接Neo4j的常见操作(以py2neo为例)。<br>
- [python\_sdk\_of\_neo4j](#python_sdk_of_neo4j)
  - [python与Neo4j：](#python与neo4j)
    - [数据格式示例:](#数据格式示例)
    - [py2neo示例代码:](#py2neo示例代码)
    - [f-string插入示例:](#f-string插入示例)
    - [测试python与Neo4j的连接状态：](#测试python与neo4j的连接状态)
    - [创建三元组：](#创建三元组)
    - [获取三元组的值：](#获取三元组的值)
  - [py2neo代码示例:](#py2neo代码示例)
    - [根据某个条件遍历属性:](#根据某个条件遍历属性)

## python与Neo4j：

在 Neo4j Desktop 中输入 Cypher 语句执行查询、插入等操作是我们工作中必须要掌握的本领，但更常见的是我们使用代码与Neo4j连接执行操作，笔者常用的语言为python，这里就介绍python连接Neo4j的常见操作。<br>

笔者惯用 `py2neo` 库连接 Neo4j，安装方法非常简单：<br>

```bash
pip install py2neo
```

### 数据格式示例:

```python
data = {
    "triplet_1": [
        {
            "entity_type": "Person",    # 实体的类型
            "properties": {
                "name": "Jerry",        # 实体的属性
                "age": 30
                }
            },
        {
            "entity_type": "Person",    # 实体的类型
            "properties": {
                "name": "Tom",          # 实体的属性
                "age": 28
                }
            },
        {
            "relationship": "Catch",    # 关系的类型
            "properties": {
                "time": "2024-2-12"     # 关系的属性
                }
            }
        ],
    "triplet_2": [
        {
            "entity_type": "Person",    # 实体的类型
            "properties": {
                "name": "Jerry",        # 实体的属性
                "age": 30
                }
            },
        {
            "entity_type": "Person",    # 实体的类型
            "properties": {
                "name": "Tom",          # 实体的属性
                "age": 28
                }
            },
        {
            "relationship": "Catch",    # 关系的类型
            "properties": {
                "time": "2024-2-12"     # 关系的属性
                }
            }
        ]
    }
```

**字段解释:**<br>

`data`中的每一个元素(`triplet_x`)为一个三元组列表，列表中含有三个字典，分别是实体A、关系、实体B的所有信息。<br>

注意⚠️:<br>

Neo4j允许一个节点有多个节点类型(标签)，例如"成龙"的标签可以是"演员"和"歌手"。<br>

如果一个节点有多个标签，需要将上述格式略微变换。<br>

```python
import json
import os
from py2neo import Graph
from dotenv import load_dotenv
load_dotenv('.env.local')  # 或者使用 load_dotenv() 来加载默认的 '.env' 文件

def connect_to_neo4j():
    """连接neo4j数据库,py2neo自动管理连接池
    """
    graph = Graph('bolt://{0}:{1}'.format(os.getenv('NEO4J_HOST'), os.getenv('NEO4J_PORT')),
                  auth=(os.getenv('NEO4J_USER'), os.getenv('NEO4J_PASS')))
    return graph

def build_set_sentence(pro_origin, pro_data):
    """构造属性设置语句
    Args:
        pro_origin: 属性源头,实体a、实体b或关系,输入值为 "a"、"b"、"r"
        pro_data: 含属性的数据
    Return:
        set_sentece: set语句
    example pro_data:
        pro_data = {'name': 'PUMM', '功能': '通过执行单元划分防止使用后自由内存和双重释放错误', '操作系统': 'Linux', '组成部分': ['离线剖析器（profiler）', '在线执行器（enforcer）'], '优点': '相比于之前的工作，将内存开销减少了52.0%，并平均产生了2.04%的运行时间开销'}
    """
    # 使用列表推导式构建每个属性的赋值字符串，对于列表类型的值，将其元素合并为以逗号间隔的字符串
    # 添加条件以跳过name键值对
    assignments_updated = [
        f"{pro_origin}.{key}='{', '.join(value)}'" if isinstance(value, list) else f"{pro_origin}.{key}='{value}'"
        for key, value in pro_data.items() if key != 'name'
    ]
    if assignments_updated:
        # 使用join方法连接所有的赋值字符串，以", "作为分隔符
        set_sentece = "SET " + ", ".join(assignments_updated)
        return set_sentece
    else:
        return ""


def insert_triplet_to_neo4j(entity_a_info, entity_b_info, relationship_info):
    # 获取neo4j连接
    neo4j_graph = connect_to_neo4j()
    
    entity_a_type = entity_a_info["entity_type"]
    properties_a = entity_a_info["properties"]
    properties_a_name = properties_a["name"]
    set_sentence_a = build_set_sentence("a", properties_a)
    
    entity_b_type = entity_b_info["entity_type"]
    properties_b = entity_b_info["properties"]
    properties_b_name = properties_b["name"]
    set_sentence_b = build_set_sentence("b", properties_b)
    
    relationship = relationship_info["relationship"]
    
    merge_sentence = f"""
    MERGE (a:{entity_a_type} {{name: '{properties_a_name}'}})
    MERGE (b:{entity_b_type} {{name: '{properties_b_name}'}})
    MERGE (a)-[r:{relationship}]->(b)
    """
    # 将SET语句和MERGE语句拼接
    complete_query = merge_sentence + '\n' + set_sentence_a + '\n' + set_sentence_b
    print(complete_query)
    neo4j_graph.run(complete_query)

if __name__ == "__main__":
    data_path = "./example.json"

    with open(data_path, 'r', encoding='utf-8') as file:
        triplet_data = json.load(file)  # <class 'dict'>

    for triplet_each in triplet_data.values():
        entity_a_info = triplet_each[0]
        entity_b_info = triplet_each[1]
        relationship_info = triplet_each[2]
        insert_triplet_to_neo4j(entity_a_info, entity_b_info, relationship_info)
```

### py2neo示例代码:

```python
from config import Neo4J_Server_Config
from py2neo import Graph

class Neo4jManager:
    """以类属性的方式创建Neo4j连接,避免连接耗时
    """
    graph = Graph("bolt://localhost:7687", auth=(Neo4J_Server_Config['user'], Neo4J_Server_Config['password']))
    
    def __init__(self):
        pass

    def run_query(self, query):
        return self.graph.run(query)

# 使用示例
neo4j_manager = Neo4jManager()
result = neo4j_manager.run_query("MATCH (n) RETURN n LIMIT 5")

# 打印查询结果
for record in result:
    print(record)
```

代码优势:<br>

1. **共享连接：** 所有的`Neo4jManager`实例将共享相同的`Graph`连接。这样可以减少多次实例化时连接Neo4j的开销。

2. **延迟初始化：** 在第一次访问类属性`graph`时，连接将被创建。这意味着，如果从不使用`Neo4jManager`，则不会创建不必要的数据库连接。

3. **配置中心化：** 通过从配置文件中导入配置，可以在一个地方管理数据库的连接信息，这使得代码更易于维护。

### f-string插入示例:

```python
from config import Neo4J_Server_Config
from py2neo import Graph
import time

class Create_Neo4j_Semantic_Relation:
    graph = Graph("bolt://localhost:7687", auth=(Neo4J_Server_Config['user'], Neo4J_Server_Config['password']))
    
    def __init__(self):
        pass

    def current_timestamp(self):
        """返回当前日期时间的字符串表示形式,格式为: 2023-08-15 11:29:22 """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def run_query_with_variables(self, entity_a, entity_b, relation, mean_zh, subject_role, object_role):
        current_time = self.current_timestamp()
        query = f"""
        MERGE (a:Entity {{name: '{entity_a}'}})
        MERGE (b:Entity {{name: '{entity_b}'}})
        SET a.last_updated = '{current_time}', b.last_updated = '{current_time}'
        MERGE (a)-[r:SEMANTIC]->(b)
        SET r.relation = '{relation}', r.mean_zh = '{mean_zh}', r.subject_role = '{subject_role}',
            r.object_role = '{object_role}', r.last_updated = '{current_time}'
        """
        self.graph.run(query)

    def query_recent_data(self, days=7):
        """查询过去几天的节点和关系"""
        current_time = time.time()
        past_time = current_time - (days * 24 * 60 * 60)  # 7天的秒数
        date_limit = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(past_time))
        query = f"""
        MATCH (a:Entity)-[r:SEMANTIC]->(b:Entity)
        WHERE a.last_updated >= '{date_limit}' OR b.last_updated >= '{date_limit}' OR r.last_updated >= '{date_limit}'
        RETURN r
        """
        return self.graph.run(query).data()

if __name__ == "__main__":
    neo4j_manager = Create_Neo4j_Semantic_Relation()
    # neo4j_manager.run_query_with_variables('卖出', '圣龙股份', 'Pat', '受事', '受事主体', '受事客体')
    recent_data = neo4j_manager.query_recent_data()
    print(recent_data)
    # start_node的属性
    start_node_name = recent_data[0]['r'].start_node['name']    # 卖出
    start_node_last_updated = recent_data[0]['r'].start_node['last_updated']    # '2023-11-14 10:55:04'
    # 关系的属性
    relation_relation = recent_data[0]['r']['relation'] # Pat
    relation_mean_zh = recent_data[0]['r']['mean_zh']   # 受事
    relation_subject_role = recent_data[0]['r']['subject_role'] # 受事主体
    relation_object_role = recent_data[0]['r']['object_role']   # 受事客体
    relation_last_updated = recent_data[0]['r']['last_updated'] # '2023-11-14 10:55:04'
```

🤨🤨🤨拓展: `self.graph.run(query).data()`为什么要加`data()`?<br>

在 Py2neo 库中，当您执行一个 Cypher 查询（如 `self.graph.run(query)`）时，返回的对象是一个 `Cursor` 实例。这个 `Cursor` 实例代表查询结果的迭代器。要从这个迭代器中获取实际的数据，您需要以某种方式遍历或转换它。这就是 `data()` 方法的用途。<br>

使用 `data()` 方法的原因和优点如下：<br>

1. **直接获取结果**：`data()` 方法将查询结果转换为一个字典列表，每个字典代表查询结果中的一行。这使得结果易于处理和访问，尤其是在需要将数据传递给其他函数或输出到屏幕时。

2. **简化数据处理**：不使用 `data()` 方法，则需要手动遍历 `Cursor` 对象来提取和处理数据。使用 `data()` 可以简化这个过程，特别是当您只对结果数据感兴趣，而不关心其他元数据时。

3. **易于理解和维护**：对于阅读和维护代码的人来说，`data()` 方法明确表示您的意图是提取查询结果的数据部分。

简而言之，`data()` 是一个方便的方法，**用于将 Cypher 查询的结果转换为易于使用的字典列表形式**。这种方法在处理数据库查询结果时非常有用，特别是在需要进一步处理这些数据的场景中。<br>

### 测试python与Neo4j的连接状态：

如果你是访问远程Neo4j数据库，可以按照类似下方代码的方式，修改自己的信息进行测试。如果你开了多个Neo4j数据库，注意端口是否正确。🚀🚀🚀<br>

```python
from py2neo import Graph
try:
    print('----开始尝试连接Neo4j----')
    # 连接到Neo4j数据库
    Graph('neo4j://8.140.203.xxx:7687', auth=("neo4j", "Flameaway3."))
    print('Neo4j连接成功!!!')
except:
    print('Neo4j连接失败')
```

如果你是在部署Neo4j的机器上操作，将 `ip` 改为 `localhost` 即可。<br>

```python
from py2neo import Graph
try:
    print('----开始尝试连接Neo4j----')
    # 连接到Neo4j数据库
    Graph('neo4j://localhost:7687', auth=("neo4j", "Flameaway3."))
    print('Neo4j连接成功!!!')
except:
    print('Neo4j连接失败')
```

### 创建三元组：

`py2neo` 支持很多类似Neo4j中Cypher的操作，比如 `create`、`Node` 等方法，但笔者用的最多的还是 `Graph` 对象和 `run` 方法，`Graph` 对象可以直接接受Cypher语句，然后使用 `run` 方法运行Cypher语句。<br>

`Graph` 对象和 `run` 方法的使用的使用很简单，通过复用之前的代码，这里介绍下具体操作：<br>

```python
from py2neo import Graph

# 连接到Neo4j数据库
graph = Graph('neo4j://localhost:7688', auth=("neo4j", "Giveaway3."))

# 使用MERGE创建或查找节点和关系
cypher_query = """
MERGE (zhangsan:Person {name: '张三'})
MERGE (lisi:Person {name: '李四'})
MERGE (zhangsan)-[:同事]->(lisi)
MERGE (zhangsan)-[:姐夫]->(lisi)
MERGE (zhangsan)-[:领导]->(lisi)
RETURN zhangsan, lisi
"""

result = graph.run(cypher_query)
```

### 获取三元组的值：

获取三元组的值时需要采用 `graph.run().data()` 方法，这样才方便操作～🌿🌿🌿<br>

假设我们构建三元组的代码如下：<br>

```python
from py2neo import Graph

# 连接到Neo4j数据库
graph = Graph('neo4j://localhost:7688', auth=("neo4j", "Giveaway3."))

# 使用MERGE来创建节点和关系信息
cypher_query = """
MERGE (m:Word {name: '卖出'})-[r:Pat {name_zh: '受事', snowflake_id: 7104708589926234047}]->(n:Word {name: '钢琴'})
return m,r,n
"""

result = graph.run(cypher_query)
```

我们如果想要利用 `py2neo` 获取详细的实体和关系信息，可以使用如下代码：<br>

```python
from py2neo import Graph

# 连接到Neo4j数据库
graph = Graph('neo4j://localhost:7688', auth=("neo4j", "Giveaway3."))

# 使用MATCH来查找节点和关系信息
cypher_query = """
MATCH (m:Word {name: '卖出'})-[r:Pat {name_zh: '受事', snowflake_id: 7104708589926234047}]->(n:Word {name: '钢琴'})
RETURN m, n, r
"""

result = graph.run(cypher_query).data()
# print(result)
# [{'m': Node('Word', name='卖出'), 'n': Node('Word', name='货币三佳'), 'r': Pat(Node('Word', name='卖出'), Node('Word', name='货币三佳'), snowflake_id=7104708589926234047)}]

#########################
# m 信息
#########################
node_m_info = result[0]['m']['name']
print(node_m_info)  # 卖出，类型为 str

#########################
# n 信息
#########################
node_n_info = result[0]['n']['name']
print(node_n_info)  # 钢琴，类型为 str

#########################
# relation 信息
#########################
relationship = result[0]['r']
relationship_type = type(relationship).__name__
print(relationship_type)  # Pat，类型为 str

name_zh = relationship['name_zh']
print(name_zh)        # 受事，类型为 str

snowflake_id = relationship['snowflake_id']
print(snowflake_id)        # 7104708589926234047，类型为 int
```


## py2neo代码示例:

```python
from config import Neo4J_Server_Config
from py2neo import Graph

# Cypher语句:创建语义关系并在关系中添加属性
# is_synonym为True表示是同义词，is_synonym为False表示近义词。虽然写的时候是小写"false"，但代码获取后是<class 'bool'>类型。
create_semantic_info = """
MERGE (entity_a:Entity {name: '投资'})
MERGE (entity_b:Entity {name: '盈米'})
MERGE (entity_a)-[rel:semantic_information]->(entity_b)
SET rel.Range = ['WJT-1', 'WJT-14']
SET rel.Exp = ['WJT-51']
SET rel.is_synonym = false
SET rel.snow_id = 288247969436697000
"""

# 获取is_synonym的值
fetch_is_synonym = """
Match (entity_a:Entity {name: '投资'})-[r:semantic_information]->(entity_b:Entity {name: '盈米'})
RETURN r.is_synonym  AS is_synonym
"""

# Cypher语句:删除neo4j中所有数据
delete_all_neo4j_data = "MATCH (m) OPTIONAL MATCH (m)-[r]-() DELETE m, r"

# Cypher语句:根据标准问句id(例如:WJT-1)查询neo4j中semantic_information关系
according_wjt_fetch_data = """
MATCH (a:Entity)-[r:semantic_information]->(b:Entity)
WITH a, b, [attr IN keys(r) WHERE "WJT-1" IN coalesce(r[attr], [])] AS attrs
WHERE size(attrs) > 0
RETURN a.name AS entity_a, b.name AS entity_b, attrs AS attribute_names
"""

def connect_to_neo4j():
    """连接neo4j数据库
    """
    neo4j_host = Neo4J_Server_Config['host']
    neo4j_port = Neo4J_Server_Config['port']
    neo4j_user = Neo4J_Server_Config['user']
    neo4j_password = Neo4J_Server_Config['password']
    return Graph(f'neo4j://{neo4j_host}:{neo4j_port}', auth=(neo4j_user, neo4j_password))

def execute_cypher_sentence(cypher_sentence):
    """执行cypher语句
    Args:
        cypher_sentence:cypher语句。
    """
    # 连接neo4j
    neo4j_conn = connect_to_neo4j()
    # 使用Graph执行cypher语句
    result = neo4j_conn.run(cypher_sentence)
    return result
    
if __name__ == "__main__":
    # 获取is_synonym的值，并查看is_synonym的数据类型
    res = execute_cypher_sentence(fetch_is_synonym)
    for record in res:
        is_synonym = record['is_synonym']
        print("is_synonym:", is_synonym)
        print("is_synonym的数据类型为:", type(is_synonym))
```

终端显示:<br>

```log
is_synonym: False
is_synonym的数据类型为: <class 'bool'>
```

如果你想要获取**节点和关系信息**，请修改`if __name__ == "__main__":`为以下形式:<br>

```python
if __name__ == "__main__":
    res = execute_cypher_sentence(according_wjt_fetch_data)
    for item in res:
        entity_a = item['entity_a']
        entity_b = item['entity_b']
        attribute_names = item['attribute_names']
        print(f"实体A为:{entity_a},实体B为:{entity_b},属性为:{attribute_names}")
```

### 根据某个条件遍历属性:

```sql
MATCH (a:Entity)-[r:semantic_information]->(b:Entity)
WITH a, b, [attr IN keys(r) WHERE "WJT-1" IN coalesce(r[attr], [])] AS attrs
WHERE size(attrs) > 0
RETURN a.name AS entity_a, b.name AS entity_b, attrs AS attribute_names
```
