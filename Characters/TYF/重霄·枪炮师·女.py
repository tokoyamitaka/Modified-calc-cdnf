from PublicReference.carry.base import *

等级 = 100 + 5


class 主动技能(主动技能):
    def 等效CD(self, 武器类型, 输出类型):
        # 重火器精通取消除觉醒之外的技能惩罚
        if self.所在等级 not in [50, 85, 100]:
            return round(self.CD / self.恢复, 1)
        else:
            return super().等效CD(武器类型, 输出类型)


class 技能0(主动技能):
    名称 = 'M3喷火器'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    data0 = [(i*1.051) for i in [0, 207, 228, 250, 270, 291, 313, 333, 355, 376, 396, 418, 439, 460, 481, 502, 523, 544, 566, 586, 607, 629, 649, 671, 692, 712, 734, 755, 776, 797, 818, 839, 860, 882, 902, 923, 945, 965, 987,
                                 1008, 1028, 1050, 1071, 1092, 1113, 1134, 1155, 1176, 1198, 1218, 1239, 1261, 1281, 1303, 1324, 1344, 1366, 1387, 1408, 1429, 1450, 1471, 1492, 1514, 1534, 1555, 1577, 1597, 1619, 1640, 1660]]
    攻击次数 = 14
    CD = 7.0
    TP成长 = 0.08
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (self.攻击次数 + (1 if self.TP等级 >= 5 else 0)) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能1(被动技能):
    名称 = '重火器精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['所有']
    关联技能2 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.01 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率2(武器类型)


class 技能2(主动技能):
    名称 = '加农炮'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    # 1235 1169
    data0 = [(i*1.0565*1.051) for i in [0, 1062, 1169, 1278, 1385, 1492, 1601, 1708, 1817, 1924, 2031, 2140, 2247, 2356, 2463, 2570, 2679, 2786, 2895, 3002, 3109, 3218, 3325, 3433, 3541, 3648, 3757, 3864, 3972, 4080, 4187, 4295, 4403,
                                        4511, 4619, 4726, 4834, 4942, 5050, 5158, 5265, 5373, 5481, 5589, 5696, 5804, 5912, 6020, 6127, 6235, 6343, 6451, 6558, 6666, 6774, 6882, 6990, 7097, 7205, 7313, 7421, 7529, 7636, 7744, 7852, 7959, 8068, 8175, 8283, 8391, 8498]]
    攻击次数 = 2
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能3(主动技能):
    名称 = '反坦克炮'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    # 187 158
    data0 = [(i*1.1835*1.051) for i in [0, 144, 158, 172, 188, 202, 216, 230, 245, 260, 274, 289, 303, 318, 333, 348, 361, 376, 392, 405, 420, 435, 449, 464, 479, 492, 508, 523, 537, 551, 566, 581, 595, 610,
                                        624, 639, 654, 668, 683, 697, 712, 727, 741, 755, 771, 785, 799, 814, 828, 843, 858, 873, 886, 902, 917, 930, 945, 961, 974, 989, 1004, 1017, 1033, 1048, 1062, 1076, 1092, 1106, 1120, 1134, 1149]]
    # 980 825
    data1 = [(i*1.1879*1.051) for i in [0, 750, 825, 902, 979, 1055, 1131, 1208, 1283, 1360, 1435, 1512, 1588, 1663, 1740, 1815, 1892, 1968, 2044, 2121, 2198, 2273, 2350, 2426, 2501, 2578, 2653, 2730, 2806, 2882, 2958, 3035, 3110,
                                        3187, 3263, 3339, 3416, 3491, 3568, 3644, 3720, 3796, 3872, 3948, 4025, 4100, 4176, 4253, 4329, 4406, 4481, 4558, 4634, 4710, 4786, 4863, 4938, 5014, 5090, 5166, 5243, 5318, 5395, 5472, 5548, 5624, 5700, 5776, 5852, 5928, 6004]]
    攻击次数2 = 3
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能4(被动技能):
    名称 = 'APG63'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.14 + 0.01 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


