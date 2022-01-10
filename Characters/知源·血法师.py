﻿from PublicReference.carry.base import *

# class 职业主动技能(职业主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '矛':
#             return round(self.CD / self.恢复 * 1.05, 1)

class 职业主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    data0 = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if len(self.data0) >= self.等级 and len(self.data0) > 0:
            等效倍率 += self.data0[self.等级] * self.攻击次数
        if len(self.data1) >= self.等级 and len(self.data1) > 0:
            等效倍率 += self.data1[self.等级] * self.攻击次数2
        if len(self.data2) >= self.等级 and len(self.data2) > 0:
            等效倍率 += self.data2[self.等级] * self.攻击次数3
        if len(self.data3) >= self.等级 and len(self.data3) > 0:
            等效倍率 += self.data3[self.等级] * self.攻击次数4
        if len(self.data4) >= self.等级 and len(self.data4) > 0:
            等效倍率 += self.data4[self.等级] * self.攻击次数5
        if len(self.data5) >= self.等级 and len(self.data5) > 0:
            等效倍率 += self.data5[self.等级] * self.攻击次数6
        if len(self.data6) >= self.等级 and len(self.data6) > 0:
            等效倍率 += self.data6[self.等级] * self.攻击次数7
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能0(被动技能):
    名称 = '鲜血融合'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 物理攻击力倍率进图(self, 武器类型):
        if self.等级<= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 *self.等级 , 5)
    def 加成倍率(self, 武器类型):
        if self.等级<= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 *self.等级 , 5)

class 技能1(被动技能):
    名称 = '血之共鸣'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)

class 技能2(被动技能):
    名称 = '血狱之力'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)

class 技能3(被动技能):
    名称 = '鲜血之殇'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

class 技能4(被动技能):
    名称 = '血源之眼'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 技能5(职业主动技能):
    名称 = '血蝠之袭'
    所在等级= 15
    等级上限 =60
    基础等级 =46
    #基础 = 3072.95454545
    #成长 = 347.62237762
    CD = 5
    TP成长 = 0.10
    TP上限 = 5
    data0 = [ int(i*1.1*1.085) for i in [0, 228, 251, 275, 297, 321, 344, 367, 390, 414, 436, 460, 483, 506, 529, 553, 575, 599, 622, 645, 668, 692, 715, 738, 761, 785, 807, 831, 854, 877, 900, 924, 946, 970, 993, 1016, 1039, 1063, 1085, 1109, 1132, 1155, 1178, 1202, 1225, 1248, 1271, 1295, 1317, 1341, 1364, 1387, 1410, 1434, 1456, 1480, 1503, 1526, 1549, 1573, 1595, 1619, 1642, 1665, 1688, 1712, 1735, 1758, 1781, 1805, 1827]]
    攻击次数 = 15

class 技能6(职业主动技能):
    名称 = '血翼突击'
    所在等级= 15
    等级上限 =60
    基础等级 =46
    #基础 = 2329.84763635444
    #成长 = 263.1339020924
    data0 = [ int(i*1.192*1.085) for i in [0, 2594, 2857, 3120, 3383, 3646, 3909, 4173, 4436, 4699, 4962, 5225, 5488, 5751, 6015, 6278, 6541, 6804, 7067, 7330, 7594, 7857, 8120, 8383, 8646, 8909, 9173, 9436, 9699, 9962, 10225, 10488, 10752, 11015, 11278, 11541, 11804, 12067, 12331, 12594, 12857, 13120, 13383, 13646, 13910, 14173, 14436, 14699, 14962, 15225, 15488, 15752, 16015, 16278, 16541, 16804, 17067, 17331, 17594, 17857, 18120, 18383, 18646, 18910, 19173, 19436, 19699, 19962, 20225, 20489, 20752]]
    CD = 5
    TP成长 = 0.10
    TP上限 = 5

