from math import *
from PublicReference.base import *


# 武器钝器
class 职业主动技能(主动技能):

    data0 = []
    data1 = []
    data2 = []
    data3 = []

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
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率

    # def 等效CD(self, 武器类型):
        # if 武器类型 == '钝器':
        # return round(self.CD / self.恢复 * 1.05, 1)

# 天使光翼


class 技能0(被动技能):
    名称 = '天使光翼'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['信仰聚合神光惩戒', '神圣意志大天使降临', '神光耀世']

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 * self.等级, 5)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.95

# 天使降临


class 技能1(被动技能):
    名称 = '天使降临'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.08 + 0.01 * self.等级, 5)
        else:
            return round(0.98 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.08 + 0.01 * self.等级, 5)
        else:
            return round(0.98 + 0.02 * self.等级, 5)

# 一觉被动


class 技能2(被动技能):
    名称 = '荣耀之光'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105+0.015 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)

# 二觉被动


class 技能3(被动技能):
    名称 = '戒律'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 技能4(职业主动技能):
    名称 = '普通攻击'
    备注 = '一轮'
    是否主动 = 0
    关联技能 = ['无']
    所在等级 = 1
    基础等级 = 1
    等级上限 = 20
    CD = 5
    攻击次数 = 1.58+1.76+1.98+2.21
    基础 = 936.3 - 8.9
    成长 = 8.9

    攻击次数2 = 5
    喷涌数据 = 0

    TP成长 = 0.10
    TP上限 = 3

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) * (1 + self.TP成长 * self.TP等级) + self.攻击次数2 * self.喷涌数据) * self.倍率)

# 神光冲击


class 技能5(职业主动技能):
    名称 = '神光冲击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    # 基础 = 1596.7
    # 成长 = 180.3
    # 攻击力：<data0>%
    data0 = [(i*1.0/1.126*1.1342) for i in [0, 1777, 1957, 2137, 2318, 2498, 2678, 2858, 3039, 3219, 3399, 3580, 3760, 3940, 4121, 4301, 4481, 4661, 4842, 5022, 5202, 5383, 5563, 5743, 5923, 6104, 6284, 6464, 6645,
                                            6825, 7005, 7186, 7366, 7546, 7726, 7907, 8087, 8267, 8448, 8628, 8808, 8988, 9169, 9349, 9529, 9710, 9890, 10070, 10251, 10431, 10611, 10791, 10972, 11152, 11332, 11513, 11693, 11873, 12053, 12234, 12414]]
    CD = 4
    TP成长 = 0.10
    TP上限 = 5

# 神光连斩


class 技能6(职业主动技能):
    名称 = '神光连斩'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    # 基础 = 2109.7
    # 成长 = 238.3
    # 第1击攻击力：<data0>%
    data0 = [(i*1.0) for i in [0, 1790, 1972, 2153, 2335, 2517, 2698, 2880, 3062, 3243, 3425, 3607, 3788, 3970, 4152, 4333, 4515, 4696, 4878, 5060, 5241, 5423, 5605, 5786, 5968, 6150, 6331, 6513, 6695, 6876, 7058, 7240, 7421, 7603, 7785, 7966, 8148, 8329, 8511, 8693, 8874, 9056, 9238, 9419, 9601, 9783, 9964, 10146, 10328, 10509, 10691, 10873, 11054, 11236, 11418, 11599, 11781, 11962, 12144, 12326, 12507]]
    # 第2击攻击力：<data1>%
    data1 = [(i*1.0) for i in [0, 1790, 1972, 2153, 2335, 2517, 2698, 2880, 3062, 3243, 3425, 3607, 3788, 3970, 4152, 4333, 4515, 4696, 4878, 5060, 5241, 5423, 5605, 5786, 5968, 6150, 6331, 6513, 6695, 6876, 7058, 7240, 7421, 7603, 7785, 7966, 8148, 8329, 8511, 8693, 8874, 9056, 9238, 9419, 9601, 9783, 9964, 10146, 10328, 10509, 10691, 10873, 11054, 11236, 11418, 11599, 11781, 11962, 12144, 12326, 12507]]
    攻击次数2 = 1
    CD = 5
    TP成长 = 0.10
    TP上限 = 5

# 圣盾突击


