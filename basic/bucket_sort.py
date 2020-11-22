# 利用for循环实现简单的桶排序

# 代码实例1：
numbers = [2, 3, 1, 5]
buckets = [None]*5
for index in numbers:
    buckets[index-1] = index
for number in buckets:
    if number is not None:
        print(number, end = " ")

# 代码实例2：
# 桶的数量的计算是利用边界值与索引的对应关系确定的
numbers = [2, 3, 3, 4, 5, 8, 11]
buckets = [None]*11
for index in numbers:
    if buckets[index-1] is not None:
        # 这里之所以可以调用append方法是因为else语句的赋值操作是赋值一个列表的地址给变量
        buckets[index-1].append(index)
    else:
        buckets[index-1] = [index]
for numbers in buckets:
    if numbers is not None:
        for number in numbers:
            print(number, end = " ")

# 代码实例3：
numbers = [-2, -3, -2.5]
buckets = [None]*2
for index in numbers:
    if buckets[int(index)+3] is None:
        buckets[int(index)+3] = [None]*6
    buckets[int(index)+3][int((index-int(index))*10)+5] = index - int(index)

for index in range(2):
    if buckets[index] is not None:
        for number in buckets[index]:
            if number is not None:
                print(index-3+number, end = " ")




# 代码实例4：
numbers = [2.1, 1.3]
buckets = [None]*2

for index in numbers:
    # 将桶的索引与元素相对应，因为元素为小数，所以这里的对应是索引与小数的整数部分建立联系
    if buckets[int(index)-1] is None:
        # 将桶构建成嵌套的桶，用来存放小数部分。赋值操作符左边是表示None的桶，然后将其赋值为嵌套的None桶。这里实际上只需要4个嵌套的桶就够用了。
        buckets[int(index) - 1] = [None] * 10
    # 与10取模是为了求出小数部分的相对应的索引。
    buckets[int(index) - 1][int(index * 10) % 10] = index - int(index)


for index in range(2):
    if buckets[index] is not None:
        for number in buckets[index]:
            if number is not None:
               print(index+1+number)

# 代码实例5：
numbers = [-2.1, -3, -1, 1, 1.2, 2, 5]
numbers1 = [number+3 for number in numbers]

buckets = [None] * 9
for index in numbers1:
        if buckets[int(index)] is None:
            buckets[int(index)] = [None]*10
        buckets[int(index)][int((index-int(index))*10)] = index - int(index)
for index in range(9):
    if buckets[index] is not None:
        for number in buckets[index]:
            if number is not None:
                print(index+number-3, end = " ")




# 代码实例6：
# 10个随机数，使用桶排序实现降序排序
numbers = [2, 5, 1, 1, 7, 10, 11, 8, 7, 6]
numbers1 = [11 + number * -1 for number in numbers]
buckets = [None]*11
for index in numbers:
    if buckets[index-1] is not None:
        buckets[index-1].append(index)
    else:
        buckets[index-1] = [index]
# for numbers in buckets:
#     if numbers is not None:
#         for number in numbers:
#             print(-1*(number-11), end = " ")

for index in range(10, -1, -1):
    if buckets[index] is not None:
        for number in buckets[index]:
            print(number, end = " ")