class 技能7(职业主动技能):
    名称 = '鲜血长枪'
    所在等级= 20
    等级上限 =60
    基础等级 =43
    #基础 = 2993.1012727272
    #成长 = 337.716727272
    data0 = [ int(i*1.193*1.085) for i in [0, 1666, 1835, 2004, 2173, 2342, 2511, 2681, 2850, 3019, 3188, 3357, 3526, 3695, 3864, 4033, 4202, 4371, 4540, 4709, 4879, 5048, 5217, 5386, 5555, 5724, 5893, 6062, 6231, 6400, 6569, 6738, 6907, 7077, 7246, 7415, 7584, 7753, 7922, 8091, 8260, 8429, 8598, 8767, 8936, 9105, 9275, 9444, 9613, 9782, 9951, 10120, 10289, 10458, 10627, 10796, 10965, 11134, 11303, 11473, 11642, 11811, 11980, 12149, 12318, 12487, 12656, 12825, 12994, 13163, 13332]]
    攻击次数 = 2
    CD = 6
    TP成长 = 0.10
    TP上限 = 5

class 技能8(职业主动技能):
    名称 = '血蝠之舞'
    所在等级 =25
    等级上限 =60
    基础等级 =41
    #基础 = 3293.18181818
    #成长 = 372.58741259
    data0 = [ int(i*1.3*1.085) for i in [0, 122, 135, 147, 159, 172, 185, 196, 209, 222, 234, 246, 259, 271, 284, 296, 308, 321, 334, 345, 358, 371, 383, 395, 408, 420, 433, 445, 457, 470, 483, 495, 507, 520, 532, 545, 557, 569, 582, 595, 606, 619, 632, 644, 656, 669, 681, 694, 706, 718, 731, 744, 755, 768, 781, 793, 805, 818, 830, 843, 855, 867, 880, 893, 905, 917, 930, 942, 955, 967, 979]]
    攻击次数 = 30
    CD = 6
    TP成长 = 0.10
    TP上限 = 5

class 技能9(职业主动技能):
    名称 = '血腥狩猎'
    所在等级 =25
    等级上限 =60
    基础等级 =41
    #基础 = 4179
    #成长 = 472.5
    data0 = [ int(i*1.114*1.085) for i in [0, 931, 1025, 1120, 1214, 1309, 1403, 1498, 1592, 1687, 1781, 1876, 1970, 2065, 2159, 2254, 2348, 2443, 2537, 2632, 2726, 2821, 2915, 3010, 3104, 3199, 3293, 3388, 3482, 3577, 3671, 3766, 3860, 3955, 4049, 4144, 4238, 4333, 4427, 4522, 4616, 4711, 4805, 4900, 4994, 5089, 5183, 5278, 5372, 5467, 5561, 5656, 5750, 5845, 5939, 6034, 6128, 6223, 6317, 6412, 6506, 6601, 6695, 6790, 6884, 6979, 7073, 7168, 7262, 7357, 7451]]
    攻击次数 = 5
    CD = 8
    TP成长 = 0.10
    TP上限 = 5


class 技能10(职业主动技能):
    名称 = '狱血之犬'
    所在等级= 30
    等级上限 =60
    基础等级 =38
    #基础 = 4162.87878788
    #成长 = 470.76223776
    #咬住敌人时物理攻击力：<data0>%
    data0 = [ int(i*1.192*1.085) for i in [0, 331, 365, 398, 432, 465, 499, 533, 566, 600, 634, 667, 701, 735, 768, 802, 835, 869, 902, 935, 969, 1003, 1036, 1070, 1104, 1137, 1171, 1205, 1238, 1272, 1305, 1339, 1373, 1406, 1440, 1474, 1507, 1541, 1575, 1608, 1642, 1675, 1709, 1743, 1776, 1810, 1844, 1877, 1911, 1945, 1978, 2012, 2045, 2079, 2113, 2145, 2179, 2213, 2246, 2280, 2314, 2347, 2381, 2415, 2448, 2482, 2515, 2549, 2583, 2616, 2650]]
    #撕咬多段攻击物理攻击力：<data1>%
    data1 = [ int(i*1.192*1.085) for i in [0, 331, 365, 398, 432, 465, 499, 533, 566, 600, 634, 667, 701, 735, 768, 802, 835, 869, 902, 935, 969, 1003, 1036, 1070, 1104, 1137, 1171, 1205, 1238, 1272, 1305, 1339, 1373, 1406, 1440, 1474, 1507, 1541, 1575, 1608, 1642, 1675, 1709, 1743, 1776, 1810, 1844, 1877, 1911, 1945, 1978, 2012, 2045, 2079, 2113, 2145, 2179, 2213, 2246, 2280, 2314, 2347, 2381, 2415, 2448, 2482, 2515, 2549, 2583, 2616, 2650]]
    攻击次数2 = 13
    CD = 10
    TP成长 = 0.10
    TP上限 = 5

