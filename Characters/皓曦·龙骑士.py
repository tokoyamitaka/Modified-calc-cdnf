from math import *
from PublicReference.base import *


class 技能0(被动技能):
    名称 = '基础精通'
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['龙人剑术', '普通攻击（一轮）']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.463 + 0.089 * self.等级, 5)


class 技能1(主动技能):
    名称 = '龙人剑术'
    备注 = '(TP为基础精通)'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    基础 = 1159.00 * 1.05 * 1.210415
    成长 = 0
    CD = 3.0
    TP成长 = 0.10
    TP上限 = 5


class 技能2(主动技能):
    名称 = '火焰吐息'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    data0 = [(i*1.210046) for i in [0, 876, 964, 1054, 1142, 1231, 1320, 1408, 1498, 1587, 1675, 1764, 1854, 1942, 2031, 2120, 2209, 2298, 2386, 2475, 2565, 2653, 2742, 2831, 2919, 3009, 3098, 3186, 3275, 3364, 3453, 3542, 3630, 3720, 3809, 3897, 3986, 4076, 4164, 4253, 4342, 4431, 4520, 4608, 4697, 4787, 4875, 4964, 5053, 5141, 5231, 5320, 5408, 5497, 5587, 5675, 5764, 5852, 5942, 6031, 6119]]
    攻击次数 = 3
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能3(主动技能):
    名称 = '龙翼突袭'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    data0 = [(i*1.209706) for i in [0, 1545, 1702, 1859, 2016, 2172, 2329, 2486, 2643, 2800, 2957, 3113, 3270, 3427, 3584, 3741, 3897, 4054, 4211, 4368, 4525, 4681, 4838, 4995, 5152, 5309, 5465, 5622, 5779, 5936, 6093, 6250, 6406, 6563, 6720, 6877, 7034, 7190, 7347, 7504, 7661, 7818, 7974, 8131, 8288, 8445, 8602, 8759, 8915, 9072, 9229, 9386, 9543, 9699, 9856, 10013, 10170, 10327, 10483, 10640, 10797, 10954, 11111, 11267, 11424, 11581, 11738, 11895, 12052, 12208, 12365]]
    攻击次数 = 1
    data1 = [(i*1.21016) for i in [0, 1399, 1541, 1683, 1825, 1967, 2109, 2251, 2393, 2535, 2677, 2819, 2961, 3103, 3245, 3387, 3529, 3671, 3813, 3955, 4097, 4239, 4381, 4523, 4665, 4807, 4949, 5091, 5233, 5375, 5517, 5659, 5801, 5943, 6085, 6227, 6369, 6511, 6653, 6795, 6937, 7079, 7221, 7363, 7505, 7647, 7789, 7931, 8073, 8215, 8357, 8499, 8641, 8783, 8925, 9067, 9209, 9351, 9493, 9635, 9777, 9919, 10061, 10203, 10345, 10487, 10629, 10771, 10913, 11055, 11197]]
    攻击次数2 = 1
    CD = 4.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能4(主动技能):
    名称 = '龙语召唤：阿斯特拉'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    data0 = [(i*1.210978) for i in [0, 2986, 3463, 3938, 4414, 4891, 5366, 5843, 6319, 6795, 7271, 7748, 8223, 8699, 9176, 9651, 10128, 10604, 11080, 11556, 12033, 12508, 12984, 13461, 13936, 14413, 14889, 15366, 15841, 16318, 16794]]
    攻击次数 = 1
    CD = 7.0
    关联技能 = ['所有']

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1.05 + 0.005 * self.等级, 5)
        else:
            return round(0.75 + 0.02 * self.等级, 5)

    def 独立攻击力倍率进图(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1.05 + 0.005 * self.等级, 5)
        else:
            return round(0.75 + 0.02 * self.等级, 5)


