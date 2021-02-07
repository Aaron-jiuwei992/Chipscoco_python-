"""
description: 使用xlsxwriter模块，将一个txt文件中的内容存储到一个表格文件中
author: Aaron-jiuwei992
date: 2021-02-07
"""
import json, xlsxwriter


def write_to_file():
    with open(r'C:\Users\T-bao\Desktop\utils\student.txt', 'r', encoding='utf8') as file_obj:
        text = json.loads(file_obj.read())
        wb = xlsxwriter.Workbook('student.xlsx')  # 创建一个工作簿
        ws = wb.add_worksheet('student')  # 创建一个sheet
        row = 0
        for k, v in text.items():
            ws.write(row, 0, k)
            col = 1
            for item in v:
                ws.write(row, col, item)
                col += 1
            row += 1
        wb.close()


if __name__ == '__main__':
    write_to_file()