class 技能7(职业主动技能):
    名称 = '圣盾突击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    # 基础 = 2756.7
    # 成长 = 311.3
    # 攻击力：<data0>% X 4
    data0 = [(i*1.0) for i in [0, 772, 851, 929, 1007, 1086, 1164, 1243, 1321, 1399, 1478, 1556, 1634, 1713, 1791, 1870, 1948, 2026, 2105, 2183, 2262, 2340, 2418, 2497, 2575, 2654, 2732, 2810, 2889, 2967, 3045, 3124, 3202, 3281, 3359, 3437, 3516, 3594, 3673, 3751, 3829, 3908, 3986, 4065, 4143, 4221, 4300, 4378, 4456, 4535, 4613, 4692, 4770, 4848, 4927, 5005, 5084, 5162, 5240, 5319, 5397]]
    攻击次数 = 4
    CD = 6
    TP成长 = 0.10
    TP上限 = 5


# 神光喷涌
class 技能8(职业主动技能):
    名称 = '神光喷涌'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    # 基础 = 4451.9
    # 成长 = 503.1
    # 锤击攻击力：<data0>%
    data0 = [(i*1.0) for i in [0, 924, 1019, 1112, 1205, 1300, 1393, 1487, 1581, 1675, 1768, 1863, 1956, 2050, 2144, 2238, 2331, 2426, 2519, 2612, 2707, 2800, 2894, 2988, 3082, 3175, 3270, 3363, 3457, 3551, 3645, 3738, 3833, 3926, 4019, 4114, 4207, 4301, 4395, 4489, 4583, 4677, 4770, 4865, 4958, 5052, 5146, 5240, 5333, 5427, 5521, 5614, 5709, 5802, 5896, 5990, 6084, 6177, 6272, 6365, 6459, 4594, 4660, 4726, 4792, 4857, 4923, 4989, 5055, 5120, 5186]]
    # 喷涌的神光攻击力：<data1>% X 4
    data1 = [(i*1.0) for i in [0, 924, 1019, 1112, 1205, 1300, 1393, 1487, 1581, 1675, 1768, 1863, 1956, 2050, 2144, 2238, 2331, 2426, 2519, 2612, 2707, 2800, 2894, 2988, 3082, 3175, 3270, 3363, 3457, 3551, 3645, 3738, 3833, 3926, 4019, 4114, 4207, 4301, 4395, 4489, 4583, 4677, 4770, 4865, 4958, 5052, 5146, 5240, 5333, 5427, 5521, 5614, 5709, 5802, 5896, 5990, 6084, 6177, 6272, 6365, 6459, 4594, 4660, 4726, 4792, 4857, 4923, 4989, 5055, 5120, 5186]]
    攻击次数2 = 4
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

    def 小型喷涌神光攻击力(self):
        return int(self.data1[self.等级] * (1 + self.TP成长 * self.TP等级)*0.1)

# 神光盾击


class 技能9(职业主动技能):
    名称 = '神光盾击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 基础 = 4908.2
    # 成长 = 554.8
    # 第1击攻击力：<data0>% X 3
    data0 = [(i*1.0) for i in [0, 906, 998, 1090, 1182, 1274, 1366, 1457, 1549, 1641, 1733, 1825, 1917, 2009, 2101, 2193, 2285, 2377, 2469, 2561, 2653, 2745, 2837, 2929, 3021, 3112, 3204, 3296, 3388, 3480, 3572, 3664, 3756, 3848, 3940, 4032, 4124, 4216, 4308, 4400, 4492, 4584, 4676, 4767, 4859, 4951, 5043, 5135, 5227, 5319, 5411, 5503, 5595, 5687, 5779, 5871, 5963, 6055, 6147, 6239, 6331]]
    攻击次数 = 3
    # 第2击攻击力：<data1>% X 3
    data1 = [(i*1.0) for i in [0, 929, 1023, 1118, 1212, 1306, 1401, 1495, 1589, 1684, 1778, 1872, 1966, 2061, 2155, 2249, 2344, 2438, 2532, 2627, 2721, 2815, 2909, 3004, 3098, 3192, 3287, 3381, 3475, 3570, 3664, 3758, 3853, 3947, 4041, 4135, 4230, 4324, 4418, 4513, 4607, 4701, 4796, 4890, 4984, 5078, 5173, 5267, 5361, 5456, 5550, 5644, 5739, 5833, 5927, 6022, 6116, 6210, 6304, 6399, 6493]]
    攻击次数2 = 3
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

