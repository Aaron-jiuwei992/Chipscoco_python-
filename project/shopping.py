# 实现一个简单的商城购物系统
"""
① 列出所有商品
输出举例：
您好，欢迎使用薯条橙子在线购物系统，以下是商城中的所有商品
+----+--------+-----------+
| id | 商品名 |  售价     |
+----+--------+-----------+
|  1 | 洗发水 |   22      |
|  2 | 牙膏   |   15      |
|  3 | 宠物绳 |   29      |
|  4 | 面包   |   16      |
|  5 | 啤酒   |   8       |
|  6 | 咖啡   |   30      |
+----+--------+-----------+
"""


def clear_shopping_cart(chipscoco):
    """
        :param chipscoco:
        chipscoco = {"goods": {
            1: {"name": "洗发水", "price": 22, "amount": 1000},
            2: {"name": "牙膏 ", "price": 15, "amount": 1000},
            3: {"name": "宠物绳 ", "price": 29, "amount": 1000},
            4: {"name": "面包", "price": 16, "amount": 1000},
            5: {"name": "啤酒", "price": 8, "amount": 1000},
            6: {"name": "咖啡", "price": 30, "amount": 1000}
        }
            , "shopping_cart": {1: {"name": "洗发水", "price": 22, "amount": 1},
            2: {"name": "牙膏 ", "price": 15, "amount": 2}}
        }
        :return:
        """
    shopping_cart = chipscoco["shopping_cart"]
    shopping_cart.clear()


def convert_dict_2_list(data):
    """
    :param data:
    {1:{"name":"洗发水", "price":22, "amount": 0},
    2:{"name":"牙膏 ", "price":15, "amount": 0}}
    :return:
    """
    goods = []
    for _ in data:
        goods.append({"id": _, "name": data[_]["name"], "price": data[_]["price"], "amount": data[_]["amount"]})
    return goods


def show(goods,flag = 0):
    """
    a dict object indicates the online shopping system chipscoco
    :param goods:
    {1:{"name":"洗发水", "price":22},
    2:{"name":"牙膏 ", "price":15 }}
    or
    {1:{"name":"洗发水", "price":22, "数量": 1},
    2:{"name":"牙膏 ", "price":15, "数量": 2}}
    or
    [
    {"id": 1, "name": "洗发水"， "price": "22"},
    {"id": 2, "name": "牙膏"， "price": "15"}
    ]
    :return:
    """
    tr = "+" + "-" * 5 + "+" + "-" * 10 + "+" + "-" * 15 + "+" + "-" * 5 + "+"
    heading = "|{:^5s}|{:^7s}|{:^13s}|{:^3s}|".format("id", "商品名", "售价", "数量")
    print(tr + "\n" + heading + "\n" + tr + "\n")
    if flag == 0:
        for _ in goods:
            print("|{0:^5d}|{1:{4}^5s}|{2:{5}^8d}|{3:^5d}|".format(_, goods[_]["name"], goods[_]["price"], goods[_]["amount"], chr(12288), chr(12288)))
        print(tr)
    elif flag == 1:
        for _ in goods:
            print("|{0:^5d}|{1:{4}^5s}|{2:{5}^8d}|{3:^5d}|".format(_["id"], _["name"], _["price"], _["amount"], chr(12288), chr(12288)))
        print(tr)
    elif flag == 2:
        for _ in goods:
            print("|{0:^5d}|{1:{4}^5s}|{2:{5}^8d}|{3:^5d}|".format(_, goods[_]["name"], goods[_]["price"], goods[_]["amount"], chr(12288), chr(12288)))
        print(tr)


def show_all_goods(chipscoco):
    print("以下是商城中的所有商品:")
    show(chipscoco["goods"])

def sort_goods(chipscoco):
    """
    :param chipscoco:
    :return:
    """
    print("您好，输入指令<asc>对商品按售价进行升序排序，输入指令<desc>对商品按售价进行降序排序:____\b\b\b\b")
    command = input("")
    """
    goods = [
    {"id": 1, "name": "洗发水"， "price": "22", "amount": 0},
    {"id": 2, "name": "牙膏"， "price": "15", "amount": 0} 
    ]
    """
    goods = convert_dict_2_list(chipscoco["goods"])
    length_goods = len(goods)
    if command.lower() == "asc":
        for i in range(length_goods-1):
            is_sort = False
            for j in range(length_goods-1-i):
                if goods[j]["price"] > goods[j+1]["price"]:
                    goods[j], goods[j+1] = goods[j+1], goods[j]
                    is_sort = True
            if not is_sort:
                break
    elif command.lower() == "desc":
        for i in range(length_goods-1):
            is_sort = False
            for j in range(length_goods-1-i):
                if goods[j]["price"] < goods[j+1]["price"]:
                    goods[j], goods[j+1] = goods[j+1], goods[j]
                    is_sort = True
            if not is_sort:
                break
    show(goods,flag = 1)

