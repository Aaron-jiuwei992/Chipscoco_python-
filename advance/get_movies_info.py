# 爬取豆瓣网电影250排行榜相关信息
import requests
from bs4 import BeautifulSoup

# 准备网站的初始网址
url = "https://movie.douban.com/top250"
# 处理反爬机制
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Cookie": 'll="118412"; bid=HhFHTXz4nlU; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1618244424%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utmc=30149280; __utma=223695111.116291786.1618244424.1618244424.1618244424.1; __utmb=223695111.0.10.1618244424; __utmc=223695111; __utmz=223695111.1618244424.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=O7s92LkwVjRcecSUkOJl2KZaMy65GMXS; _vwo_uuid_v2=DDFCC896F35CFE633CF1F91EF25A0FF8C|3190a9e0275afd83fb2c50a8b6903b44; __utma=30149280.269360611.1617031330.1618244424.1618244471.3; __utmz=30149280.1618244471.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1618244471; _pk_id.100001.4cf6=0c64e881844b58e4.1618244424.1.1618244529.1618244424.; ct=y',
}
# 拿到网页的源代码
resp = requests.get(url, headers=headers)
# 解析源代码
parent_page = BeautifulSoup(resp.text, "html.parser")
div_list = parent_page.find_all("div", class_="info")

mov_information = []
for div in div_list:
    movie_title = div.find("span", class_="title").text
    movie_cores = div.find("span", class_="rating_num").text
    movie_comment = div.find("div", class_="star").find_all("span")[3].text
    movie_information = movie_title + "," + movie_cores + "," + movie_comment
    mov_information.append(movie_information)
print(mov_information)