class 技能5(主动技能):
    名称 = '激光炮'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    # 3163 2693
    data0 = [(i*1.1745*1.052) for i in [0, 2444, 2693, 2940, 3188, 3436, 3684, 3933, 4180, 4429, 4677, 4924, 5173, 5420, 5669, 5917, 6164, 6413, 6660, 6909, 7157, 7405, 7653, 7900, 8149, 8397, 8645, 8893, 9140, 9389, 9637, 9885, 10133, 10380, 10629, 10877,
                                        11125, 11373, 11622, 11869, 12117, 12365, 12613, 12862, 13109, 13358, 13605, 13853, 14102, 14349, 14598, 14845, 15093, 15342, 15589, 15838, 16085, 16334, 16582, 16829, 17078, 17325, 17574, 17822, 18069, 18318, 18566, 18814, 19062, 19309, 19558]]
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能6(被动技能):
    名称 = '蓄电激光炮'
    所在等级 = 25
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['激光炮']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.25+0.05 * self.等级, 5)


class 技能7(主动技能):
    名称 = '聚焦喷火器'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    # 263 224
    data0 = [(i*1.1741*1.052) for i in [0, 203, 224, 244, 265, 285, 306, 327, 347, 368, 389, 409, 430, 450, 471, 492, 512, 533, 554, 574, 595, 616, 636, 657, 677, 698, 719, 739, 760, 781, 801, 822, 842, 863, 884, 904,
                                        925, 946, 966, 987, 1008, 1028, 1049, 1069, 1090, 1111, 1131, 1152, 1173, 1193, 1214, 1234, 1255, 1276, 1296, 1317, 1338, 1358, 1379, 1398, 1419, 1440, 1460, 1481, 1502, 1522, 1543, 1563, 1584, 1605, 1625]]
    攻击次数 = 29
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能8(主动技能):
    名称 = 'FM31榴弹发射器'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    # 1077 916
    data0 = [(i*1.1758*1.052) for i in [0, 831, 916, 1000, 1084, 1168, 1253, 1337, 1423, 1507, 1591, 1675, 1760, 1844, 1929, 2013, 2097, 2181, 2266, 2350, 2436, 2520, 2604, 2688, 2773, 2857, 2942, 3026, 3110, 3194, 3279, 3363, 3448,
                                        3532, 3616, 3700, 3786, 3870, 3955, 4039, 4123, 4207, 4292, 4376, 4461, 4545, 4629, 4713, 4799, 4883, 4968, 5052, 5135, 5220, 5304, 5389, 5473, 5558, 5642, 5724, 5808, 5891, 5975, 6057, 6141, 6223, 6307, 6390, 6474, 6556]]
    攻击次数 = 8
    CD = 15.0
    TP成长 = 0.20
    TP上限 = 1

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础释放次数 = 4
            self.攻击次数 = 2
            self.倍率 *= 1.18
            self.CD *= float(4 / 15)
        elif x == 1:
            self.基础释放次数 = 4
            self.攻击次数 = 2
            self.倍率 *= 1.27
            self.CD *= float(4 / 15)

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>M102-CERM弹药</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[FM-31榴弹发射器]<br>"
            temp += "可以补充榴弹<br>"
            temp += "榴弹冷却时间 : 4秒<br>"
            temp += "长按技能键可以连续发射<br>"
            temp += "攻击力 +18%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "装弹数上限 +2 (学习强化技能后 +1)<br>"
            temp += "爆炸范围 +20%"
        elif x == 1:
            temp = "<font color='#FF00FF'>M102-CERM弹药</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[FM-31榴弹发射器]<br>"
            temp += "可以补充榴弹<br>"
            temp += "榴弹冷却时间 : 4秒<br>"
            temp += "长按技能键可以连续发射<br>"
            temp += "攻击力 +18%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "装弹数上限 +2 (学习强化技能后 +1)<br>"
            temp += "爆炸范围 +20%<br>"
            temp += "攻击力 +9%"
        return temp