class 技能11(职业主动技能):
    名称 = '狱血之牙'
    所在等级= 30
    等级上限 =60
    基础等级 =38
    #基础 = 5281.5666666
    #成长 = 596.353846154
    data0 = [ int(i*1.2*1.085) for i in [0, 5878, 6474, 7071, 7667, 8263, 8861, 9456, 10052, 10649, 11245, 11842, 12438, 13034, 13631, 14227, 14823, 15420, 16016, 16612, 17210, 17805, 18402, 18998, 19594, 20191, 20787, 21383, 21980, 22576, 23172, 23769, 24365, 24962, 25559, 26154, 26751, 27347, 27943, 28540, 29136, 29732, 30329, 30925, 31522, 32118, 32714, 33311, 33908, 34503, 35100, 35696, 36292, 36889, 37485, 38082, 38678, 39274, 39871, 40467, 41063, 41660, 42257, 42852, 43449, 44045, 44642, 45238, 45834, 46431, 47027]]
    CD = 12
    TP成长 = 0.10
    TP上限 = 5
    额外倍率 = 0
    触发概率 = 0
    def 等效百分比(self, 武器类型):
        return (1 + self.额外倍率 * self.触发概率) * super().等效百分比(武器类型)

class 技能12(职业主动技能):
    名称 = '血腥炼狱'
    所在等级= 35
    等级上限 =60
    基础等级 =36
    #基础 = 9392.703939
    #成长 = 1061.7061888
    data0 = [ int(i*1.161*1.085) for i in [0, 1046, 1152, 1259, 1365, 1471, 1577, 1683, 1790, 1896, 2002, 2108, 2214, 2320, 2427, 2533, 2639, 2745, 2851, 2958, 3064, 3170, 3276, 3382, 3489, 3595, 3701, 3807, 3913, 4020, 4126, 4232, 4338, 4444, 4550, 4657, 4763, 4869, 4975, 5081, 5188, 5294, 5400, 5506, 5612, 5719, 5825, 5931, 6037, 6143, 6249, 6356, 6462, 6568, 6674, 6780, 6887, 6993, 7099, 7205, 7311, 7418, 7524, 7630, 7736, 7842, 7949, 8055, 8161, 8267, 8373]]
    攻击次数 = 10
    CD =18
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2
            # self.基础 *= 1.2
            # self.成长 *= 1.2
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.29
            # self.基础 *= 1.29
            # self.成长 *= 1.29
            self.CD *= 0.9

class 技能13(职业主动技能):
    名称 = '噬魂囚笼'
    所在等级= 40
    等级上限 =60
    基础等级 =33
    #数组不正确，但仅体现在游戏数据中，计算器最终得出结果无异常
    #基础 = 12175.36181818/31*30
    #成长 = 1333.46433566/31*30
    data0 = [ int(i*1.193*1.085) for i in [0, 437, 481, 526, 570, 615, 659, 703, 748, 792, 837, 881, 925, 970, 1014, 1059, 1103, 1147, 1192, 1236, 1281, 1325, 1369, 1414, 1458, 1502, 1547, 1591, 1636, 1680, 1724, 1769, 1813, 1858, 1902, 1946, 1991, 2035, 2080, 2124, 2168, 2213, 2257, 2302, 2346, 2390, 2435, 2479, 2523, 2568, 2612, 2657, 2701, 2745, 2790, 2834, 2879, 2923, 2967, 3012, 3056, 3101, 3145, 3189, 3234, 3278, 3323, 3367, 3411, 3456, 3500]]
    攻击次数 = 30
    CD =20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2
            # self.基础 *= 1.2
            # self.成长 *= 1.2
            self.CD *= 0.82
        elif x == 1:
            self.倍率 *= 1.29
            # self.基础 *= 1.29
            # self.成长 *= 1.29
            self.CD *= 0.82

