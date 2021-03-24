from PublicReference.base import *

#2020年7月22日 数组

# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '太刀':
#             return round(self.CD / self.恢复 * 0.95, 1)

class 极诣·剑影技能0(主动技能):
    名称 = '鬼步'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据1 = [0, 636, 701, 766, 830, 895, 959, 1024, 1089, 1153, 1218, 1282, 1347, 1412, 1476, 1541, 1606, 1670, 1735, 1799, 1864, 1929, 1993, 2058, 2122, 2187, 2252, 2316, 2381, 2445, 2510, 2575, 2639, 2704, 2768, 2833, 2898, 2962, 3027, 3092, 3156, 3221, 3285, 3350, 3415, 3479, 3544, 3608, 3673, 3738, 3802, 3867, 3931, 3996, 4061, 4125, 4190, 4255, 4319, 4384, 4448, 4513, 4578, 4642, 4707, 4771, 4836, 4901, 4965, 5030, 5094]
    攻击次数1 = 3
    #倍率 = 1
    CD = 5.0
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率



class 极诣·剑影技能1(主动技能):
    名称 = '鬼连斩'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据1 = [0, 516, 568, 621, 673, 726, 778, 830, 883, 935, 988, 1040, 1092, 1145, 1197, 1250, 1302, 1354, 1407, 1459, 1512, 1564, 1616, 1669, 1721, 1774, 1826, 1878, 1931, 1983, 2036, 2088, 2140, 2193, 2245, 2298, 2350, 2402, 2455, 2507, 2560, 2612, 2664, 2717, 2769, 2822, 2874, 2926, 2979, 3031, 3084, 3136, 3188, 3241, 3293, 3346, 3398, 3450, 3503, 3555, 3608, 3660, 3712, 3765, 3817, 3870, 3922, 3974, 4027, 4079, 4132]
    #攻击次数1 = 1
    数据2 = [0, 619, 682, 745, 808, 871, 934, 997, 1059, 1122, 1185, 1248, 1311, 1374, 1437, 1500, 1563, 1625, 1688, 1751, 1814, 1877, 1940, 2003, 2066, 2128, 2191, 2254, 2317, 2380, 2443, 2506, 2569, 2631, 2694, 2757, 2820, 2883, 2946, 3009, 3072, 3135, 3197, 3260, 3323, 3386, 3449, 3512, 3575, 3638, 3700, 3763, 3826, 3889, 3952, 4015, 4078, 4141, 4203, 4266, 4329, 4392, 4455, 4518, 4581, 4644, 4707, 4769, 4832, 4895, 4958]
    #攻击次数2 = 1
    数据3 = [0, 929, 1024, 1118, 1212, 1307, 1401, 1495, 1589, 1684, 1778, 1872, 1967, 2061, 2155, 2250, 2344, 2438, 2533, 2627, 2721, 2816, 2910, 3004, 3099, 3193, 3287, 3382, 3476, 3570, 3664, 3759, 3853, 3947, 4042, 4136, 4230, 4325, 4419, 4513, 4608, 4702, 4796, 4891, 4985, 5079, 5174, 5268, 5362, 5457, 5551, 5645, 5740, 5834, 5928, 6022, 6117, 6211, 6305, 6400, 6494, 6588, 6683, 6777, 6871, 6966, 7060, 7154, 7249, 7343, 7437]
    #攻击次数3 = 1
    数据4 = [0, 790, 869, 949, 1030, 1110, 1190, 1269, 1350, 1430, 1510, 1591, 1671, 1750, 1831, 1911, 1991, 2071, 2151, 2231, 2311, 2392, 2472, 2552, 2632, 2712, 2792, 2872, 2953, 3032, 3112, 3193, 3273, 3353, 3434, 3513, 3593, 3673, 3754, 3834, 3913, 3994, 4074, 4154, 4235, 4314, 4394, 4474, 4555, 4635, 4715, 4795, 4875, 4955, 5036, 5116, 5195, 5275, 5356, 5436, 5516, 5597, 5676, 5756, 5837, 5917, 5997, 6076, 6157, 6237, 6317]
    攻击次数4 = 3
    CD = 5.0
    TP成长 = 0.1
    TP上限 = 5
    被动开关 = 0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级] + self.数据3[self.等级] + self.数据4[self.等级] * self.攻击次数4 * self.被动开关) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·剑影技能2(被动技能):
    名称 = '剑影太刀精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.0 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)

class 极诣·剑影技能3(主动技能):
    名称 = '幻鬼：一闪'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据1 = [0, 2131, 2348, 2564, 2780, 2997, 3213, 3429, 3645, 3862, 4078, 4294, 4511, 4727, 4943, 5159, 5376, 5592, 5808, 6024, 6241, 6457, 6673, 6890, 7106, 7322, 7538, 7755, 7971, 8187, 8404, 8620, 8836, 9052, 9269, 9485, 9701, 9918, 10134, 10350, 10566, 10783, 10999, 11215, 11431, 11648, 11864, 12080, 12297, 12513, 12729, 12945, 13162, 13378, 13594, 13811, 14027, 14243, 14459, 14676, 14892, 15108, 15325, 15541, 15757, 15973, 16190, 16406, 16622, 16839, 17055]
    CD = 6
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·剑影技能4(被动技能):
    名称 = '幻鬼之力'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.02 * self.等级, 5)

