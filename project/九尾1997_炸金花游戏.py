# - * - coding: utf - 8 -*-
# author: jiuwei1997
# description: 炸金花游戏小程序
# date: 2021-4-18
import random, time


class Card:
    """一张牌"""

    def __init__(self, suite, face):
        self.__suite = suite
        self.__face = face

    @property
    def suite(self):
        return self.__suite

    @property
    def face(self):
        return self.__face

    def __str__(self):
        if self.__face == 1:
            face_str = "A"
        elif self.__face == 11:
            face_str = "J"
        elif self.__face == 12:
            face_str = 'Q'
        elif self.__face == 13:
            face_str = 'K'
        else:
            face_str = str(self.__face)
        return "%s%s" % (self.__suite, face_str)


class Poker:
    """一副牌（不含大小王）"""

    def __init__(self):
        self.cards = []
        self.current_id = 1
        for suite in '♠♥♣♦':
            for face in range(1, 14):
                card = Card(suite, face)
                self.cards.append(card)

    def shuffle(self):
        """洗牌的功能"""
        random.shuffle(self.cards)

    @property
    def distribute_cards(self):
        """发牌的功能"""
        card = self.cards[self.current_id]
        self.current_id += 1
        return card


class Player:
    def __init__(self, name):
        self.name = name
        self.cards_on_hand = []
        self.cards_on_hand_type = None

    def get_cards(self, card):
        """拿牌的功能"""
        self.cards_on_hand.append(card)

    def sort_cards(self):
        """整理牌的功能"""
        self.cards_on_hand.sort(key=get_card_face)

    def judge_cards(self):
        """
        判断玩家手里牌的牌型的功能
        :return:
        """
        cards = self.cards_on_hand
        cards_face = []
        cards_suite = []
        for card in cards:
            cards_face.append(card.face)
            cards_suite.append(card.suite)
        cards_face.sort()

        if len(set(cards_face)) == 1:
            self.cards_on_hand_type = "豹子"
            return self.cards_on_hand_type
        elif len(set(cards_face)) == 2:
            self.cards_on_hand_type = "对子"
            return self.cards_on_hand_type
        elif len(set(cards_face)) == 3:
            self.cards_on_hand_type = "单张"
            return self.cards_on_hand_type
        else:
            if len(set(cards_suite)) == 1:
                if cards_face[2] - cards_face[0] == 2:
                    self.cards_on_hand_type = "顺金"
                    return self.cards_on_hand_type
                else:
                    self.cards_on_hand_type = "金花"
                    return self.cards_on_hand_type
            else:
                if cards_face[2] - cards_face[0] == 2:
                    self.cards_on_hand_type = "顺子"
                    return self.cards_on_hand_type


def get_card_face(card):
    return card.face


class Winner:
    # 炸金花游戏取胜机制
    """
    最简单的游戏规则：
    牌型：豹子：三张同样大小的牌。顺金：花色相同的三张连牌。金花：三张花色相同的牌。 顺子：三张花色不全相同的连牌。
    对子：三张牌中有两张同样大小的牌。单张：除以上牌型的牌。
    玩法比较简单，豹子> 顺金 > 金花 > 顺子 > 对子 > 单张，
    当牌型不一致的话，谁牌型大谁胜出；
    当牌型一致的时候，又分为三种情况，一是豹子、顺金、顺子，比较玩家手中牌的最大值，谁拥有最大牌面值谁胜出；
    二是对子，比较玩家手中对子的牌面大小，如果相同再另行比较；三是金花、单张，比较玩家手中所有牌面大小之和。
    """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def get_card_max_face(self, player):
        """
        筛选出三张牌中最大的牌,
        当牌是豹子，顺金，金花，顺子时，需要比较牌的值的大小。
        :param player:
        :return:
        """
        cards = player.cards_on_hand
        cards_face = []
        for card in cards:
            cards_face.append(card.face)
        return max(cards_face)

    def get_card_suite(self, player):
        """
        返回扑克牌花色大小
        :return:
        """
        cards = player.cards_on_hand
        cards_suite = []
        for card in cards:
            cards_suite.append(card.suite)
        return max(cards_suite)

    def get_card_face(self, player):
        """
        当牌型是对子时，需要同时判断对子牌的值大小，以及剩余的单张牌的值大小。
        :param player:
        :return:
        """
        repeate_poker_face = single_poker_face = None
        cards = player.cards_on_hand
        cards_face = []
        for card in cards:
            cards_face.append(card.face)
        cards_face.sort()
        if cards_face[0] != cards_face[1]:
            repeate_poker_face = cards_face[1]
            single_poker_face = cards_face[0]
        else:
            repeate_poker_face = cards_face[0]
            single_poker_face = cards_face[1]
        return repeate_poker_face, single_poker_face

    def get_card_score(self, player):
        """
        当牌型是单张时，计算三张牌值的总和来比较大小。
        :return:
        """
        cards = player.cards_on_hand
        cards_face = []
        for card in cards:
            cards_face.append(card.face)
        score = sum(cards_face)
        return score

    def get_winner(self):
        player1, player2 = self.player1, self.player2
        if player1.cards_on_hand_type == "豹子":
            if player2.cards_on_hand_type == "豹子":
                player1_card_max_face = self.get_card_face(player1)
                player2_card_max_face = self.get_card_face(player2)
                if player1_card_max_face > player2_card_max_face:
                    return player1
                elif player1_card_max_face < player2_card_max_face:
                    return player2
                else:
                    return None
            else:
                return player1
        elif player1.cards_on_hand_type == "顺金":
            if player2.cards_on_hand_type == "豹子":
                return player2
            elif player2.cards_on_hand_type == "顺金":
                player1_card_max_face = self.get_card_face(player1)
                player2_card_max_face = self.get_card_face(player2)
                if player1_card_max_face > player2_card_max_face:
                    return player1
                elif player1_card_max_face < player2_card_max_face:
                    return player2
                else:
                    return None
            else:
                return player1
        elif player1.cards_on_hand_type == "金花":
            if player2.cards_on_hand_type == "豹子" or player2.cards_on_hand_type == "顺金":
                return player2
            elif player2.cards_on_hand_type == "金花":
                player1_card_max_face = self.get_card_face(player1)
                player2_card_max_face = self.get_card_face(player2)
                if player1_card_max_face > player2_card_max_face:
                    return player1
                elif player1_card_max_face < player2_card_max_face:
                    return player2
                else:
                    return None
            else:
                return player1
        elif player1.cards_on_hand_type == "顺子":
            if player2.cards_on_hand_type == "豹子" or player2.cards_on_hand_type == "顺金" or player2.cards_on_hand_type == "金花":
                return player2
            elif player2.cards_on_hand_type == "顺子":
                player1_card_max_face = self.get_card_face(player1)
                player2_card_max_face = self.get_card_face(player2)
                if player1_card_max_face > player2_card_max_face:
                    return player1
                elif player1_card_max_face < player2_card_max_face:
                    return player2
                else:
                    return None
            else:
                return player1
        elif player1.cards_on_hand_type == "对子":
            if player2.cards_on_hand_type == "豹子" or player2.cards_on_hand_type == "顺金" or player2.cards_on_hand_type == "金花" \
                    or player2.cards_on_hand_type == "顺子":
                return player2
            elif player2.cards_on_hand_type == "对子":
                player1_repeate_poker_face, player1_single_poker_face = self.get_card_face(player1)
                player2_repeate_poker_face, player2_single_poker_face = self.get_card_face(player2)
                if player1_repeate_poker_face > player2_repeate_poker_face:
                    return player1
                elif player1_repeate_poker_face < player2_repeate_poker_face:
                    return player2
                else:
                    if player1_single_poker_face > player2_single_poker_face:
                        return player1
                    elif player1_single_poker_face < player2_single_poker_face:
                        return player2
                    else:
                        return None
            else:
                return player1
        else:
            if player2.cards_on_hand_type == "豹子" or player2.cards_on_hand_type == "顺金" or player2.cards_on_hand_type == "金花" \
                    or player2.cards_on_hand_type == "顺子" or player2.cards_on_hand_type == "对子":
                return player2
            else:
                player1_card_score, player2_card_score = self.get_card_score(player1), self.get_card_score(player2)
                if player1_card_score > player2_card_score:
                    return player1
                elif player1_card_score < player2_card_score:
                    return player2
                else:
                    return None