class 技能14(职业主动技能):
    名称 = '狱血之噬'
    所在等级= 45
    等级上限 =60
    基础等级 =31
    #基础 = 23208.8198030
    #成长 = 2620.41055594
    #吸血物理攻击力：<data0>%
    data0 = [ int(i*1.192*1.085) for i in [0, 25837, 28458, 31079, 33701, 36322, 38943, 41564, 44185, 46807, 49428, 52049, 54670, 57291, 59913, 62534, 65155, 67776, 70397, 73018, 75640, 78261, 80882, 83503, 86124, 88746, 91367, 93988, 96609, 99230, 101852, 104473, 107094, 109715, 112336, 114958, 117579, 120200, 122821, 125442, 128064, 130685, 133306, 135927, 138548, 141170, 143791, 146412, 149033, 151654, 154275, 156897, 159518, 162139, 164760, 167381, 170003, 172624, 175245, 177866, 180487, 183109, 185730, 188351, 190972, 193593, 196215, 198836, 201457, 204078, 206699]]
    CD =40
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2
            # self.基础 *= 1.2
            # self.成长 *= 1.2
        elif x == 1:
            self.倍率 *= 1.28
            # self.基础 *= 1.28
            # self.成长 *= 1.28

class 技能15(职业主动技能):
    名称 = '伯爵之歌'
    所在等级= 50
    等级上限 =60
    基础等级 =12
    # 基础 = 46649
    # 成长 = 14081
    #多段物理攻击力：<data0>%
    data0 = [ int(i*1.223*1.085) for i in [0, 3036, 3740, 4445, 5148, 5853, 6556, 7261, 7965, 8668, 9373, 10076, 10781, 11485, 12189, 12893, 13597, 14301, 15005, 15709, 16414, 17117, 17822, 18525, 19230, 19934, 20638, 21342, 22046, 22750, 23455, 24158, 24863, 25566, 26271, 26975, 27679, 28383, 29087, 29791, 30495, 105760, 107882, 110002, 112124, 114245, 116367, 118488, 120609, 122731, 124852, 126973, 129094, 131216, 133337, 135458, 137579, 139701, 141822, 143943, 146064, 148186, 150307, 152428, 154550, 156671, 158793, 160913, 163035, 165156, 167278]]
    攻击次数 = 14
    #最终一击物理攻击力：<data1>%
    data1 = [ int(i*1.223*1.085) for i in [0, 18218, 22443, 26667, 30892, 35116, 39341, 43565, 47790, 52014, 56238, 60463, 64687, 68912, 73136, 77361, 81585, 85810, 90035, 94259, 98484, 102708, 106933, 111157, 115382, 119606, 123831, 128055, 132280, 136505, 140729, 144954, 149178, 153403, 157627, 161852, 166076, 170301, 174525, 178750, 182975, 105760, 107882, 110002, 112124, 114245, 116367, 118488, 120609, 122731, 124852, 126973, 129094, 131216, 133337, 135458, 137579, 139701, 141822, 143943, 146064, 148186, 150307, 152428, 154550, 156671, 158793, 160913, 163035, 165156, 167278]]
    攻击次数2 = 1
    CD = 145

