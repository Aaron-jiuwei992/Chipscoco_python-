"""
所有回调函数都遵循相同的接口规范，读者在实际开发中，可以将回调函数作为业务层的代码
分离到其它文件
"""
def show(goods, flag = 0):
    """
    :param goods: goods table, e.g:{
            1: {"name": "洗发水", "price": 22},
            2: {"name": "牙膏", "price": 15},
        }, or [{"id": 1, "name": "洗发水", "price": 22}, ]
    :return:
    """
    tr = "+"+"-"*5+"+"+"-"*16+"+"+"-"*10+"+"
    heading = "|{:^5s}|{:^13s}|{:^8s}|".format("id", "商品名", "售价")

    print(tr+"\n"+heading+"\n"+tr)
    if flag == 0:
        for id_ in goods:
            print("|{0:^5s}|{1:{3}^8s}|{2:^10s}|".format(str(id_), goods[id_]["name"],
                                                     str(goods[id_]["price"]), chr(12288)))
    else:
        for item in goods:
            print("|{0:^5s}|{1:{3}^8s}|{2:^10s}|".format(str(item["id"]), item["name"],
                                                         str(item["price"]), chr(12288)))
    print(tr)


class ShowGoodsHandler:
    __instance = None

    def __call__(self, chipscoco):
        print("以下是商城中的所有商品:")
        show(chipscoco["goods"])

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = ShowGoodsHandler()
        return cls.__instance


class ChipsCoco:
    def __init__(self, data):
        self.__data = data
        self.__handlers = {}
        self.__begin_prompt = "您好，欢迎使用薯条橙子在线购物系统chipscoco，输入<>中对应的指令来使用购物系统:\n"
        self.__end_prompt = "<quit>:退出系统\n请输入指令:____\b\b\b\b"
        self.__prompts = []
        self.__exit_commands = {"quit", "exit"}
        self.__handler_index = 1

    def __obtain_user_command(self, prompt):

        command, valid = "quit", True
        try:
            command = input(prompt)
            _ = self.__handlers[int(command)]
        except (ValueError, KeyError):
            command = command.lower()
            if command != "quit":
                command = None
                valid = False
        return command, valid

    def add_handler(self, handler, prompt):
        self.__handlers[self.__handler_index] = handler.get_instance()
        self.__handler_index +=1
        self.__prompts.append(prompt)

    def __generate_prompt(self):
        prompt = self.__begin_prompt
        for index, value in enumerate(self.__prompts):
            prompt += "<{}>:{}\n".format(index+1, value)
        prompt += self.__end_prompt
        return prompt

    def serve_forever(self):
        prompt =  self.__generate_prompt()
        while True:
            command, valid = self.__obtain_user_command(prompt)
            if not valid:
                print("你输入了非法的指令!")
                continue

            if command in self.__exit_commands:
                    break
            self.__handlers[int(command)](self.__data)
            input("按下键盘任意键，继续使用该系统...")


if __name__ == "__main__":
    chipscoco = {
        "goods": {
            1: {"name": "洗发水", "price": 22},
            2: {"name": "牙膏", "price": 15},
            3: {"name": "宠物绳", "price": 29},
            4: {"name": "面包", "price": 16},
            5: {"name": "啤酒", "price": 8},
            6: {"name": "咖啡", "price": 30},
        },
        "shopping_cart": {}
    }

    chipscoco = ChipsCoco(chipscoco)
    chipscoco.add_handler(ShowGoodsHandler, "查看所有商品")
    chipscoco.add_handler()
    chipscoco.serve_forever()
