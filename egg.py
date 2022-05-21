"""
@Author: Bluemangoo
@Date: 2022.05
@Copyright: 2022 Bluemangoo. All rights reserved.
@Description: A game
"""
import os
import random

EN = {"lang.name": "EN", "lang.set.tip": "Choose a language：\n[1] English\n[2] 简体中文\n[3] 繁體中文",
      "lang.set.error.bad_input": "Wrong input, please enter the correct option"}
ZH_CN = {"lang.name": "ZH_CN", "lang.set.tip": "请选择语言：\n[1] English\n[2] 简体中文\n[3] 繁體中文",
         "lang.set.error.bad_input": "错误的输入，请输入正确的选项","game.hello":"\033[32m丢鸡蛋游戏\033[0m\n作者：Bluemangoo\n"}
ZH_HK = {"lang.name": "ZH_HK", "lang.set.tip": "請選擇語言：\n[1] English\n[2] 简体中文\n[3] 繁體中文",
         "lang.set.error.bad_input": "錯誤的輸入，請輸入正確的選項"}
lang = EN

file_data = 'egg.data'

game_count_global = 0
egg_all_global = 0
egg_remain_global = 0
step_used_global = 0
climb_used_global = 0
score_global = 0


def cls():
    os.system('cls')


def get_lang(force):
    global lang
    flag = True
    while flag:
        inp = input(lang["lang.set.tip"])
        if inp == '1':
            lang = EN
            flag = False
        elif inp == '2':
            lang = ZH_CN
            flag = False
        elif inp == '3':
            lang = ZH_HK
            flag = False
        else:
            if force:
                cls()
                print(lang["lang.set.error.bad_input"])
            else:
                flag = False
                cls()


def initialize():
    global lang
    if not os.path.exists(file_data):
        get_lang(True)
        with open(file_data, mode='w', encoding='utf-8') as file_data_stream:
            file_data_stream.write(lang["lang.name"]+'\n')
            file_data_stream.write('0\n0\n0\n0\n0\n0')
            file_data_stream.close()
    with open(file_data, mode='r', encoding='utf-8') as file_data_stream:
        lang = globals()[file_data_stream.readline()[:-1]]
        file_data_stream.close()


initialize()