class 技能5(主动技能):
    名称 = '爆破龙角'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data0 = [(i*1.208141) for i in [0, 1715, 1888, 2062, 2237, 2410, 2584, 2757, 2932, 3106, 3279, 3454, 3628, 3801, 3976, 4150, 4323, 4498, 4672, 4845, 5020, 5193, 5367, 5542, 5715, 5889, 6064, 6237, 6411, 6586, 6759, 6933, 7108, 7281, 7455, 7629, 7803, 7977, 8150, 8325, 8499, 8672, 8847, 9020, 9194, 9369, 9542, 9716, 9891, 10064, 10238, 10413, 10586, 10760, 10935, 11108, 11282, 11456, 11630, 11804, 11978]]
    攻击次数 = 1
    data1 = [(i*1.207952) for i in [0, 4001, 4406, 4813, 5218, 5625, 6030, 6436, 6842, 7248, 7654, 8060, 8466, 8872, 9277, 9684, 10089, 10496, 10901, 11306, 11713, 12118, 12525, 12930, 13337, 13742, 14148, 14554, 14960, 15366, 15772, 16178, 16584, 16989, 17396, 17801, 18208, 18613, 19019, 19425, 19831, 20237, 20643, 21049, 21455, 21860, 22267, 22672, 23079, 23484, 23890, 24296, 24702, 25108, 25514, 25920, 26326, 26731, 27138, 27543, 27950]]
    攻击次数2 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能6(主动技能):
    名称 = '龙拳(地面释放)'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    data0 = [(i*1.218204) for i in [0,1998, 2201, 2403, 2607, 2809, 3012, 3214, 3418, 3621, 3823, 4027, 4229, 4432, 4634, 4838, 5040, 5243, 5445, 5649, 5851, 6054, 6257, 6460, 6662, 6865, 7068, 7271, 7473, 7676, 7879, 8082, 8284, 8488, 8690, 8893, 9095, 9299, 9501, 9704, 9906, 10110, 10312, 10515, 10717, 10921, 11123, 11326, 11528, 11732, 11935, 12137, 12341, 12543, 12746, 12948, 13152, 13354, 13557, 13759, 13963]]
    攻击次数 = 1
    data1 = [(i*1.218133) for i in [0, 2998, 3302, 3606, 3911, 4214, 4518, 4822, 5127, 5431, 5735, 6040, 6344, 6648, 6952, 7257, 7560, 7864, 8168, 8473, 8777, 9081, 9386, 9690, 9994, 10297, 10602, 10906, 11210, 11514, 11819, 12123, 12427, 12731, 13036, 13340, 13643, 13948, 14252, 14556, 14860, 15165, 15469, 15773, 16077, 16382, 16686, 16989, 17293, 17598, 17902, 18206, 18511, 18815, 19119, 19423, 19728, 20031, 20335, 20639, 20944]]
    攻击次数2 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能7(主动技能):
    名称 = '龙拳(空中释放)'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    data0 = [(i*1.218269) for i in [0, 550, 607, 662, 718, 774, 830, 885, 941, 998, 1053, 1109, 1165, 1221, 1276, 1333, 1389, 1444, 1501, 1556, 1612, 1667, 1724, 1780, 1835, 1892, 1947, 2003, 2059, 2115, 2171, 2227, 2283, 2338, 2395, 2451, 2506, 2562, 2618, 2674, 2729, 2786, 2842, 2897, 2954, 3009, 3065, 3121, 3177, 3233, 3288, 3345, 3400, 3456, 3512, 3568, 3624, 3680, 3736, 3791, 3848]]
    攻击次数 = 1
    data1 = [(i*1.218074) for i in [0, 4957, 5460, 5963, 6466, 6969, 7472, 7975, 8478, 8980, 9484, 9987, 10490, 10993, 11495, 11998, 12501, 13005, 13508, 14010, 14513, 15016, 15519, 16023, 16525, 17028, 17531, 18034, 18536, 19040, 19543, 20046, 20549, 21051, 21554, 22058, 22561, 23064, 23566, 24069, 24572, 25076, 25579, 26081, 26584, 27087, 27590, 28092, 28596, 29099, 29602, 30105, 30607, 31110, 31614, 32117, 32620, 33122, 33625, 34128, 34632]]
    攻击次数2 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能8(主动技能):
    名称 = '龙之撕咬'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    data0 = [(i*1.208623) for i in [0, 930, 1025, 1120, 1214, 1309, 1403, 1497, 1592, 1687, 1781, 1875, 1970, 2064, 2159, 2254, 2347, 2442, 2537, 2631, 2726, 2821, 2914, 3009, 3104, 3198, 3293, 3387, 3481, 3576, 3671, 3765, 3859, 3954, 4048, 4143, 4238, 4331, 4426, 4521, 4615, 4710, 4804, 4898, 4993, 5088, 5182, 5277, 5371, 5465, 5560, 5655, 5749, 5843, 5938, 6032, 6127, 6222, 6315, 6410, 6505]]
    攻击次数 = 6
    CD = 10
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能9(主动技能):
    名称 = '龙翼穿刺(2hit+踢击)'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data0 = [(i*1.210245) for i in [0, 119, 130, 142, 155, 167, 178, 190, 203, 215, 226, 239, 251, 263, 276, 287, 299, 311, 324, 335, 347, 360, 372, 383, 395, 408, 420, 431, 444, 456, 468, 479, 492, 504, 516, 529, 540, 552, 564, 577, 588, 600, 613, 625, 636, 648, 661, 673, 684, 697, 709, 721, 734, 745, 757, 769, 782, 793, 805, 818, 830]]
    攻击次数 = 2
    data1 = [(i*1.209936) for i in [0, 7269, 8006, 8744, 9481, 10218, 10956, 11693, 12431, 13168, 13906, 14643, 15380, 16118, 16855, 17593, 18330, 19067, 19805, 20542, 21280, 22017, 22755, 23492, 24229, 24967, 25704, 26442, 27179, 27917, 28654, 29391, 30129, 30866, 31604, 32341, 33079, 33816, 34553, 35291, 36028, 36766, 37503, 38241, 38978, 39715, 40453, 41190, 41928, 42665, 43402, 44140, 44877, 45615, 46352, 47090, 47827, 48564, 49302, 50039, 50777]]
    攻击次数2 = 1
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能10(主动技能):
    名称 = '龙翼穿刺(撕咬附着)'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data0 = [(i*1.209994) for i in [0, 7962, 8764, 9574, 10384, 11192, 11995, 12804, 13615, 14423, 15226, 16035, 16845, 17655, 18464, 19267, 20076, 20886, 21696, 22497, 23307, 24117, 24927, 25729, 26537, 27348, 28157, 28960, 29768, 30579, 31388, 32190, 33000, 33809, 34619, 35429, 36232, 37041, 37850, 38660, 39462, 40272, 41082, 41891, 42693, 43502, 44313, 45121, 45924, 46733, 47543, 48353, 49162, 49964, 50774, 51584, 52394, 53196, 54005, 54815, 55625]]
    攻击次数 = 1
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能11(主动技能):
    名称 = '飞龙斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data0 = [(i*1.21087) for i in [0, 2243, 2471, 2698, 2925, 3153, 3381, 3609, 3836, 4063, 4292, 4519, 4747, 4974, 5201, 5430, 5657, 5884, 6112, 6339, 6568, 6795, 7022, 7250, 7478, 7706, 7933, 8160, 8388, 8616, 8844, 9071, 9298, 9526, 9754, 9981, 10209, 10436, 10665, 10892, 11119, 11347, 11574, 11803, 12030, 12257, 12485, 12712, 12940, 13168, 13395, 13623, 13851, 14078, 14306, 14533, 14760, 14989, 15216, 15444, 15671]]
    攻击次数 = 2
    data1 = [(i*1.210964) for i in [0, 6589, 7256, 7925, 8594, 9262, 9931, 10600, 11268, 11936, 12604, 13273, 13942, 14610, 15279, 15947, 16615, 17284, 17952, 18621, 19290, 19957, 20626, 21295, 21963, 22632, 23300, 23968, 24637, 25305, 25974, 26643, 27311, 27980, 28647, 29316, 29985, 30653, 31322, 31991, 32658, 33327, 33995, 34664, 35333, 36001, 36669, 37337, 38006, 38675, 39343, 40012, 40680, 41348, 42017, 42685, 43354, 44023, 44691, 45359, 46028]]
    攻击次数2 = 1
    CD = 15
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 3.25
            self.CD *= 0.9
        elif x == 1:
            self.攻击次数 = 3.7
            self.CD *= 0.9

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能12(被动技能):
    名称 = '大胃王'
    所在等级 = 35
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.0 + 0.01 * self.等级, 5)
        else:
            return round(0.9 + 0.02 * self.等级, 5)


