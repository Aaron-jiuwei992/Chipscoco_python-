"""
description: 生成一定数量、一定长度且不重复的激活码（提供存储到数据库的方法）
author: Aaron-jiuwei992
date: 2021-02-03
"""
import random, MySQLdb, redis


class ActiveCodeGenerator:
    def __init__(self, code_length, code_amount):
        self.code_length = code_length
        self.code_amount = code_amount
        self.__elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.__code = []

    def __generate_code(self):
        for _ in range(self.code_length):
            self.__code.append(random.choice(self.__elements))
        code = "".join(self.__code)
        self.__code.clear()
        return code

    def __removal(self, codes):
        for i in range(self.code_amount):
            for j in range(i + 1, self.code_amount):
                if codes[i] == codes[j]:
                    print("重复的激活码", codes[i])
                    codes[i] = -1

    def generate_active_code(self):
        active_codes = [self.__generate_code() for _ in range(self.code_amount)]
        self.__removal(active_codes)
        index = 0
        while index < len(active_codes):
            if active_codes[index] == -1:
                print("删除重复的激活码", active_codes[index])
                active_codes.remove(active_codes[index])
                index -= 1
            else:
                index += 1
        return active_codes

    def save_to_mysql(self, active_codes):
        db = MySQLdb.connect(host='localhost', port=3306, user='root', password='root', database='code', charset='utf8')
        cursor = db.cursor()
        sql = 'insert into active_code(active_code) values (%s);'
        try:
            for index in range(200):
                cursor.execute(sql, active_codes[index])
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

    def save_to_redis(self, active_codes):
        r = redis.Redis(host='localhost', port='6379', db=0)
        for index in range(200):
            r.set(index, str(active_codes[index]))



if __name__ == '__main__':
    acg = ActiveCodeGenerator(16, 200)
    active_codes = acg.generate_active_code()
    print(active_codes)