def play_poker():
    print("炸金花游戏初始化中，请稍等。。。")
    while True:
        user_input = input("游戏开始，请输入多名游戏玩家的名字，以逗号分隔，然后开始进行炸金花游戏。"
                           "（温馨提示，该游戏只能两个人玩!!!）\n玩家名字：")
        players_name = user_input.split(",")
        # 根据用户输入的名字实例化相应个数的玩家，存储到列表中
        players = []
        for index, player_name in enumerate(players_name):
            p = Player(player_name)
            players.append(p)
        # 生成一副新牌，并洗好牌
        poker = Poker()
        poker.shuffle()

        # 亮牌：显示当次游戏的所有牌的情况
        cards = poker.cards
        cards_str = []
        for card in cards:
            cards_str.append(card.suite+str(card.face))
        print(cards_str)

        # 为每个玩家发(三张)牌,一副牌至多进行8局游戏
        while poker.current_id <= len(poker.cards) - 4:
            # 一个while循环代表一局游戏
            while True:
                # 发牌
                print("正在给每位玩家发牌，请稍等...")
                for player in players:
                    for i in range(3):
                        player.get_cards(poker.distribute_cards)
                    player.sort_cards()
                    # 发牌结束后，玩家判断牌型
                    player.judge_cards()
                print("发牌和理牌结束，正在准备出牌比点，请稍等...")
                time.sleep(2)
                # 比点
                # 注意：这里考虑到人数太多，比较会很麻烦，就先简化成两个人的游戏。

                # 实例化一个游戏取胜机制机器对象
                win = Winner(players[0], players[1])
                winner = win.get_winner()

                # 打印比点结果，并提示点最大和点最小的玩家
                if winner:
                    print(f"两位玩家的牌型分别是{players[0].cards_on_hand_type}、{players[1].cards_on_hand_type},"
                          f"玩家{winner.name}赢了!")
                else:
                    print("两位玩家的牌型大小一样！")
                # 亮牌
                player1_cards_on_hand, player2_cards_on_hand = players[0].cards_on_hand, players[1].cards_on_hand
                player1_cards = []
                player2_cards = []
                for player1_card in player1_cards_on_hand:
                    player1_cards.append(player1_card.suite+str(player1_card.face))

                for player2_card in player2_cards_on_hand:
                    player2_cards.append(player2_card.suite+str(player2_card.face))


                print(f"两位玩家的牌分别是{player1_cards}\n{player2_cards}")

                # 亮牌结束后清空玩家手里的牌
                player1_cards_on_hand.clear()
                player2_cards_on_hand.clear()

                # 本局结束，退出循环进行下一局游戏
                break
        print("一大轮游戏已经结束，正在准备下一轮...")


if __name__ == '__main__':
    play_poker()

