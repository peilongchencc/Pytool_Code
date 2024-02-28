import requests

# 图片的URL
url = "https://xxxxxx.com/pic/2024-02-22/be0c6836-6bc2-4dc1-bf0d-cf88029c522c.png?Expires=4862173056&OSSAccessKeyId=LTAI4Fqnoczaf1rSV6Vd7sLe&Signature=9YYZgqhN6eSuoQUrWhUndD40pSU%3D"

# 发起GET请求下载图片
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 将内容写入文件
    with open("downloaded_image.png", "wb") as file:
        file.write(response.content)
    print("图片下载成功")
else:
    print("下载失败，状态码：", response.status_code)