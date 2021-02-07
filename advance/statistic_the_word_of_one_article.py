"""
description: 一个目录下，多个txt文件，统计出每篇日记最重要的词
author: Aaron-jiuwei992
date: 2021-02-07
"""
import os, re


def get_files():
    path = r'C:\Users\T-bao\Desktop\utils\diary'
    files = []
    for file in os.listdir(path):
        if file.endswith('.txt'):
            files.append(file)
    return files


def statistic_most_important_word(word):
    files = get_files()
    words_amount = []
    for file in files:
        word_amount = {word: 0}
        with open('C:\\Users\\T-bao\\Desktop\\utils\\diary\\'+file, 'r', encoding='utf8') as file_obj:
            chars = file_obj.read().replace('[^a-zA-Z]', ' ')
            words = chars.split(' ')
            for char in words:
                if char in word_amount:
                    word_amount[word] += 1
            words_amount.append(word_amount)
    return words_amount


if __name__ == '__main__':
    words_amount = statistic_most_important_word('the')
    for word_amount in words_amount:
        print(word_amount)