# 烈光


class 技能10(职业主动技能):
    名称 = '烈光'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 基础 = 4966.2
    # 成长 = 560.8
    # 上挑攻击力：<data0>%
    data0 = [(i*1.0) for i in [0, 2780, 3062, 3344, 3626, 3908, 4190, 4472, 4754, 5036, 5318, 5600, 5882, 6164, 6446, 6728, 7010, 7292, 7574, 7856, 8138, 8420, 8702, 8984, 9266, 9548, 9830, 10112, 10394, 10676, 10958, 11240, 11522, 11804, 12086, 12369, 12651, 12933, 13215, 13497, 13779, 14061, 14343, 14625, 14907, 15189, 15471, 15753, 16035, 16317, 16599, 16881, 17163, 17445, 17727, 18009, 18291, 18573, 18855, 19137, 19419, 19701]]
    # 下砸攻击力：<data1>%
    data1 = [(i*1.0) for i in [0, 2788, 3071, 3354, 3637, 3919, 4202, 4485, 4768, 5051, 5334, 5617, 5900, 6183, 6465, 6748, 7031, 7314, 7597, 7880, 8163, 8446, 8728, 9011, 9294, 9577, 9860, 10143, 10426, 10709, 10992, 11274, 11557, 11840, 12123, 12406, 12689, 12972, 13255, 13537, 13820, 14103, 14386, 14669, 14952, 15235, 15518, 15801, 16083, 16366, 16649, 16932, 17215, 17498, 17781, 18064, 18346, 18629, 18912, 19195, 19478, 19761]]
    攻击次数2 = 1
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

# 神光闪耀


class 技能11(职业主动技能):
    名称 = '神光闪耀'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 基础 = 7816.3
    # 成长 = 882.7
    # 多段攻击力：<data0>% X 10
    data0 = [(i*1.0) for i in [0, 674, 743, 811, 880, 948, 1016, 1085, 1153, 1222, 1290, 1359, 1427, 1496, 1564, 1633, 1701, 1769, 1838, 1906, 1975, 2043, 2112, 2180, 2249, 2317, 2385, 2454, 2522, 2591, 2659, 2728, 2796, 2865, 2933, 3002, 3070, 3138, 3207, 3275, 3344, 3412, 3481, 3549, 3618, 3686, 3754, 3823, 3891, 3960, 4028, 4097, 4165, 4234, 4302, 4371, 4439, 4507, 4576, 4644, 4713, 4781, 4850, 4918, 4987, 5055, 5123, 5192, 5260, 5329, 5397]]
    攻击次数 = 10
    # 最后一击攻击力：<data1>%
    data1 = [(i*1.0) for i in [0, 2891, 3185, 3478, 3771, 4065, 4358, 4651, 4945, 5238, 5531, 5825, 6118, 6411, 6705, 6998, 7292, 7585, 7878, 8172, 8465, 8758, 9052, 9345, 9638, 9932, 10225, 10518, 10812, 11105, 11399, 11692, 11985, 12279, 12572, 12865, 13159, 13452, 13745, 14039, 14332, 14625, 14919, 15212, 15506, 15799, 16092, 16386, 16679, 16972, 17266, 17559, 17852, 18146, 18439, 18732, 19026, 19319, 19613, 19906, 20199, 20493, 20786, 21079, 21373, 21666, 21959, 22253, 22546, 22839, 23133]]
    攻击次数2 = 1
    CD = 16
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 2

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.24 + 0.09

# 神光闪影击


class 技能12(职业主动技能):
    名称 = '神光闪影击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 基础 = 10235.5
    # 成长 = 1155.5
    data0 = [(i*1.0) for i in [0, 530, 583, 637, 691, 745, 799, 852, 906, 960, 1014, 1067, 1121, 1175, 1229, 1283, 1336, 1390, 1444, 1498, 1552, 1605, 1659, 1713, 1767, 1820, 1874, 1928, 1982, 2036, 2089, 2143, 2197, 2251, 2304, 2358, 2412, 2466, 2520, 2573, 2627, 2681, 2735, 2788, 2842, 2896, 2950, 3004, 3057, 3111, 3165, 3219, 3273, 3326, 3380, 3434, 3488, 3541, 3595, 3649, 3703]]
    攻击次数 = 15
    data1 = [(i*1.0) for i in [0, 3526, 3884, 4242, 4599, 4957, 5315, 5673, 6031, 6388, 6746, 7104, 7462, 7819, 8177, 8535, 8893, 9251, 9608, 9966, 10324, 10682, 11039, 11397, 11755, 12113, 12471, 12828, 13186, 13544, 13902, 14259, 14617, 14975, 15333, 15691, 16048, 16406, 16764, 17122, 17479, 17837, 18195, 18553, 18911, 19268, 19626, 19984, 20342, 20699, 21057, 21415, 21773, 22131, 22488, 22846, 23204, 23562, 23919, 24277, 24635]]
    攻击次数2 = 1
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


