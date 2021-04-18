from PublicReference.base import *


class 极诣·契魔者主动技能(主动技能):

    # 武器CD = {'短剑':1, '巨剑':1.1, '钝器':1.05, '太刀':0.95}

    # def 等效CD(self, 武器类型):
    #     return round(self.CD / self.恢复  * self.武器CD[武器类型], 1)

    数据 = []
    次数 = []

    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率


class 极诣·契魔者技能0(被动技能):
    名称 = '唤魔蛇腹剑'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)


class 极诣·契魔者技能1(极诣·契魔者主动技能):
    名称 = '蛇腹剑破'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 660, 727, 794, 861, 928, 995, 1062, 1129, 1196, 1263, 1330, 1397, 1464, 1531, 1598, 1665, 1732, 1799, 1866, 1933, 2000, 2067, 2134, 2201, 2268, 2335, 2402, 2469, 2536, 2603, 2670, 2737, 2804, 2870, 2937,
             3004, 3071, 3138, 3205, 3272, 3339, 3406, 3473, 3540, 3607, 3674, 3741, 3808, 3875, 3942, 4009, 4076, 4143, 4210, 4277, 4344, 4411, 4478, 4545, 4612, 4679, 4746, 4813, 4880, 4947, 5014, 5081, 5148, 5215, 5282]
    数据 = [data1]
    次数 = [4]


class 极诣·契魔者技能2(极诣·契魔者主动技能):
    名称 = '蛇腹剑舞'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 949, 1046, 1142, 1238, 1335, 1431, 1528, 1624, 1720, 1817, 1913, 2009, 2106, 2202, 2299, 2395, 2491, 2588, 2684, 2780, 2877, 2973, 3069, 3166, 3262, 3359, 3455, 3551, 3648, 3744, 3840, 3937, 4033, 4129,
             4226, 4322, 4419, 4515, 4611, 4708, 4804, 4900, 4997, 5093, 5190, 5286, 5382, 5479, 5575, 5671, 5768, 5864, 5960, 6057, 6153, 6250, 6346, 6442, 6539, 6635, 6731, 6828, 6924, 7020, 7117, 7213, 7310, 7406, 7502, 7599]
    data2 = [0, 900, 991, 1082, 1174, 1265, 1356, 1448, 1539, 1631, 1722, 1813, 1905, 1996, 2087, 2179, 2270, 2361, 2453, 2544, 2635, 2727, 2818, 2909, 3001, 3092, 3183, 3275, 3366, 3457, 3549, 3640, 3731, 3823, 3914,
             4005, 4097, 4188, 4279, 4371, 4462, 4553, 4645, 4736, 4827, 4919, 5010, 5101, 5193, 5284, 5375, 5467, 5558, 5649, 5741, 5832, 5923, 6015, 6106, 6197, 6289, 6380, 6471, 6563, 6654, 6745, 6837, 6928, 7019, 7111, 7202]
    data3 = [0, 1182, 1302, 1422, 1542, 1662, 1782, 1902, 2022, 2142, 2261, 2381, 2501, 2621, 2741, 2861, 2981, 3101, 3221, 3341, 3461, 3581, 3701, 3821, 3941, 4061, 4181, 4301, 4421, 4541, 4661, 4780, 4900, 5020, 5140,
             5260, 5380, 5500, 5620, 5740, 5860, 5980, 6100, 6220, 6340, 6460, 6580, 6700, 6820, 6940, 7060, 7180, 7299, 7419, 7539, 7659, 7779, 7899, 8019, 8139, 8259, 8379, 8499, 8619, 8739, 8859, 8979, 9099, 9219, 9339, 9459]
    数据 = [data1, data2, data3]
    次数 = [1, 1, 1]


class 极诣·契魔者技能3(极诣·契魔者主动技能):
    名称 = '蛇腹剑刺'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 2103, 2317, 2530, 2744, 2957, 3170, 3384, 3597, 3811, 4024, 4238, 4451, 4664, 4878, 5091, 5305, 5518, 5732, 5945, 6158, 6372, 6585, 6799, 7012, 7226, 7439, 7652, 7866, 8079, 8293, 8506, 8720, 8933, 9146, 9360, 9573, 9787,
             10000, 10214, 10427, 10640, 10854, 11067, 11281, 11494, 11708, 11921, 12134, 12348, 12561, 12775, 12988, 13202, 13415, 13628, 13842, 14055, 14269, 14482, 14696, 14909, 15122, 15336, 15549, 15763, 15976, 16190, 16403, 16616, 16830]
    data2 = [0, 2837, 3125, 3413, 3701, 3989, 4277, 4565, 4852, 5140, 5428, 5716, 6004, 6292, 6580, 6868, 7156, 7443, 7731, 8019, 8307, 8595, 8883, 9171, 9459, 9747, 10034, 10322, 10610, 10898, 11186, 11474, 11762, 12050, 12338, 12625, 12913,
             13201, 13489, 13777, 14065, 14353, 14641, 14929, 15216, 15504, 15792, 16080, 16368, 16656, 16944, 17232, 17520, 17807, 18095, 18383, 18671, 18959, 19247, 19535, 19823, 20111, 20398, 20686, 20974, 21262, 21550, 21838, 22126, 22414, 22702]
    数据 = [data1, data2]
    次数 = [1, 1]


