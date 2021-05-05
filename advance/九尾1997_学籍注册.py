# -*- coding: utf-8 -*-
# author: jiuwei1997
# description:学籍注册
# date:2021-4-19
import json, time


def register():
    while True:
        prompt = "请输入您的"
        courses = ["Python", "Linux", "网络安全", "前端", "数据分析"]
        student_info = {}
        print(f"欢迎您注册，请开始输入您的一些信息以完成注册！\n温馨提示，您只能从以下课程中选择您的课程！\n{courses}")
        name = input(prompt+"姓名：")
        age = input(prompt+"年龄：")
        phone = input(prompt+"手机号：")
        id = input(prompt + "身份证号：")
        course = input(prompt+"课程：")
        print("请稍等，正在注册......")
        time.sleep(2)
        if student_info.get(name):
            if student_info.get(name).get("phone") or student_info.get(name).get("id"):
                with open("student_register_info.json", "r+", encoding="utf-8") as f:
                    student_info = json.loads(f.read())
                print(f"很抱歉，您已经注册过了，这是您的注册信息。\n{student_info}")
            continue
        else:
            student_info[name] = {"name": name, "age": age, "phone": phone, "id": id, "course": course}
            with open("student_register_info.json", "r+", encoding="utf-8") as f:
                f.write(json.dumps(student_info))
            print(f"恭喜你，注册成功，这是您的注册信息。\n{student_info}")
            break


if __name__ == '__main__':
    register()