class 极诣·剑影技能5(主动技能):
    名称 = '鬼连牙'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据1 = [0, 3862, 4254, 4646, 5038, 5430, 5822, 6214, 6605, 6997, 7389, 7781, 8173, 8565, 8957, 9349, 9741, 10132, 10524, 10916, 11308, 11700, 12092, 12484, 12876, 13267, 13659, 14051, 14443, 14835, 15227, 15619, 16011, 16402, 16794, 17186, 17578, 17970, 18362, 18754, 19146, 19537, 19929, 20321, 20713, 21105, 21497, 21889, 22281, 22673, 23064, 23456, 23848, 24240, 24632, 25024, 25416, 25808, 26199, 26591, 26983, 27375, 27767, 28159, 28551, 28943, 29334, 29726, 30118, 30510, 30902]
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·剑影技能6(主动技能):
    名称 = '幻鬼：连斩'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据1 = [0, 527, 580, 634, 687, 741, 794, 848, 901, 955, 1008, 1062, 1115, 1169, 1222, 1276, 1329, 1383, 1436, 1490, 1543, 1597, 1650, 1704, 1757, 1811, 1864, 1918, 1971, 2025, 2078, 2132, 2185, 2239, 2292, 2346, 2399, 2453, 2506, 2560, 2613, 2667, 2720, 2774, 2827, 2881, 2934, 2988, 3041, 3095, 3148, 3202, 3255, 3309, 3362, 3416, 3469, 3523, 3576, 3630, 3683, 3737, 3790, 3844, 3897, 3951, 4004, 4058, 4111, 4165, 4218]
    数据2 = [0, 703, 774, 845, 917, 988, 1059, 1131, 1202, 1273, 1345, 1416, 1487, 1559, 1630, 1701, 1773, 1844, 1915, 1987, 2058, 2129, 2201, 2272, 2343, 2415, 2486, 2557, 2629, 2700, 2771, 2842, 2914, 2985, 3056, 3128, 3199, 3270, 3342, 3413, 3484, 3556, 3627, 3698, 3770, 3841, 3912, 3984, 4055, 4126, 4198, 4269, 4340, 4412, 4483, 4554, 4626, 4697, 4768, 4840, 4911, 4982, 5054, 5125, 5196, 5268, 5339, 5410, 5482, 5553, 5624]
    数据3 = [0, 878, 968, 1057, 1146, 1235, 1324, 1413, 1503, 1592, 1681, 1770, 1859, 1948, 2037, 2127, 2216, 2305, 2394, 2483, 2572, 2662, 2751, 2840, 2929, 3018, 3107, 3197, 3286, 3375, 3464, 3553, 3642, 3732, 3821, 3910, 3999, 4088, 4177, 4267, 4356, 4445, 4534, 4623, 4712, 4802, 4891, 4980, 5069, 5158, 5247, 5336, 5426, 5515, 5604, 5693, 5782, 5871, 5961, 6050, 6139, 6228, 6317, 6406, 6496, 6585, 6674, 6763, 6852, 6941, 7031]
    数据4 = [0, 1406, 1548, 1691, 1834, 1976, 2119, 2262, 2404, 2547, 2690, 2832, 2975, 3118, 3260, 3403, 3546, 3688, 3831, 3974, 4116, 4259, 4402, 4544, 4687, 4830, 4972, 5115, 5258, 5400, 5543, 5685, 5828, 5971, 6113, 6256, 6399, 6541, 6684, 6827, 6969, 7112, 7255, 7397, 7540, 7683, 7825, 7968, 8111, 8253, 8396, 8539, 8681, 8824, 8967, 9109, 9252, 9395, 9537, 9680, 9823, 9965, 10108, 10251, 10393, 10536, 10679, 10821, 10964, 11107, 11249]
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级] + self.数据3[self.等级] + self.数据4[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·剑影技能7(主动技能):
    名称 = '共鸣：离魂一闪'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据1 = [0, 1626, 1791, 1956, 2121, 2286, 2451, 2616, 2781, 2946, 3111, 3276, 3441, 3606, 3771, 3936, 4101, 4266, 4431, 4596, 4761, 4926, 5091, 5256, 5421, 5586, 5750, 5915, 6080, 6245, 6410, 6575, 6740, 6905, 7070, 7235, 7400, 7565, 7730, 7895, 8060, 8225, 8390, 8555, 8720, 8885, 9050, 9215, 9380, 9545, 9710, 9875, 10040, 10205, 10370, 10535, 10700, 10865, 11030, 11195, 11360, 11525, 11690, 11855, 12020, 12185, 12350, 12515, 12680, 12845, 13010]
    数据2 = [0, 3794, 4179, 4564, 4949, 5334, 5719, 6104, 6489, 6874, 7259, 7644, 8029, 8414, 8799, 9184, 9569, 9954, 10339, 10724, 11109, 11494, 11879, 12264, 12649, 13034, 13418, 13803, 14188, 14573, 14958, 15343, 15728, 16113, 16498, 16883, 17268, 17653, 18038, 18423, 18808, 19193, 19578, 19963, 20348, 20733, 21118, 21503, 21888, 22273, 22658, 23043, 23428, 23813, 24198, 24583, 24968, 25353, 25738, 26123, 26507, 26892, 27277, 27662, 28047, 28432, 28817, 29202, 29587, 29972, 30357]
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 极诣·剑影技能8(主动技能):
    名称 = '魂破斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [0, 6213, 6843, 7473, 8104, 8734, 9364, 9995, 10625, 11255, 11886, 12516, 13146, 13777, 14407, 15037, 15668, 16298, 16928, 17559, 18189, 18819, 19450, 20080, 20710, 21341, 21971, 22601, 23232, 23862, 24492, 25123, 25753, 26383, 27014, 27644, 28274, 28905, 29535, 30165, 30796, 31426, 32056, 32687, 33317, 33947, 34578, 35208, 35838, 36469, 37099, 37729, 38360, 38990, 39620, 40251, 40881, 41511, 42142, 42772, 43402, 44033, 44663, 45293, 45924, 46554, 47184, 47815, 48445, 49075, 49706]
    CD = 12
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.15
            self.CD *= 0.89
        elif x== 1:
            self.倍率 *= 1.24
            self.CD *= 0.89

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

    

class 极诣·剑影技能9(主动技能):
    名称 = '共鸣：鬼灵斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [0, 6957, 7663, 8369, 9075, 9781, 10487, 11193, 11898, 12604, 13310, 14016, 14722, 15428, 16134, 16840, 17545, 18251, 18957, 19663, 20369, 21075, 21781, 22487, 23192, 23898, 24604, 25310, 26016, 26722, 27428, 28133, 28839, 29545, 30251, 30957, 31663, 32369, 33075, 33780, 34486, 35192, 35898, 36604, 37310, 38016, 38722, 39427, 40133, 40839, 41545, 42251, 42957, 43663, 44369, 45074, 45780, 46486, 47192, 47898, 48604, 49310, 50015, 50721, 51427, 52133, 52839, 53545, 54251, 54957, 55662]
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·剑影技能10(主动技能):
    名称 = '幻鬼：回天'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据1 = [0, 3208, 3534, 3859, 4185, 4510, 4836, 5161, 5487, 5812, 6138, 6463, 6789, 7114, 7440, 7765, 8091, 8416, 8742, 9067, 9393, 9718, 10044, 10369, 10695, 11020, 11346, 11671, 11997, 12322, 12648, 12973, 13299, 13624, 13950, 14275, 14601, 14926, 15252, 15577, 15903, 16228, 16554, 16879, 17205, 17530, 17856, 18181, 18507, 18832, 19158, 19483, 19809, 20134, 20460, 20785, 21111, 21436, 21762, 22087, 22413, 22738, 23064, 23389, 23715, 24040, 24366, 24691, 25017, 25342, 25668]
    数据2 = [0, 4812, 5301, 5789, 6277, 6765, 7254, 7742, 8230, 8718, 9207, 9695, 10183, 10671, 11160, 11648, 12136, 12624, 13113, 13601, 14089, 14577, 15066, 15554, 16042, 16530, 17019, 17507, 17995, 18484, 18972, 19460, 19948, 20437, 20925, 21413, 21901, 22390, 22878, 23366, 23854, 24343, 24831, 25319, 25807, 26296, 26784, 27272, 27760, 28249, 28737, 29225, 29713, 30202, 30690, 31178, 31666, 32155, 32643, 33131, 33619, 34108, 34596, 35084, 35573, 36061, 36549, 37037, 37526, 38014, 38502]
    攻击次数2 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 1.40
        elif x== 1:
            self.攻击次数2 = 1.43#待测试

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 极诣·剑影技能11(主动技能):
    名称 = '冥灵断魂斩'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据1 = [0, 18941, 20863, 22784, 24706, 26628, 28549, 30471, 32393, 34314, 36236, 38157, 40079, 42001, 43922, 45844, 47766, 49687, 51609, 53530, 55452, 57374, 59295, 61217, 63139, 65060, 66982, 68903, 70825, 72747, 74668, 76590, 78512, 80433, 82355, 84276, 86198, 88120, 90041, 91963, 93884, 95806, 97728, 99649, 101571, 103493, 105414, 107336, 109257, 111179, 113101, 115022, 116944, 118866, 120787, 122709, 124630, 126552, 128474, 130395, 132317, 134239, 136160, 138082, 140003, 141925, 143847, 145768, 147690, 149612, 151533]
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1     
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.15
        elif x== 1:
            self.倍率 *= 1.23

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·剑影技能12(主动技能):
    名称 = '冥夜鬼天杀'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据1 = [0, 12680, 15621, 18561, 21502, 24442, 27382, 30323, 33263, 36204, 39144, 42085, 45025, 47966, 50906, 53846, 56787, 59727, 62668, 65608, 68549, 71489, 74430, 77370, 80310, 83251, 86191, 89132, 92072, 95013, 97953, 100894, 103834, 106774, 109715, 112655, 115596, 118536, 121477, 124417, 127358, 130298, 133239, 136179, 139119, 142060, 145000, 147941, 150881, 153822, 156762, 159703, 162643, 165583, 168524, 171464, 174405, 177345, 180286, 183226, 186167, 189107, 192047, 194988, 197928, 200869, 203809, 206750, 209690, 212631, 215571]
    攻击次数1 = 4
    CD = 145.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * self.倍率


class 极诣·剑影技能13(被动技能):
    名称 = '鬼夜'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.035 + 0.02 * self.等级, 5)