class 极诣·契魔者技能4(极诣·契魔者主动技能):
    名称 = '蛇腹剑缠'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 2083, 2295, 2506, 2717, 2929, 3140, 3351, 3563, 3774, 3986, 4197, 4408, 4620, 4831, 5042, 5254, 5465, 5677, 5888, 6099, 6311, 6522, 6734, 6945, 7156, 7368, 7579, 7790, 8002, 8213, 8425, 8636, 8847, 9059, 9270, 9482, 9693,
             9904, 10116, 10327, 10538, 10750, 10961, 11173, 11384, 11595, 11807, 12018, 12230, 12441, 12652, 12864, 13075, 13286, 13498, 13709, 13921, 14132, 14343, 14555, 14766, 14978, 15189, 15400, 15612, 15823, 16034, 16246, 16457, 16669]
    data2 = [0, 1023, 1126, 1230, 1334, 1438, 1542, 1645, 1749, 1853, 1957, 2061, 2164, 2268, 2372, 2476, 2580, 2683, 2787, 2891, 2995, 3099, 3202, 3306, 3410, 3514, 3618, 3721, 3825, 3929, 4033, 4137, 4240, 4344, 4448,
             4552, 4656, 4759, 4863, 4967, 5071, 5175, 5278, 5382, 5486, 5590, 5694, 5797, 5901, 6005, 6109, 6213, 6317, 6420, 6524, 6628, 6732, 6836, 6939, 7043, 7147, 7251, 7355, 7458, 7562, 7666, 7770, 7874, 7977, 8081, 8185]
    数据 = [data1, data2]
    次数 = [1, 3]


class 极诣·契魔者技能5(极诣·契魔者主动技能):
    名称 = '蛇腹剑灭'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 523, 576, 629, 683, 736, 789, 842, 895, 948, 1001, 1055, 1108, 1161, 1214, 1267, 1320, 1373, 1426, 1480, 1533, 1586, 1639, 1692, 1745, 1798, 1852, 1905, 1958, 2011, 2064, 2117, 2170, 2223, 2277, 2330,
             2383, 2436, 2489, 2542, 2595, 2648, 2702, 2755, 2808, 2861, 2914, 2967, 3020, 3074, 3127, 3180, 3233, 3286, 3339, 3392, 3445, 3499, 3552, 3605, 3658, 3711, 3764, 3817, 3870, 3924, 3977, 4030, 4083, 4136, 4189]
    数据 = [data1]
    次数 = [12]


class 极诣·契魔者技能6(被动技能):
    名称 = '魔剑控制'
    所在等级 = 30
    等级上限 = 30
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 20:
                return round(1.000 + 0.015 * self.等级, 5)
            else:
                return round(1.300 + 0.025 * (self.等级 - 20), 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


class 极诣·契魔者技能7(极诣·契魔者主动技能):
    名称 = '血饮狂舞'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 639, 704, 769, 834, 899, 964, 1029, 1094, 1159, 1224, 1289, 1353, 1418, 1483, 1548, 1613, 1678, 1743, 1808, 1873, 1938, 2003, 2067, 2132, 2197, 2262, 2327, 2392, 2457, 2522, 2587, 2652, 2717, 2782, 2846,
             2911, 2976, 3041, 3106, 3171, 3236, 3301, 3366, 3431, 3496, 3560, 3625, 3690, 3755, 3820, 3885, 3950, 4015, 4080, 4145, 4210, 4275, 4339, 4404, 4469, 4534, 4599, 4664, 4729, 4794, 4859, 4924, 4989, 5054, 5118]
    data2 = [0, 1647, 1814, 1981, 2149, 2316, 2483, 2650, 2817, 2984, 3152, 3319, 3486, 3653, 3820, 3987, 4154, 4322, 4489, 4656, 4823, 4990, 5157, 5325, 5492, 5659, 5826, 5993, 6160, 6327, 6495, 6662, 6829, 6996, 7163, 7330, 7498,
             7665, 7832, 7999, 8166, 8333, 8501, 8668, 8835, 9002, 9169, 9336, 9503, 9671, 9838, 10005, 10172, 10339, 10506, 10674, 10841, 11008, 11175, 11342, 11509, 11676, 11844, 12011, 12178, 12345, 12512, 12679, 12847, 13014, 13181]
    数据 = [data1, data2]
    次数 = [14, 1]

    # 猩红女王
    # 多段攻击次数 +100%
    # 多段攻击力 -44%
    # 冷却时间 -10%
    # 范围 +20%
    # 最后一击攻击力 +72%
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.次数 = [14 * 2 * 0.56, 1 + 0.72]
            self.CD *= 0.9
        elif x == 1:
            self.次数 = [14 * 2 * 0.56, 1 + 1.25]
            self.CD *= 0.9

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>猩红女王</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[血饮狂舞]<br>"
            temp += "多段攻击次数 +100%<br>"
            temp += "多段攻击力 -44%<br>"
            temp += "冷却时间 -10%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "范围 +20%<br>"
            temp += "最后一击攻击力 +72%"
        elif x == 1:
            temp = "<font color='#FF00FF'>猩红女王</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[血饮狂舞]<br>"
            temp += "多段攻击次数 +100%<br>"
            temp += "多段攻击力 -44%<br>"
            temp += "冷却时间 -10%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "范围 +20%<br>"
            temp += "最后一击攻击力 +125%"
        return temp