# 神罚之锤
class 技能13(职业主动技能):
    名称 = '神罚之锤'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    # 基础 = 11383.6
    # 成长 = 1285.4
    data0 = [(i*1.0) for i in [0, 12762, 14056, 15351, 16646, 17941, 19235, 20530, 21825, 23120, 24414, 25709, 27004, 28298, 29593, 30888, 32183, 33477, 34772, 36067, 37361, 38656, 39951, 41246, 42540, 43835, 45130, 46424, 47719, 49014, 50309, 51603, 52898, 54193, 55488, 56782, 58077, 59372, 60666, 61961, 63256, 64551, 65845, 67140, 68435, 69729, 71024, 72319, 73614, 74908, 76203, 77498, 78793, 80087, 81382, 82677, 83971, 85266, 86561, 87856, 89150]]
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.27
        elif x == 1:
            self.倍率 *= 1.27 + 0.09


# 神光之跃
class 技能14(职业主动技能):
    名称 = '神光之跃'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    # 基础 = 19198.4
    # 成长 = 2167.6
    data0 = [(i*1.0) for i in [0, 21521, 23705, 25888, 28071, 30255, 32438, 34622, 36805, 38988, 41172, 43355, 45538, 47722, 49905, 52089, 54272, 56455, 58639, 60822, 63005, 65189, 67372, 69556, 71739, 73922, 76106, 78289, 80472, 82656, 84839, 87023, 89206, 91389, 93573, 95756, 97939, 100123, 102306, 104490, 106673, 108856, 111040, 113223, 115406, 117590, 119773, 121957, 124140, 126323, 128507, 130690, 132873, 135057, 137240, 139424, 141607, 143790, 145974, 148157, 150340]]
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.24 + 0.08


# 一觉
class 技能15(职业主动技能):
    名称 = '信仰聚合神光惩戒'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    # 基础 = 46241.6
    # 成长 = 13959.2
    data0 = [(i*1.0) for i in [0, 60638, 74699, 88760, 102821, 116882, 130943, 145004, 159065, 173126, 187187, 201248, 215309, 229370, 243431, 257492, 271553, 285614, 299675, 313736, 327797, 341858, 355919, 369980, 384041, 398102, 412163, 426224, 440285, 454346, 468407, 482468, 496529, 510590, 524651, 538712, 552773, 566834, 580895, 594956, 609017]]
    CD = 145.0


# 圣盾裁决
class 技能16(职业主动技能):
    名称 = '圣盾裁决'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    # 基础 = 14912.3
    # 成长 = 1683.7
    data0 = [(i*1.0) for i in [0, 16717, 18413, 20109, 21805, 23501, 25197, 26893, 28589, 30285, 31981, 33677, 35373, 37069, 38765, 40461, 42157, 43853, 45549, 47245, 48941, 50637, 52333, 54029, 55725, 57421, 59116, 60812, 62508, 64204, 65900, 67596, 69292, 70988, 72684, 74380, 76076, 77772, 79468, 81164, 82860]]
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
            self.CD *= 0.90
        elif x == 1:
            self.倍率 *= 1.24 + 0.08
            self.CD *= 0.90

# 破晓之光


class 技能17(职业主动技能):
    名称 = '破晓之光'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    # 基础 = 29092.3
    # 成长 = 3284.7
    data0 = [(i*1.0) for i in [0, 32613, 35922, 39230, 42539, 45848, 49156, 52465, 55774, 59082, 62391, 65699, 69008, 72317, 75625, 78934, 82243, 85551, 88860, 92168, 95477, 98786, 102094, 105403, 108712, 112020, 115329, 118637, 121946, 125255, 128563, 131872, 135181, 138489, 141798, 145107, 148415, 151724, 155032, 158341, 161650]]
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.11
        self.CD *= 0.90