class 极诣·剑影技能14(主动技能):
    名称 = '幻鬼：奈落'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    数据1 = [0, 10573, 11645, 12718, 13791, 14863, 15936, 17009, 18081, 19154, 20227, 21299, 22372, 23444, 24517, 25590, 26662, 27735, 28808, 29880, 30953, 32026, 33098, 34171, 35244, 36316, 37389, 38461, 39534, 40607, 41679, 42752, 43825, 44897, 45970, 47043, 48115, 49188, 50261, 51333, 52406, 53478, 54551, 55624, 56696, 57769, 58842, 59914, 60987, 62060, 63132, 64205, 65278, 66350, 67423, 68495, 69568, 70641, 71713, 72786, 73859, 74931, 76004, 77077, 78149, 79222, 80295, 81367, 82440, 83513, 84585]
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.13
            self.CD *= 0.85
        elif x== 1:
            self.倍率 *= 1.22
            self.CD *= 0.85

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·剑影技能15(主动技能):
    名称 = '共鸣：聚渊'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [0, 2628, 2895, 3162, 3429, 3695, 3962, 4229, 4495, 4762, 5029, 5295, 5562, 5829, 6096, 6362, 6629, 6896, 7162, 7429, 7696, 7962, 8229, 8496, 8763, 9029, 9296, 9563, 9829, 10096, 10363, 10629, 10896, 11163, 11430, 11696, 11963, 12230, 12496, 12763, 13030, 13296, 13563, 13830, 14097, 14363, 14630, 14897, 15163, 15430, 15697, 15963, 16230, 16497, 16764, 17030, 17297, 17564, 17830, 18097, 18364, 18631, 18897, 19164, 19431, 19697, 19964, 20231, 20497, 20764, 21031]
    数据2 = [0, 10515, 11582, 12649, 13716, 14782, 15849, 16916, 17983, 19050, 20116, 21183, 22250, 23317, 24384, 25450, 26517, 27584, 28651, 29718, 30784, 31851, 32918, 33985, 35052, 36119, 37185, 38252, 39319, 40386, 41453, 42519, 43586, 44653, 45720, 46787, 47853, 48920, 49987, 51054, 52121, 53187, 54254, 55321, 56388, 57455, 58521, 59588, 60655, 61722, 62789, 63855, 64922, 65989, 67056, 68123, 69190, 70256, 71323, 72390, 73457, 74524, 75590, 76657, 77724, 78791, 79858, 80924, 81991, 83058, 84125]
    数据3 = [0, 13144, 14478, 15811, 17145, 18478, 19812, 21145, 22479, 23812, 25146, 26479, 27813, 29146, 30480, 31813, 33147, 34480, 35814, 37147, 38481, 39814, 41148, 42481, 43815, 45148, 46482, 47815, 49149, 50482, 51816, 53149, 54483, 55816, 57150, 58483, 59817, 61150, 62484, 63817, 65151, 66484, 67818, 69151, 70485, 71818, 73152, 74485, 75819, 77152, 78486, 79819, 81153, 82486, 83820, 85154, 86487, 87821, 89154, 90488, 91821, 93155, 94488, 95822, 97155, 98489, 99822, 101156, 102489, 103823, 105156]
    攻击次数3 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数3 = 1.23 * 1.20
        elif x== 1:
            self.攻击次数3 = 1.36 * 1.20


    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级] + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·剑影技能16(主动技能):
    名称 = '幻鬼：大回天'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据1 = [0, 12620, 13900, 15180, 16461, 17741, 19021, 20302, 21582, 22862, 24143, 25423, 26703, 27984, 29264, 30544, 31825, 33105, 34385, 35666, 36946, 38226, 39506, 40787, 42067, 43347, 44628, 45908, 47188, 48469, 49749, 51029, 52310, 53590, 54870, 56151, 57431, 58711, 59992, 61272, 62552, 63833, 65113, 66393, 67674, 68954, 70234, 71514, 72795, 74075, 75355, 76636, 77916, 79196, 80477, 81757, 83037, 84318, 85598, 86878, 88159, 89439, 90719, 92000, 93280, 94560, 95841, 97121, 98401, 99681, 100962]
    攻击次数1 = 3
    倍率 = 1
    CD = 40.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 = 1.36

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * self.倍率