class 技能13(主动技能):
    名称 = '龙刃无双'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    data0 = [(i*1.210019) for i in [0, 15232, 16778, 18324, 19869, 21415, 22960, 24505, 26051, 27596, 29142, 30687, 32233, 33777, 35323, 36869, 38414, 39960, 41505, 43050, 44596, 46141, 47687, 49232, 50777, 52323, 53868, 55414, 56959, 58505, 60050, 61595, 63141, 64686, 66232, 67778, 69322, 70868, 72413, 73959, 75504, 77049, 78595, 80140, 81686, 83231, 84777, 86322, 87867, 89413, 90958, 92504, 94050, 95594, 97140, 98685, 100231, 101777, 103321, 104867, 106412]]
    攻击次数 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.28
        elif x == 1:
            self.倍率 *= 1.37

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能14(主动技能):
    名称 = '魔龙之息(脱手)'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    data0 = [(i * 1.215692) for i in [0, 1706, 1879, 2052, 2225, 2399, 2571, 2745, 2918, 3091, 3264, 3437, 3611, 3783, 3957, 4129, 4303, 4475, 4649, 4823, 4995, 5169, 5341, 5515, 5687, 5861, 6034, 6207, 6381, 6553, 6727, 6899, 7073, 7246, 7419, 7592, 7765, 7938, 8112, 8285, 8458, 8631, 8804, 8977, 9150, 9324, 9496, 9670, 9842, 10016, 10190, 10362, 10536, 10708, 10882, 11054, 11228, 11400, 11574, 11747, 11920]]
    攻击次数 = 13
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.22
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.30
            self.CD *= 0.9

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能15(主动技能):
    名称 = '魔龙之息(骑乘)'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    data0 = [(i*1.215904) for i in [0, 1130, 1244, 1359, 1474, 1588, 1703, 1818, 1932, 2047, 2161, 2276, 2391, 2505, 2620, 2735, 2849, 2964, 3079, 3193, 3308, 3422, 3537, 3651, 3765, 3880, 3995, 4109, 4224, 4338, 4453, 4568, 4682, 4797, 4912, 5026, 5141, 5256, 5370, 5485, 5600, 5714, 5829, 5943, 6058, 6173, 6287, 6402, 6517, 6631, 6746, 6861, 6975, 7090, 7204, 7319, 7434, 7548, 7663, 7778, 7892]]
    攻击次数 = 23
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    护石CD缩减 = 0

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.9
            self.攻击次数 = 25
            self.护石CD缩减 = 4
        elif x == 1:
            self.倍率 *= 1.07
            self.CD *= 0.9
            self.攻击次数 = 25
            self.护石CD缩减 = 4

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 等效CD(self, 武器类型, 输出类型):
        return round((self.CD * 武器冷却惩罚(武器类型, 输出类型, self.版本)-self.护石CD缩减) / self.恢复, 1)