class 极诣·契魔者技能8(极诣·契魔者主动技能):
    名称 = '碎魔剑'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 1935, 2131, 2328, 2524, 2720, 2917, 3113, 3309, 3506, 3702, 3898, 4095, 4291, 4488, 4684, 4880, 5077, 5273, 5469, 5666, 5862, 6058, 6255, 6451, 6647, 6844, 7040, 7236, 7433, 7629, 7826, 8022, 8218, 8415, 8611, 8807,
             9004, 9200, 9396, 9593, 9789, 9985, 10182, 10378, 10574, 10771, 10967, 11163, 11360, 11556, 11753, 11949, 12145, 12342, 12538, 12734, 12931, 13127, 13323, 13520, 13716, 13912, 14109, 14305, 14501, 14698, 14894, 15091, 15287, 15483]
    数据 = [data1]
    次数 = [5]


class 极诣·契魔者技能9(极诣·契魔者主动技能):
    名称 = '群魔乱舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 22
    基础 = 13855
    成长 = 2595
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5

    # [蛇腹剑 : 破]
    data1 = [0, 815, 945, 1075, 1205, 1335, 1465, 1595, 1726, 1856, 1986, 2116, 2246, 2376, 2506, 2636, 2766, 2896, 3026, 3156, 3286, 3416, 3546, 3676, 3806, 3936, 4066, 4196, 4326, 4456,
             4586, 4716, 4847, 4977, 5107, 5237, 5367, 5497, 5627, 5757, 5887, 6017, 6147, 6277, 6407, 6537, 6667, 6797, 6927, 7057, 7187, 7317, 7447, 7577, 7707, 7838, 7968, 8098, 8228, 8358, 8488]
    # [蛇腹剑 : 舞]
    data2 = [0, 1087, 1261, 1434, 1607, 1781, 1954, 2127, 2301, 2474, 2648, 2821, 2994, 3168, 3341, 3515, 3688, 3861, 4035, 4208, 4382, 4555, 4728, 4902, 5075, 5248, 5422, 5595, 5769, 5942, 6115,
             6289, 6462, 6636, 6809, 6982, 7156, 7329, 7503, 7676, 7849, 8023, 8196, 8370, 8543, 8716, 8890, 9063, 9236, 9410, 9583, 9757, 9930, 10103, 10277, 10450, 10624, 10797, 10970, 11144, 11317]
    # [蛇腹剑 : 刺]
    data3 = [0, 1631, 1891, 2151, 2411, 2671, 2931, 3191, 3452, 3712, 3972, 4232, 4492, 4752, 5012, 5272, 5532, 5792, 6052, 6312, 6573, 6833, 7093, 7353, 7613, 7873, 8133, 8393, 8653, 8913, 9173, 9433,
             9694, 9954, 10214, 10474, 10734, 10994, 11254, 11514, 11774, 12034, 12294, 12555, 12815, 13075, 13335, 13595, 13855, 14115, 14375, 14635, 14895, 15155, 15415, 15676, 15936, 16196, 16456, 16716, 16976]
    # [蛇腹剑 : 灭]
    data4 = [0, 271, 315, 358, 401, 445, 488, 531, 575, 618, 662, 705, 748, 792, 835, 878, 922, 965, 1008, 1052, 1095, 1138, 1182, 1225, 1268, 1312, 1355, 1398, 1442, 1485, 1528, 1572,
             1615, 1659, 1702, 1745, 1789, 1832, 1875, 1919, 1962, 2005, 2049, 2092, 2135, 2179, 2222, 2265, 2309, 2352, 2395, 2439, 2482, 2525, 2569, 2612, 2656, 2699, 2742, 2786, 2829]
    # [血饮狂舞]
    data5 = [0, 296, 343, 391, 438, 485, 533, 580, 627, 674, 722, 769, 816, 864, 911, 958, 1005, 1053, 1100, 1147, 1195, 1242, 1289, 1336, 1384, 1431, 1478, 1526, 1573, 1620, 1667,
             1715, 1762, 1809, 1857, 1904, 1951, 1998, 2046, 2093, 2140, 2188, 2235, 2282, 2330, 2377, 2424, 2471, 2519, 2566, 2613, 2661, 2708, 2755, 2802, 2850, 2897, 2944, 2992, 3039, 3086]
    数据 = [data1, data2, data3, data4, data5]
    次数 = [4, 3, 2, 12, 11]

    # 魔人大军
    # 幻影可使用技能增加[蛇腹剑 : 破]、 [蛇腹剑 : 舞]、 [蛇腹剑 : 刺]
    # 敌人可承受攻击的幻影数量上限增加至8个
    # 寻敌范围 +10%
    # 幻影攻击力 -28%
    # 幻影可使用技能增加[蛇腹剑 : 灭]、 [血饮狂舞]
    # 敌人可承受攻击的幻影数量上限增加至10个
    # 寻敌范围 +10%
    # 幻影攻击力 -10%
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 = 1.24
        elif x == 1:
            self.倍率 = 1.34

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>魔人大军</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[群魔乱舞]<br>"
            temp += "幻影可使用技能增加[蛇腹剑 : 破]、 [蛇腹剑 : 舞]、 [蛇腹剑 : 刺]<br>"
            temp += "敌人可承受攻击的幻影数量增加至8个<br>"
            temp += "寻敌范围 +10%<br>"
            temp += "幻影攻击力 -28%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "幻影可使用技能增加[蛇腹剑 : 灭]、 [血饮狂舞]<br>"
            temp += "敌人可承受攻击的幻影数量上限增加至10个<br>"
            temp += "寻敌范围 +10%<br>"
            temp += "幻影攻击力 -10%"
        elif x == 1:
            temp = "<font color='#FF00FF'>魔人大军</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[群魔乱舞]<br>"
            temp += "幻影可使用技能增加[蛇腹剑 : 破]、 [蛇腹剑 : 舞]、 [蛇腹剑 : 刺]<br>"
            temp += "敌人可承受攻击的幻影数量增加至8个<br>"
            temp += "寻敌范围 +10%<br>"
            temp += "幻影攻击力 -28%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "幻影可使用技能增加[蛇腹剑 : 灭]、 [血饮狂舞]<br>"
            temp += "敌人可承受攻击的幻影数量上限增加至10个<br>"
            temp += "寻敌范围 +10%<br>"
            temp += "幻影攻击力 -5%"
        return temp