class 技能9(主动技能):
    名称 = 'FM92mk2榴弹'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    # 1398 1190
    data0 = [(i*1.1748*1.052) for i in [0, 1080, 1190, 1299, 1410, 1519, 1628, 1739, 1848, 1957, 2068, 2177, 2286, 2396, 2506, 2615, 2725, 2835, 2945, 3054, 3163, 3274, 3383, 3492, 3603, 3712, 3821, 3932, 4041, 4151, 4260, 4370, 4480,
                                        4589, 4698, 4809, 4918, 5027, 5138, 5247, 5356, 5467, 5576, 5686, 5795, 5905, 6015, 6124, 6234, 6344, 6453, 6562, 6673, 6782, 6891, 7002, 7111, 7221, 7331, 7440, 7550, 7659, 7769, 7879, 7988, 8098, 8208, 8317, 8428, 8537, 8646]]
    攻击次数 = 8
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能10(主动技能):
    名称 = '量子爆弹'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    # 873 743
    data1 = [(i*1.1750*1.085) for i in [0, 675, 743, 812, 880, 949, 1016, 1085, 1154, 1222, 1291, 1359, 1428, 1497, 1565, 1634, 1701, 1770, 1838, 1907, 1976, 2044, 2113, 2181, 2250, 2317, 2386, 2455, 2523, 2592, 2660, 2729, 2798,
                                        2866, 2935, 3002, 3071, 3140, 3208, 3277, 3345, 3414, 3482, 3551, 3620, 3687, 3756, 3824, 3893, 3962, 4030, 4099, 4167, 4236, 4305, 4372, 4441, 4509, 4578, 4646, 4715, 4784, 4852, 4921, 4989, 5057, 5125, 5194, 5263, 5331, 5400]]
    攻击次数1 = 1
    # 10047 8550
    data2 = [(i*1.1751*1.085) for i in [0, 7762, 8550, 9337, 10125, 10913, 11701, 12487, 13275, 14063, 14850, 15638, 16426, 17212, 18000, 18788, 19576, 20363, 21151, 21938, 22725, 23513, 24301, 25089, 25876, 26663, 27451, 28238, 29026, 29814, 30602, 31388, 32176, 32964,
                                        33751, 34539, 35327, 36113, 36901, 37689, 38477, 39264, 40052, 40839, 41626, 42414, 43202, 43990, 44776, 45564, 46352, 47139, 47927, 48715, 49501, 50289, 51077, 51865, 52652, 53440, 54227, 55014, 55802, 56590, 57378, 58165, 58952, 59740, 60527, 61315, 62103]]
    攻击次数2 = 1

    # 感电
    data3 = [(i*1.0) for i in [0, 10, 10, 10, 10, 10, 10, 11, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 19, 19, 20, 21, 21, 22, 23, 23, 24, 25, 25, 26, 27, 27, 28, 29, 30, 30, 31, 32, 32, 33, 34, 34, 35, 36, 36, 37, 38, 39, 39, 40, 41, 41,
                               42, 43, 43, 44, 45, 45, 46, 47, 47, 48, 49, 50, 50, 51, 52, 52, 53, 54, 54]]
    攻击次数3 = 10
    CD = 18.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数1 + self.data2[self.等级] * self.攻击次数2 + self.data3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 0
            self.攻击次数2 = 0.16 * 8 * 1.07
            self.攻击次数3 *= 0.16 * 8 * 1.07
            self.CD *= 0.9
        elif x == 1:
            self.攻击次数1 = 0
            self.攻击次数2 = 0.16 * 8 * 1.14
            self.攻击次数3 *= 0.16 * 8 * 1.14
            self.CD *= 0.9

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>原力轰炸</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[量子爆弹]<br>"
            temp += "变更为地毯式轰炸<br>"
            temp += "删除导弹物理攻击力<br>"
            temp += "导弹大小 -65%<br>"
            temp += "每次爆炸攻击力 -84%<br>"
            temp += "爆炸次数 +7次<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -10%<br>"
            temp += "爆炸攻击力 +7%"
        elif x == 1:
            temp = "<font color='#FF00FF'>原力轰炸</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[量子爆弹]<br>"
            temp += "变更为地毯式轰炸<br>"
            temp += "删除导弹物理攻击力<br>"
            temp += "导弹大小 -65%<br>"
            temp += "每次爆炸攻击力 -84%<br>"
            temp += "爆炸次数 +7次<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -10%<br>"
            temp += "爆炸攻击力 +14%"
        return temp


class 技能11(主动技能):
    名称 = 'X1压缩量子炮'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    # 23534 19226
    data0 = [(i*1.2241*1.065) for i in [0, 17455, 19226, 20996, 22767, 24538, 26310, 28081, 29851, 31622, 33393, 35164, 36934, 38705, 40476, 42247, 44018, 45789, 47560, 49331, 51101, 52872, 54643, 56414, 58184, 59956, 61727, 63498, 65269, 67039, 68810, 70581, 72352, 74122, 75893,
                                        77665, 79436, 81206, 82977, 84748, 86519, 88289, 90060, 91831, 93602, 95374, 97144, 98915, 100686, 102457, 104227, 105998, 107769, 109540, 111310, 113082, 114853, 116624, 118394, 120165, 121936, 123707, 125477, 127248, 129019, 130791, 132562, 134332, 136103, 137874, 139645]]
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.1
            self.CD *= 0.88
        elif x == 1:
            self.倍率 *= 1.18
            self.CD *= 0.88

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>AC.X-1压缩量子炮</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[X-1压缩量子炮]<br>"
            temp += "立即发射并在最远射程处自动蓄气后爆炸<br>"
            temp += "冷却时间 -12%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "爆炸范围 +10%<br>"
            temp += "攻击力 +10%"
        elif x == 1:
            temp = "<font color='#FF00FF'>AC.X-1压缩量子炮</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[X-1压缩量子炮]<br>"
            temp += "立即发射并在最远射程处自动蓄气后爆炸<br>"
            temp += "冷却时间 -12%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "爆炸范围 +10%<br>"
            temp += "攻击力 +18%"
        return temp


