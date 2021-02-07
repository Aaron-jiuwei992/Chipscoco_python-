"""
description: 爬取某网站的图片，并下载下来存到文件夹里
author: Aaron-jiuwei992
date: 2021-02-07
"""
import requests, re, os, time


def fetch_photos(url):
    r = requests.get(url)
    pattern = re.compile('img src="(https://img.tupianzj.com/uploads/allimg/\d+/.*?(.jpg|.png|.gif))"', re.S)
    text = r.text
    print(text, r.status_code)
    photo_urls = []
    urls = re.findall(pattern, text)
    for url in urls:
        photo_urls.append(url[0])
    return photo_urls


def save_photo(photo_urls, name, i):
    j = 0
    # 在当目录下创建文件夹
    if not os.path.exists('./' + name):
        os.makedirs('./' + name)

    # 下载图片
    for photo_url in photo_urls:
        print('正在保存第{}个'.format(j))
        try:
            pic = requests.get(photo_url, timeout=10)
            time.sleep(1)
        except:
            print('当前图片无法下载')
            j += 1
            continue
        # 把图片保存到文件夹
        file_full_name = './' + name + '/' + str(i) + '-' + str(j) + '.jpg'
        with open(file_full_name, 'wb') as f:
            f.write(pic.content)
        j += 1


if __name__ == '__main__':
    url = 'https://www.tupianzj.com/meinv/mm/xingganshaofu/'
    photo_urls = fetch_photos(url)
    save_photo(photo_urls, 'images', 00)