class 极诣·契魔者技能10(极诣·契魔者主动技能):
    名称 = '唤魔塔莫斯之袭'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 983, 1083, 1183, 1283, 1382, 1482, 1582, 1682, 1782, 1881, 1981, 2081, 2181, 2281, 2380, 2480, 2580, 2680, 2780, 2879, 2979, 3079, 3179, 3278, 3378, 3478, 3578, 3678, 3777, 3877, 3977, 4077, 4177, 4276,
             4376, 4476, 4576, 4676, 4775, 4875, 4975, 5075, 5175, 5274, 5374, 5474, 5574, 5674, 5773, 5873, 5973, 6073, 6173, 6272, 6372, 6472, 6572, 6672, 6771, 6871, 6971, 7071, 7171, 7270, 7370, 7470, 7570, 7669, 7769, 7869]
    data2 = [0, 7730, 8515, 9299, 10083, 10868, 11652, 12436, 13221, 14005, 14789, 15573, 16358, 17142, 17926, 18711, 19495, 20279, 21064, 21848, 22632, 23416, 24201, 24985, 25769, 26554, 27338, 28122, 28907, 29691, 30475, 31259, 32044, 32828, 33612,
             34397, 35181, 35965, 36750, 37534, 38318, 39102, 39887, 40671, 41455, 42240, 43024, 43808, 44593, 45377, 46161, 46946, 47730, 48514, 49298, 50083, 50867, 51651, 52436, 53220, 54004, 54789, 55573, 56357, 57141, 57926, 58710, 59494, 60279, 61063, 61847]
    data3 = [0, 2967, 3268, 3569, 3870, 4171, 4472, 4773, 5074, 5376, 5677, 5978, 6279, 6580, 6881, 7182, 7483, 7784, 8085, 8386, 8687, 8988, 9289, 9590, 9891, 10192, 10494, 10795, 11096, 11397, 11698, 11999, 12300, 12601, 12902, 13203, 13504,
             13805, 14106, 14407, 14708, 15009, 15310, 15612, 15913, 16214, 16515, 16816, 17117, 17418, 17719, 18020, 18321, 18622, 18923, 19224, 19525, 19826, 20127, 20428, 20730, 21031, 21332, 21633, 21934, 22235, 22536, 22837, 23138, 23439, 23740]
    数据 = [data1, data2, data3]
    次数 = [8, 1, 1]

    # 塔莫斯的觉醒
    # 用除觉醒技之外的技能攻击时， 立即发动[唤魔 : 塔莫斯之袭]
    #- 删除斩击攻击
    #- 塔莫斯出现在技能命中的敌人身边发动攻击
    #- 未命中的状态下无法使用该技能
    # - 攻击力 +29%
    # 塔莫斯大小 +20%
    # 攻击力 +10%
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.39
            self.次数 = [8, 1, 0]
        elif x == 1:
            self.倍率 *= 1.48
            self.次数 = [8, 1, 0]

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>塔莫斯的觉醒</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[唤魔 : 塔莫斯之袭]<br>"
            temp += "用除觉醒技之外的技能攻击时， 立即发动[唤魔 : 塔莫斯之袭]<br>"
            temp += "- 删除斩击攻击<br>"
            temp += "- 塔莫斯出现在技能命中的敌人身边发动攻击<br>"
            temp += "- 未命中的状态下无法使用该技能<br>"
            temp += "- 攻击力 +29%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "塔莫斯大小 +20%<br>"
            temp += "攻击力 +10%"
        elif x == 1:
            temp = "<font color='#FF00FF'>塔莫斯的觉醒</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[唤魔 : 塔莫斯之袭]<br>"
            temp += "用除觉醒技之外的技能攻击时， 立即发动[唤魔 : 塔莫斯之袭]<br>"
            temp += "- 删除斩击攻击<br>"
            temp += "- 塔莫斯出现在技能命中的敌人身边发动攻击<br>"
            temp += "- 未命中的状态下无法使用该技能<br>"
            temp += "- 攻击力 +29%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "塔莫斯大小 +20%<br>"
            temp += "攻击力 +19%"
        return temp


