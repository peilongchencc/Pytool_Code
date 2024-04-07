# python_sdk_of_neo4j

介绍python连接Neo4j的常见操作(以py2neo为例)。<br>
- [python\_sdk\_of\_neo4j](#python_sdk_of_neo4j)
  - [python与Neo4j：](#python与neo4j)
    - [数据格式示例:](#数据格式示例)
  - [py2neo将数据写入neo4j并查询完整示例:](#py2neo将数据写入neo4j并查询完整示例)
    - [example.json:](#examplejson)
    - [将数据写入Neo4j:](#将数据写入neo4j)
    - [py2neo查询、输出示例:](#py2neo查询输出示例)
  - [类属性方式调用neo4j连接:](#类属性方式调用neo4j连接)
  - [f-string插入示例:](#f-string插入示例)
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

## py2neo将数据写入neo4j并查询完整示例:

### example.json:

```json
{
    "triplet_1": [
        {
            "entity_type": "Person",
            "properties": {
                "name": "张三",
                "age": 30
                }
            },
        {
            "entity_type": "Person",
            "properties": {
                "name": "王五",
                "age": 28
                }
            },
        {
            "relationship": "同事",
            "properties": {
                "time": "2024-02-12",
                "friendly_level": "perfect"
                }
            }
        ],
    "triplet_2": [
            {
                "entity_type": "Person",
                "properties": {
                    "name": "张三",
                    "age": 30
                    }
                },
            {
                "entity_type": "Person",
                "properties": {
                    "name": "王五",
                    "age": 28
                    }
                },
            {
                "relationship": "同学",
                "properties": {
                    "start_time": "2015-09-12",
                    "end_time": "2019-06-24"
                    }
                }
            ],
    "triplet_3": [
        {
            "entity_type": "Person",
            "properties": {
                "name": "张三",
                "age": 30
                }
            },
        {
            "entity_type": "Person",
            "properties": {
                "name": "李四",
                "age": 26
                }
            },
        {
            "relationship": "同事",
            "properties": {
                "time": "2023-05-11",
                "friendly_level": "just so so"
                }
            }
        ],
    "triplet_4": [
            {
                "entity_type": "Person",
                "properties": {
                    "name": "赵六",
                    "age": 52
                    }
                },
            {
                "entity_type": "Person",
                "properties": {
                    "name": "张三",
                    "age": 30
                    }
                },
            {
                "relationship": "下属",
                "properties": {
                    "time": "2022-02-11",
                    "friendly_level": "terrible",
                    "often_promises_pie": "always"
                    }
                }
            ]
}
```

### 将数据写入Neo4j:

```python
# insert_data_to_neo4j.py
"""
Author: peilongchencc@163.com
Description: 读取json文件,利用py2neo执行cypher语句,将三元组信息写入neo4j。
Requirements: 
1. pip install py2neo python-dotenv
2. 当前目录下创建 `.env.local` 文件,写入配置项
3. 构建 `example.json` 文件
Reference Link: 
Notes: 
三元组信息包括实体A的实体类型、所有属性,实体B的实体类型、所有属性,关系的关系类型、所有属性。
"""
import json
import os
from py2neo import Graph
from dotenv import load_dotenv
load_dotenv('.env.local')  # 或者使用 load_dotenv() 来加载默认的 '.env' 文件

def connect_to_neo4j():
    """连接neo4j数据库,py2neo自动管理连接池
    """
    neo4j_graph = Graph('bolt://{0}:{1}'.format(os.getenv('NEO4J_HOST'), os.getenv('NEO4J_PORT')),
                  auth=(os.getenv('NEO4J_USER'), os.getenv('NEO4J_PASS')))
    return neo4j_graph

def build_set_sentence(pro_origin, pro_data):
    """构造属性设置语句,关键词为 `set`。
    Args:
        pro_origin(str): 属性源头,实体a、实体b或关系,输入值为 "a"、"b"、"r"
        pro_data(dict): 含属性的数据。
    Return:
        set_sentece: set语句或空字符串。
    Example of pro_data:
        pro_data = {'name': 'PUMM', '功能': '通过执行单元划分防止使用后自由内存和双重释放错误', '操作系统': 'Linux', '组成部分': ['离线剖析器（profiler）', '在线执行器（enforcer）'], '优点': '相比于之前的工作，将内存开销减少了52.0%，并平均产生了2.04%的运行时间开销'}
    Notes:
        `name`属性在上一级 Merge 语句中使用了,当前函数不必重复设置。
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
    """将三元组写入neo4j
    Args:
        entity_a_info(dict):包含实体A的实体类型、所有属性的字典。
        entity_b_info(dict):包含实体B的实体类型、所有属性的字典。
        relationship_info(dict):包含关系的关系类型、所有属性的字典。
    Return:
        写入操作,无返回值。
    """
    # 获取neo4j连接
    neo4j_graph = connect_to_neo4j()
    
    # 从实体A信息字典中提取出所有需要的信息
    entity_a_type = entity_a_info["entity_type"]
    properties_a = entity_a_info["properties"]
    properties_a_name = properties_a["name"]
    # 根据实体A的属性为实体A构建set语句
    set_sentence_a = build_set_sentence("a", properties_a)
    
    # 从实体B信息字典中提取出所有需要的信息
    entity_b_type = entity_b_info["entity_type"]
    properties_b = entity_b_info["properties"]
    properties_b_name = properties_b["name"]
    # 根据实体A的属性为实体A构建set语句
    set_sentence_b = build_set_sentence("b", properties_b)
    
    # 从关系字典中提取出所有需要的信息
    relationship = relationship_info["relationship"]
    properties_r = relationship_info["properties"]
    # 根据关系的属性为关系构建set语句
    set_sentence_r = build_set_sentence("r", properties_r)
    
    # 利用Merge语句进行节点构建,如果节点已经存在,不重复创建。
    merge_sentence = f"""
    MERGE (a:{entity_a_type} {{name: '{properties_a_name}'}})
    MERGE (b:{entity_b_type} {{name: '{properties_b_name}'}})
    MERGE (a)-[r:{relationship}]->(b)
    """
    # 将SET语句和MERGE语句拼接
    complete_query = merge_sentence + '\n' + set_sentence_a + '\n' + set_sentence_b + '\n' + set_sentence_r
    print(complete_query)
    # 执行cypher语句
    neo4j_graph.run(complete_query)

if __name__ == "__main__":
    # 读取json文件为字典
    data_path = "example.json"
    with open(data_path, 'r', encoding='utf-8') as file:
        triplet_data = json.load(file)  # <class 'dict'>
    # 将三元组字典遍历，依次写入neo4j
    for triplet_each in triplet_data.values():
        entity_a_info = triplet_each[0]
        entity_b_info = triplet_each[1]
        relationship_info = triplet_each[2]
        insert_triplet_to_neo4j(entity_a_info, entity_b_info, relationship_info)
```

**neo4j显示如下:**<br>

![](./example_json对应的图片.jpg)

### py2neo查询、输出示例:

```python
# fetch_data_from_neo4j.py
"""
Author: peilongchencc@163.com
Description: py2neo执行cypher查询示例,以关系作为切入点进行介绍。
Requirements: 
1. pip install py2neo python-dotenv
2. 当前目录下创建 `.env.local` 文件,写入配置项
Reference Link: 
Notes: 
1. Neo4j的返回结果中,关系是最特殊的,关系包含三元组的所有信息。即起始节点的实体类型、所有属性,终止节点的实体类型、所有属性,关系的关系类型、所有属性。
2. 如果你的目标场景是返回start_node或end_node,代码中`list(start_node.labels)`、`dict(start_node)`可以为你提供参考。
"""
import os
from py2neo import Graph
from dotenv import load_dotenv
load_dotenv('.env.local')

def connect_to_neo4j():
    """连接neo4j数据库,py2neo自动管理连接池
    """
    neo4j_graph = Graph('bolt://{0}:{1}'.format(os.getenv('NEO4J_HOST'), os.getenv('NEO4J_PORT')),
                  auth=(os.getenv('NEO4J_USER'), os.getenv('NEO4J_PASS')))
    return neo4j_graph

def cypher_run(cypher_query):
    """在neo4j中执行cypher语句。
    Args:
        cypher_query: cypher语句。
    Return:
        query_result: 以列表嵌套字典的形式返回查询结果。例如:`[{'n': Node('Person', name='王五')}]`
    Notes:
        `data()`方法将查询结果转换为一个字典列表,每个字典代表查询结果中的一行,这使得结果易于处理和访问,如果不使用`data()`方法,
        即常规的`neo4j_graph.run(cypher_query)`,需要自己去整合格式,使用`data()`可以简化这个过程。
    """
    neo4j_graph = connect_to_neo4j()
    query_result = neo4j_graph.run(cypher_query).data()
    return query_result

# 编写并执行Cypher查询
cypher_query = """
MATCH (m:Person {name: "张三"})-[r]-(n)
RETURN r
"""

if __name__ == "__main__":
    query_result = cypher_run(cypher_query)
    
    print(f"查询结果为:\n{query_result}\n")
    
    for record in query_result:
        # 起始节点
        start_node = record['r'].start_node
        # `start_node.labels`终端输出看似是字符串,实际为py2neo.data下的类,需要进行list转换,转换为常规数据格式。
        # 以列表第一项元素为例`type(list(node_labels)[0])`,此时结果才为字符串形式。
        start_node_labels = list(start_node.labels)
        # 起始节点的所有属性
        start_node_properties = dict(start_node)
        print(f"起始节点的标签为:{start_node_labels},起始节点的所有属性为:{start_node_properties}")
        
        # 终止节点
        end_node = record['r'].end_node
        end_node_labels = list(end_node.labels)
        # 终止节点的所有属性
        end_node_properties = dict(end_node)
        print(f"终止节点的标签为:{end_node_labels},起始节点的所有属性为:{end_node_properties}")
        
        # 关系的类型
        relationship_type = type(record['r']).__name__  # <class 'str'>
        # 关系的所有属性
        relationship_properties = dict(record['r'])
        print(f"关系的类型为:{relationship_type},关系的所有属性为:{relationship_properties}\n")
```


**终端输出:**<br>

```txt
查询结果为:
[
    {
        "r": 下属(Node("Person", age="52", name="赵六"), Node("Person", age="30", name="张三"), friendly_level="terrible", often_promises_pie="always", time="2022-02-11")
    },
    {
        "r": 同事(Node("Person", age="30", name="张三"), Node("Person", age="26", name="李四"), friendly_level="just so so", time="2023-05-11")
    },
    {
        "r": 同学(Node("Person", age="30", name="张三"), Node("Person", age="28", name="王五"), end_time="2019-06-24", start_time="2015-09-12")
    },
    {
        "r": 同事(Node("Person", age="30", name="张三"), Node("Person", age="28", name="王五"), friendly_level="perfect", time="2024-02-12")
    }
]

起始节点的标签为:['Person'],起始节点的所有属性为:{'name': '赵六', 'age': '52'}
终止节点的标签为:['Person'],起始节点的所有属性为:{'name': '张三', 'age': '30'}
关系的类型为:下属,关系的所有属性为:{'time': '2022-02-11', 'often_promises_pie': 'always', 'friendly_level': 'terrible'}

起始节点的标签为:['Person'],起始节点的所有属性为:{'name': '张三', 'age': '30'}
终止节点的标签为:['Person'],起始节点的所有属性为:{'name': '李四', 'age': '26'}
关系的类型为:同事,关系的所有属性为:{'friendly_level': 'just so so', 'time': '2023-05-11'}

起始节点的标签为:['Person'],起始节点的所有属性为:{'name': '张三', 'age': '30'}
终止节点的标签为:['Person'],起始节点的所有属性为:{'name': '王五', 'age': '28'}
关系的类型为:同学,关系的所有属性为:{'end_time': '2019-06-24', 'start_time': '2015-09-12'}

起始节点的标签为:['Person'],起始节点的所有属性为:{'name': '张三', 'age': '30'}
终止节点的标签为:['Person'],起始节点的所有属性为:{'name': '王五', 'age': '28'}
关系的类型为:同事,关系的所有属性为:{'friendly_level': 'perfect', 'time': '2024-02-12'}
```


## 类属性方式调用neo4j连接:

```python
"""
Author: peilongchencc@163.com
Description: 以python类的方式使用py2neo连接neo4j,并执行常见操作。
Requirements: 
1. pip install py2neo python-dotenv
2. 当前目录下创建 `.env.local` 文件,写入配置项
Reference Link: 
Notes: 
"""
import os
from py2neo import Graph
from dotenv import load_dotenv
load_dotenv('.env.local')  # 或者使用 load_dotenv() 来加载默认的 '.env' 文件

class Neo4jManager:
    """以类属性的方式创建Neo4j连接,避免连接耗时(py2neo自动管理连接池)
    """
    neo4j_graph = Graph('bolt://{0}:{1}'.format(os.getenv('NEO4J_HOST'), os.getenv('NEO4J_PORT')),
                  auth=(os.getenv('NEO4J_USER'), os.getenv('NEO4J_PASS')))
    
    def __init__(self):
        pass

    def run_query(self, cypher_query):
        """执行写入/更新/删除类型的cypher语句
        Args:
            cypher_query(str):cypher语句。
        Return:
            写入/更新/删除操作,无返回值。
        """
        self.neo4j_graph.run(cypher_query)
    
    def run_query_with_data(self, cypher_query):
        """执行查询类型的cypher语句
        Args:
            cypher_query(str):cypher语句。
        Return:
            以列表的形式返回结果,每一项为字典。
        """
        return self.neo4j_graph.run(cypher_query).data()

# 使用示例
neo4j_manager = Neo4jManager()
result = neo4j_manager.run_query_with_data("MATCH (n) RETURN n LIMIT 5")
print(result)
# 打印查询结果
for record in result:
    print(record)
    # 实体类型
    entity_labels = list(record['n'].labels)
    # 实体的所有属性
    entity_properties = dict(record['n'])
    print(f"查询到的节点的标签为:{entity_labels},节点的所有属性为:{entity_properties}\n")
```

**终端输出:**<br>

```txt
[
    {
        "n": Node("Person", age="30", name="张三")
    },
    {
        "n": Node("Person", age="28", name="王五")
    },
    {
        "n": Node("Person", age="26", name="李四")
    },
    {
        "n": Node("Person", age="52", name="赵六")
    }
]
{'n': Node('Person', age='30', name='张三')}
查询到的节点的标签为:['Person'],起始节点的所有属性为:{'name': '张三', 'age': '30'}

{'n': Node('Person', age='28', name='王五')}
查询到的节点的标签为:['Person'],起始节点的所有属性为:{'name': '王五', 'age': '28'}

{'n': Node('Person', age='26', name='李四')}
查询到的节点的标签为:['Person'],起始节点的所有属性为:{'name': '李四', 'age': '26'}

{'n': Node('Person', age='52', name='赵六')}
查询到的节点的标签为:['Person'],起始节点的所有属性为:{'name': '赵六', 'age': '52'}

{'n': Node('Entity', last_updated='2024-04-07 16:46:16', name='卖出')}
查询到的节点的标签为:['Entity'],起始节点的所有属性为:{'name': '卖出', 'last_updated': '2024-04-07 16:46:16'}
```


## f-string插入示例:

```python
"""
Author: peilongchencc@163.com
Description: 利用python中`f-string`的特性,通过传入的变量,利用cypher语句模版进行neo4j数据库中数据的更新。
Requirements: 
1. pip install py2neo python-dotenv
2. 当前目录下创建 `.env.local` 文件,写入配置项
Reference Link: 
Notes: 
根据 `if __name__ == "__main__":` 中的注释执行即可,无需加载外部数据。
"""
import os
import time
from py2neo import Graph
from dotenv import load_dotenv
load_dotenv('.env.local')  # 或者使用 load_dotenv() 来加载默认的 '.env' 文件

class Neo4jManager:
    """以类属性的方式创建Neo4j连接,避免连接耗时(py2neo自动管理连接池)
    """
    neo4j_graph = Graph('bolt://{0}:{1}'.format(os.getenv('NEO4J_HOST'), os.getenv('NEO4J_PORT')),
                  auth=(os.getenv('NEO4J_USER'), os.getenv('NEO4J_PASS')))
    
    def __init__(self):
        pass

    def current_timestamp(self):
        """返回当前日期时间的字符串表示形式,格式为: 2023-08-15 11:29:22 """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def run_query_with_variables(self, entity_a, entity_b, relation, mean_zh, subject_role, object_role):
        """通过传入的变量,利用cypher语句模版进行neo4j数据库中数据的更新。
        Args:
            entity_a(str): 实体A的name属性
            entity_b(str): 实体B的name属性
            relation(str): 关系类型的英文表示
            mean_zh(str): 关系类型的中文表示
            subject_role(str): 实体A在当前三元组中的语法角色
            object_role(str): 实体B在当前三元组中的语法角色
        Return:
            无返回值。
        """
        current_time = self.current_timestamp()
        query = f"""
        MERGE (a:Entity {{name: '{entity_a}'}})
        MERGE (b:Entity {{name: '{entity_b}'}})
        SET a.last_updated = '{current_time}', b.last_updated = '{current_time}'
        MERGE (a)-[r:SEMANTIC]->(b)
        SET r.relation = '{relation}', r.mean_zh = '{mean_zh}', r.subject_role = '{subject_role}',
            r.object_role = '{object_role}', r.last_updated = '{current_time}'
        """
        self.neo4j_graph.run(query)

    def query_recent_data(self, days=7):
        """查询过去几天的节点和关系
        """
        current_time = time.time()
        past_time = current_time - (days * 24 * 60 * 60)  # 7天的秒数
        date_limit = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(past_time))
        query = f"""
        MATCH (a:Entity)-[r:SEMANTIC]->(b:Entity)
        WHERE a.last_updated >= '{date_limit}' OR b.last_updated >= '{date_limit}' OR r.last_updated >= '{date_limit}'
        RETURN r
        """
        return self.neo4j_graph.run(query).data()

if __name__ == "__main__":
    neo4j_manager = Neo4jManager()
    
    # 写入时取消下一行注释
    # neo4j_manager.run_query_with_variables('卖出', '圣龙股份', 'Pat', '受事', '受事主体', '受事客体')
    
    # 写入时将下列内容注释,查询时将上一行注释。
    recent_data = neo4j_manager.query_recent_data()
    print(recent_data)
    
    # 这里就不进行遍历、输出了,只简单调用`index=0`,即 `recent_data[0]` 说明一下效果。
    
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

**终端输出:**<br>

```txt
[
    {
        "r": SEMANTIC(Node("Entity", last_updated="2024-04-07 16:46:16", name="卖出"), Node("Entity", last_updated="2024-04-07 16:46:16", name="圣龙股份"), last_updated="2024-04-07 16:46:16", mean_zh="受事", object_role="受事客体", relation="Pat", subject_role="受事主体")
    }
]
```

🤨🤨🤨拓展: `self.graph.run(query).data()`为什么要加`data()`?<br>

在 Py2neo 库中，当您执行一个 Cypher 查询（如 `self.graph.run(query)`）时，返回的对象是一个 `Cursor` 实例。这个 `Cursor` 实例代表查询结果的迭代器。要从这个迭代器中获取实际的数据，您需要以某种方式遍历或转换它。这就是 `data()` 方法的用途。<br>

使用 `data()` 方法的原因和优点如下：<br>

1. **直接获取结果**：`data()` 方法将查询结果转换为一个字典列表，每个字典代表查询结果中的一行。这使得结果易于处理和访问，尤其是在需要将数据传递给其他函数或输出到屏幕时。

2. **简化数据处理**：不使用 `data()` 方法，则需要手动遍历 `Cursor` 对象来提取和处理数据。使用 `data()` 可以简化这个过程，特别是当您只对结果数据感兴趣，而不关心其他元数据时。

3. **易于理解和维护**：对于阅读和维护代码的人来说，`data()` 方法明确表示您的意图是提取查询结果的数据部分。

简而言之，`data()` 是一个方便的方法，**用于将 Cypher 查询的结果转换为易于使用的字典列表形式**。这种方法在处理数据库查询结果时非常有用，特别是在需要进一步处理这些数据的场景中。<br>


## 根据某个条件遍历属性:

```sql
MATCH (a:Entity)-[r:semantic_information]->(b:Entity)
WITH a, b, [attr IN keys(r) WHERE "WJT-1" IN coalesce(r[attr], [])] AS attrs
WHERE size(attrs) > 0
RETURN a.name AS entity_a, b.name AS entity_b, attrs AS attribute_names
```
