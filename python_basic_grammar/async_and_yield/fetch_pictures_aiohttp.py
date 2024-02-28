"""
@author:PeilongChen(peilongchencc@163.com)
@description:这个脚本首先定义了一个异步函数 `download_image`，它接受图片的 URL 和要保存的文件名。使用 `aiohttp.ClientSession()` 异步发送 HTTP GET 请求获取图片，然后利用 `aiofiles.open` 异步写入文件，这样可以在不阻塞主线程的情况下下载并保存图片。
"""
import os
import aiohttp
import asyncio
import aiofiles
from urllib.parse import urlparse, parse_qs

async def download_image(url):
    # 解析 URL 获取文件名
    parsed_url = urlparse(url)
    if "filePath" in parse_qs(parsed_url.query):
        # 如果是查询参数中包含文件路径，则从查询参数中提取文件名
        file_path = parse_qs(parsed_url.query)["filePath"][0]
        filename = file_path.split('/')[-1]
    else:
        # 否则，从 URL 路径中直接提取文件名
        filename = parsed_url.path.split('/')[-1]
    
    # 定义文件保存路径
    save_path = f"ocr_pictures/{filename}"
    # 获取给定路径中的路径名，例如对于 f"ocr_pictures/{filename}" 会返回 "ocr_pictures"
    save_dir = os.path.dirname(save_path)

    # 检查保存路径是否存在，不存在则创建
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                # 使用 aiofiles 异步写文件，需要安装 aiofiles
                # 如果没有安装，可以通过运行 pip install aiofiles 来安装
                async with aiofiles.open(save_path, mode='wb') as f:
                    await f.write(await response.read())
                    print(f"图片已保存到 {save_path}")

async def main(urls):
    tasks = [download_image(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
        "https://xxxxxx.com/pic/2024-02-22/be0c6836-6bc2-4dc1-bf0d-cf88029c522c.png?Expires=4862173056&OSSAccessKeyId=LTAI4Fqnoczaf1rSV6Vd7sLe&Signature=9YYZgqhN6eSuoQUrWhUndD40pSU%3D",
        "https://xxxxxx.com.cn/user/file/download/?filePath=/positionimages/202401/20240112102706-1.jpg"
    ]

    # 运行异步任务
    asyncio.run(main(urls))