class 极诣·契魔者技能11(被动技能):
    名称 = '贪欲之燔祭'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class 极诣·契魔者技能12(极诣·契魔者主动技能):
    名称 = '空绝斩千刃'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    倍率 = 1.1  # 三级效果
    CD = 145.0
    data1 = [0, 6948, 8559, 10171, 11782, 13393, 15005, 16616, 18227, 19838, 21450, 23061, 24672, 26283, 27895, 29506, 31117, 32729, 34340, 35951, 37562, 39174, 40785, 42396, 44007, 45619, 47230, 48841, 50453, 52064, 53675, 55286, 56898, 58509, 60120, 61732,
             63343, 64954, 66565, 68177, 69788, 71399, 73010, 74622, 76233, 77844, 79456, 81067, 82678, 84289, 85901, 87512, 89123, 90735, 92346, 93957, 95568, 97180, 98791, 100402, 102013, 103625, 105236, 106847, 108459, 110070, 111681, 113292, 114904, 116515, 118126]
    data2 = [0, 10690, 13169, 15647, 18126, 20605, 23084, 25563, 28042, 30521, 33000, 35479, 37957, 40436, 42915, 45394, 47873, 50352, 52831, 55310, 57789, 60267, 62746, 65225, 67704, 70183, 72662, 75141, 77620, 80099, 82577, 85056, 87535, 90014, 92493, 94972, 97451, 99930,
             102409, 104887, 107366, 109845, 112324, 114803, 117282, 119761, 122240, 124718, 127197, 129676, 132155, 134634, 137113, 139592, 142071, 144550, 147028, 149507, 151986, 154465, 156944, 159423, 161902, 164381, 166860, 169338, 171817, 174296, 176775, 179254, 181733]
    data3 = [0, 14966, 18436, 21907, 25377, 28848, 32318, 35788, 39259, 42729, 46200, 49670, 53141, 56611, 60082, 63552, 67022, 70493, 73963, 77434, 80904, 84375, 87845, 91315, 94786, 98256, 101727, 105197, 108668, 112138, 115609, 119079, 122549, 126020, 129490, 132961, 136431,
             139902, 143372, 146843, 150313, 153783, 157254, 160724, 164195, 167665, 171136, 174606, 178077, 181547, 185017, 188488, 191958, 195429, 198899, 202370, 205840, 209311, 212781, 216251, 219722, 223192, 226663, 230133, 233604, 237074, 240544, 244015, 247485, 250956, 254426]
    data4 = [0, 1679, 2069, 2458, 2848, 3238, 3627, 4017, 4406, 4796, 5185, 5575, 5964, 6354, 6743, 7133, 7522, 7912, 8302, 8691, 9081, 9470, 9860, 10249, 10639, 11028, 11418, 11807, 12197, 12586, 12976, 13366, 13755, 14145, 14534, 14924, 15313,
             15703, 16092, 16482, 16871, 17261, 17651, 18040, 18430, 18819, 19209, 19598, 19988, 20377, 20767, 21156, 21546, 21935, 22325, 22715, 23104, 23494, 23883, 24273, 24662, 25052, 25441, 25831, 26220, 26610, 26999, 27389, 27779, 28168, 28558]
    data5 = [0, 0, 0, 0, 0, 0, 2803, 3104, 3405, 3706, 4007, 4308, 4609, 4910, 5211, 5512, 5813, 6114, 6415, 6716, 7017, 7318, 7619, 7920, 8221, 8522, 8823, 9124, 9425, 9726, 10027, 10328, 10629, 10930, 11231, 11532, 11833, 12134,
             12435, 12736, 13037, 13338, 13639, 13940, 14241, 14542, 14843, 15144, 15445, 15746, 16047, 16348, 16649, 16950, 17251, 17552, 17853, 18154, 18455, 18756, 19057, 19358, 19659, 19960, 20261, 20562, 20863, 21164, 21465, 21766, 22067]
    数据 = [data1, data2, data3, data4, data5]
    次数 = [1, 1, 1, 7, 7]


