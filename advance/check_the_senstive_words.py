"""
description: 用户输入敏感词打印Freedom，否则打印出Human Rights（敏感词用*号替换后输出）。
author: Aaron-jiuwei992
date: 2021-02-03
"""


def get_words():
    path = r'C:\Users\T-bao\Desktop\utils\filtered_words.txt'
    with open(path, 'r', encoding='utf8') as file_obj:
        char = file_obj.read()
        words = char.split('\n')
    return words


def just_print():
    words = get_words()
    print(words)
    while True:
        user_input = input("请随便输入一些内容：")
        for word in words:
            if word in user_input:
                # print("Freedom")
                # break
                user_input = user_input.replace(word, '*'*len(word))
        else:
            # print("Human Rights")
            print(user_input)


if __name__ == '__main__':
    just_print()