class 技能16(职业主动技能):
    名称 = '魔仆召唤：狱犬'
    所在等级= 60
    等级上限 =40
    基础等级 =23
    #数组不正确，但仅体现在游戏数据中，计算器最终得出结果无异常
    #基础 = 18037.9022727225
    #成长 = 2037.774650352
    #多段物理攻击力：<data0>%
    data0 = [ int(i*1.174*1.085) for i in [0, 956, 1053, 1150, 1247, 1344, 1441, 1538, 1635, 1732, 1829, 1926, 2023, 2120, 2217, 2314, 2412, 2509, 2606, 2703, 2800, 2897, 2994, 3091, 3188, 3285, 3382, 3479, 3576, 3673, 3770, 3867, 3964, 4061, 4158, 4255, 4352, 4449, 4546, 4643, 4740, 4837, 4934, 5031, 5129, 5226, 5323, 5420, 5517, 5614, 5711, 5808, 5905, 6002, 6099, 6196, 6293, 6390, 6487, 6584, 6681, 6778, 6875, 6972, 7069, 7166, 7263, 7360, 7457, 7554, 7651]]
    攻击次数 = 21
    CD =25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.13
            # self.基础 *= 1.13
            # self.成长 *= 1.13
            self.CD *= 0.8
        elif x == 1:
            self.倍率 *= 1.22
            # self.基础 *= 1.22
            # self.成长 *= 1.22
            self.CD *= 0.8

class 技能17(职业主动技能):
    名称 = '血翼绽放'
    所在等级= 70
    等级上限 =40
    基础等级 =18
    #基础 = 25260.95
    #成长 = 2852.003846153
    #蝙蝠群冲击波攻击力：<data0>%
    data0 = [ int(i*1.265*1.085) for i in [0, 11245, 12386, 13527, 14667, 15808, 16949, 18090, 19231, 20372, 21512, 22653, 23794, 24935, 26076, 27217, 28358, 29498, 30639, 31780, 32921, 34062, 35203, 36343, 37484, 38625, 39766, 40907, 42048, 43188, 44329, 45470, 46611, 47752, 48893, 50034, 51174, 52315, 53456, 54597, 55738]]
    #血气之翼物理攻击力：<data1>%
    data1 = [ int(i*1.265*1.085) for i in [0, 16869, 18579, 20290, 22001, 23713, 25424, 27135, 28846, 30558, 32269, 33980, 35691, 37403, 39114, 40825, 42537, 44248, 45959, 47670, 49382, 51093, 52804, 54515, 56227, 57938, 59649, 61360, 63072, 64783, 66494, 68206, 69917, 71628, 73339, 75050, 76762, 78473, 80185, 81895, 83607]]
    攻击次数2 = 1
    CD =50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.25
            # self.基础 *= 1.25
            # self.成长 *= 1.25
        elif x == 1:
            self.倍率 *= 1.33
            # self.基础 *= 1.33
            # self.成长 *= 1.33

class 技能18(职业主动技能):
    名称 = '地狱冥犬'
    所在等级= 75
    等级上限 =40
    基础等级 =16
    #基础 = 30218.85
    #成长 = 5734.946153849
    #撕咬攻击力：<data0>%
    data0 = [ int(i*1.227*1.085) for i in [0, 899, 1042, 1186, 1329, 1471, 1616, 1759, 1902, 2046, 2189, 2332, 2476, 2619, 2761, 2906, 3049, 3192, 3336, 3478, 3623, 3766, 3909, 4054, 4197, 4340, 4483, 4626, 4769, 4914, 5056, 5199, 5343, 5486, 5629, 5773, 5916, 6059, 6204, 6346, 6489, 6633, 6776, 6920, 7063, 7206, 7350, 7493, 7636, 7780, 7923, 8066, 8210, 8353, 8496, 8640, 8783, 8926, 9070, 9213, 9356, 9500, 9643, 9787, 9930, 10073, 10217, 10360, 10503, 10647, 10790]]
    攻击次数 = 20
    #冲向地面攻击力：<data1>%
    data1 = [ int(i*1.227*1.085) for i in [0, 17984, 20851, 23718, 26586, 29453, 32320, 35188, 38055, 40922, 43789, 46655, 49522, 52390, 55257, 58124, 60992, 63859, 66726, 69594, 72461, 75327, 78194, 81061, 83928, 86796, 89663, 92530, 95398, 98265, 101132, 104000, 106866, 109732, 112600, 115467, 118334, 121202, 124069, 126936, 129804, 132670, 135538, 138405, 141272, 144139, 147006, 149873, 152740, 155608, 158475, 161342, 164209, 167076, 169943, 172811, 175678, 178545, 181412, 184279, 187146, 190013, 192881, 195748, 198615, 201482, 204349, 207216, 210084, 212951, 215818]]
    攻击次数2 = 1
    CD =30
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.29
            # self.基础 *= 1.29
            # self.成长 *= 1.29
            self.CD *= 0.9