class 技能16(被动技能):
    名称 = '魔龙之力'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)


class 技能17(主动技能):
    名称 = '魔龙之力(火球)'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    data0 = [(i*1.0) for i in [0, 935, 1084, 1233, 1383, 1532, 1681, 1830, 1979, 2128, 2278, 2427, 2576, 2725, 2874, 3023, 3172, 3322, 3471, 3620, 3769, 3918, 4067, 4217, 4366, 4515, 4664, 4813, 4962, 5112, 5261, 5410, 5559, 5708, 5857, 6006, 6156, 6305, 6454, 6603, 6752]]
    攻击次数 = 1
    CD = 3.0
    TP上限 = 0

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能18(主动技能):
    名称 = '雷光嘶吼'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    data0 = [(i*1.208969) for i in [0, 2480, 3054, 3630, 4204, 4780, 5354, 5930, 6504, 7080, 7655, 8230, 8805, 9380, 9956, 10530, 11106, 11680, 12256, 12830, 13406, 13980, 14556, 15130, 15706, 16280, 16856, 17430, 18006, 18581, 19156, 19731, 20306, 20882, 21456, 22032, 22606, 23182, 23756, 24332, 24906]]
    攻击次数 = 8
    data1 = [(i*1.208998) for i in [0, 44091, 54315, 64540, 74763, 84988, 95212, 105437, 115660, 125885, 136109, 146333, 156557, 166782, 177006, 187229, 197454, 207678, 217902, 228126, 238351, 248575, 258799, 269023, 279248, 289472, 299696, 309920, 320144, 330368, 340592, 350817, 361041, 371265, 381489, 391714, 401937, 412162, 422386, 432611, 442834]]
    攻击次数2 = 1
    CD = 145

    def 等效百分比(self, 武器类型):
        if self.等级 <= 8:
            return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * self.倍率
        else:
            return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2 * 1.1) * self.倍率


class 技能19(主动技能):
    名称 = '龙皇制裁'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    data0 = [(i*1.207984) for i in [0, 23146, 25495, 27842, 30191, 32538, 34887, 37236, 39583, 41932, 44279, 46628, 48976, 51324, 53673, 56020, 58369, 60717, 63065, 65414, 67761, 70110, 72457, 74806, 77155, 79502, 81851, 84198, 86547, 88896, 91243, 93592, 95939, 98288, 100636, 102984, 105333, 107680, 110029, 112377, 114725, 117074, 119421, 121770, 124118, 126466, 128815, 131162, 133511, 135859, 138207, 140556, 142903, 145252, 147600, 149948, 152296, 154644, 156993, 159341, 161689]]
    攻击次数 = 1
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.32

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能20(主动技能):
    名称 = '魔龙天翔(脱手)'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    data0 = [(i*1.201) for i in [0, 33015, 36364, 39713, 43062, 46413, 49762, 53111, 56461, 59810, 63159, 66510, 69859, 73208, 76557, 79907, 83256, 86605, 89955, 93304, 96653, 100003, 103352, 106701, 110050, 113400, 116749, 120098, 123448, 126797, 130146, 133497, 136846, 140195, 143544, 146894, 150244, 153593, 156943, 160292, 163641]]
    攻击次数 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.18
        elif x == 1:
            self.倍率 *= 1.26

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能21(主动技能):
    名称 = '魔龙天翔(骑乘)'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    data0 = [(i*1.201019) for i in [0, 12133, 13365, 14596, 15826, 17058, 18289, 19519, 20751, 21982, 23212, 24444, 25675, 26905, 28137, 29367, 30597, 31830, 33059, 34290, 35523, 36752, 37983, 39215, 40445, 41676, 42908, 44138, 45369, 46601, 47831, 49062, 50294, 51524, 52755, 53987, 55217, 56448, 57680, 58910, 60141]]
    攻击次数 = 1
    data1 = [(i*1.201014) for i in [0, 9437, 10394, 11351, 12310, 13267, 14224, 15181, 16139, 17097, 18054, 19011, 19968, 20926, 21883, 22841, 23798, 24755, 25713, 26670, 27627, 28585, 29543, 30501, 31458, 32415, 33373, 34330, 35288, 36245, 37202, 38160, 39117, 40075, 41032, 41989, 42946, 43905, 44862, 45819, 46776]]
    攻击次数2 = 3
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.31

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能22(被动技能):
    名称 = '龙神血脉'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.02 * self.等级, 5)


