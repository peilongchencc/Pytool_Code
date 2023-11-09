from sanic import Sanic
from sanic import response
from albert_text_vec import Convert_Text_2_Vector
from search_from_milvus import search_data
from pymilvus import connections

app = Sanic(__name__)
# 词向量转化类的实例化
embed_model = Convert_Text_2_Vector()

# 连接milvus(milvus会自动构建连接池，全局形式)，不确定多进程/线程中是否要重新建立连接
connections.connect(host='localhost', port='19530')

@app.route("/vector_similarity", methods=["POST"])
async def answer(request):
    # 获取用户数据
    usr_text = request.form.get("usr_input")
    if not usr_text:
        return response.json({"error": "Missing 'usr_input' parameter"}, status=400)
    # 将用户数据转为向量
    usr_text_vector = embed_model.convert_to_vec(usr_text)
    # 在Milvus中查询相似向量
    similarity_vec = search_data(usr_text_vector)

    return response.json({"相似度计算的结果为：": similarity_vec})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8848)