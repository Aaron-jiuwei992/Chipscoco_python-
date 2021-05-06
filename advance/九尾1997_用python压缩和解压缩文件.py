# -*- coding: utf-8 -*-
# author: jiuwei1997
# description:从某个网站下载压缩文件，然后解压缩该文件
# date:2021-5-6

import requests
import shutil, os

# 1.下载文件
file_url = 'https://files.cnblogs.com/files/wupeiqi/HtmlStore.zip'
res = requests.get(url=file_url)
content = res.content
# 2.将下载的文件保存到当前执行脚本同级目录下 /files/package/ 目录下（且文件名为HtmlStore.zip）
# 文件路径处理
base_dir = os.path.dirname(os.path.abspath(__file__))
target_directory_path = os.path.join(base_dir, "files", "package")
target_file_path = os.path.join(target_directory_path, "HtmlStore.zip")
# 判断文件路径是否存在，不存在则创建该路径
if not os.path.exists(target_directory_path):
    os.makedirs(target_directory_path)
    with open(target_file_path, "wb") as f:
        f.write(content)
# 3.在将下载下来的文件解压到 /files/html/ 目录下
zip_file_path = os.path.join(os.path.dirname(target_directory_path), "html")
if not os.path.exists(zip_file_path):
    os.makedirs(zip_file_path)
    shutil.unpack_archive(filename=target_file_path, extract_dir=zip_file_path, format="zip")

