# -*- coding: utf-8 -*-
# author: jiuwei1997
# description:通过代码下载网易云音乐上的付费音乐
# date:2021-5-6

import requests


url = "https://m701.music.126.net/20210506223243/3d772be419ccc9ca75acb549eaba3bbc/" \
      "jdyyaac/030f/5453/5652/4e5faf5d3fc9cdc4f6a5a8e8e066776c.m4a"
resp = requests.get(url)
content = resp.content
# 将请求下的数据写入文件
with open("记事本.m4a", "wb") as f:
    f.write(content)
print("下载成功！")