class 技能19(职业主动技能):
    名称 = '死亡之握'
    所在等级= 80
    等级上限 =40
    基础等级 =13
    #基础 = 60756.9115151488
    #成长 = 6859.7572027936
    data0 = [ int(i*1.225*1.085) for i in [0, 67617, 74477, 81337, 88196, 95056, 101916, 108776, 115634, 122494, 129354, 136214, 143074, 149933, 156793, 163653, 170513, 177372, 184232, 191092, 197952, 204811, 211671, 218530, 225391, 232250, 239110, 245969, 252830, 259689, 266549, 273409, 280269, 287129, 293988, 300848, 307707, 314568, 321427, 328287, 335145]]
    CD =50
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.34
            # self.基础 *= 1.34
            # self.成长 *= 1.34

class 技能20(职业主动技能):
    名称 = '血界彼岸'
    所在等级= 85
    等级上限 =40
    基础等级 =5
    #基础 = 108898.72
    #成长 = 32796.96
    #多段攻击力：<data0>%
    data0 = [ int(i*1.223*1.085) for i in [0, 2052, 2527, 3003, 3479, 3955, 4430, 4906, 5382, 5858, 6334, 6810, 7286, 7760, 8236, 8712, 9188, 9663, 10140, 10615, 11091, 11566, 12043, 12518, 12994, 13470, 13946, 14421, 14897, 15373, 15849, 16324, 16801, 17276, 17752, 18228, 18704, 19180, 19655, 20132, 20607]]
    攻击次数 = 35
    #最终一击攻击力：<data1>%
    data1 = [ int(i*1.223*1.085) for i in [0, 69761, 85938, 102115, 118291, 134468, 150644, 166821, 182998, 199175, 215351, 231528, 247705, 263881, 280058, 296234, 312411, 328588, 344764, 360941, 377117, 393294, 409471, 425648, 441823, 458000, 474178, 490354, 506531, 522707, 538884, 555061, 571238, 587414, 603590, 619768, 635944, 652121, 668297, 684473, 700651]]
    攻击次数2 = 1
    CD = 180

class 技能21(职业主动技能):
    名称 = '血翼蔽空'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    data0 = [ int(i*1.186*1.085) for i in [0, 116057, 127831, 139604, 151378, 163152, 174926, 186700, 198474, 210248, 222022, 233796, 245570, 257344, 269117, 280891, 292665, 304439, 316213, 327987, 339761, 351535, 363309, 375083, 386857, 398630, 410404, 422178, 433952, 445726, 457500, 469274, 481048, 492822, 504596, 516370, 528144, 539917, 551691, 563465, 575239, 587013, 598787, 610561, 622335, 634109, 645883, 657657, 669430, 681204, 692978, 704752, 716526, 728300, 740074, 751848, 763622, 775396, 787170, 798943, 810717, 822491, 834265, 846039, 857813, 869587, 881361, 893135, 904909, 916683, 928456]]
    CD = 60.0