class 极诣·契魔者技能13(极诣·契魔者主动技能):
    名称 = '唤魔逆天之普诺'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 1302, 1435, 1567, 1699, 1831, 1963, 2095, 2228, 2360, 2492, 2624, 2756, 2888, 3021, 3153, 3285, 3417, 3549, 3681, 3814, 3946, 4078, 4210, 4342, 4474, 4607, 4739, 4871, 5003, 5135, 5267, 5400, 5532, 5664,
             5796, 5928, 6061, 6193, 6325, 6457, 6589, 6721, 6854, 6986, 7118, 7250, 7382, 7514, 7647, 7779, 7911, 8043, 8175, 8307, 8440, 8572, 8704, 8836, 8968, 9100, 9233, 9365, 9497, 9629, 9761, 9893, 10026, 10158, 10290, 10422]
    data2 = [0, 1085, 1195, 1305, 1416, 1526, 1636, 1746, 1856, 1966, 2076, 2187, 2297, 2407, 2517, 2627, 2737, 2847, 2958, 3068, 3178, 3288, 3398, 3508, 3618, 3729, 3839, 3949, 4059, 4169, 4279, 4389, 4500, 4610, 4720,
             4830, 4940, 5050, 5160, 5271, 5381, 5491, 5601, 5711, 5821, 5931, 6042, 6152, 6262, 6372, 6482, 6592, 6702, 6813, 6923, 7033, 7143, 7253, 7363, 7473, 7584, 7694, 7804, 7914, 8024, 8134, 8244, 8355, 8465, 8575, 8685]
    data3 = [0, 6427, 7079, 7731, 8383, 9035, 9687, 10339, 10991, 11643, 12296, 12948, 13600, 14252, 14904, 15556, 16208, 16860, 17512, 18164, 18816, 19468, 20120, 20772, 21424, 22076, 22729, 23381, 24033, 24685, 25337, 25989, 26641, 27293, 27945, 28597,
             29249, 29901, 30553, 31205, 31857, 32509, 33161, 33814, 34466, 35118, 35770, 36422, 37074, 37726, 38378, 39030, 39682, 40334, 40986, 41638, 42290, 42942, 43594, 44247, 44899, 45551, 46203, 46855, 47507, 48159, 48811, 49463, 50115, 50767, 51419]
    数据 = [data1, data2, data3]
    次数 = [5, 8, 1]

    # 魔人监狱
    # 克库斯和塔莫斯在角色前方出现并发动攻击
    #- 克库斯的攻击可以吸附敌人
    # - 塔莫斯终结爆炸攻击力 +8%
    # 敌人被克库斯和塔莫斯击中时无法行动
    # 塔莫斯终结爆炸范围 +20%

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.次数 = [5, 8, 1 + 0.08]

        elif x == 1:
            self.次数 = [5, 8, 1 + 0.08 + 0.31]

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>魔人监狱</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[唤魔 : 逆天之普诺]<br>"
            temp += "克库斯和塔莫斯在角色前方出现并发动攻击<br>"
            temp += "- 克库斯的攻击可以吸附敌人<br>"
            temp += "- 塔莫斯终结爆炸攻击力 +8%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "敌人被克库斯和塔莫斯击中时无法行动<br>"
            temp += "塔莫斯终结爆炸范围 +20%"
        elif x == 1:
            temp = "<font color='#FF00FF'>魔人监狱</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[唤魔 : 逆天之普诺]<br>"
            temp += "克库斯和塔莫斯在角色前方出现并发动攻击<br>"
            temp += "- 克库斯的攻击可以吸附敌人<br>"
            temp += "- 塔莫斯终结爆炸攻击力 +8%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "敌人被克库斯和塔莫斯击中时无法行动<br>"
            temp += "塔莫斯终结爆炸范围 +20%<br>"
            temp += "塔莫斯终结爆炸攻击力 +31%<br>"
        return temp


class 极诣·契魔者技能14(极诣·契魔者主动技能):
    名称 = '汲血魔剑'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 32119, 35377, 38636, 41894, 45153, 48411, 51670, 54928, 58187, 61445, 64704, 67962, 71221, 74479, 77738, 80996, 84255, 87513, 90772, 94030, 97289,
             100547, 103806, 107064, 110322, 113581, 116839, 120098, 123356, 126615, 129873, 133132, 136390, 139649, 142907, 146166, 149424, 152683, 155941, 159200]
    数据 = [data1]
    次数 = [1]

    # 魔血峥嵘
    # 施放蛇腹剑技能过程中， 可以强制中断并立即施放[汲血魔剑]
    # - 施放[汲血魔剑]过程中， 可以强制中断并施放其他蛇腹剑技能
    # - 中断蛇腹剑技能施放[汲血魔剑]时删除施放动作
    # - 施放[蛇腹剑 : 缠]、 [弑神剑 : 极]、 [空绝斩 : 地裂]时无法强制中断
    # - 攻击力 +7%
    # 范围 +20%
    # 攻击力 +7%
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.次数 = [1 + 0.07 + 0.07]
        elif x == 1:
            self.次数 = [1 + 0.07 + 0.15]

    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>魔血峥嵘</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[汲血魔剑]<br>"
            temp += "施放蛇腹剑技能过程中， 可以强制中断并立即施放[汲血魔剑]<br>"
            temp += "- 施放[汲血魔剑]过程中， 可以强制中断并施放其他蛇腹剑技能<br>"
            temp += "- 中断蛇腹剑技能施放[汲血魔剑]时删除施放动作<br>"
            temp += "- 施放[蛇腹剑 : 缠]、 [弑神剑 : 极]、 [空绝斩 : 地裂]时无法强制中断<br>"
            temp += "- 攻击力 +7%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "范围 +20%<br>"
            temp += "攻击力 +7%"
        elif x == 1:
            temp = "<font color='#FF00FF'>魔血峥嵘</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[汲血魔剑]<br>"
            temp += "施放蛇腹剑技能过程中， 可以强制中断并立即施放[汲血魔剑]<br>"
            temp += "- 施放[汲血魔剑]过程中， 可以强制中断并施放其他蛇腹剑技能<br>"
            temp += "- 中断蛇腹剑技能施放[汲血魔剑]时删除施放动作<br>"
            temp += "- 施放[蛇腹剑 : 缠]、 [弑神剑 : 极]、 [空绝斩 : 地裂]时无法强制中断<br>"
            temp += "- 攻击力 +7%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "范围 +20%<br>"
            temp += "攻击力 +15%"
        return temp


