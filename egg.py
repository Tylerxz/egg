"""
@Author: Bluemangoo
@Date: 2022.05
@Copyright: 2022 Bluemangoo. All rights reserved.
@Description: A game
"""
import os
import random

EN = {"lang.name": "EN", "lang.set.tip": "Choose a language：\n[1] English\n[2] 简体中文\n[3] 繁體中文",
      "lang.set.error.bad_input": "\033[31mWrong input\033[0m"}
ZH_CN = {"lang.name": "ZH_CN", "lang.set.tip": "请选择语言：\n[1] English\n[2] 简体中文\n[3] 繁體中文",
         "error.bad_input": "\033[31m无效的输入\033[0m",
         "egg.hello": "\033[32m丢鸡蛋游戏\033[0m\n作者: Bluemangoo\nGithub: https://github.com/Bluemangoo/egg\n\n",
         "egg.help": "h|help 帮助\ns|start 开始游戏\nq|query 查询数据(游戏内)\na|analyse 查询统计数据\nc|cls 清屏\nq|quit 退出",
         "egg.help.short": "s|start 开始游戏\nh|help 帮助\n", "analyse.game": "共赢得 %d/%d 盘游戏",
         "analyse.egg": "共损失 %d/%d 个鸡蛋", "analyse.step": "共执行 %d 步", "analyse.score": "平均得分 %.2f",
         "game.intro": "有一座 %d 层高的大楼, 你手上有 %d 个一模一样的鸡蛋.\n这些鸡蛋非常坚韧, 以致于可以承受比较大的冲击.\n"
                       "从低层落下去不会摔破, 但在一定层数以上会.\n请你通过实验找出这个刚好能使鸡蛋摔破的层数\n\n"
                       "假设这个鸡蛋在49层摔下去不会破, 但是在50层就会.\n"
                       "这时你需要在49层和50层都尝试过以证明它摔破的临界楼层为50\n接下来就开始吧\n\n",
         "game.get_floor": "请输入猜测的层数(2~%d): ", "error.game.too_low": ""}
ZH_HK = {"lang.name": "ZH_HK", "lang.set.tip": "請選擇語言：\n[1] English\n[2] 简体中文\n[3] 繁體中文",
         "lang.set.error.bad_input": "\033[31m無效的輸入\033[0m"}
lang = ZH_CN

file_data = 'egg.data'


def cls():
    os.system('cls')


def get_lang(force):
    global lang
    flag = True
    while flag:
        input_get_lang = input(lang["lang.set.tip"])
        if input_get_lang == '1':
            lang = EN
            flag = False
        elif input_get_lang == '2':
            lang = ZH_CN
            flag = False
        elif input_get_lang == '3':
            lang = ZH_HK
            flag = False
        else:
            if force:
                cls()
                print(lang["error.bad_input"])
            else:
                flag = False
                cls()


def initialize():
    global lang
    if not os.path.exists(file_data):
        get_lang(True)
        with open(file_data, mode='w', encoding='utf-8') as file_data_stream:
            file_data_stream.write(lang["lang.name"] + '\n')
            file_data_stream.write('0\n0\n0\n0\n0\n0')
            file_data_stream.close()
    with open(file_data, mode='r', encoding='utf-8') as file_data_stream:
        lang = globals()[file_data_stream.readline()[:-1]]
        file_data_stream.close()


def hello():
    print(lang["egg.hello"])
    print(lang["egg.help.short"])


def analyse():
    with open(file_data, mode='r', encoding='utf-8') as file_data_stream:
        file_data_stream.readline()
        game_count_global = int(file_data_stream.readline()[:-1])
        game_win_global = int(file_data_stream.readline()[:-1])
        egg_all_global = int(file_data_stream.readline()[:-1])
        egg_remain_global = int(file_data_stream.readline()[:-1])
        step_used_global = int(file_data_stream.readline()[:-1])
        score_global = int(file_data_stream.readline()[:-1])
        file_data_stream.close()
        print(lang["analyse.game"] % (game_win_global, game_count_global))
        print(lang["analyse.egg"] % (egg_remain_global, egg_all_global))
        print(lang["analyse.step"] % step_used_global)
        if game_count_global > 0:
            print(lang["analyse.score"] % (score_global / game_count_global))
        else:
            print(lang["analyse.score"] % 0)


def game():
    cls()
    floor_all = random.randint(10, 500)
    floor_break = int(random.randint(2, floor_all))
    egg_all = random.randint(2, 10)
    print(lang["game.intro"] % (floor_all, egg_all))
    while True:
        guess = int(
            input(lang["game.get_floor"] % floor_all).join(filter(str.isdigit, 'Colour Temperature is 2700 Kelvin')))
        if guess < 2:
            print()


initialize()
hello()
while True:
    inp = input()
    if inp == "h" or inp == "help":
        print(lang["egg.help"])
    elif inp == "a" or inp == "analyse":
        analyse()
    elif inp == "s" or inp == "start":
        game()
    elif inp == "c" or inp == "cls":
        cls()
    elif inp == "q" or inp == "quit":
        break
    else:
        print(lang["error.bad_input"])