class 技能23(主动技能):
    名称 = '魔龙星落'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    data0 = [(i*1.211005) for i in [0, 4142, 4562, 4983, 5403, 5823, 6243, 6663, 7084, 7504, 7924, 8344, 8765, 9185, 9605, 10025, 10445, 10866, 11286, 11706, 12126, 12547, 12967, 13387, 13807, 14227, 14648, 15068, 15488, 15908, 16328, 16750, 17170, 17590, 18010, 18431, 18851, 19271, 19691, 20111, 20532, 20952, 21372, 21792, 22213, 22633, 23053, 23473, 23893, 24314, 24734, 25154, 25574, 25995, 26415, 26835, 27255, 27675, 28096, 28516, 28936]]
    攻击次数 = 9
    data1 = [(i*1.210992) for i in [0, 24854, 27375, 29897, 32418, 34940, 37462, 39983, 42504, 45026, 47547, 50068, 52591, 55112, 57633, 60155, 62676, 65197, 67720, 70241, 72762, 75284, 77805, 80326, 82848, 85370, 87891, 90412, 92934, 95455, 97976, 100499, 103020, 105541, 108063, 110584, 113105, 115628, 118149, 120670, 123192, 125713, 128234, 130757, 133278, 135799, 138321, 140842, 143363, 145884, 148407, 150928, 153449, 155971, 158492, 161013, 163536, 166057, 168578, 171100, 173621]]
    攻击次数2 = 1
    CD = 40.0
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 = 1.37

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能24(主动技能):
    名称 = '征战无双'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    data0 = [(i*1.216006) for i in [0, 26689, 29396, 32104, 34811, 37520, 40227, 42935, 45643, 48350, 51058, 53765, 56473, 59180, 61888, 64595, 67303, 70010, 72720, 75427, 78135, 80842, 83550, 86257, 88965, 91672, 94380, 97087, 99795, 102502, 105211, 107918, 110626, 113333, 116041, 118748, 121456, 124163, 126871, 129579, 132286, 134995, 137702, 140410, 143117, 145825, 148532, 151240, 153947, 156655, 159362, 162070, 164777, 167485, 170192, 172901, 175608, 178316, 181023, 183731, 186438]]
    攻击次数 = 1
    data1 = [(i*1.215992) for i in [0, 41159, 45335, 49511, 53686, 57862, 62038, 66213, 70389, 74564, 78740, 82916, 87091, 91267, 95443, 99618, 103794, 107970, 112145, 116321, 120497, 124672, 128847, 133024, 137199, 141374, 145551, 149726, 153901, 158078, 162253, 166428, 170605, 174780, 178955, 183132, 187307, 191482, 195659, 199834, 204009, 208185, 212361, 216536, 220712, 224888, 229063, 233239, 237415, 241590, 245766, 249941, 254117, 258293, 262468, 266644, 270820, 274995, 279171, 283347, 287522]]
    攻击次数2 = 1
    CD = 50.0
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 1.23
            self.倍率 = 1.16
            self.CD *= 0.9

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能25(主动技能):
    名称 = '龙神裁决：终末之光'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    data0 = [(i*1.215001) for i in [0, 173732, 214019, 254304, 294591, 334877, 375162, 415449, 455734, 496020, 536307, 576592, 616878, 657164, 697450, 737735, 778022, 818308, 858593, 898880, 939165, 979452, 1019738, 1060023, 1100310, 1140595, 1180881, 1221168, 1261453, 1301739, 1342025, 1382311, 1422597, 1462883, 1503169, 1543454, 1583741, 1624027, 1664312, 1704599, 1744884, 1785171, 1825457, 1865742, 1906029, 1946314, 1986600, 2026887, 2067172, 2107458, 2147744, 2188030, 2228315, 2268602, 2308888, 2349173, 2389460, 2429745, 2470032, 2510318, 2550603, 2590890, 2631175, 2671461, 2711748, 2752033, 2792319, 2832605, 2872891, 2913177, 2953463]]
    攻击次数 = 1
    CD = 180

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能26(被动技能):
    名称 = '龙血誓约'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能27(主动技能):
    名称 = '龙咆雷鸣'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    data0 = [int(i*1.214998) for i in [0, 10824, 11923, 13021, 14119, 15217, 16315, 17414, 18512, 19610, 20708, 21806, 22905, 24003, 25101, 26199, 27297, 28395, 29494, 30592, 31690, 32788, 33886, 34985, 36083, 37181, 38279, 39377, 40476, 41574, 42672, 43770, 44868, 45966, 47065, 48163, 49261, 50359, 51457, 52556, 53654, 54752, 55850, 56948, 58047, 59145, 60243, 61341, 62439, 63537, 64636, 65734, 66832, 67930, 69028, 70127, 71225, 72323, 73421, 74519, 75618]]
    攻击次数 = 5
    data1 = [int(i*1.214986) for i in [0, 81187, 89423, 97660, 105896, 114133, 122369, 130605, 138842, 147078, 155315, 163551, 171787, 180024, 188260, 196497, 204733, 212969, 221206, 229442, 237679, 245915, 254151, 262388, 270624, 278861, 287097, 295333, 303570, 311806, 320043, 328279, 336515, 344752, 352988, 361225, 369461, 377698, 385934, 394170, 402407, 410643, 418880, 427116, 435352, 443589, 451825, 460062, 468298, 476534, 484771, 493007, 501244, 509480, 517716, 525953, 534189, 542426, 550662, 558898, 567135]]
    攻击次数2 = 1
    CD = 60.0

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2) * self.倍率


