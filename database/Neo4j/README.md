# Neo4j

Neo4j是一种图形数据库管理系统，用于存储和管理图形数据。它是一个基于Java的开源软件，支持高度可扩展的图形数据模型，可以用于各种应用领域，如社交网络分析、推荐系统、网络安全分析等。Neo4j使用Cypher查询语言来操作和查询图形数据，并提供了丰富的API和工具来帮助开发人员与数据库进行交互。由于其图形数据模型的优势，Neo4j可以有效地表示和处理复杂的关系数据，提供了快速且灵活的数据访问和分析能力。<br>

虽然Neo4j是基于Java的软件，但不妨碍我们python用户使用🤣🤣🤣。接下来，笔者就讲一下 Ubuntu 18.4 安装Neo4j 4.1.0和Neo4j的使用经验。<br>
- [Neo4j](#neo4j)
  - [目录概览:](#目录概览)

## 目录概览:

目录                                     |作用                                                |备注
----------------------------------------|----------------------------------------------------|---------------
installation_process_of_neo4j           | 介绍Neo4j在Ubuntu 18.04系统上的安装与启动              | 
install_multi_neo4j_on_one_system       | 介绍在同一台ubuntu 18.04服务器上安装多个Neo4j数据库的方法 | 不需要多个neo4j可以跳过当前篇章
common_commands_and_operations_in_neo4j | 介绍Neo4j常见命令(终端)与操作                          | 
backup_and_migration_of_neo4j_data      | 介绍Neo4j数据备份与迁移                               | 
uninstall_neo4j_and_jdk                 | 介绍Neo4j和JDK的卸载                                 | 
python_sdk_of_neo4j                     | 介绍python连接Neo4j的常见操作(以py2neo为例)            | 