# 神光回旋斩 择优


class 技能18(职业主动技能):
    名称 = '神光回旋斩'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    # 基础 = 46139.6
    # 成长 = 5209.4
    data0 = [(i*1.0) for i in [0, 49688, 54729, 59770, 64811, 69852, 74892, 79933, 84974, 90015, 95056, 100097, 105138, 110178, 115219, 120260, 125301, 130342, 135383, 140424, 145465, 150505, 155546, 160587, 165628, 170669, 175710, 180751, 185791, 190832, 195873, 200914, 205955, 210996, 216037, 221078, 226118, 231159, 236200, 241241, 246282]]
    CD = 40
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.368

# 神圣信约


class 技能19(职业主动技能):
    名称 = '神圣信约'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    # 基础 = 50250.4
    # 成长 = 5673.6
    data0 = [(i*1.0) for i in [0, 5111, 5630, 6149, 6667, 7186, 7705, 8223, 8742, 9260, 9779, 10298, 10816, 11335, 11853, 12372, 12891, 13409, 13928, 14446, 14965, 15484, 16002, 16521, 17039, 17558, 18077, 18595, 19114, 19633, 20151, 20670, 21188, 21707, 22226, 22744, 23263, 23781, 24300, 24819, 25337]]
    攻击次数 = 11
    CD = 45
    是否有护石 = 1
    蓄力 = 0

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0 and self.蓄力 == 0:
            self.攻击次数 = 0
            self.攻击次数2 = 1
            self.data1 = [(i*11*1.32) for i in self.data0]
        if x == 0 and self.蓄力 == 1:
            self.攻击次数 = 0
            self.攻击次数2 = 1
            self.data1 = [(i*(11+0.23)*1.32) for i in self.data0]

# 二觉


class 技能20(职业主动技能):
    名称 = '神圣意志大天使降临'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    # 基础 = 106483
    # 成长 = 32147
    data0 = [(i*1.0) for i in [0, 139642, 172022, 204403, 236784, 269165, 301546, 333926, 366307, 398688, 431069, 463450, 495830, 528211, 560592, 592973, 625354, 657734, 690115, 722496, 754877, 787258, 819638, 852019, 884400, 916781, 949162, 981542, 1013923, 1046304, 1078685, 1111066, 1143446, 1175827, 1208208, 1240589, 1272970, 1305350, 1337731, 1370112, 1402493]]
    CD = 180


class 技能21(被动技能):
    名称 = '超越之翼'
    所在等级 = 95
    等级上限 = 40
    等级精通 = 30
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能22(职业主动技能):
    名称 = '神光耀世'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    data0 = [int(i*1.0) for i in [0, 9575, 10546, 11518, 12489, 13461, 14432, 15404, 16375, 17346, 18318, 19289, 20261, 21232, 22204, 23175, 24146, 25118, 26089, 27061, 28032, 29004, 29975, 30947, 31918, 32889, 33861, 34832, 35804, 36775, 37747, 38718, 39689, 40661, 41632, 42604, 43575, 44547, 45518, 46489, 47461]]
    攻击次数 = 4
    data1 = [int(i*1.0) for i in [0, 12767, 14062, 15357, 16653, 17948, 19243, 20538, 21834, 23129, 24424, 25719, 27015, 28310, 29605, 30900, 32195, 33491, 34786, 36081, 37376, 38672, 39967, 41262, 42557, 43853, 45148, 46443, 47738, 49034, 50329, 51624, 52919, 54215, 55510, 56805, 58100, 59396, 60691, 61986, 63281]]
    攻击次数2 = 1
    data2 = [int(i*1.0) for i in [0, 12767, 14062, 15357, 16653, 17948, 19243, 20538, 21834, 23129, 24424, 25719, 27015, 28310, 29605, 30900, 32195, 33491, 34786, 36081, 37376, 38672, 39967, 41262, 42557, 43853, 45148, 46443, 47738, 49034, 50329, 51624, 52919, 54215, 55510, 56805, 58100, 59396, 60691, 61986, 63281]]
    攻击次数3 = 6
    CD = 60