class 技能12(被动技能):
    名称 = '超温重火器'
    所在等级 = 48
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.04 + 0.02 * self.等级, 5)


class 技能13(主动技能):
    名称 = '远古粒子炮'
    所在等级 = 50
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    # 19254 16400
    data1 = [(i*1.1740*1.05) for i in [0, 4618, 5689, 6760, 7831, 8902, 9973, 11044, 12115, 13186, 14258, 15329, 16400, 17471, 18542, 19613, 20684, 21755, 22826, 23897, 24968, 26039, 27110, 28181, 29252, 30323, 31394, 32465, 33536, 34607, 35678, 36749, 37820, 38891,
                                       39962, 41033, 42104, 43175, 44247, 45318, 46389, 47460, 48531, 49602, 50673, 51744, 52815, 53886, 54957, 56028, 57099, 58170, 59241, 60312, 61383, 62454, 63525, 64596, 65667, 66738, 67809, 68880, 69951, 71022, 72093, 73164, 74235, 75307, 76378, 77449, 78520]]
    攻击次数1 = 0
    # 22387 19069
    data2 = [(i*1.1740*1.05) for i in [0, 5370, 6615, 7861, 9106, 10352, 11597, 12843, 14088, 15334, 16579, 17823, 19069, 20314, 21560, 22805, 24051, 25296, 26542, 27787, 29033, 30278, 31524, 32769, 34013, 35259, 36504, 37750, 38995, 40241, 41486, 42732, 43977, 45223,
                                       46468, 47714, 48959, 50205, 51449, 52694, 53940, 55185, 56431, 57676, 58922, 60167, 61413, 62658, 63904, 65149, 66395, 67639, 68884, 70130, 71375, 72621, 73866, 75112, 76357, 77603, 78848, 80094, 81339, 82585, 83829, 85074, 86320, 87565, 88811, 90056, 91302]]
    攻击次数2 = 10
    CD = 145

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数1 + self.data2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能14(主动技能):
    名称 = '等离子放射器'
    所在等级 = 60
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    # 587 452
    data0 = [(i*1.2987*1.051) for i in [0, 411, 452, 494, 536, 577, 619, 660, 702, 744, 785, 827, 869, 910, 952, 994, 1035, 1077, 1119, 1160, 1202, 1244, 1285, 1327, 1369, 1410, 1452, 1493, 1535, 1577, 1618, 1661, 1703, 1744,
                                        1786, 1828, 1869, 1911, 1953, 1994, 2036, 2078, 2119, 2161, 2202, 2244, 2286, 2327, 2369, 2411, 2452, 2494, 2536, 2577, 2619, 2661, 2702, 2744, 2786, 2827, 2869, 2911, 2952, 2994, 3035, 3077, 3120, 3160, 3203, 3245, 3286]]
    攻击次数 = 37
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 1:
            self.倍率 *= 0.94
            self.CD *= 0.60
        elif x == 0:
            self.倍率 *= 0.85
            self.CD *= 0.60

    def 护石描述(self, x):
        if x == 1:
            temp = "<font color='#FF00FF'>高功率等离子体发生器</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[等离子放射器]<br>"
            temp += "立即发射等离子放射器<br>"
            temp += "发射位置残留电场<br>"
            temp += "总攻击力 +8%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -40%<br>"
            temp += "总攻击力 -23%"
        elif x == 0:
            temp = "<font color='#FF00FF'>高功率等离子体发生器</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[等离子放射器]<br>"
            temp += "立即发射等离子放射器<br>"
            temp += "发射位置残留电场<br>"
            temp += "总攻击力 +8%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -40%<br>"
            temp += "总攻击力 -14%"
        return temp


