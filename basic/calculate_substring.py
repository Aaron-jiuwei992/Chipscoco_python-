# 计算字符串中的指定子串的数量
# 实例1：使用字符串的find方法
string = "chipsococo,coco,coco,coco,chipscoco"
substring = "coco"
length = len(substring)
count = 0
substring_index = string.find("coco")
while substring_index != -1:
    count += 1
    substring_index = string.find("coco", substring_index+1)
print(count)


# 实例2：仅仅使用for循环遍历
string = "python is a good python"
sub_string = "python"
string_length = len(string)
count = 0
for index in range(string_length):
    """
    将问题拆解，构建外层循环：通过拆解子串的第一个字符为一次外循环，
    然后第二个字符为第二次外循环
    """
    if string[index] == sub_string[0]:
        # 保存主串第一个字符的位置
        index_ = index + 1
        """
        内层循环是通过移动外层循环的字符与子串的第二个元素第三个元素等等逐个比较的。
        从子串的第二个元素开始遍历，遍历子串的每一个元素和主串的第二个元素开始比较
        """
        for char in sub_string[1:]:
            """
            这里的比较要注意更新外层字符所取的索引以实现移动字符，
            另外要注意这里index_仅仅表示外层字符的索引。
            """
            if char != string[index_]:
                break
            index_ += 1
        else:
            count += 1
print(count)




















