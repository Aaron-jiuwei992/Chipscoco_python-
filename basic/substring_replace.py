# 将子串替换为指定子串

master = "ok is not ok"
substring = "ok"
replace_string = "bad"
new_string = ""
indices = []  # 用于保存查找到的每一个字串的起始位置

master_length = len(master)
substring_length = len(substring)

for index in range(master_length):
    if master[index] == substring[0]:
        index_ = index + 1
        for char in substring[1:]:
            if char != master[index_]:
                break
            index_ += 1
        else:
            # 注意，这里是添加子串的起始位置
            indices.append(index)
# 通过构建动态索引来实现动态切片
begin_index = end_index = 0
# 遍历子串起始位置的列表
for index in indices:
    end_index = index
    """
    核心是让master[]切片变成我们想要的一个动态变化的量，那么就想到更新切片前后的索引边界。
    规律可以通过一般性的例子寻找。
    """
    new_string = new_string + master[begin_index:end_index] + replace_string
    begin_index = end_index + substring_length
print(new_string)

# 寻找一般例子中的规律：后面一个master的end_index会在循环中不断更新为新的index，
# 而后面一个master的begin_index会更新为前一个master的end_index+子串长度，
# 这就是不断变化中的规律。
# master_string = "ok is not ok"
# new_string = master_string[:0]+replace_string+master_string[0+2:10]+replace_string+
# master_string[10+2:18]+replace_string


# 使用while循环+字符串的find方法替换子串
master = "ok is not ok"
substring = "ok"
replace_string = "bad"
new_string = ""
master_length = len(master)
substring_length = len(substring)
index = master.find(substring)
begin_index = 0
while index != -1:
    end_index = index

    new_string += master[begin_index:end_index] + replace_string

    begin_index = end_index + substring_length
    index = master.find(substring, index+1)
    print(new_string)












