from mongodb_utils import insert_onedata_to_mongodb
from db_config import Mongodb_Server_Config, Mongodb_Id_Path

# 插入文档
document = {
    "name": "Alice",
    "hobbies": [
        {"name": "Reading", "level": "Intermediate"},
        {"name": "Painting", "level": "Beginner"}
    ]
}
my_dict = {'name': 'John', 'age': 30, 'score': {'chinese':87, 'math':99, 'english':92}}

print(document)
print(my_dict)

collection_name = Mongodb_Server_Config['mongodb_collection']

insert_onedata_to_mongodb(document, collection_name, Mongodb_Id_Path, "financial")
insert_onedata_to_mongodb(my_dict, collection_name, Mongodb_Id_Path, "sale")