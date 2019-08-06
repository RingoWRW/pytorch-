#!/use/bin/env python3
# -*- coding uft-8 -*-
# @Time     :2019/8/6 16:07
__author__ = 'Ringo_wu'

menu = {'汽车':{'德系汽车':{'大众','宝马','奥迪'},'美系汽车':{'Jeep','悍马','特斯拉'},'中系汽车':{'众泰','BYD'}},
        '自行车':{'中系自行车':{'上海','北京'},'德系自行车':{'捷安特自行车','宝马自行车'},'美系自行车':{'美利达','JEEP'}},
        '电动车':{'中系电动车':{'艾玛','众泰电动车'},'德系电动车':{'捷安特电动车','宝马电动车'},'美系电动车':{'特斯拉电动车'}}}

layer = [menu]
tag = True
while tag:
    p = {}  # 存储编号和对应名称
    now_layer = layer[-1]

    if len(layer) == 1:
        print('啥子车')
    if len(layer) == 2:
        print('啥子国家的啥车')
    if len(layer) == 3:
        print('啥子型号的车')

    for i, k in zip(range(len(now_layer)), now_layer):
        print("编号:{}{}名称:{}".format(i + 1, ' ' * 8, k))
        p[i + 1] = k

    key = input('请输出操作')   # q exit  b continue

    if key == 'q':
        break
    if key == 'b':
        continue

    try:
        key = p[eval(key)]
        layer.append(now_layer[key])
    except:
        continue