class 技能28(主动技能):
    名称 = '龙神君临·虚空烬灭'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    data0 = [int(i*1.237999) for i in [0, 43811, 53971, 64131, 74289, 84449, 94608, 104768, 114926, 125086, 135245, 145404, 155564, 165723, 175883, 186041, 196201, 206360, 216520, 226678, 236838, 246998, 257157, 267316, 277475, 287635, 297794, 307953, 318112, 328272, 338432, 348590, 358750, 368909, 379069, 389227, 399387, 409546, 419706, 429865, 440024, 450184, 460342, 470502, 480661, 490821, 500979, 511139, 521299, 531458, 541617, 551776, 561936, 572095, 582254, 592413, 602573, 612733, 622891, 633051, 643210, 653370, 663528, 673688, 683847, 694007, 704166, 714325, 724485, 734644, 744803]]
    攻击次数 = 1
    data1 = [int(i*1.238017) for i in [0, 21906, 26985, 32065, 37145, 42224, 47303, 52384, 57463, 62542, 67622, 72702, 77782, 82861, 87941, 93021, 98100, 103179, 108260, 113339, 118419, 123499, 128578, 133658, 138737, 143817, 148897, 153976, 159056, 164136, 169215, 174295, 179375, 184454, 189534, 194613, 199694, 204773, 209852, 214933, 220012, 225091, 230171, 235251, 240330, 245410, 250489, 255570, 260649, 265728, 270809, 275888, 280967, 286047, 291127, 296207, 301286, 306366, 311446, 316525, 321604, 326685, 331764, 336844, 341923, 347003, 352083, 357162, 362242, 367322, 372401]]
    攻击次数2 = 8
    data2 = [int(i*1.238004) for i in [0, 131435, 161913, 192392, 222869, 253347, 283825, 314303, 344781, 375259, 405736, 436214, 466693, 497170, 527648, 558126, 588604, 619082, 649560, 680037, 710516, 740994, 771471, 801949, 832427, 862905, 893383, 923861, 954338, 984817, 1015295, 1045772, 1076250, 1106728, 1137206, 1167684, 1198162, 1228639, 1259118, 1289596, 1320073, 1350551, 1381030, 1411507, 1441985, 1472463, 1502940, 1533419, 1563897, 1594374, 1624852, 1655331, 1685808, 1716286, 1746764, 1777241, 1807720, 1838198, 1868675, 1899153, 1929632, 1960109, 1990587, 2021065, 2051542, 2082021, 2112499, 2142976, 2173454, 2203933, 2234411]]
    攻击次数3 = 1
    data3 = [int(i*1.238011) for i in [0, 21906, 26985, 32065, 37145, 42224, 47303, 52384, 57463, 62542, 67622, 72702, 77782, 82861, 87941, 93021, 98100, 103179, 108260, 113339, 118419, 123499, 128578, 133658, 138737, 143817, 148897, 153976, 159056, 164136, 169215, 174295, 179375, 184454, 189534, 194613, 199694, 204773, 209852, 214933, 220012, 225091, 230171, 235251, 240330, 245410, 250489, 255570, 260649, 265728, 270809, 275888, 280967, 286047, 291127, 296207, 301286, 306366, 311446, 316525, 321604, 326685, 331764, 336844, 341923, 347003, 352083, 357162, 362242, 367322, 372401]]
    攻击次数4 = 4
    CD = 290.0

    def 加成倍率(self, 武器类型):
        return 0.0

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级] * self.攻击次数2+ self.data2[self.等级] * self.攻击次数3+ self.data3[self.等级] * self.攻击次数4) * self.倍率