class 极诣·剑影技能17(被动技能):
    名称 = '鬼咲'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

class 极诣·剑影技能18(主动技能):
    名称 = '裂魂乱舞'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    数据1 = [0, 2658, 2927, 3197, 3467, 3736, 4006, 4276, 4545, 4815, 5085, 5354, 5624, 5894, 6163, 6433, 6703, 6972, 7242, 7511, 7781, 8051, 8320, 8590, 8860, 9129, 9399, 9669, 9938, 10208, 10478, 10747, 11017, 11287, 11556, 11826, 12096, 12365, 12635, 12905, 13174, 13444, 13714, 13983, 14253, 14523, 14792, 15062, 15332, 15601, 15871, 16141, 16410, 16680, 16950, 17219, 17489, 17759, 18028, 18298, 18568, 18837, 19107, 19377, 19646, 19916, 20186, 20455, 20725, 20995, 21264]
    攻击次数1 = 1
    数据2 = [0, 7974, 8783, 9592, 10401, 11210, 12019, 12828, 13637, 14446, 15255, 16064, 16873, 17682, 18491, 19300, 20109, 20918, 21727, 22535, 23344, 24153, 24962, 25771, 26580, 27389, 28198, 29007, 29816, 30625, 31434, 32243, 33052, 33861, 34670, 35479, 36288, 37097, 37906, 38715, 39524, 40333, 41142, 41951, 42760, 43569, 44378, 45187, 45996, 46805, 47614, 48423, 49232, 50041, 50850, 51659, 52468, 53277, 54086, 54895, 55704, 56513, 57322, 58131, 58940, 59749, 60558, 61367, 62176, 62985, 63794]
    攻击次数2 = 1
    数据3 = [0, 10632, 11711, 12789, 13868, 14946, 16025, 17104, 18182, 19261, 20340, 21418, 22497, 23576, 24654, 25733, 26812, 27890, 28969, 30047, 31126, 32205, 33283, 34362, 35441, 36519, 37598, 38677, 39755, 40834, 41913, 42991, 44070, 45149, 46227, 47306, 48384, 49463, 50542, 51620, 52699, 53778, 54856, 55935, 57014, 58092, 59171, 60250, 61328, 62407, 63485, 64564, 65643, 66721, 67800, 68879, 69957, 71036, 72115, 73193, 74272, 75351, 76429, 77508, 78587, 79665, 80744, 81822, 82901, 83980, 85058]
    攻击次数3 = 1
    数据4 = [0, 6645, 7319, 7993, 8667, 9341, 10015, 10690, 11364, 12038, 12712, 13386, 14060, 14735, 15409, 16083, 16757, 17431, 18105, 18779, 19454, 20128, 20802, 21476, 22150, 22824, 23499, 24173, 24847, 25521, 26195, 26869, 27543, 28218, 28892, 29566, 30240, 30914, 31588, 32263, 32937, 33611, 34285, 34959, 35633, 36307, 36982, 37656, 38330, 39004, 39678, 40352, 41027, 41701, 42375, 43049, 43723, 44397, 45071, 45746, 46420, 47094, 47768, 48442, 49116, 49791, 50465, 51139, 51813, 52487, 53161]
    攻击次数4 = 2
    护石倍率1 = 1
    数据5 = [0, 18606, 20494, 22381, 24269, 26157, 28044, 29932, 31820, 33707, 35595, 37482, 39370, 41258, 43145, 45033, 46921, 48808, 50696, 52583, 54471, 56359, 58246, 60134, 62022, 63909, 65797, 67684, 69572, 71460, 73347, 75235, 77123, 79010, 80898, 82786, 84673, 86561, 88448, 90336, 92224, 94111, 95999, 97887, 99774, 101662, 103549, 105437, 107325, 109212, 111100, 112988, 114875, 116763, 118650, 120538, 122426, 124313, 126201, 128089, 129976, 131864, 133752, 135639, 137527, 139414, 141302, 143190, 145077, 146965, 148853]
    攻击次数5 = 1
    护石倍率2 = 1
    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 0
            self.攻击次数2 = 0
            self.攻击次数3 = 0
            self.护石倍率1 = 2.11
            self.护石倍率2 = 2.3

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3 + self.数据4[self.等级] * self.攻击次数4 * self.护石倍率1 + self.数据5[self.等级] * self.攻击次数5 * self.护石倍率2 ) * self.倍率

