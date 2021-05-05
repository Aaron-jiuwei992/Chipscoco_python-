# -*- coding: utf-8 -*-
# author: jiuwei1997
# description:基于csv格式存储数据实现的注册和登录认证系统
# date:2021-5-4
"""
基于csv格式实现 用户的注册 & 登录认证。详细需求如下：
- 用户注册时，新注册用户要写入文件csv文件中，输入Q或q则退出。
- 用户登录时，逐行读取csv文件中的用户信息并进行校验。
- 提示：文件路径须使用os模块构造的绝对路径的方式。
"""
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "data.csv")
prompt = "欢迎使用该注册和登录系统，请输入对应的序号来完成你的操作：\n1, 注册\n2, 登录\n0, 退出系统\n>>>"
while True:
    user_input = input(prompt)
    if not user_input.isdigit():
        print("您输入的不是数字，请输入有效的命令！")
        continue
    else:
        command = int(user_input)
        if command == 1:
            # 注册功能实现
            us_input = input("请输入你的账户名和登录密码来进行注册,中间用逗号来分隔：")
            if us_input.upper() == "Q":
                break
            else:
                info = us_input.strip()
                with open(file_path, "r+", encoding="utf-8") as f:
                    for message in f:
                        message = message.strip().split(",")
                        username = message[0]
                        if info.split(",")[0] == username:
                            print("请输入别的用户名，你输入的用户已经注册过了！")
                            break

                    else:
                        f.write(info+"\n")
                        print("注册成功！")
                        break
        elif command == 2:
            # 登录功能实现
            username = input("请输入你的账户名：")
            password = input("请输入你的登录密码：")
            with open(file_path, "r", encoding="utf-8") as f:
                for info in f:
                    info_list = info.strip().split(",")
                    if info_list[0] != username or info_list[1] != password:
                        continue
                    else:
                        print("登录成功！")
                        exit()
                else:
                    print("登录失败！")
        else:
            break