class 技能29(主动技能):
    名称 = '普通攻击（一轮）'
    所在等级 = 1
    等级上限 = 1
    基础等级 = 1
    基础 = 1114.6981
    成长 = 0
    CD = 1


技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能' + str(i) + '())')
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
    temp = i
    if i.是否有伤害 == 1 and i.是否有护石 == 1 and i.所在等级 != 45 and i.所在等级 != 70:
        护石选项.append(i.名称)
护石选项.append('魔龙之息')
护石选项.append('魔龙天翔')

符文选项 = ['无']
for i in 技能列表:
    temp = i
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.所在等级 != 48 and i.是否有伤害 == 1 and i.所在等级 != 45 and i.所在等级 != 70:
        符文选项.append(i.名称)
符文选项.append('魔龙之息')
符文选项.append('魔龙天翔')


class 职业角色属性(角色属性):
    实际名称 = '皓曦·龙骑士'
    角色 = '守护者'
    职业 = '龙骑士'

    武器选项 = ['太刀', '钝器', '巨剑', '短剑']

    类型选择 = ['物理固伤']

    类型 = '物理固伤'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 1.850

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[17].等级 = self.技能栏[16].等级

        if self.装备检查('守护的抉择'):
            if self.护石第一栏 == '魔龙之息':
                self.技能栏[self.技能序号['魔龙之息(脱手)']].CD *= 0.7
                self.技能栏[self.技能序号['魔龙之息(脱手)']].倍率 *= 1.55
                self.技能栏[self.技能序号['魔龙之息(骑乘)']].CD *= 0.7
                self.技能栏[self.技能序号['魔龙之息(骑乘)']].倍率 *= 1.55
            if self.护石第二栏 == '魔龙之息':
                self.技能栏[self.技能序号['魔龙之息(脱手)']].CD *= 0.75
                self.技能栏[self.技能序号['魔龙之息(脱手)']].倍率 *= 1.45
                self.技能栏[self.技能序号['魔龙之息(骑乘)']].CD *= 0.75
                self.技能栏[self.技能序号['魔龙之息(骑乘)']].倍率 *= 1.45
            if self.护石第一栏 == '魔龙天翔':
                self.技能栏[self.技能序号['魔龙天翔(脱手)']].CD *= 0.7
                self.技能栏[self.技能序号['魔龙天翔(脱手)']].倍率 *= 1.55
                self.技能栏[self.技能序号['魔龙天翔(骑乘)']].CD *= 0.7
                self.技能栏[self.技能序号['魔龙天翔(骑乘)']].倍率 *= 1.55
            if self.护石第二栏 == '魔龙天翔':
                self.技能栏[self.技能序号['魔龙天翔(脱手)']].CD *= 0.75
                self.技能栏[self.技能序号['魔龙天翔(脱手)']].倍率 *= 1.45
                self.技能栏[self.技能序号['魔龙天翔(骑乘)']].CD *= 0.75
                self.技能栏[self.技能序号['魔龙天翔(骑乘)']].倍率 *= 1.45