class 极诣·剑影技能19(主动技能):
    名称 = '鬼隐·夜奈落'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据1 = [0, 18411, 22680, 26949, 31218, 35488, 39757, 44026, 48296, 52565, 56834, 61103, 65373, 69642, 73911, 78180, 82450, 86719, 90988, 95257, 99527, 103796, 108065, 112334, 116604, 120873, 125142, 129411, 133681, 137950, 142219, 146488, 150758, 155027, 159296, 163566, 167835, 172104, 176373, 180643, 184912, 189181, 193450, 197720, 201989, 206258, 210527, 214797, 219066, 223335, 227604, 231874, 236143, 240412, 244681, 248951, 253220, 257489, 261758, 266028, 270297, 274566, 278836, 283105, 287374, 291643, 295913, 300182, 304451, 308720, 312990]
    数据2 = [0, 18411, 22680, 26949, 31218, 35488, 39757, 44026, 48296, 52565, 56834, 61103, 65373, 69642, 73911, 78180, 82450, 86719, 90988, 95257, 99527, 103796, 108065, 112334, 116604, 120873, 125142, 129411, 133681, 137950, 142219, 146488, 150758, 155027, 159296, 163566, 167835, 172104, 176373, 180643, 184912, 189181, 193450, 197720, 201989, 206258, 210527, 214797, 219066, 223335, 227604, 231874, 236143, 240412, 244681, 248951, 253220, 257489, 261758, 266028, 270297, 274566, 278836, 283105, 287374, 291643, 295913, 300182, 304451, 308720, 312990]
    数据3 = [0, 18411, 22680, 26949, 31218, 35488, 39757, 44026, 48296, 52565, 56834, 61103, 65373, 69642, 73911, 78180, 82450, 86719, 90988, 95257, 99527, 103796, 108065, 112334, 116604, 120873, 125142, 129411, 133681, 137950, 142219, 146488, 150758, 155027, 159296, 163566, 167835, 172104, 176373, 180643, 184912, 189181, 193450, 197720, 201989, 206258, 210527, 214797, 219066, 223335, 227604, 231874, 236143, 240412, 244681, 248951, 253220, 257489, 261758, 266028, 270297, 274566, 278836, 283105, 287374, 291643, 295913, 300182, 304451, 308720, 312990]
    数据4 = [0, 67507, 83161, 98815, 114469, 130123, 145777, 161431, 177085, 192739, 208393, 224047, 239701, 255355, 271009, 286662, 302316, 317970, 333624, 349278, 364932, 380586, 396240, 411894, 427548, 443202, 458856, 474510, 490164, 505818, 521472, 537126, 552780, 568434, 584088, 599742, 615395, 631049, 646703, 662357, 678011, 693665, 709319, 724973, 740627, 756281, 771935, 787589, 803243, 818897, 834551, 850205, 865859, 881513, 897167, 912821, 928475, 944128, 959782, 975436, 991090, 1006744, 1022398, 1038052, 1053706, 1069360, 1085014, 1100668, 1116322, 1131976, 1147630]
    CD = 180.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级] + self.数据3[self.等级] + self.数据4[self.等级]) * self.倍率