class 技能15(主动技能):
    名称 = 'FM92mk2SW榴弹'
    所在等级 = 70
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    # 4143 3758
    data0 = [(i*1.1024*1.1) for i in [0, 3411, 3758, 4103, 4450, 4796, 5143, 5488, 5835, 6181, 6527, 6873, 7220, 7565, 7912, 8258, 8604, 8950, 9297, 9642, 9989, 10335, 10681, 11027, 11374, 11719, 12066, 12412, 12758, 13104, 13451, 13796, 14142, 14489, 14834,
                                      15181, 15527, 15873, 16219, 16566, 16911, 17258, 17604, 17950, 18296, 18643, 18988, 19335, 19681, 20027, 20373, 20720, 21066, 21412, 21758, 22105, 22450, 22797, 23143, 23489, 23835, 24182, 24527, 24873, 25220, 25565, 25912, 26258, 26604, 26950, 27297]]
    攻击次数 = 8
    # 205 186
    data1 = [(i*1.1022*1.1) for i in [0, 169, 186, 204, 221, 237, 255, 272, 289, 307, 323, 340, 358, 375, 393, 410, 426, 444, 461, 478, 496, 512, 530, 547, 564, 582, 599, 615, 633, 650, 667, 685, 701, 719, 736,
                                      753, 771, 788, 804, 822, 839, 857, 874, 890, 908, 925, 942, 960, 977, 993, 1011, 1028, 1046, 1063, 1079, 1097, 1114, 1131, 1149, 1166, 1182, 1200, 1217, 1235, 1252, 1268, 1286, 1303, 1320, 1338, 1355]]
    攻击次数2 = 24
    # 灼烧攻击力,在点TP之后删除
    data2 = [(i*1.0) for i in [0, 28, 31, 34, 36, 39, 42, 45, 48, 51, 53, 56, 59, 62, 65, 68, 70, 73, 76, 79, 82, 85, 87, 90, 93, 96, 99, 102, 104, 107, 110, 113, 116, 119, 121, 124,
                               127, 130, 133, 136, 138, 141, 144, 147, 150, 153, 155, 158, 161, 164, 167, 170, 172, 175, 178, 181, 184, 187, 189, 192, 195, 198, 201, 204, 206, 209, 212, 215, 218, 221, 223]]
    攻击次数3 = 0
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级]*self.攻击次数 + self.data1[self.等级]*self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.27
            self.CD *= 0.9

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>MIBC诱导装置</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[FM-92 mk2 SW榴弹]<br>"
            temp += "删除长按技能键操作<br>"
            temp += "诱导范围扩大为长按操作可调整的范围<br>"
            temp += "攻击力 +14%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -10%<br>"
            temp += "攻击力 +5%</font>"
        elif x == 1:
            temp = "<font color='#FF00FF'>MIBC诱导装置</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[FM-92 mk2 SW榴弹]<br>"
            temp += "删除长按技能键操作<br>"
            temp += "诱导范围扩大为长按操作可调整的范围<br>"
            temp += "攻击力 +14%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -10%<br>"
            temp += "攻击力 +13%</font>"
        return temp


class 技能16(被动技能):
    名称 = '重武装改造'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)


class 技能17(主动技能):
    名称 = 'FSC7'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    # 2647 2249
    data1 = [(i*1.1770*1.052) for i in [0, 2042, 2249, 2457, 2663, 2871, 3078, 3285, 3492, 3700, 3906, 4113, 4320, 4528, 4736, 4942, 5150, 5357, 5564, 5771, 5979, 6185, 6393, 6600, 6806, 7015, 7223, 7429, 7636, 7844, 8050, 8258, 8465, 8672, 8879, 9087,
                                        9293, 9500, 9709, 9915, 10123, 10329, 10537, 10744, 10951, 11158, 11366, 11572, 11780, 11987, 12195, 12402, 12610, 12816, 13023, 13231, 13437, 13645, 13852, 14059, 14266, 14474, 14680, 14889, 15096, 15302, 15510, 15716, 15924, 16131, 16338]]
    攻击次数1 = 1
    # 5030 4274
    data2 = [(i*1.1769*1.052) for i in [0, 3880, 4274, 4668, 5061, 5454, 5848, 6242, 6635, 7030, 7423, 7818, 8210, 8603, 8998, 9391, 9785, 10179, 10573, 10965, 11359, 11753, 12147, 12541, 12934, 13329, 13721, 14116, 14509, 14902, 15297, 15690, 16083, 16477, 16871,
                                        17265, 17659, 18052, 18446, 18839, 19232, 19627, 20020, 20415, 20808, 21202, 21595, 21988, 22382, 22776, 23170, 23564, 23958, 24350, 24745, 25138, 25531, 25926, 26319, 26714, 27106, 27500, 27894, 28288, 28681, 29075, 29468, 29861, 30256, 30649, 31044]]
    攻击次数2 = 10
    CD = 40.0

    def 等效百分比(self, 武器类型):
        return (self.data1[self.等级] * self.攻击次数1 + self.data2[self.等级] * self.攻击次数2) * self.倍率

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 0.64
            self.CD *= 0.45
            self.基础释放次数 = 1.0
            # self.恢复 = 1.0