class 极诣·契魔者技能15(被动技能):
    名称 = '唤魔弑神剑'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

    def 特殊倍率(self):
        return round(1.38 + 0.02 * self.等级, 5)

    data = [0, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11,
            12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19]

    def 次数加成(self):
        return self.data[self.等级]


class 极诣·契魔者技能16(极诣·契魔者主动技能):
    名称 = '空绝斩地裂'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    CD = 40.0
    data1 = [0, 51106, 56291, 61476, 66661, 71845, 77030, 82215, 87400, 92584, 97769, 102954, 108139, 113324, 118508, 123693, 128878, 134063, 139247, 144432, 149617, 154802, 159986, 165171, 170356, 175541, 180725, 185910, 191095, 196280, 201464, 206649, 211834, 217019, 222203, 227388,
             232573, 237758, 242943, 248127, 253312, 258497, 263682, 268866, 274051, 279236, 284421, 289605, 294790, 299975, 305160, 310344, 315529, 320714, 325899, 331083, 336268, 341453, 346638, 351822, 357007, 362192, 367377, 372561, 377746, 382931, 388116, 393301, 398485, 403670, 408855]
    数据 = [data1]
    次数 = [1]

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.34


class 极诣·契魔者技能17(极诣·契魔者主动技能):
    名称 = '弑神剑极'
    备注 = '(无法抓取)'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    CD = 45.0
    data1 = [0, 56553, 62292, 68031, 73765, 79503, 85242, 90981, 96716, 102454, 108192, 113931, 119670, 125405, 131143, 136882, 142620, 148355, 154093, 159832, 165571, 171306, 177043, 182782, 188521, 194256, 199995, 205733, 211471, 217210, 222945, 228683, 234422, 240161, 245895, 251634,
             257372, 263111, 268846, 274585, 280322, 286061, 291796, 297535, 303273, 309012, 314746, 320485, 326224, 331962, 337701, 343436, 349174, 354912, 360651, 366386, 372125, 377864, 383601, 389336, 395075, 400814, 406552, 412287, 418025, 423764, 429502, 435237, 440976, 446714, 452453]
    数据 = [data1]
    次数 = [1]

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.34
            self.CD *= 0.9


class 极诣·契魔者技能18(极诣·契魔者主动技能):
    名称 = '弑神剑诸神献祭'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    CD = 180.0
    data1 = [0, 4288, 5282, 6276, 7271, 8265, 9259, 10254, 11248, 12242, 13237, 14231, 15225, 16220, 17214, 18208, 19203, 20197, 21191, 22186, 23180, 24174, 25169, 26163, 27157, 28151, 29146, 30140, 31134, 32129, 33123, 34117, 35112, 36106, 37100, 38095,
             39089, 40083, 41078, 42072, 43066, 44061, 45055, 46049, 47044, 48038, 49032, 50027, 51021, 52015, 53010, 54004, 54998, 55993, 56987, 57981, 58976, 59970, 60964, 61959, 62953, 63947, 64942, 65936, 66930, 67925, 68919, 69913, 70908, 71902, 72896]
    data2 = [0, 15892, 19578, 23263, 26948, 30633, 34319, 38004, 41689, 45375, 49060, 52745, 56430, 60116, 63801, 67486, 71172, 74857, 78542, 82227, 85913, 89598, 93283, 96968, 100654, 104339, 108024, 111710, 115395, 119080, 122765, 126451, 130136, 133821, 137507, 141192, 144877,
             148562, 152248, 155933, 159618, 163304, 166989, 170674, 174359, 178045, 181730, 185415, 189101, 192786, 196471, 200156, 203842, 207527, 211212, 214898, 218583, 222268, 225953, 229639, 233324, 237009, 240695, 244380, 248065, 251750, 255436, 259121, 262806, 266491, 270177]
    data3 = [0, 59373, 73140, 86908, 100676, 114443, 128211, 141978, 155746, 169514, 183281, 197049, 210817, 224584, 238352, 252120, 265887, 279655, 293423, 307190, 320958, 334726, 348493, 362261, 376029, 389796, 403564, 417332, 431099, 444867, 458635, 472402, 486170, 499938, 513705, 527473,
             541241, 555008, 568776, 582544, 596311, 610079, 623847, 637614, 651382, 665150, 678917, 692685, 706453, 720220, 733988, 747755, 761523, 775291, 789058, 802826, 816594, 830361, 844129, 857897, 871664, 885432, 899200, 912967, 926735, 940503, 954270, 968038, 981806, 995573, 1009341]
    数据 = [data1, data2, data3]
    次数 = [10, 3, 1]