class 极诣·剑影技能20(被动技能):
    名称 = '睥睨万物'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 极诣·剑影技能21(主动技能):
    名称 = '无式·极影剑'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    数据1 = [0, 4853, 5345, 5838, 6330, 6822, 7315, 7807, 8299, 8792, 9284, 9777, 10269, 10761, 11254, 11746, 12238, 12731, 13223, 13716, 14208, 14700, 15193, 15685, 16177, 16670, 17162, 17655, 18147, 18639, 19132, 19624, 20116, 20609, 21101, 21593, 22086, 22578, 23071, 23563, 24055, 24548, 25040, 25532, 26025, 26517, 27010, 27502, 27994, 28487, 28979, 29471, 29964, 30456, 30949, 31441, 31933, 32426, 32918, 33410, 33903, 34395, 34887, 35380, 35872, 36365, 36857, 37349, 37842, 38334, 38826]
    攻击次数1 = 5
    数据2 = [0, 4853, 5345, 5838, 6330, 6822, 7315, 7807, 8299, 8792, 9284, 9777, 10269, 10761, 11254, 11746, 12238, 12731, 13223, 13716, 14208, 14700, 15193, 15685, 16177, 16670, 17162, 17655, 18147, 18639, 19132, 19624, 20116, 20609, 21101, 21593, 22086, 22578, 23071, 23563, 24055, 24548, 25040, 25532, 26025, 26517, 27010, 27502, 27994, 28487, 28979, 29471, 29964, 30456, 30949, 31441, 31933, 32426, 32918, 33410, 33903, 34395, 34887, 35380, 35872, 36365, 36857, 37349, 37842, 38334, 38826]
    攻击次数2 = 5
    数据3 = [0, 24266, 26728, 29190, 31652, 34114, 36576, 39037, 41499, 43961, 46423, 48885, 51347, 53809, 56270, 58732, 61194, 63656, 66118, 68580, 71042, 73503, 75965, 78427, 80889, 83351, 85813, 88275, 90736, 93198, 95660, 98122, 100584, 103046, 105508, 107969, 110431, 112893, 115355, 117817, 120279, 122740, 125202, 127664, 130126, 132588, 135050, 137512, 139973, 142435, 144897, 147359, 149821, 152283, 154745, 157206, 159668, 162130, 164592, 167054, 169516, 171978, 174439, 176901, 179363, 181825, 184287, 186749, 189211, 191672, 194134]
    攻击次数3 = 1
    数据4 = [0, 24266, 26728, 29190, 31652, 34114, 36576, 39037, 41499, 43961, 46423, 48885, 51347, 53809, 56270, 58732, 61194, 63656, 66118, 68580, 71042, 73503, 75965, 78427, 80889, 83351, 85813, 88275, 90736, 93198, 95660, 98122, 100584, 103046, 105508, 107969, 110431, 112893, 115355, 117817, 120279, 122740, 125202, 127664, 130126, 132588, 135050, 137512, 139973, 142435, 144897, 147359, 149821, 152283, 154745, 157206, 159668, 162130, 164592, 167054, 169516, 171978, 174439, 176901, 179363, 181825, 184287, 186749, 189211, 191672, 194134]
    攻击次数4 = 1
    数据5 = [0, 8166, 8994, 9823, 10651, 11479, 12308, 13136, 13965, 14793, 15622, 16450, 17279, 18107, 18936, 19764, 20592, 21421, 22249, 23078, 23906, 24735, 25563, 26392, 27220, 28048, 28877, 29705, 30534, 31362, 32191, 33019, 33848, 34676, 35505, 36333, 37161, 37990, 38818, 39647, 40475, 41304, 42132, 42961, 43789, 44617, 45446, 46274, 47103, 47931, 48760, 49588, 50417, 51245, 52074, 52902, 53730, 54559, 55387, 56216, 57044, 57873, 58701, 59530, 60358, 61186, 62015, 62843, 63672, 64500, 65329]
    攻击次数5 = 0
    数据6 = [0, 40830, 44973, 49115, 53257, 57399, 61542, 65684, 69826, 73968, 78111, 82253, 86395, 90537, 94680, 98822, 102964, 107106, 111249, 115391, 119533, 123675, 127818, 131960, 136102, 140244, 144387, 148529, 152671, 156813, 160956, 165098, 169240, 173382, 177525, 181667, 185809, 189951, 194094, 198236, 202378, 206520, 210663, 214805, 218947, 223089, 227232, 231374, 235516, 239658, 243801, 247943, 252085, 256227, 260370, 264512, 268654, 272796, 276939, 281081, 285223, 289365, 293508, 297650, 301792, 305934, 310077, 314219, 318361, 322503, 326646]
    攻击次数6 = 0
    CD = 60.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3 + self.数据4[self.等级] * self.攻击次数4 + self.数据5[self.等级] * self.攻击次数5 + self.数据6[self.等级] * self.攻击次数6) * self.倍率

class 极诣·剑影技能22(主动技能):
    名称 = '灭魂极影剑·止煞'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    数据1 = [0, 19897, 24512, 29126, 33740, 38354, 42968, 47582, 52196, 56810, 61424, 66038, 70652, 75266, 79880, 84494, 89108, 93722, 98336, 102950, 107564, 112178, 116792, 121406, 126020, 130634, 135248, 139862, 144476, 149090, 153704, 158318, 162932, 167546, 172160, 176774, 181388, 186002, 190616, 195231, 199845, 204459, 209073, 213687, 218301, 222915, 227529, 232143, 236757, 241371, 245985, 250599, 255213, 259827, 264441, 269055, 273669, 278283, 282897, 287511, 292125, 296739, 301353, 305967, 310581, 315195, 319809, 324423, 329037, 333651, 338265]
    数据2 = [0, 5685, 7003, 8321, 9640, 10958, 12276, 13594, 14913, 16231, 17549, 18868, 20186, 21504, 22822, 24141, 25459, 26777, 28096, 29414, 30732, 32051, 33369, 34687, 36005, 37324, 38642, 39960, 41279, 42597, 43915, 45233, 46552, 47870, 49188, 50507, 51825, 53143, 54461, 55780, 57098, 58416, 59735, 61053, 62371, 63690, 65008, 66326, 67644, 68963, 70281, 71599, 72918, 74236, 75554, 76872, 78191, 79509, 80827, 82146, 83464, 84782, 86101, 87419, 88737, 90055, 91374, 92692, 94010, 95329, 96647]
    攻击次数2 = 7
    数据3 = [0, 19897, 24512, 29126, 33740, 38354, 42968, 47582, 52196, 56810, 61424, 66038, 70652, 75266, 79880, 84494, 89108, 93722, 98336, 102950, 107564, 112178, 116792, 121406, 126020, 130634, 135248, 139862, 144476, 149090, 153704, 158318, 162932, 167546, 172160, 176774, 181388, 186002, 190616, 195231, 199845, 204459, 209073, 213687, 218301, 222915, 227529, 232143, 236757, 241371, 245985, 250599, 255213, 259827, 264441, 269055, 273669, 278283, 282897, 287511, 292125, 296739, 301353, 305967, 310581, 315195, 319809, 324423, 329037, 333651, 338265]
    数据4 = [0, 17055, 21010, 24965, 28920, 32874, 36829, 40784, 44739, 48694, 52649, 56604, 60559, 64513, 68468, 72423, 76378, 80333, 84288, 88243, 92198, 96153, 100107, 104062, 108017, 111972, 115927, 119882, 123837, 127792, 131746, 135701, 139656, 143611, 147566, 151521, 155476, 159431, 163386, 167340, 171295, 175250, 179205, 183160, 187115, 191070, 195025, 198979, 202934, 206889, 210844, 214799, 218754, 222709, 226664, 230618, 234573, 238528, 242483, 246438, 250393, 254348, 258303, 262258, 266212, 270167, 274122, 278077, 282032, 285987, 289942]
    攻击次数4 = 7
    数据5 = [0, 26530, 32682, 38834, 44986, 51138, 57290, 63442, 69594, 75746, 81898, 88051, 94203, 100355, 106507, 112659, 118811, 124963, 131115, 137267, 143419, 149571, 155723, 161875, 168027, 174179, 180331, 186483, 192635, 198787, 204939, 211091, 217243, 223395, 229547, 235699, 241851, 248003, 254155, 260308, 266460, 272612, 278764, 284916, 291068, 297220, 303372, 309524, 315676, 321828, 327980, 334132, 340284, 346436, 352588, 358740, 364892, 371044, 377196, 383348, 389500, 395652, 401804, 407956, 414108, 420260, 426413, 432565, 438717, 444869, 451021]
    数据6 = [0, 26530, 32682, 38834, 44986, 51138, 57290, 63442, 69594, 75746, 81898, 88051, 94203, 100355, 106507, 112659, 118811, 124963, 131115, 137267, 143419, 149571, 155723, 161875, 168027, 174179, 180331, 186483, 192635, 198787, 204939, 211091, 217243, 223395, 229547, 235699, 241851, 248003, 254155, 260308, 266460, 272612, 278764, 284916, 291068, 297220, 303372, 309524, 315676, 321828, 327980, 334132, 340284, 346436, 352588, 358740, 364892, 371044, 377196, 383348, 389500, 395652, 401804, 407956, 414108, 420260, 426413, 432565, 438717, 444869, 451021]
    数据7 = [0, 79591, 98048, 116504, 134960, 153416, 171872, 190328, 208784, 227240, 245696, 264153, 282609, 301065, 319521, 337977, 356433, 374889, 393345, 411801, 430258, 448714, 467170, 485626, 504082, 522538, 540994, 559450, 577906, 596363, 614819, 633275, 651731, 670187, 688643, 707099, 725555, 744011, 762467, 780924, 799380, 817836, 836292, 854748, 873204, 891660, 910116, 928572, 947029, 965485, 983941, 1002397, 1020853, 1039309, 1057765, 1076221, 1094677, 1113134, 1131590, 1150046, 1168502, 1186958, 1205414, 1223870, 1242326, 1260782, 1279239, 1297695, 1316151, 1334607, 1353063]
    CD = 290.0

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] + self.数据4[self.等级] * self.攻击次数4 + self.数据5[self.等级] + self.数据6[self.等级] + self.数据7[self.等级]) * self.倍率