class 技能23(职业主动技能):
    名称 = '启示录：末日救赎'
    所在等级 = 100
    等级上限 = 40
    等级精通 = 30
    基础等级 = 2
    关联技能 = ['无']
    CD = 290.0

    data0 = [int(i*1.0) for i in [0, 36449, 44902, 53354, 61806, 70258, 78710, 87163, 95615, 104067, 112519, 120971, 129423, 137876, 146328, 154780, 163232, 171684, 180136, 188589, 197041, 205493, 213945, 222397, 230849, 239302, 247754, 256206, 264658, 273110, 281563, 290015, 298467, 306919, 315371, 323823, 332276, 340728, 349180, 357632, 366084]]
    攻击次数 = 1

    data1 = [int(i*1.0) for i in [0, 10414, 12829, 15244, 17659, 20073, 22488, 24903, 27318, 29733, 32148, 34563, 36978, 39393, 41808, 44222, 46637, 49052, 51467, 53882, 56297, 58712, 61127, 63542, 65957, 68372, 70786, 73201, 75616, 78031, 80446, 82861, 85276, 87691, 90106, 92521, 94936, 97350, 99765, 102180, 104595]]
    攻击次数2 = 7

    data2 = [int(i*1.0) for i in [0, 145799, 179608, 213417, 247226, 281034, 314843, 348652, 382460, 416269, 450078, 483886, 517695, 551504, 585312, 619121, 652930, 686739, 720547, 754356, 788165, 821973, 855782, 889591, 923399, 957208, 991017, 1024825, 1058634, 1092443, 1126252, 1160060, 1193869, 1227678, 1261486, 1295295, 1329104, 1362912, 1396721, 1430530, 1464338]]
    攻击次数3 = 1

    data3 = [0, 15621, 19243, 22866, 26488, 30110, 33733, 37355, 40977, 44600, 48222, 51845, 55467, 59089, 62712, 66334, 69956, 73579, 77201, 80823, 84446, 88068, 91690, 95313, 98935, 102558, 106180, 109802, 113425, 117047, 120669, 124292, 127914, 131536, 135159, 138781, 142404, 146026, 149648, 153271, 156893]
    攻击次数4 = 7


    def 加成倍率(self, 武器类型):
        return 0.0


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
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        护石选项.append(i.名称)

符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        符文选项.append(i.名称)


class 职业属性(角色属性):
    实际名称 = '皓曦·帕拉丁'
    角色 = '守护者'
    职业 = '帕拉丁'

    武器选项 = ['钝器']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '板甲'
    防具精通属性 = ['力量']

    主BUFF = 1.89

    蓄力神圣信约 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()

        self.技能栏[self.技能序号['普通攻击']
                 ].喷涌数据 = self.技能栏[self.技能序号['神光喷涌']].小型喷涌神光攻击力()

        if self.蓄力神圣信约 == 1:
            # print(self.蓄力神圣信约)
            self.技能栏[self.技能序号['神圣信约']].蓄力 = 1
            self.技能栏[self.技能序号['神圣信约']].装备护石(0)


class 皓曦·帕拉丁(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业属性()
        self.角色属性A = 职业属性()
        self.角色属性B = 职业属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)

    def 护石判断(self):
        sign = 0
        sign2 = 0
        for x in range(3):
            if self.护石栏[x].currentText() == '神圣信约':
                sign = 1
        if sign == 1:
            # self.蓄力神圣信约.setChecked(False)
            self.蓄力神圣信约.setEnabled(True)
            self.蓄力神圣信约.setStyleSheet(复选框样式)
        else:
            self.蓄力神圣信约.setChecked(False)
            self.蓄力神圣信约.setEnabled(False)
            self.蓄力神圣信约.setStyleSheet(复选框样式)

    def 界面(self):
        super().界面()
        for i in range(3):
            self.护石栏[i].currentIndexChanged.connect(lambda state: self.护石判断())

        self.蓄力神圣信约 = QCheckBox("蓄力-神圣信约", self.main_frame2)
        self.蓄力神圣信约.setStyleSheet(复选框样式)
        self.蓄力神圣信约.setChecked(False)
        self.蓄力神圣信约.resize(120, 20)
        self.蓄力神圣信约.move(325, 380)

        self.职业存档.append(('蓄力神圣信约', self.蓄力神圣信约, 1))

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        if self.蓄力神圣信约.isChecked():
            属性.蓄力神圣信约 = 1