class 技能18(主动技能):
    名称 = 'PT15原始型压缩炮'
    备注 = '(向前)'
    所在等级 = 80
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通) + 1
    # 66219 56254
    data0 = [(i*1.1771*1.051) for i in [0, 51073, 56254, 61435, 66617, 71797, 76979, 82161, 87342, 92523, 97705, 102886, 108067, 113248, 118430, 123612, 128792, 133974, 139156, 144336, 149518, 154699, 159881, 165062, 170243, 175425, 180605, 185787, 190969, 196150, 201331, 206512, 211694, 216875,
                                        222056, 227238, 232420, 237600, 242782, 247963, 253144, 258326, 263507, 268689, 273869, 279051, 284233, 289413, 294595, 299777, 304958, 310139, 315320, 320502, 325683, 330864, 336046, 341228, 346408, 351590, 356771, 361952, 367134, 372315, 377497, 382677, 387859, 393041, 398221, 403403, 408585]]
    CD = 45.0

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.倍率

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35


class 技能19(主动技能):
    名称 = '火力全开'
    所在等级 = 85
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    # 1258 1071
    data1 = [(i*1.1746*1.05) for i in [0, 556, 684, 814, 943, 1071, 1201, 1329, 1459, 1588, 1716, 1846, 1974, 2104, 2232, 2361, 2491, 2619, 2749, 2877, 3007, 3135, 3264, 3394, 3522, 3652, 3780, 3909, 4038, 4167, 4297, 4425, 4554,
                                       4683, 4812, 4941, 5070, 5199, 5328, 5457, 5586, 5715, 5844, 5973, 6102, 6231, 6360, 6488, 6618, 6747, 6876, 7005, 7133, 7263, 7391, 7521, 7650, 7779, 7908, 8036, 8166, 8294, 8424, 8553, 8681, 8811, 8939, 9069, 9198, 9326, 9456]]
    # 9364 7974
    data2 = [(i*1.1743*1.05) for i in [0, 4137, 5096, 6055, 7014, 7974, 8932, 9892, 10852, 11811, 12770, 13729, 14689, 15649, 16607, 17567, 18526, 19485, 20445, 21404, 22364, 23322, 24282, 25242, 26200, 27160, 28119, 29078, 30038, 30997, 31957, 32915, 33875, 34835,
                                       35793, 36753, 37712, 38672, 39631, 40590, 41550, 42508, 43468, 44428, 45387, 46346, 47305, 48265, 49223, 50183, 51143, 52102, 53061, 54020, 54980, 55940, 56898, 57858, 58817, 59776, 60736, 61695, 62654, 63613, 64573, 65533, 66491, 67451, 68410, 69369, 70329]]
    # 5351 4557
    data3 = [(i*1.1742*1.05) for i in [0, 2364, 2912, 3460, 4008, 4557, 5105, 5653, 6200, 6748, 7298, 7845, 8393, 8941, 9489, 10038, 10586, 11134, 11682, 12230, 12779, 13327, 13875, 14423, 14971, 15520, 16068, 16616, 17164, 17712, 18261, 18809, 19357, 19905, 20453,
                                       21001, 21550, 22098, 22646, 23194, 23742, 24291, 24839, 25387, 25935, 26483, 27032, 27580, 28128, 28676, 29224, 29773, 30321, 30869, 31417, 31964, 32514, 33062, 33609, 34157, 34705, 35254, 35802, 36350, 36898, 37446, 37995, 38543, 39091, 39639, 40187]]
    # 1114 949
    data4 = [(i*1.1739*1.05) for i in [0, 492, 606, 720, 835, 949, 1062, 1177, 1291, 1405, 1520, 1634, 1748, 1863, 1976, 2090, 2205, 2319, 2433, 2548, 2662, 2775, 2890, 3004, 3118, 3233, 3347, 3461, 3576, 3689, 3803, 3918, 4032, 4146,
                                       4261, 4375, 4489, 4604, 4717, 4831, 4946, 5060, 5174, 5289, 5403, 5516, 5631, 5745, 5859, 5974, 6088, 6202, 6317, 6430, 6544, 6659, 6773, 6887, 7002, 7116, 7229, 7344, 7458, 7572, 7687, 7801, 7915, 8030, 8143, 8257, 8372]]
    # 786 670
    data5 = [(i*1.1731*1.05) for i in [0, 347, 427, 508, 589, 670, 750, 830, 912, 992, 1072, 1153, 1234, 1315, 1395, 1475, 1557, 1637, 1718, 1798, 1878, 1960, 2040, 2120, 2201, 2282, 2363, 2443, 2523, 2605, 2685, 2765, 2846, 2927,
                                       3008, 3088, 3168, 3249, 3330, 3410, 3491, 3571, 3653, 3733, 3813, 3894, 3975, 4056, 4136, 4216, 4298, 4378, 4458, 4539, 4619, 4701, 4781, 4861, 4942, 5023, 5103, 5184, 5264, 5346, 5426, 5506, 5587, 5668, 5749, 5829, 5909]]
    # 1337 1138
    data6 = [(i*1.1749*1.05) for i in [0, 590, 728, 865, 1001, 1138, 1276, 1413, 1550, 1686, 1824, 1961, 2098, 2235, 2372, 2509, 2646, 2783, 2921, 3057, 3194, 3331, 3469, 3606, 3742, 3879, 4016, 4154, 4291, 4427, 4564, 4702, 4839,
                                       4976, 5112, 5250, 5387, 5524, 5661, 5798, 5935, 6072, 6209, 6347, 6483, 6620, 6757, 6895, 7032, 7168, 7305, 7443, 7580, 7717, 7853, 7991, 8128, 8265, 8402, 8539, 8676, 8813, 8950, 9088, 9224, 9361, 9498, 9636, 9773, 9909, 10046]]
    # 66892 56958
    data7 = [(i*1.1744*1.05) for i in [0, 29549, 36402, 43254, 50106, 56958, 63811, 70663, 77515, 84367, 91220, 98072, 104924, 111776, 118629, 125481, 132333, 139185, 146038, 152890, 159741, 166593, 173445, 180298, 187150, 194002, 200854, 207707, 214559, 221411, 228263, 235116, 241968, 248820, 255672,
                                       262524, 269377, 276229, 283081, 289933, 296786, 303638, 310490, 317342, 324195, 331047, 337899, 344751, 351604, 358456, 365307, 372159, 379011, 385864, 392716, 399568, 406420, 413273, 420125, 426977, 433829, 440682, 447534, 454386, 461238, 468091, 474943, 481795, 488647, 495500, 502352]]

    data0 = [data1, data2, data3, data4, data5, data6, data7]
    次数 = [17, 4, 4, 47, 37, 40, 1]
    #  次数可能有波动
    #  17 右上端辅助激光炮攻击力
    #  4 主激光炮攻击力
    #  4 左下端辅助激光炮攻击力
    #  47 左下端格林机枪攻击力
    #  37 右下端榴弹发射器攻击力
    #  40 火箭炮导弹爆炸攻击力
    #  1 火箭炮爆炸攻击力
    CD = 180.0

    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(7):
            sum += self.data0[i][self.等级] * self.次数[i]
        return sum * self.倍率