class 极诣·剑影技能23(被动技能):
    名称 = '鬼连斩：极'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 1
    技能图标顺序 = 7
    关联技能 = ['鬼连斩']

    def 加成倍率(self, 武器类型):
        return 1.0
    


极诣·剑影技能列表 = []
i = 0
while i >= 0:
    try:
        exec('极诣·剑影技能列表.append(极诣·剑影技能'+str(i)+'())')
        i += 1
    except:
        i = -1

极诣·剑影技能序号 = dict()
for i in range(len(极诣·剑影技能列表)):
    极诣·剑影技能序号[极诣·剑影技能列表[i].名称] = i

极诣·剑影一觉序号 = 0
极诣·剑影二觉序号 = 0
极诣·剑影三觉序号 = 0
for i in 极诣·剑影技能列表:
    if i.所在等级 == 50:
        极诣·剑影一觉序号 = 极诣·剑影技能序号[i.名称]
    if i.所在等级 == 85:
        极诣·剑影二觉序号 = 极诣·剑影技能序号[i.名称]
    if i.所在等级 == 100:
        极诣·剑影三觉序号 = 极诣·剑影技能序号[i.名称]

极诣·剑影护石选项 = ['无']
for i in 极诣·剑影技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        极诣·剑影护石选项.append(i.名称)

极诣·剑影符文选项 = ['无']
for i in 极诣·剑影技能列表:
    if i.所在等级 >= 15 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        极诣·剑影符文选项.append(i.名称)

class 极诣·剑影角色属性(角色属性):

    实际名称 = '极诣·剑影'
    角色 = '鬼剑士(男)'
    职业 = '剑影'

    武器选项 = ['太刀']
    
    类型选择 = ['物理百分比']
    
    类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 2.00
   
    无式极影剑形态 = 0
    符文鬼连斩倍率 = 1
    鬼连斩极显示开关 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(极诣·剑影技能列表)
        self.技能序号= deepcopy(极诣·剑影技能序号)

    def 武器基础(self):
        temp = 装备列表[装备序号[self.装备栏[11]]]

        self.力量 += temp.力量
        self.智力 += temp.智力
        self.物理攻击力 += temp.魔法攻击力
        self.魔法攻击力 += temp.魔法攻击力
        self.独立攻击力 += temp.独立攻击力

        if temp.所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(temp.等级,temp.品质,self.强化等级[11],self.武器类型,'魔法')
            self.魔法攻击力 += 武器计算(temp.等级,temp.品质,self.强化等级[11],self.武器类型,'魔法')
            self.独立攻击力 += 锻造计算(temp.等级,temp.品质,self.武器锻造等级)

    def 技能等级加成(self, 加成类型, minLv, maxLv, lv, 可变=0):
        lv = int(lv)
        if self.装备描述 == 1:
            if 加成类型 == "所有":
                if minLv == maxLv:
                    return "Lv{} 技能等级+{}<br>".format(minLv, lv)
                else:
                    return "Lv{}-{} 技能等级+{}<br>".format(minLv, maxLv, lv)
            else:
                if minLv == maxLv:
                    return "Lv{} 主动技能等级+{}<br>".format(minLv, lv)
                else:
                    return "Lv{}-{} 主动技能等级+{}<br>".format(minLv, maxLv, lv)
        else:
            if self.远古记忆 > 0:
                if minLv <= 15 and maxLv >= 15:
                    self.远古记忆 = min(20, self.远古记忆 + lv)

            if self.刀魂之卡赞 > 0:
                if minLv <= 5 and maxLv >= 5:
                    self.刀魂之卡赞 = min(20, self.刀魂之卡赞 + lv)

            for i in self.技能栏:
                if i.所在等级 >= minLv and i.所在等级 <= maxLv:
                    if 加成类型 == '所有':
                        #鬼连斩极的等级加成非常特别，装备同时加成鬼连斩和鬼连斩极时，两者等级都+1,，只加成鬼连斩时，两者等级+1，只加成鬼连斩极时，只有鬼连斩等级+1
                        if minLv > 15 and maxLv >= 30:
                            i.等级加成(lv)
                        elif i.名称 != '鬼连斩：极':
                            i.等级加成(lv)
                    else:
                        if i.是否主动 == 1:
                            i.等级加成(lv)
            if 可变 > 0:
                self.变换词条[可变 - 1] = [6, 2, 14 + (2 if 可变 > 1 else 4), 14 + (8 if 可变 > 1 else 16)]
        return ''

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['冥夜鬼天杀']].被动倍率 *= 1.1

        if self.无式极影剑形态 == 0:
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数1 = 5
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数2 = 5
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数3 = 1
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数4 = 1
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数5 = 0
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数6 = 0
        if self.无式极影剑形态 == 1:
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数1 = 0
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数2 = 0
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数3 = 0
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数4 = 0
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数5 = 5
            self.技能栏[self.技能序号['无式·极影剑']].攻击次数6 = 1

    def 数据计算(self, x = 0, y = -1):
        self.预处理()
        #初步计算
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算(y)
        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        if self.技能栏[self.技能序号['鬼连斩：极']].等级 != 0:
           a = self.技能栏[self.技能序号['鬼连斩：极']]
           b = self.技能栏[self.技能序号['鬼连斩']]
           技能释放次数[self.技能序号['鬼连斩：极']] = 技能释放次数[self.技能序号['鬼连斩']]
           a.等级 = a.等级 + b.等级 - 1
           等效百分比a = (b.数据4[a.等级] * b.攻击次数4) * (1 + b.TP成长 * b.TP等级) * b.倍率/ self.符文鬼连斩倍率
           技能总伤害[self.技能序号['鬼连斩：极']] = (等效百分比a * self.伤害指数 * b.被动倍率) * 技能释放次数[self.技能序号['鬼连斩：极']] * \
                                      (1 + self.白兔子技能 * 0.20 + self.年宠技能 * 0.10 * self.宠物次数[self.技能序号['鬼连斩']] / 技能释放次数[self.技能序号['鬼连斩']]+ self.斗神之吼秘药 * 0.12)
           if self.装备检查('奔流不息之狂风'):
               技能总伤害[self.技能序号['鬼连斩：极']] *= 0.7
           if self.鬼连斩极显示开关 == 0:
               技能总伤害[self.技能序号['鬼连斩']] += 技能总伤害[self.技能序号['鬼连斩：极']]
               技能总伤害[self.技能序号['鬼连斩：极']] = 0
               b.被动开关 = 1

               #返回结果
        return self.数据返回(x, 技能释放次数, 技能总伤害)


