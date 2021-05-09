# -*- coding: utf-8 -*-
# author: jiuwei1997
# description:基于openpyxl模块读取Excel文件实现用户认证
# date:2021-5-10
from openpyxl import load_workbook
import hashlib


def encrypt(origin):
    origin_bytes = origin.encode('utf-8')
    md5_object = hashlib.md5()
    md5_object.update(origin_bytes)
    return md5_object.hexdigest()


def authenticate():
    wb = load_workbook('files/user.xlsx')
    sheet = wb['Sheet1']
    user_dict = {}
    for row in sheet.rows:
        user_dict[row[1].value] = row[2].value
    user_name = input("user_name:")
    password = input("password:")
    secret_pd = encrypt(password)
    pd = user_dict.get(user_name)
    if pd is None:
        print("用户名错误！")
    elif pd == secret_pd:
        print("登录成功！")
    else:
        print("密码错误！")


if __name__ == '__main__':
    authenticate()



