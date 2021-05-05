# -*- coding: utf-8 -*-
# author: jiuwei1997
# description: 用户登录认证程序
# date: 2021-4-17
import json


def authenticate():
    """
    cookie:
    {
  "Alex": {
    "username": "Alex",
    "password": "123456",
    "status": 0,
    "count_login_in": 0,
    "lock_time": 0
  },
  "black_girl": {
    "username": "black_girl",
    "password": "123456",
    "status": 0,
    "count_login_in": 0,
    "lock_time": 0
  },
  "bob": {
    "username": "bob",
    "password": "123456",
    "count_login_in": 0,
    "status": 0,
    "lock_time": 0
  }
}
    :return:
    """
    with open("cookie.json", "r+", encoding="utf-8") as f:
        cookie = json.loads(f.read())
    while True:
        acount = input("请输入您的账户：")
        if acount in cookie:
            print("账户输入正确！")
            if cookie[acount]["lock_time"] != 0:
                print("很抱歉，出于安全，您的账户已被锁定10分钟，请10分钟后再登录！")
                continue
            secret_key = input("请输入您账户的密码：")
            if cookie[acount]["password"] == secret_key:
                cookie[acount]["status"] = 1
                print("密码正确，登录成功！")
                cookie = json.dumps(cookie)
                with open("cookie.json", "w", encoding="utf-8") as f:
                    f.write(cookie)
                break
            else:
                print("很抱歉，您的密码错误，请重新输入！")
                cookie[acount]["count_login_in"] += 1
                if cookie[acount]["count_login_in"] >= 3:
                    print("很抱歉，出于安全，您的账户已被锁定10分钟，请10分钟后再登录！")
                    cookie[acount]["lock_time"] = 600
                    with open("cookie.json", "w", encoding="utf-8") as f:
                        f.write(json.dumps(cookie))


if __name__ == '__main__':
    authenticate()
