import requests, time
from bs4 import BeautifulSoup
import ssl

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                  "/89.0.4389.82 Safari/537.36",


}
requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
s = requests.session()
s.keep_alive = False # 关闭多余连接
s.proxies = {"https": "https://116.17.102.215:3128"}
# ssl._create_default_https_context = ssl._create_unverified_context

for page in range(1, 50):
    url = f"https://www.umei.cc/bizhitupian/meinvbizhi/{page}.htm"
    try:
        resp = s.get(url, headers=headers, verify=False)
        # 请求成功后关闭请求
        resp.close()
    except requests.exceptions.RequestException as e:
        print(e)
        continue

    resp.encoding = "utf-8"
    parent_page = BeautifulSoup(resp.text, "html.parser")
    a_list = parent_page.find("div", class_="TypeList").find_all("a")
    for a in a_list:
        href = a.get("href")
        try:
            resp = s.get(href, headers=headers, verify=False)
            # 请求成功后关闭请求
            resp.close()
        except requests.exceptions.RequestException as e:
            print(e)
            continue

        resp.encoding = "utf-8"
        child_page = BeautifulSoup(resp.text, "html.parser")
        p = child_page.find("p", align="center")
        img = p.find("img")
        img_src = img.get("src")
        try:
            img_resp = s.get(img_src, headers=headers, verify=False)
            # 请求成功后关闭请求
            img_resp.close()
        except requests.exceptions.RequestException as e:
            print(e)
            continue

        img_name = img_src.split("/")[-1]
        with open("beautiful_girls/"+img_name, "wb") as f:
            img_content = img_resp.content
            f.write(img_content)
        print("over!", img_name)
        time.sleep(2)
    print(f"第{page}页 download over!")
    time.sleep(1)
print("all pictures download over!")