def add_goods(chipscoco):
    """
    :param chipscoco:
    chipscoco = {"goods": {
        1: {"name": "洗发水", "price": 22, "amount": 0},
        2: {"name": "牙膏 ", "price": 15, "amount": 0},
        3: {"name": "宠物绳 ", "price": 29, "amount": 0},
        4: {"name": "面包", "price": 16, "amount": 0},
        5: {"name": "啤酒", "price": 8, "amount": 0},
        6: {"name": "咖啡", "price": 30, "amount": 0}
    }
        , "shopping_cart": {}
    }
    :return:
    """

    while True:
        id = int(input("请输入商品id:__\b\b"))
        if id in chipscoco["goods"]:
            if id in chipscoco["shopping_cart"]:
                chipscoco["shopping_cart"][id]["amount"] += 1
                print("您好，已将商品{}加入购物车".format(chipscoco["goods"][id]["name"]))
            else:
                chipscoco["shopping_cart"][id] = {"name": chipscoco["goods"][id]["name"], "price": chipscoco["goods"][id]["price"], "amount": 1}
                print("您好，已将商品{}加入购物车".format(chipscoco["goods"][id]["name"]))
        else:
            print("请输入有效的商品id！")
        break

def delete_goods(chipscoco):
    """
    :param chipscoco:
    chipscoco = {"goods": {
        1: {"name": "洗发水", "price": 22, "amount": 0},
        2: {"name": "牙膏 ", "price": 15, "amount": 0},
        3: {"name": "宠物绳 ", "price": 29, "amount": 0},
        4: {"name": "面包", "price": 16, "amount": 0},
        5: {"name": "啤酒", "price": 8, "amount": 0},
        6: {"name": "咖啡", "price": 30, "amount": 0}
    }
        , "shopping_cart": {1: {"name": "洗发水", "price": 22, "amount": 1},
        2: {"name": "牙膏 ", "price": 15, "amount": 2}}
    }
    :return:
    """
    while True:
        id = int(input("请输入你要删除的商品id:__\b\b"))
        if id in chipscoco["shopping_cart"]:
            if chipscoco["shopping_cart"][id]["amount"] != 0:
                chipscoco["shopping_cart"][id]["amount"] -= 1
                if chipscoco["shopping_cart"][id]["amount"] != 0:
                    print("您好，已将商品{}的数量减1。".format(chipscoco["goods"][id]["name"]))
                else:
                    chipscoco["shopping_cart"].pop(id)
                    print("您好，已将商品{}从购物车中删除。".format(chipscoco["goods"][id]["name"]))
        else:
            print("请输入有效的商品id！")
        break


def show_shopping_cart(chipscoco):
    print("这是您的购物清单:")
    show(chipscoco["shopping_cart"],flag=2)


def pay(chipscoco):
    """
    :param chipscoco:
     chipscoco = {"goods": {
        1: {"name": "洗发水", "price": 22, "amount": 0},
        2: {"name": "牙膏 ", "price": 15, "amount": 0},
        3: {"name": "宠物绳 ", "price": 29, "amount": 0},
        4: {"name": "面包", "price": 16, "amount": 0},
        5: {"name": "啤酒", "price": 8, "amount": 0},
        6: {"name": "咖啡", "price": 30, "amount": 0}
    }
        , "shopping_cart": {1: {"name": "洗发水", "price": 22, "amount": 1},
        2: {"name": "牙膏 ", "price": 15, "amount": 2}}
    }
    :return:
    """
    show_shopping_cart(chipscoco)
    goods = chipscoco["shopping_cart"]
    sum_price = 0
    for id in goods:
        sum_price += goods[id]["amount"]*goods[id]["price"]
    print("总价：{}元，输入指令0进行付款，输入指令1继续购物。".format(sum_price))
    user_input =  int(input(""))
    if user_input == 0:
        print("正在前往支付页面，请稍候......")
        clear_shopping_cart(chipscoco)
    elif user_input == 1:
        print("正在前往购物页面，请稍候......")


def shopping():

    chipscoco = {"goods": {
        1: {"name": "洗发水", "price": 22, "amount": 0},
        2: {"name": "牙膏 ", "price": 15, "amount": 0},
        3: {"name": "宠物绳 ", "price": 29, "amount": 0},
        4: {"name": "面包", "price": 16, "amount": 0},
        5: {"name": "啤酒", "price": 8, "amount": 0},
        6: {"name": "咖啡", "price": 30, "amount": 0}
    }
        , "shopping_cart": {}
    }

    welcome = "您好，欢迎使用薯条橙子在线购物系统chipscoco，输入<>中对应的指令来使用购物系统:\n" \
                "<1>:查看所有商品\n" \
                "<2>:对商品按售价进行排序(asc表示升序，desc表示降序)\n" \
                "<3>:添加商品到购物车\n" \
                "<4>:查看购物车\n" \
                "<5>:删除购物车指定商品\n" \
                "<6>:下单结账\n" \
                "<0>:退出系统\n"
    commands = {
        1: show_all_goods, 2: sort_goods, 3: add_goods, 4: show_shopping_cart, 5: delete_goods, 6: pay
    }

    while True:
        print(welcome)
        command = int(input("please enter the specify command to use the chipscoco:__\b\b"))
        if command in commands:
            commands[command](chipscoco)
        elif command == 0:
            break
        elif command not in commands:
            print("请输入有效的指令！")
        user_input = input("按下键盘任意键，继续使用系统......")


if __name__ == "__main__":
    shopping()

