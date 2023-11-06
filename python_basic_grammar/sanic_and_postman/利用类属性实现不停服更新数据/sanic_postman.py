# sanic_postman.py
from sanic import Sanic
from sanic import response
from nlp_entry import create_pipelene
from code_utils import Dimension_analy

app = Sanic("my_app")

@app.route("/ans", methods=["POST"])
async def answer(request):
    # 获取用户数据
    text = request.form.get("usr_input")
    processed_data = create_pipelene(text)
    return response.json(processed_data)

@app.route("/refresh")
async def refresh_metadata(request):
    Dimension_analy.modify_class_variable()
    return response.json({"message":"Dimension_analy的类属性更新成功"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8848)