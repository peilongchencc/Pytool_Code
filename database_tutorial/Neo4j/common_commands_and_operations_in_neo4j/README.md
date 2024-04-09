# common_commands_and_operations_in_neo4j

本章介绍Neo4j常见命令(终端)与操作。<br>

- [common\_commands\_and\_operations\_in\_neo4j](#common_commands_and_operations_in_neo4j)
  - [终端Neo4j常用指令：](#终端neo4j常用指令)
  - [Neo4j中的创建操作：](#neo4j中的创建操作)
    - [CREATE创建有向关系示例：](#create创建有向关系示例)
    - [CREATE创建中文三元组：](#create创建中文三元组)
    - [MERGE创建三元组：](#merge创建三元组)
    - [CREATE的必要性：](#create的必要性)
    - [为2个节点创建多个关系：](#为2个节点创建多个关系)
    - [更新Neo4j中实体间的关系：](#更新neo4j中实体间的关系)
    - [实体间创建相同名称的关系(关系含有的属性不同)：](#实体间创建相同名称的关系关系含有的属性不同)
  - [Neo4j中的查询操作：](#neo4j中的查询操作)
    - [查询创建的节点和关系：](#查询创建的节点和关系)
    - [拓展--不指定实体类型查看节点:](#拓展--不指定实体类型查看节点)
    - [查看节点--限制返回25条数据：](#查看节点--限制返回25条数据)
    - [查看所有节点和关系：](#查看所有节点和关系)
    - [查看所有节点：](#查看所有节点)
    - [查看所有关系：](#查看所有关系)
    - [查看某种关系的所有节点：](#查看某种关系的所有节点)
    - [根据关系查看节点的指向：](#根据关系查看节点的指向)
    - [将查询节点按照某个属性排序：](#将查询节点按照某个属性排序)
    - [查询Neo4j中是否有某种关系类型：](#查询neo4j中是否有某种关系类型)
    - [精确查找和模糊查找：](#精确查找和模糊查找)
    - [根据关系查询并返回多层节点：](#根据关系查询并返回多层节点)
  - [Neo4j属性的数据格式：](#neo4j属性的数据格式)
    - [正确写法示例1:](#正确写法示例1)
    - [正确写法示例2:](#正确写法示例2)
    - [错误示例1:](#错误示例1)
    - [错误写法示例2:](#错误写法示例2)
  - [Neo4j中的设置/更新操作：](#neo4j中的设置更新操作)
    - [更新Neo4j中实体的属性的值：](#更新neo4j中实体的属性的值)
    - [为实体添加新的属性：](#为实体添加新的属性)
    - [更新Neo4j中实体的属性的名称：](#更新neo4j中实体的属性的名称)
    - [更新Neo4j中实体的类型：](#更新neo4j中实体的类型)
    - [为节点和关系添加多个属性：](#为节点和关系添加多个属性)
  - [Neo4j中的删除操作：](#neo4j中的删除操作)
    - [删除某种类型的实体和其关系:](#删除某种类型的实体和其关系)
    - [删除指定关系：](#删除指定关系)
    - [删除Neo4j中所有节点和关系：](#删除neo4j中所有节点和关系)

## 终端Neo4j常用指令：

启动Neo4j数据库作为后台服务:<br>

```bash
neo4j start
```

以后台方式启动：<br>

```bash
nohup sudo neo4j start &
```

停止Neo4j数据库服务:<br>

```bash
neo4j stop
```

重新启动Neo4j数据库服务:<br>

```bash
neo4j restart
```

检查Neo4j数据库服务的状态:<br>

```bash
neo4j status
```

显示Neo4j的版本信息:<br>

```bash
neo4j version
```

以控制台模式查看 Neo4j 数据库基本信息:<br>

```bash
neo4j console 
```

## Neo4j中的创建操作：

在Neo4j中，关系是有向的‼️‼️‼️。这意味着当你创建一个关系时，你必须指定它的方向🥶🥶🥶。然而，当查询这些关系时，你可以选择忽略方向🥴🥴🥴。<br>

### CREATE创建有向关系示例：

假设你想创建一个描述 `汤姆抓杰瑞` 的三元组信息，你可以使用以下指令：<br>

```sql
// Neo4j支持以 "//" 作为注释
CREATE (m:Leading_role {name: 'Tom'})-[r:catch]->(n:supporting_role {name: 'Jerry'})
RETURN m,r,n
```

> 注意变量名不能以空格为间隔，`Leading role` 会报错，需要使用 `Leading_role` 或 `LeadingRole` 形式。

这里详细解释下上述语句：<br>

`CREATE`: 这是一个Cypher命令，用于创建节点或关系。<br>
`(m:Leading_role {name: 'Tom'})`: <br>
- 此处创建了一个名为`Tom`的`Leading_role`类型节点。<br>
- `(m)`表示节点的变量名或引用🔥🔥🔥，这样在后面的查询中你可以使用这个变量名引用该节点。<br>
- `:Leading_role` 表示节点的标签，标签通常用来表示**节点的类型或类别**。🌿🌿🌿<br>
- `{name: 'Tom'}` 是节点的属性，这里定义了一个名为`name`的属性，其值为`Tom`。<br>

`-[r:catch]->`: <br>
- 此处创建了一个从`Tom`节点到`Jerry`节点的关系。<br>
- `-[]->` 是一个关系的模式，其中`-`表示开始节点，`->`表示关系的方向，指向结束节点。<br>
- `[r:catch]` 中，`r`是关系的变量名🔥🔥🔥，`:catch`是关系的类型。<br>

`(n:supporting_role {name: 'Jerry'})`: <br>
- 此处创建了一个名为`Jerry`的`supporting_role`类型节点。<br>
- `(n)`表示节点的变量名。<br>
- `:supporting_role` 是节点的标签。<br>
- `{name: 'Jerry'}` 是节点的属性。<br>

`RETURN m,r,n`:<br>
- 在执行完上述创建操作后，返回创建的节点`m`和`n`以及关系`r`作为结果。<br>

所以，这条Cypher语句的大致意思是：“创建一个名为`Tom`的`Leading_role`类型节点，一个名为`Jerry`的`supporting_role`类型节点，并在它们之间创建一个类型为`catch`的关系，之后返回创建的实体与关系。”<br>
<br>

Neo4j中效果如下：<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/e78e22cd-fe02-4115-a0ba-df5529bbf9a2" alt="image" width="30%" height="30%">

🚀🚀🚀节点颜色、节点大小、关系颜色、对外显示的属性都可以通过点击对应图标设置：<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/45fb1c3d-8e82-4cb8-8c2f-80f267787e7f" alt="image" width="50%" height="50%">


### CREATE创建中文三元组：

Neo4j中的关系类型、节点标签以及属性的键和值都支持中文字符。你可以使用中文字符来定义关系类型或属性名称:<br>

```sql
CREATE (m:Person {name: '张三'})-[r:知道]->(n:Person {name: '李四'})
RETURN m,r,n
```

Neo4j中效果如下：<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/ec50592e-1b2a-4e6c-ba9b-a596ab00dce2" alt="image" width="30%" height="30%">

### MERGE创建三元组：

`CREATE` 和 `MERGE` 都是用于在Neo4j中创建数据的命令，`CREATE` 更关注于直接创建，`MERGE` 更关注于检查Neo4j中是否有重复数据。<br>
举例来说，当你依次运行下面两个语句时，会在Neo4j中创建2个名为 `张三` 的节点，而不是关联了2组关系。<br>

```sql
// 语句1
CREATE (m:Person {name: '张三'})-[r:知道]->(n:Person {name: '李四'})
RETURN m,r,n
```

```sql
// 语句2
CREATE (m:Person {name: '张三'})-[r:知道]->(n:Person {name: '王五'})
RETURN m,r,n
```

Neo4j效果：<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/db837467-b0cd-4d20-8511-863641efa6a1" alt="image" width="30%" height="30%">


如果你想将2组关系关联起来，需要使用关键字 `MERGE` ：<br>

```sql
// 首先检查张三的节点是否存在，如果不存在，会创建一个名为张三的节点
MERGE (m:Person {name: '张三'})

// 然后检查张三与李四之间的知道关系是否存在，如果不存在，会创建张三与李四之间的知道关系
MERGE (m)-[r1:知道]->(n1:Person {name: '李四'})

// 最后检查张三与王五之间的知道关系是否存在，如果不存在，会创建张三与王五之间的知道关系
MERGE (m)-[r2:知道]->(n2:Person {name: '王五'})

RETURN m, r1, n1, r2, n2
```

Neo4j效果：<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/742ff813-972f-4e18-b277-460ae5a4be56" alt="image" width="30%" height="30%">


‼️‼️‼️注意：`MERGE` 的使用一定要正确，必须按照上述语句中的逻辑。举个例子，假设你依次运行了下面2个语句，猜猜会发生什么~🥴🥴🥴<br>

```sql
// 语句1
MERGE (m:Person {name: '张三'})-[r:知道]->(n:Person {name: '李四'})
RETURN m,r,n
```

```sql
// 语句2
MERGE (m:Person {name: '张三'})-[r:知道]->(n:Person {name: '王五'})
RETURN m,r,n
```

Bingo! 答案是和使用 `CREATE` 效果相同，会在Neo4j中创建2个张三节点，而不是关联了2组关系。🥹🥹🥹<br>

Neo4j效果：<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/db837467-b0cd-4d20-8511-863641efa6a1" alt="image" width="30%" height="30%">


### CREATE的必要性：

讲了 `MERGE` 后，可能有人会想: 既然 `MERGE` 这么好用，为什么还要有 `CREATE` 呢❓❓❓ 这里就需要讲一下使用 `CREATE` 的一些必要性和场景了：<br>

**明确性**：当你知道要创建的节点或关系绝对不在数据库中时，使用 `CREATE` 可以明确地表示这一点。这在语义上为读代码的人提供了清晰性。<br>
**性能**：在某些情况下，`CREATE` 可能比 `MERGE` 更快，因为它不需要先检查节点或关系是否已存在。<br>
**数据导入**：当从没有重复数据的来源导入数据时，使用 `CREATE` 是有意义的。<br>
**临时或测试数据**：当需要插入临时或测试数据并且不担心数据重复时，`CREATE` 是一个好选择。<br>
**特定的模型设计**：在某些图形模型设计中，可能需要允许具有相同属性的多个节点存在。在这种情况下，`CREATE` 可以确保总是创建一个新节点，而不是复用现有节点。<br>

总的来说，尽管 `MERGE` 提供了确保数据唯一性的功能，但 `CREATE` 仍然在很多场景下是有必要的。选择使用哪一个取决于你的具体需求和上下文。<br>

### 为2个节点创建多个关系：

工作中，你可能会遇到需要为2个节点创建多个关系的情况，例如张三和李四既是同事，张三又是李四的姐夫，张三还是李四的领导。下面介绍一下这种创建方式：<br>

```sql
// 首先确保张三和李四的节点存在
MERGE (zhangsan:Person {name: '张三'})
MERGE (lisi:Person {name: '李四'})

// 创建“同事”关系
MERGE (zhangsan)-[:同事]->(lisi)

// 创建“姐夫”关系
MERGE (zhangsan)-[:姐夫]->(lisi)

// 创建“领导”关系
MERGE (zhangsan)-[:领导]->(lisi)

RETURN zhangsan, lisi
```

Neo4j效果：<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/26e4c2f1-f5eb-4ec5-b66c-d3a55cf70ffe" alt="image" width="30%" height="30%">

你可能注意到了，我这里使用的变量名为 `zhangsan`、`lisi`，不是前面经常使用的 `m,n,r`，这是因为在Cypher中，变量名的选择完全取决于开发者的个人习惯和上下文。🤣🤣🤣<br>

为了避免遗忘，这里我们再回顾一下查询，假设你要查询含有 `领导` 关系的所有节点，你只需要输入以下语句即可：<br>

```sql
MATCH (m)-[r:领导]->(n)
RETURN m,n,r
```

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/cc3083d9-4c93-4924-8695-4b440c7bce6b" alt="image" width="40%" height="40%">

别被 `Graph` 吓到了，从 `Text` 选项我们可以看到，返回的内容是正确的～🌿🌿🌿🤭🤭🤭<br>

### 更新Neo4j中实体间的关系：

假如现在张三和李四的姐姐离婚了，你要将张三和李四的 `姐夫` 关系改为 `前姐夫`，运行下列语句即可：<br>

```sql
MATCH (zhangsan:Person {name: '张三'})-[rel:姐夫]->(lisi:Person {name: '李四'})
DELETE rel
CREATE (zhangsan)-[:前姐夫]->(lisi)
```

‼️‼️注意，Neo4j不支持直接重命名关系类型，所以这里的方法是删除旧的关系并创建一个新的关系。<br>

<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/4e9f6183-a2bc-4f2d-9e37-a238c021cbba" alt="image" width="30%" height="30%">


### 实体间创建相同名称的关系(关系含有的属性不同)： 

```sql
// 以检查重复的方式创建两个节点
MERGE (a:Entity {name: '卖出'})
MERGE (b:Entity {name: '圣龙股份'})
// 在这两个节点之间创建第一个SEMANTIC关系
MERGE (a)-[:SEMANTIC {relation: 'Pat', mean_zh: '受事', subject_role: '谓语', object_role: '受事'}]->(b)
// 创建第二个FRIEND关系，具有不同的属性
MERGE (a)-[:SEMANTIC {relation: 'Exp', mean_zh: '当事', subject_role: '谓语', object_role: '当事'}]->(b);
```

要在Neo4j中修改已经存在的关系的属性，你可以使用 `MATCH` 语句来定位特定的关系，然后使用 `SET` 语句来更新这个关系的属性。根据你的需求，假设你想修改第一个 `SEMANTIC` 关系的属性，你可以这样做：<br>

1. **使用 `MATCH` 定位关系**：首先，你需要使用 `MATCH` 语句和一个模式来找到你想要修改的特定关系。在你的例子中，这个模式可能是 `(a:Entity {name: '卖出'})-[r:SEMANTIC]->(b:Entity {name: '圣龙股份'})`，其中 `r` 是关系的引用。

2. **指定要修改的关系**：由于存在两个 `SEMANTIC` 关系，你需要指定要修改的关系。这可以通过关系的特定属性来实现，比如 `relation`。

3. **使用 `SET` 更新属性**：一旦找到正确的关系，你可以使用 `SET` 语句来更新其属性。

例如，如果你想修改 `relation` 属性为 `Pat` 的关系，使其 `mean_zh` 属性变为 `'新受事'`，你可以这样写：<br>

```sql
MATCH (a:Entity {name: '卖出'})-[r:SEMANTIC]->(b:Entity {name: '圣龙股份'})
WHERE r.relation = 'Pat'
SET r.mean_zh = '新受事'
```

这个语句会找到从 `'卖出'` 实体到 `'圣龙股份'` 实体的 `SEMANTIC` 关系，其中 `relation` 属性为 `'Pat'`，然后将这个关系的 `mean_zh` 属性设置为 `'新受事'`。<br>


## Neo4j中的查询操作：

### 查询创建的节点和关系：

虽然物理存储的关系是有向的，但你可以通过查询时的方式来看待它们为无向关系。查询时可以选择忽略关系方向，视为无向关系：<br>

```sql
MATCH (m:Leading_role {name: 'Tom'})-[r:catch]-(n:supporting_role {name: 'Jerry'})
RETURN m,r,n
```

当然，你也可以把方向带上：<br>

```sql
MATCH (m:Leading_role {name: 'Tom'})-[r:catch]->(n:supporting_role {name: 'Jerry'})
RETURN m,r,n
```

总之，虽然在创建时必须指定关系的方向，但在查询时你可以选择视其为无向关系。<br>

### 拓展--不指定实体类型查看节点:

从neo4j检索数据时，可以不指定实体类型，只使用实体的 `name` 属性，例如:<br>

```sql
MATCH (n)
WHERE n.name = '指定的名字'
RETURN n
```

### 查看节点--限制返回25条数据：

从Neo4j数据库中匹配所有的节点`n`、关系`r`和节点`m`的组合，并返回这些结果，但限制返回的记录数为25。<br>

> 默认情况下，当你不指定排序或其他筛选条件时，Neo4j可能会基于内部存储和处理的顺序返回结果🌿🌿🌿，这可能会看起来像是随机的，尤其是在大型数据集中。

```sql
MATCH (n)-[r]->(m) RETURN n, r, m LIMIT 25
```

### 查看所有节点和关系：

如果你想要查看Neo4j中所有节点和关系，可以使用：<br>

```sql
MATCH (n)-[r]->(m) RETURN n, r, m
```

### 查看所有节点：

如果你只想要查看所有节点，可以使用：<br>

```sql
MATCH (n) RETURN n
```

### 查看所有关系：

如果你只是想要查看所有关系，可以使用：<br>

```sql
MATCH ()-[r]->() RETURN r
```

### 查看某种关系的所有节点：

如果你想要查看含有 `catch` 关系的所有节点，可以使用：

```sql
MATCH (m)-[r:catch]->(n)
RETURN m,n,r
```

### 根据关系查看节点的指向：

如果你想要根据关系查看节点的指向，可以参考以下代码：<br>

节点、关系创建语句:<br>

```sql
// 首先确保张三和李四的节点存在
MERGE (zhangsan:Person {name: '张三'})
MERGE (lisi:Person {name: '李四'})
MERGE (wangwu:Person {name: '王五'})

// 创建“同事”关系
MERGE (zhangsan)-[:同事]->(lisi)

// 创建“姐夫”关系
MERGE (zhangsan)-[:姐夫]->(lisi)

// 创建“领导”关系
MERGE (lisi)-[:领导]->(zhangsan)

// 创建“同事”关系
MERGE (wangwu)-[:同事]->(lisi)
```

Neo4j中效果：<br>

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/9d17e6e0-5969-4d84-82bf-4513ec328fce)

python代码：<br>

```python
from py2neo import Graph

# 连接到Neo4j数据库
graph = Graph('neo4j://localhost:7687', auth=("neo4j", "Flameaway3."))

# 使用MATCH来查找节点和关系信息
cypher_query = """
MATCH (m:Person {name: '李四'})-[r]-(n)
RETURN r
"""

result = graph.run(cypher_query).data()

for item in result:
    relation = item['r']
    print(f"节点指向为:{relation}，关系的数据类型为:{type(relation)}。")
    node_a = relation.start_node['name']
    node_b = relation.end_node['name']
    relationship_type = type(relation).__name__
    print(f"起始节点为:{node_a},终止节点为:{node_b},关系类型为:{relationship_type}")
```

终端效果：<br>

```log
节点指向为:(李四)-[:领导 {}]->(张三)，关系的数据类型为:<class 'py2neo.data.领导'>。
起始节点为:李四,终止节点为:张三,关系类型为:领导
节点指向为:(张三)-[:姐夫 {}]->(李四)，关系的数据类型为:<class 'py2neo.data.姐夫'>。
起始节点为:张三,终止节点为:李四,关系类型为:姐夫
节点指向为:(张三)-[:同事 {}]->(李四)，关系的数据类型为:<class 'py2neo.data.同事'>。
起始节点为:张三,终止节点为:李四,关系类型为:同事
节点指向为:(王五)-[:同事 {}]->(李四)，关系的数据类型为:<class 'py2neo.data.同事'>。
起始节点为:王五,终止节点为:李四,关系类型为:同事
```

### 将查询节点按照某个属性排序：

如果你想按节点`n`的`name`属性排序，你可以这样写：<br>

```sql
MATCH (n)-[r]->(m)
RETURN n, r, m
ORDER BY n.name
LIMIT 25
```

### 查询Neo4j中是否有某种关系类型：

假设你想要查询Neo4j中是否有关系`SEMANTIC_RECOGNITION`存在，可以使用如下代码：<br>

```sql
OPTIONAL MATCH (startNode)-[r:SEMANTIC_RECOGNITION]->(endNode)
WITH r
RETURN r IS NOT NULL AS relationshipExists
```

这个Cypher查询是用于在Neo4j图数据库中检查是否存在某种关系的存在，并返回一个布尔值来指示这种关系是否存在。让我逐步解释这个Cypher查询：<br>

1. `OPTIONAL MATCH (startNode)-[r:SEMANTIC_RECOGNITION]->(endNode)`:

- `OPTIONAL MATCH` 是Cypher中的关键字，用于匹配模式，但不会中断查询，**即使模式没有匹配项也会继续执行查询**。这里，它用于匹配以`startNode`为起始节点、以`endNode`为结束节点，且关系类型为`SEMANTIC_RECOGNITION`的关系。如果没有匹配的关系，`r`将会是null。

2. `WITH r`:

- `WITH` 子句用于将之前匹配到的关系`r`传递到后续的操作。这里它只是将关系`r`传递到下一步的操作。

3. `RETURN r IS NOT NULL AS relationshipExists`:

- `RETURN` 子句用于返回查询的结果。

- `r IS NOT NULL` 是一个条件表达式，它检查关系`r`是否不为空（即存在）。如果`r`不为空，这个条件将返回true，否则返回false。

- `AS relationshipExists` 是为查询结果创建了一个别名，将其命名为`relationshipExists`，这个别名是一个布尔值，表示关系是否存在。

❤️❤️❤️**没有明确指定节点的类型，因此查询将匹配任何类型的节点。**最终的查询结果将包含一个名为`relationshipExists`的布尔值，它指示了是否存在起始节点和结束节点之间的`SEMANTIC_RECOGNITION`关系。如果关系存在，则`relationshipExists`为true；如果关系不存在，则`relationshipExists`为false。<br>

这个查询非常适用于在图数据库中检查某种关系是否存在的情况。<br>

### 精确查找和模糊查找：

讲精确查找和模糊查找前，首先要明确一个关键点：Neo4j 中查找时遵循的是匹配节点标签(类型)和属性，要查找到你想要寻找的节点，知道其一才能快速匹配。如果这2者你都不知道，那就需要进行模糊匹配查找了。<br>

然而，这种查询可能会在大型数据库中变得很慢，因为它需要遍历所有节点和属性。这只是一种尝试，如果可能的话，还是建议在设计数据库时为节点名称使用明确的属性或给所有节点配一个统一的属性，例如 `name`，以便更有效地进行查询。🚨🚨🚨<br>

举个例子，假设其他人根据下列语句创建了一个三元组信息。<br>

```sql
// 创建节点信息
CREATE (m:Charactor {name:'Tom'})-[r:catch]->(n:Charactor {name:'Jerry'}) RETURN m,n,r
```

现在你只知道节点的`name`属性为 `Tom`，你想知道这个节点的更多信息，可以根据需要执行以下代码：<br>

返回匹配到的节点的所有信息：<br>
```sql
MATCH (n) WHERE n.name = 'Tom' RETURN n;
```
返回匹配到的节点的标签(类型)信息：<br>
```sql
MATCH (n) WHERE n.name = 'Tom' RETURN labels(n);
```
<br>

假设你同时知道节点的`name`属性为 `Tom`，关系为 `catch`，你想知道这个节点的更多信息，可以根据需要执行以下代码：<br>
```sql
MATCH (n {name: 'Tom'})-[r:catch]->()
RETURN n, r
```
如果你想获取特定属性的值，比如假设节点`Tom`还有一个`age`属性，你可以这样查询：<br>
```sql
MATCH (n {name: 'Tom'})-[r:catch]->()
RETURN n.name, n.age, r
```

如果你想获取节点的所有属性，可以使用以下查询：<br>
```sql
MATCH (n {name: 'Tom'})-[r:catch]->()
RETURN n, r, keys(n) as node_properties
```

### 根据关系查询并返回多层节点：

假设你在Neo4j中创建节点的语句如下：<br>

```sql
// 检查重复并创建节点
MERGE (A:Node {name: 'A'})
MERGE (B:Node {name: 'B'})
MERGE (C:Node {name: 'C'})
MERGE (D:Node {name: 'D'})
MERGE (E:Node {name: 'E'})
MERGE (F:Node {name: 'F'})
MERGE (G:Node {name: 'G'})
MERGE (H:Node {name: 'H'})
MERGE (J:Node {name: 'J'})
MERGE (K:Node {name: 'K'})
MERGE (I:Node {name: 'I'})
MERGE (L:Node {name: 'L'})

// 创建关系
MERGE (A)-[:同义词]->(B)
MERGE (A)-[:同义词]->(C)
MERGE (A)-[:同义词]->(D)

MERGE (B)-[:同义词]->(E)
MERGE (B)-[:同义词]->(F)

MERGE (C)-[:同义词]->(G)
MERGE (C)-[:同义词]->(H)

MERGE (D)-[:同义词]->(J)

MERGE (E)-[:同义词]->(I)
MERGE (E)-[:同义词]->(L)

MERGE (H)-[:同义词]->(K)
```

Neo4j中显示效果如下：<br>

![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/4a4f71c9-845e-4938-b1e2-592e4fba53e4)

此时，你想要查询节点A的同义词的同义词，限定查询深度为2层，可以使用以下语句：<br>

```sql
MATCH (a {name: 'A'})-[:同义词*1..2]->(synonym)
RETURN DISTINCT synonym.name
```

这个语句是用于查询一个图数据库中的数据，通常使用Cypher查询语言，用于与Neo4j等图数据库交互。下面是对这个Cypher查询语句的详细解释：

1. `MATCH (a {name: 'A'})`: 这是一个MATCH子句，用于匹配图数据库中的节点。它指定了一个变量a，该节点具有一个名为'name'且值为'A'的属性。这意味着我们正在查找所有具有这个属性的节点，其中'name'属性等于'A'的节点。

2. `-[:同义词*1..2]->`: 这是一个关系模式，`[:SYNONYM*1..2]`表示查询关系`SYNONYM`的1到2次，也就是向下查询两层。

3. `(synonym)`: 这是一个变量，用于表示与节点a连接的同义词节点。它将在查询中用于引用这些节点。

4. `RETURN DISTINCT synonym.name`: 这是一个RETURN子句，用于指定我们要从匹配的节点中返回的属性。在这里，我们想要返回同义词节点的'name'属性，并使用DISTINCT关键字确保返回的结果是唯一的，避免重复。

综合起来，这个Cypher查询的作用是查找与名为'A'的节点通过"同义词"关系连接的所有同义词节点，并返回这些同义词节点的名称属性。如果有多个路径连接到同一个同义词节点，由于使用了DISTINCT关键字，结果集将包含每个同义词节点的唯一名称。这种查询可用于查找具有类似含义的节点或词汇的网络。<br>

✅✅✅在py2neo中，你可以这样使用：<br>

```python
from py2neo import Graph, Node, Relationship

graph = Graph("bolt://localhost:7687", auth=("neo4j", "your_password"))

query = """
MATCH (a {name: 'A'})-[:SYNONYM*1..2]->(synonym)
RETURN DISTINCT synonym.name
"""

results = graph.run(query)
synonyms = [record["synonym.name"] for record in results]

print(synonyms)
```

这将返回A的所有同义词，包括它的直接同义词以及这些同义词的同义词。如果你只想要查询特定层级的同义词，可以相应地调整`*1..2`中的数字。<br>

## Neo4j属性的数据格式：

Neo4j是一个图数据库，其中节点和关系可以有属性。这些属性可以是各种数据类型。以下是Neo4j支持的基本数据类型：<br>

1. **数值**:

类型|解释
---|---
整数 | int
浮点数 | float

2. **字符串** (`string`)

3. **布尔值** (`boolean`)

4. **列表**：这些列表可以是以上提到的任何基本数据类型的列表。例如你可以有一个整数列表或字符串列表。

5. **时间和日期相关类型**：

类型|解释
---|---
Date | 日期
Time | 时间
LocalTime | 本地时间
DateTime | 日期时间
LocalDateTime | 本地日期时间
Duration | 持续时间

6. **空值** (`null`)

但是，要注意的是，**Neo4j不直接支持像"字典"或"映射"这样的复杂数据结构作为属性值**🚨🚨🚨。<br>

⚠️⚠️⚠️不过，如果你需要存储这样的数据，可以考虑将其序列化为字符串格式（例如JSON字符串），然后存储为字符串属性。但这样做的话，你将失去对那些内部键值对的直接查询能力❌❌❌。<br>

### 正确写法示例1:

```sql
MERGE (entity_a:Entity {name: '买'})
MERGE (entity_b:Entity {name: '基金'})
MERGE (entity_a)-[rel:semantic_information]->(entity_b)
SET rel.Pat = ['WJT-12', 'WJT-14']
SET rel.Exp = ['WJT-5', 'WJT-104']
```

### 正确写法示例2:

```sql
MERGE (entity_a:Entity {name: '买'})
MERGE (entity_b:Entity {name: '基金'})
MERGE (entity_a)-[rel:semantic_information]->(entity_b)
SET rel.semantic_relation = "{'Pat': ['WJT-12', 'WJT-14'], 'Exp': ['WJT-5', 'WJT-104']}"
```

⛔️⛔️⛔️如果你采用这种写法，semantic_relation属性对应的内容为字符串格式。<br>

### 错误示例1:

```sql
MERGE (entity_a:Entity {name: '买'})
MERGE (entity_b:Entity {name: '基金'})
MERGE (entity_a)-[rel:semantic_information]->(entity_b)
SET rel.semantic_relation = {'Pat': ['WJT-12', 'WJT-14'], 'Exp': ['WJT-5', 'WJT-104']}
```
运行错误示例的代码后，会显示以下错误提示:<br>

```log
ERROR Neo.ClientError.Statement.SyntaxError
Invalid input ''': expected whitespace, an identifier, UnsignedDecimalInteger, a property key name or '}' (line 4, column 30 (offset: 158))
"SET rel.semantic_relation = {'Pat': ['WJT-12', 'WJT-14'], 'Exp': ['WJT-5', 'WJT-104']}
                              ^
```

### 错误写法示例2:

```sql
MERGE (entity_a:Entity {name: '买'})
MERGE (entity_b:Entity {name: '基金'})
MERGE (entity_a)-[rel:semantic_information]->(entity_b)
SET rel.semantic_relation = [
  {'Pat': ['WJT-12', 'WJT-14'], 'Exp': ['WJT-5', 'WJT-104']}
]
```

运行错误示例的代码后，会显示以下错误提示:<br>

```log
ERROR Neo.ClientError.Statement.SyntaxError
Invalid input ''': expected whitespace, an identifier, UnsignedDecimalInteger, a property key name or '}' (line 5, column 4 (offset: 162))
"  {'Pat': ['WJT-12', 'WJT-14'], 'Exp': ['WJT-5', 'WJT-104']}"
    ^
```



## Neo4j中的设置/更新操作：

### 更新Neo4j中实体的属性的值：
假设现在李四觉得自己的名字不好听，改名了，改成了 `李斯`，你可以运行下列语句更新数据：<br>
```sql
MATCH (lisi:Person {name: '李四'})
SET lisi.name = '李斯'
RETURN lisi
```
‼️‼️注意，更改属性时需要点击实体或知道创建语句，知道 `实体名称` 对应的属性名称。例如 `李四` 是实体类型为 `Person` 的 `name` 属性。<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/d3e7d7d7-87ee-401f-a463-59922d60c8e7" alt="image" width="30%" height="30%">
<br>

### 为实体添加新的属性：
为实体添加新的属性使用的依旧是 `SET` 关键字，例如：为 `李四` 添加一个新的属性 `age`：<br>
```sql
MATCH (lisi:Person {name: '李四'})
SET lisi.age = 26
RETURN lisi
```
注意要确定你 `MATCH` 的节点信息是正确的，`Person`、`name` 和 `李四` 的信息是对应的。如果你 `MATCH` 的信息是错误的，是无法修改信息的，或者错误的修改为了其他节点的信息。🚀🚀🚀<br>

### 更新Neo4j中实体的属性的名称：
假设你现在觉得 `name` 属性无法完全体现 `李斯` 的意义，想要将 `name` 属性的名称改为 `true_name` 可以使用以下语句：<br>
```sql
MATCH (lisi:Person {name: '李斯'})
SET lisi.true_name = lisi.name
// 删除原属性需要视情况而定
REMOVE lisi.name
RETURN lisi
```
Cypher语句解释：<br>
使用`MATCH`语句查找到名为`李斯`的节点。<br>
使用`SET`设置`true_name`属性的值为`name`属性的值。<br>
使用`REMOVE`删除原先的`name`属性。<br>
最后返回更新后的`lisi`节点。<br>

Neo4j效果：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/4e86442b-8390-4eb0-bfac-8590d7f3784f" alt="image" width="50%" height="50%">

咦？好像和我们设想的有些出入，为什么只有一个实体显示了内容，另一个实体什么也不显示❓❓❓<br>
🚀🚀🚀这是因为一个实体只能有一个对外显示的属性，而 `张三` 并没有 `true_name` 属性，`张三` 是 `name` 属性，所以对外显示的内容为空。<br>

这种做法看似不合理，但在某些时候实体有某些独有的属性时，这种设置就比较合理了，具体的使用场景需要你在工作中慢慢体会～<br>

Ps:这里再介绍下将所有 `Person` 类型的 `name` 属性改名为 `true_name` 的语句：<br>
```sql
MATCH (p:Person)
// 使用 `SET` 设置每个节点的 `true_name` 属性为当前的 `name` 属性值。
SET p.true_name = p.name
REMOVE p.name
RETURN p
```
Neo4j效果：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/63c4f4c3-917e-44d1-b1e0-a001cb423525" alt="image" width="50%" height="50%">

可以看到，`Person` 类型现在已经没有 `name` 属性了，只有 `true_name` 属性了，且 `张三` 和 `李斯` 两个 `true_name` 都正常显示了。<br>

### 更新Neo4j中实体的类型：
假如 `李斯` 翻身了，从一个普通人变成了 `Actor`，你此时需要将他的标签类型更改，可以使用下列语句：<br>
```sql
MATCH (m:Person{true_name:'李斯'}) remove m:Person  set m:Actor
RETURN m
```
Cypher语句解释：<br>
`MATCH (m:Person{true_name:'李斯'})`: <br>
- 这是一个匹配指令，它在数据库中查找一个标签为`Person`且`true_name`属性为 `'李斯'` 的节点，并将其赋给变量`m`。<br>
`remove m:Person`:<br>
- 这是一个删除操作，它从与变量`m`匹配的节点中移除`Person`标签。注意‼️‼️‼️，这并不是删除节点本身，而只是移除该节点的`Person`标签。🌿🌿🌿<br>
`set m:Actor`:<br>
- 这是一个设置操作，它为与变量`m`匹配的节点添加`Actor`标签。🌿🌿🌿<br>
`RETURN m`:<br>
- 这个指令表示将经过上述操作修改的节点返回给用户。<br>

简而言之，这个Cypher语句的功能是找到名为'李斯'的`Person`节点，移除其`Person`标签，并为其添加一个`Actor`标签，然后返回这个修改后的节点。<br>

假如你是想将 `李斯` 设定为2种实体类型，可以参考下方语句写法：<br>
```sql
MATCH (m:Person{true_name:'李斯'}) remove m:Person  set m:Actor:Man
```

### 为节点和关系添加多个属性：
前面折腾张三和李四(斯)已经够多了，这里暂且放过他们，同时用一个简单的例子实现为节点和关系添加多个属性，这样也方便大家查看效果。如果你只想为单个节点添加多个属性可以使用以下代码：<br>
```sql
MERGE (a:Person {name: 'Alice', age: 30, email: 'alice@example.com'})
```

如果你想同时为节点和关系添加多个属性，可以使用以下代码：🤗🤗🤗<br>
```sql
MERGE (m:Person {name: 'Alice', age: 30, email: 'alice@example.com'})-[r:KNOWS {since: 2020, reason: 'work'}]->(n:Person {name: 'Bob', age: 26, email: 'bob@example.com'})
return m,r,n
```
Neo4j效果：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/59e9c5e7-17cd-45cf-b9b7-dc2d43d39b64" alt="image" width="50%" height="50%">

这里再回顾一下查询，假如你想要查看节点 `Alice` 的 `email` 属性的值，使用下列语句即可：<br>
```sql
MATCH (m:Person {name: 'Alice'}) RETURN m.email
```
Neo4j效果如下：<br>
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/053bbba1-3a9a-4dcd-9336-b7ba5db3d243" alt="image" width="50%" height="50%">

## Neo4j中的删除操作：

### 删除某种类型的实体和其关系:

假设你想要删除 `neo4j` 中实体类型为 `Entity` 的数据，可以参考一下步骤:<br>

要删除Neo4j中实体类型为Entity的数据，您可以使用Cypher查询语言来执行删除操作。以下是一个示例Cypher查询，演示如何删除实体类型为Entity的所有节点及其关系：<br>

```cypher
MATCH (e:Entity)
DETACH DELETE e
```

这个查询执行以下操作：<br>

1. 使用`MATCH`子句来匹配所有具有标签`Entity`的节点，并将它们的引用命名为`e`。
2. 使用`DETACH DELETE`子句来删除匹配到的节点以及与这些节点相关的关系。这将删除节点及其关系，而不会保留任何关联关系。

请谨慎使用此操作，因为它会永久删除数据。确保在执行此操作之前备份数据库，以防需要恢复数据。<br>

如果您只想删除节点而保留相关的关系，可以使用以下查询：<br>

```cypher
MATCH (e:Entity)
DELETE e
```

这将删除所有具有标签`Entity`的节点，但保留与这些节点相关的关系。<br>

### 删除指定关系：

假设你现在想删除张三和李四之间的"前姐夫"关系，运行下列语句即可：(做法与 `更新Neo4j中实体间的关系` 那一节的语句相似)<br>

```sql
MATCH (zhangsan:Person {true_name: '张三'})-[r:前姐夫]->(lisi:Person {true_name: '李斯'})
DELETE r

RETURN zhangsan, lisi
```
<img src="https://github.com/peilongchencc/Pytool_Code/assets/89672905/6ba391a2-760d-451f-943a-3c1f9c950da7" alt="image" width="70%" height="70%">
<br>

如果你是想要删除所有 `Person` 类型实体间的 `前姐夫` 关系，可以使用下列语句：<br>
```sql
MATCH (m:Person)-[r:前姐夫]->(n:Person)
DELETE r

RETURN m, n
```

### 删除Neo4j中所有节点和关系：

删除操作无法撤回，尤其是删除所有‼️‼️‼️除非你打算删库跑路🥴🥴🥴<br>

```sql
MATCH (m) OPTIONAL MATCH (m)-[r]-() DELETE m, r
```
