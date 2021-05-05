import random


def lottery():
    employees = list(range(300))
    award_3 = []
    award_2 = []
    award_1 = []
    i = j = k = 0
    while True:
        print("欢迎使用该抽奖程序，抽奖结束后程序将自动结束！")
        print("三等奖抽奖开始！")
        while i < 30:
            winner = random.choice(employees)
            award_3.append(winner)
            employees.remove(winner)
            i += 1
        print("三等奖抽奖结束，获奖者员工编号如下：{}，他们将获得避孕套一盒。".format(award_3))

        print("二等奖抽奖开始！")
        while j < 6:
            winner = random.choice(employees)
            award_2.append(winner)
            employees.remove(winner)
            j += 1
        print("二等奖抽奖结束，获奖者员工编号如下：{}，他们将获得iPhone手机一部。".format(award_2))

        print("一等奖抽奖开始！")
        while k < 3:
            winner = random.choice(employees)
            award_1.append(winner)
            employees.remove(winner)
            k += 1
        print("一等奖抽奖结束，获奖者员工编号如下：{}，他们将获得泰国5日游。".format(award_1))
        print("抽奖结束！")
        break


if __name__ == '__main__':
    lottery()