class 技能22(职业主动技能):
    名称 = '血域帷幕·陨灭'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    data0 = [ int(i*1.192*1.085) for i in [0, 40404, 49773, 59142, 68512, 77881, 87250, 96619, 105988, 115357, 124727, 134096, 143465, 152834, 162203, 171573, 180942, 190311, 199680, 209049, 218418, 227788, 237157, 246526, 255895, 265264, 274634, 284003, 293372, 302741, 312110, 321479, 330849, 340218, 349587, 358956, 368325, 377694, 387064, 396433, 405802, 415171, 424540, 433910, 443279, 452648, 462017, 471386, 480755, 490125, 499494, 508863, 518232, 527601, 536970, 546340, 555709, 565078, 574447, 583816, 593186, 602555, 611924, 621293, 630662, 640031, 649401, 658770, 668139, 677508, 686877]]

    data1 = [ int(i*1.192*1.085) for i in [0, 4040, 4977, 5914, 6851, 7788, 8725, 9661, 10598, 11535, 12472, 13409, 14346, 15283, 16220, 17157, 18094, 19031, 19968, 20904, 21841, 22778, 23715, 24652, 25589, 26526, 27463, 28400, 29337, 30274, 31211, 32147, 33084, 34021, 34958, 35895, 36832, 37769, 38706, 39643, 40580, 41517, 42454, 43390, 44327, 45264, 46201, 47138, 48075, 49012, 49949, 50886, 51823, 52760, 53697, 54634, 55570, 56507, 57444, 58381, 59318, 60255, 61192, 62129, 63066, 64003, 64940, 65877, 66813, 67750, 68687]]
    data2 = [ int(i*1.192*1.085) for i in [0, 282832, 348416, 414000, 479584, 545168, 610753, 676337, 741921, 807505, 873090, 938674, 1004258, 1069842, 1135427, 1201011, 1266595, 1332179, 1397764, 1463348, 1528932, 1594516, 1660100, 1725685, 1791269, 1856853, 1922437, 1988022, 2053606, 2119190, 2184774, 2250359, 2315943, 2381527, 2447111, 2512696, 2578280, 2643864, 2709448, 2775033, 2840617, 2906201, 2971785, 3037369, 3102954, 3168538, 3234122, 3299706, 3365291, 3430875, 3496459, 3562043, 3627628, 3693212, 3758796, 3824380, 3889965, 3955549, 4021133, 4086717, 4152301, 4217886, 4283470, 4349054, 4414638, 4480223, 4545807, 4611391, 4676975, 4742560, 4808144]]
    攻击次数 = 1
    攻击次数2 = 20
    攻击次数3 = 1
    CD = 290.0

    def 加成倍率(self, 武器类型):
        return 0.0

技能列表 = []
i = 0
while i >= 0:
    try:
        tem = eval('技能'+str(i)+'()')
        tem.基础等级计算()
        技能列表.append(tem)
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

知源·血法师一觉序号 = 0
知源·血法师二觉序号 = 0
知源·血法师三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        知源·血法师一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        知源·血法师二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        知源·血法师三觉序号 = 技能序号[i.名称]

知源·血法师护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        知源·血法师护石选项.append(i.名称)

知源·血法师符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        知源·血法师符文选项.append(i.名称)

class 知源·血法师角色属性(角色属性):

    实际名称 = '知源·血法师'
    角色 = '魔法师(男)'
    职业 = '血法师'

    武器选项 = ['矛']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    狱血之牙触发概率 = 0

    主BUFF = 1.97

    def 被动倍率计算(self):
        if equ.get_equ_by_name(self.装备栏[11]).名称 == '歼灵灭魂矛':
            self.技能栏[self.技能序号['狱血之牙']].触发概率 = self.狱血之牙触发概率
        super().被动倍率计算()

    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(技能列表)
        self.技能序号= deepcopy(技能序号)

class 知源·血法师(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 知源·血法师角色属性()
        self.角色属性A = 知源·血法师角色属性()
        self.角色属性B = 知源·血法师角色属性()
        self.一觉序号 = 知源·血法师一觉序号
        self.二觉序号 = 知源·血法师二觉序号
        self.三觉序号 = 知源·血法师三觉序号
        self.护石选项 = deepcopy(知源·血法师护石选项)
        self.符文选项 = deepcopy(知源·血法师符文选项)

    def 界面(self):
        super().界面()
        self.狱血之牙概率=MyQComboBox(self.main_frame2)
        self.狱血之牙概率.resize(130,20)
        self.狱血之牙概率.move(320,450)
        for i in range(11):
            self.狱血之牙概率.addItem('歼灵灭魂矛：' + str(i * 10) + '%')
        self.狱血之牙概率.setCurrentIndex(1)

        self.职业存档.append(('狱血之牙概率', self.狱血之牙概率, 1))

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        属性.狱血之牙触发概率 = round(self.狱血之牙概率.currentIndex() / 10, 2)