class 极诣·剑影(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 极诣·剑影角色属性()
        self.角色属性A = 极诣·剑影角色属性()
        self.角色属性B = 极诣·剑影角色属性()
        self.一觉序号 = 极诣·剑影一觉序号
        self.二觉序号 = 极诣·剑影二觉序号
        self.三觉序号 = 极诣·剑影三觉序号
        self.护石选项 = deepcopy(极诣·剑影护石选项)
        self.符文选项 = deepcopy(极诣·剑影符文选项)

    def 界面(self):
        super().界面()
        self.无式极影剑形态选择=MyQComboBox(self.main_frame2)
        self.无式极影剑形态选择.addItem('无式极影剑(共鸣)')
        self.无式极影剑形态选择.addItem('无式极影剑(幻鬼)')
        self.无式极影剑形态选择.setCurrentIndex(0)
        self.无式极影剑形态选择.resize(130,20)
        self.无式极影剑形态选择.move(325,330)

        self.鬼连斩极显示开关=QCheckBox('鬼连斩极伤害独立显示',self.main_frame2)
        self.鬼连斩极显示开关.resize(140,20)
        self.鬼连斩极显示开关.move(325,360)
        self.鬼连斩极显示开关.setStyleSheet(复选框样式)
        self.鬼连斩极显示开关.setChecked(False)

    def 载入配置(self, path='set'):
        super().载入配置(path)
        try:
           setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'r',encoding='utf-8').readlines()
           self.无式极影剑形态选择.setCurrentIndex(int(setfile[0].replace('\n', '')))
           self.鬼连斩极显示开关.setChecked(True if int(setfile[1].replace('\n', '')) == 1 else False)
        except:
            pass

    def 保存配置(self, path='set'):
        if self.禁用存档.isChecked():
            return
        super().保存配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'w', encoding='utf-8')
            setfile.write(str(self.无式极影剑形态选择.currentIndex())+'\n')
            setfile.write('1\n' if self.鬼连斩极显示开关.isChecked() else '0\n')
        except:
            pass

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性,x)

        属性.无式极影剑形态 = self.无式极影剑形态选择.currentIndex()
        if self.鬼连斩极显示开关.isChecked():
            属性.鬼连斩极显示开关 = 1

    def 加载护石(self, 属性):
        for k in range(3):
            if self.护石栏[k].currentText() != '无':
                try:
                    属性.技能栏[self.角色属性A.技能序号[self.护石栏[k].currentText()]].装备护石()
                except:
                    属性.技能栏[self.角色属性A.技能序号[self.护石栏[k].currentText()]].装备护石(self.护石类型选项[k].currentIndex())

        属性.护石第一栏 = self.护石栏[0].currentText()
        属性.护石第二栏 = self.护石栏[1].currentText()
        属性.护石第三栏 = self.护石栏[2].currentText()

        属性.符文鬼连斩倍率 = 1
        for i in range(0, 9):
            if self.符文[i].currentText() != '无' and self.符文效果[i].currentText() != '无':
                for j in self.符文效果[i].currentText().split(','):
                    if '攻击' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].倍率 *= 1 + int(
                            j.replace('攻击', '').replace('%', '')) / 100
                        if self.符文[i].currentText() == '鬼连斩':
                            属性.符文鬼连斩倍率 *= 1 + int(j.replace('攻击', '').replace('%', '')) / 100
                    if 'CD' in j:
                        属性.技能栏[self.角色属性A.技能序号[self.符文[i].currentText()]].CD *= 1 + int(
                            j.replace('CD', '').replace('%', '')) / 100