class 技能20(被动技能):
    名称 = 'Pandora_01'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能21(主动技能):
    名称 = 'UHT-03爆炎喷火器'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)+1
    CD = 60.0
    # 4920 4072
    data0 = [(i*1.2083*1.052) for i in [0, 3696, 4072, 4447, 4821, 5197, 5572, 5946, 6321, 6696, 7071, 7447, 7822, 8197, 8571, 8947, 9322, 9697, 10072, 10447, 10822, 11196, 11573, 11947, 12321, 12697, 13073, 13447, 13822, 14197, 14572, 14947, 15323, 15698, 16073,
                                        16448, 16823, 17197, 17572, 17949, 18322, 18698, 19073, 19448, 19823, 20198, 20573, 20948, 21323, 21699, 22072, 22447, 22823, 23198, 23574, 23948, 24323, 24698, 25073, 25449, 25823, 26198, 26574, 26949, 27323, 27700, 28073, 28449, 28823, 29200, 29573]]
    攻击次数 = 24

    def 等效百分比(self, 武器类型):

        # sum = (3322.4 + self.等级 * 374.8) * 24
        # for i in range(4):
        #    sum += self.data0[i][self.等级] * self.次数[i]
        # return sum * self.倍率
        return self.data0[self.等级] * self.攻击次数 * self.倍率