class 皓曦·龙骑士(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业角色属性()
        self.角色属性A = 职业角色属性()
        self.角色属性B = 职业角色属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)

    def 护石类型选项更新(self, x):
        self.护石类型选项[x].clear()
        if self.护石栏[x].currentText() != '无':
            if self.护石栏[x].currentText() not in ['魔龙天翔', '魔龙之息']:
                try:
                    self.护石类型选项[x].addItems(
                        self.初始属性.技能栏[self.初始属性.技能序号[self.护石栏[x].currentText()]].护石选项)
                except:
                    self.护石类型选项[x].addItem('魔界')
                    self.护石栏[x].setCurrentIndex(0)
            elif self.护石栏[x].currentText() in ['魔龙天翔', '魔龙之息']:
                self.护石类型选项[x].addItem('魔界')
                self.护石类型选项[x].addItem('圣痕')
        else:
            self.护石类型选项[x].addItem('魔界')

    def 加载护石(self, 属性):
        for k in range(3):
            if self.护石栏[k].currentText() != '无' and self.护石栏[k].currentText() != '魔龙之息' and self.护石栏[k].currentText() != '魔龙天翔':
                try:
                    属性.技能栏[self.角色属性A.技能序号[self.护石栏[k].currentText()]].装备护石()
                except:
                    属性.技能栏[self.角色属性A.技能序号[self.护石栏[k].currentText()]].装备护石(
                        self.护石类型选项[k].currentIndex())
            elif self.护石栏[k].currentText() == '魔龙之息':
                if self.护石类型选项[k].currentText() == '魔界':
                    属性.技能栏[self.角色属性A.技能序号['魔龙之息(脱手)']].装备护石(0)
                    属性.技能栏[self.角色属性A.技能序号['魔龙之息(骑乘)']].装备护石(0)
                elif self.护石类型选项[k].currentText() == '圣痕':
                    属性.技能栏[self.角色属性A.技能序号['魔龙之息(脱手)']].装备护石(1)
                    属性.技能栏[self.角色属性A.技能序号['魔龙之息(骑乘)']].装备护石(1)
            elif self.护石栏[k].currentText() == '魔龙天翔':
                if self.护石类型选项[k].currentText() == '魔界':
                    属性.技能栏[self.角色属性A.技能序号['魔龙天翔(脱手)']].装备护石(0)
                    属性.技能栏[self.角色属性A.技能序号['魔龙天翔(骑乘)']].装备护石(0)
                elif self.护石类型选项[k].currentText() == '圣痕':
                    属性.技能栏[self.角色属性A.技能序号['魔龙天翔(脱手)']].装备护石(1)
                    属性.技能栏[self.角色属性A.技能序号['魔龙天翔(骑乘)']].装备护石(1)

        属性.护石第一栏 = self.护石栏[0].currentText()
        属性.护石第二栏 = self.护石栏[1].currentText()
        属性.护石第三栏 = self.护石栏[2].currentText()

        for i in range(9):
            if self.符文[i].currentText() != '无' and self.符文效果[i].currentText() != '无' and self.符文[i].currentText() != '魔龙之息' and self.符文[i].currentText() != '魔龙天翔':
                for j in self.符文效果[i].currentText().split(','):
                    if '攻击' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].倍率 *= 1 + int(
                            j.replace('攻击', '').replace('%', '')) / 100
                    if 'CD' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].CD *= 1 + int(
                            j.replace('CD', '').replace('%', '')) / 100
            elif self.符文[i].currentText() == '魔龙之息':
                for j in self.符文效果[i].currentText().split(','):
                    if '攻击' in j:
                        属性.技能栏[self.角色属性A.技能序号['魔龙之息(脱手)']].倍率 *= 1 + int(
                            j.replace('攻击', '').replace('%', '')) / 100
                        属性.技能栏[self.角色属性A.技能序号['魔龙之息(骑乘)']].倍率 *= 1 + int(
                            j.replace('攻击', '').replace('%', '')) / 100
                    if 'CD' in j:
                        属性.技能栏[self.角色属性A.技能序号['魔龙之息(脱手)']].CD *= 1 + int(
                            j.replace('CD', '').replace('%', '')) / 100
                        属性.技能栏[self.角色属性A.技能序号['魔龙之息(骑乘)']].CD *= 1 + int(
                            j.replace('CD', '').replace('%', '')) / 100
            elif self.符文[i].currentText() == '魔龙天翔':
                for j in self.符文效果[i].currentText().split(','):
                    if '攻击' in j:
                        属性.技能栏[self.角色属性A.技能序号['魔龙天翔(脱手)']].倍率 *= 1 + int(
                            j.replace('攻击', '').replace('%', '')) / 100
                        属性.技能栏[self.角色属性A.技能序号['魔龙天翔(骑乘)']].倍率 *= 1 + int(
                            j.replace('攻击', '').replace('%', '')) / 100
                    if 'CD' in j:
                        属性.技能栏[self.角色属性A.技能序号['魔龙天翔(脱手)']].CD *= 1 + int(
                            j.replace('CD', '').replace('%', '')) / 100
                        属性.技能栏[self.角色属性A.技能序号['魔龙天翔(骑乘)']].CD *= 1 + int(
                            j.replace('CD', '').replace('%', '')) / 100
