from pymilvus import Collection, connections
import time

def search_data(data_vec):
    # 连接milvus(milvus会自动构建连接池)
    connections.connect(host='localhost', port='19530')
    # 选择需要的集合，并将其加载到内存
    albert_collection = Collection('search_article_in_medium')
    albert_collection.load()
    # 构建search参数
    search_params = {
        "metric_type": 'COSINE',
        "top_K":10,
    }
    
    start_time = time.time()
    # limit=3，表示无论top_K为多少，也将返回的数量限制为limit的值。limit的优先级高于top_K。
    search_result = albert_collection.search(data_vec, "text_vector", search_params, limit=3, output_fields=['id', 'text'])
    end_time = time.time()
    total_time = end_time-start_time
    print(f"**********************************")
    print(f"查询的耗时为:{total_time}")
    print(f"**********************************")
    
    # search_result是一个<class 'pymilvus.client.abstract.SearchResult'>类，但可像列表一样调用，查询结果在索引0。
    search_result_extract = search_result[0]
    # 将最终返回的结果放入一个字典
    all_search_result = {}
    for idx, item in enumerate(search_result_extract,1):
        each_res = item.__dict__    # 结果类似：{'id': 263663, 'distance': 1.0, 'fields': {'id': 263663, 'text': '老师'}}，类型为<class 'dict'>
        idx_name = f"结果{idx}"
        all_search_result[idx_name] = each_res

    return all_search_result