class 技能22(主动技能):
    名称 = '制胜·最终兵器'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    关联技能 = ['无']
    # 15927
    data1 = [(i*1.2090) for i in [0, 13174, 16230, 19286, 22340, 25396, 28452, 31506, 34562, 37616, 40672, 43728, 46782, 49838, 52894, 55948, 59003, 62059, 65114, 68169, 71226, 74280, 77335, 80391, 83445, 86501, 89556, 92611, 95667, 98722, 101777, 104832, 107888, 110943, 113998, 117054,
                                  120108, 123164, 126220, 129275, 132330, 135385, 138439, 141495, 144550, 147606, 150662, 153717, 156772, 159826, 162882, 165937, 168993, 172048, 175103, 178158, 181214, 184269, 187324, 190380, 193434, 196490, 199546, 202600, 205656, 208712, 211765, 214821, 217877, 220932, 223988]]
    # 7964
    data2 = [(i*1.2090) for i in [0, 6587, 8115, 9643, 11170, 12698, 14226, 15753, 17281, 18808, 20336, 21864, 23391, 24919, 26447, 27974, 29501, 31029, 32557, 34085, 35613, 37140, 38668, 40196, 41722, 43250, 44778, 46306, 47833, 49361, 50888, 52416, 53944, 55471, 56999,
                                  58527, 60054, 61582, 63110, 64637, 66165, 67692, 69220, 70748, 72275, 73803, 75331, 76859, 78386, 79913, 81441, 82968, 84496, 86024, 87551, 89079, 90607, 92134, 93662, 95190, 96717, 98245, 99773, 101300, 102828, 104356, 105883, 107411, 108938, 110466, 111994]]
    # 3982
    data3 = [(i*1.2125) for i in [0, 3294, 4058, 4822, 5585, 6349, 7113, 7877, 8641, 9404, 10168, 10932, 11696, 12460, 13224, 13987, 14751, 15515, 16278, 17042, 17806, 18570, 19334, 20098, 20861, 21625, 22389, 23153, 23917, 24681, 25444, 26208, 26972, 27736, 28500,
                                  29263, 30027, 30791, 31555, 32319, 33083, 33846, 34610, 35374, 36138, 36902, 37665, 38429, 39193, 39957, 40721, 41484, 42248, 43012, 43776, 44540, 45303, 46067, 46831, 47595, 48359, 49123, 49886, 50650, 51414, 52178, 52941, 53705, 54469, 55233, 55997]]
    # 9556
    data4 = [(i*1.2089) for i in [0, 7905, 9738, 11572, 13404, 15238, 17071, 18904, 20737, 22570, 24403, 26237, 28069, 29903, 31736, 33569, 35402, 37235, 39068, 40901, 42735, 44568, 46401, 48235, 50067, 51900, 53734, 55567, 57400, 59233, 61066, 62899, 64733, 66566, 68399,
                                  70232, 72065, 73898, 75732, 77565, 79398, 81231, 83064, 84897, 86730, 88564, 90397, 92230, 94063, 95896, 97729, 99562, 101396, 103229, 105062, 106895, 108728, 110561, 112395, 114228, 116061, 117894, 119727, 121560, 123394, 125227, 127059, 128893, 130726, 132559, 134393]]

    data0 = [data1, data2, data3, data4]
    次数 = [5, 5, 10, 25]
    CD = 290.0

    def 加成倍率(self, 武器类型):
        return 0.0

    def 等效百分比(self, 武器类型):
        sum = 0
        # sum = 252985 + self.等级 * 76385
        for i in range(4):
            sum += self.data0[i][self.等级] * self.次数[i]
        return sum * self.倍率


技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能'+str(i)+'())')
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

一觉序号 = 0
二觉序号 = 0
三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        三觉序号 = 技能序号[i.名称]

护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        护石选项.append(i.名称)

符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        符文选项.append(i.名称)


class 职业属性(角色属性):

    实际名称 = '重霄·枪炮师·女'
    角色 = '神枪手(女)'
    职业 = '枪炮师'

    武器选项 = ['手炮']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量']

    主BUFF = 1.957

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)


class 重霄·枪炮师·女(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业属性()
        self.角色属性A = 职业属性()
        self.角色属性B = 职业属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)