class 极诣·契魔者技能19(被动技能):
    名称 = '魔源觉醒'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 极诣·契魔者技能20(极诣·契魔者主动技能):
    名称 = '蛇舞血轮剑'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 105546.60
    成长 = 11917.40
    CD = 60.0
    data1 = [0, 11746, 12938, 14130, 15321, 16513, 17705, 18896, 20088, 21280, 22472, 23663, 24855, 26047, 27238, 28430, 29622, 30813, 32005, 33197, 34388, 35580, 36772, 37964, 39155, 40347, 41539, 42730, 43922, 45114, 46305, 47497, 48689, 49881, 51072,
             52264, 53456, 54647, 55839, 57031, 58222, 59414, 60606, 61798, 62989, 64181, 65373, 66564, 67756, 68948, 70139, 71331, 72523, 73715, 74906, 76098, 77290, 78481, 79673, 80865, 82056, 83248, 84440, 85631, 86823, 88015, 89207, 90398, 91590, 92782, 93973]
    data2 = [0, 70480, 77630, 84780, 91930, 99081, 106231, 113381, 120531, 127681, 134832, 141982, 149132, 156282, 163432, 170583, 177733, 184883, 192033, 199183, 206333, 213484, 220634, 227784, 234934, 242084, 249235, 256385, 263535, 270685, 277835, 284985, 292136, 299286, 306436, 313586,
             320736, 327887, 335037, 342187, 349337, 356487, 363638, 370788, 377938, 385088, 392238, 399388, 406539, 413689, 420839, 427989, 435139, 442290, 449440, 456590, 463740, 470890, 478040, 485191, 492341, 499491, 506641, 513791, 520942, 528092, 535242, 542392, 549542, 556693, 563843]
    数据 = [data1, data2]
    次数 = [4, 1]


class 极诣·契魔者技能21(极诣·契魔者主动技能):
    名称 = '弑神剑恶魔孤岛'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 296448.00
    成长 = 89516.00
    CD = 290.0
    data1 = [0, 10293, 12679, 15066, 17453, 19840, 22227, 24613, 27000, 29387, 31774, 34161, 36547, 38934, 41321, 43708, 46095, 48481, 50868, 53255,
             55642, 58029, 60415, 62802, 65189, 67576, 69963, 72349, 74736, 77123, 79510, 81897, 84283, 86670, 89057, 91444, 93831, 96217, 98604, 100991, 103378]
    data2 = [0, 231594, 285297, 339000, 392703, 446406, 500109, 553812, 607515, 661218, 714921, 768624, 822327, 876030, 929733, 983436, 1037139, 1090842, 1144545, 1198248, 1251952,
             1305655, 1359358, 1413061, 1466764, 1520467, 1574170, 1627873, 1681576, 1735279, 1788982, 1842685, 1896388, 1950091, 2003794, 2057497, 2111200, 2164903, 2218606, 2272309, 2326012]
    数据 = [data1, data2]
    次数 = [15, 1]

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0


极诣·契魔者技能列表 = []
i = 0
while i >= 0:
    try:
        exec('极诣·契魔者技能列表.append(极诣·契魔者技能'+str(i)+'())')
        i += 1
    except:
        i = -1

极诣·契魔者技能序号 = dict()
for i in range(len(极诣·契魔者技能列表)):
    极诣·契魔者技能序号[极诣·契魔者技能列表[i].名称] = i

极诣·契魔者一觉序号 = 0
极诣·契魔者二觉序号 = 0
极诣·契魔者三觉序号 = 0
for i in 极诣·契魔者技能列表:
    if i.所在等级 == 50:
        极诣·契魔者一觉序号 = 极诣·契魔者技能序号[i.名称]
    if i.所在等级 == 85:
        极诣·契魔者二觉序号 = 极诣·契魔者技能序号[i.名称]
    if i.所在等级 == 100:
        极诣·契魔者三觉序号 = 极诣·契魔者技能序号[i.名称]

极诣·契魔者护石选项 = ['无']
for i in 极诣·契魔者技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        极诣·契魔者护石选项.append(i.名称)

极诣·契魔者符文选项 = ['无']
for i in 极诣·契魔者技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        极诣·契魔者符文选项.append(i.名称)


class 极诣·契魔者角色属性(角色属性):

    实际名称 = '极诣·契魔者'
    角色 = '鬼剑士(女)'
    职业 = '契魔者'

    武器选项 = ['巨剑', '钝器', '太刀', '短剑']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量']

    主BUFF = 2.00

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(极诣·契魔者技能列表)
        self.技能序号 = deepcopy(极诣·契魔者技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()

        x = self.技能栏[self.技能序号['唤魔弑神剑']].加成倍率(self.武器类型)
        self.技能栏[self.技能序号['血饮狂舞']].被动倍率 /= x
        self.技能栏[self.技能序号['唤魔塔莫斯之袭']].被动倍率 /= x

        y = self.技能栏[self.技能序号['魔源觉醒']].加成倍率(self.武器类型)
        self.技能栏[self.技能序号['蛇腹剑缠']].被动倍率 *= (x + y - 1) / (x * y)

        唤魔弑神剑 = self.技能栏[self.技能序号['唤魔弑神剑']]
        self.技能栏[self.技能序号['血饮狂舞']].被动倍率 *= 唤魔弑神剑.特殊倍率()
        self.技能栏[self.技能序号['唤魔塔莫斯之袭']].次数[1] = 唤魔弑神剑.特殊倍率()
        self.技能栏[self.技能序号['唤魔塔莫斯之袭']].次数[0] = 8 + 唤魔弑神剑.次数加成()


class 极诣·契魔者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 极诣·契魔者角色属性()
        self.角色属性A = 极诣·契魔者角色属性()
        self.角色属性B = 极诣·契魔者角色属性()
        self.一觉序号 = 极诣·契魔者一觉序号
        self.二觉序号 = 极诣·契魔者二觉序号
        self.三觉序号 = 极诣·契魔者三觉序号
        self.护石选项 = deepcopy(极诣·契魔者护石选项)
        self.符文选项 = deepcopy(极诣·契魔者符文选项)
