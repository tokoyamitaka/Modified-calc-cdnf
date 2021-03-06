from PublicReference.carry.base import *

class 主动技能(主动技能):
    收招倍率 = 0
    收招倍率2 = 0
    收招倍率3 = 0


class 技能0(主动技能):
    名称 = '终结追击'
    所在等级 = 15
    等级上限 = 30
    基础等级 = 20
    是否有伤害 = 0

    def 终结追击倍率(self):
        if self.等级 == 0:
            return 0.0
        else:
            return round(0.79 + 0.02 * self.等级, 5)


class 技能1(被动技能):
    名称 = '武器精通'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    data1 = [0, 36, 53, 70, 87, 104, 121, 138, 155, 172, 189, 206, 223, 240, 257, 274, 291, 308, 325, 342, 359, 387, 415, 443, 471, 499, 527, 555, 583, 611, 639, 667, 695, 723, 751, 779, 807, 835,
             863, 891, 919, 947, 975, 1003, 1031, 1059, 1087, 1115, 1143, 1171, 1199, 1227, 1255, 1283, 1311, 1339, 1367, 1395, 1423, 1451, 1479, 1507, 1535, 1563, 1591, 1619, 1647, 1675, 1703, 1731, 1759]
    data2 = [0, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100, 103, 106, 109, 112, 115, 118,
             121, 124, 127, 130, 133, 136, 139, 142, 145, 148, 151, 154, 157, 160, 163, 166, 169, 172, 175, 178, 181, 184, 187, 190, 193, 196, 199, 202, 205, 208, 211, 214, 217]
    data3 = [0, 22, 23, 25, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 59, 60, 61, 62,
             63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 83, 84, 85, 86, 88, 89, 90, 91, 92, 94, 95, 96, 97, 98, 100, 101, 102, 103, 104, 106]

    def 加成倍率(self, 武器类型):
        return round(1 + self.data1[self.等级] / 1000, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    冷却关联技能 = ['所有']

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '匕首':
            return 1.0
        else:
            return round(1 - self.data2[self.等级] / 1000, 5)

    def 终结追击倍率(self):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + self.data3[self.等级] / 100, 5)


class 技能2(被动技能):
    名称 = '月弧'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.095 + 0.02 * self.等级, 5)


class 技能3(被动技能):
    名称 = '极限追击'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)

    def 物理攻击力倍率进图(self, 武器类型):
        return self.加成倍率(武器类型)


class 技能4(主动技能):
    名称 = '双刃穿刺'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    data = [0, 536, 589, 644, 698, 753, 806, 861, 916, 970, 1024, 1078, 1133, 1188, 1241, 1296, 1350, 1405, 1458, 1513, 1568, 1621, 1676, 1730, 1786, 1838, 1893, 1949, 2003, 2056, 2111, 2166, 2221, 2274, 2329, 2383, 2438, 2491, 2546, 2601, 2655, 2709, 2763, 2818, 2872, 2926, 2981, 3035, 3090, 3143, 3198, 3252, 3306, 3361, 3415, 3470, 3523, 3578, 3632, 3688, 3740, 3796, 3851, 3905, 3959, 4014, 4068, 4123, 4176, 4231, 4285]
    # hit = 1
    data1 = [0, 803, 884, 966, 1047, 1128, 1210, 1291, 1375, 1456, 1537, 1619, 1700, 1781, 1863, 1944, 2025, 2108, 2189, 2271, 2352, 2433, 2515, 2596, 2677, 2759, 2841, 2922, 3004, 3085, 3166, 3249, 3330, 3412, 3493, 3575, 3657, 3738, 3819, 3901, 3982, 4064, 4145, 4226, 4309, 4390, 4471, 4553, 4634, 4715, 4797, 4878, 4959, 5043, 5124, 5206, 5287, 5368, 5450, 5531, 5612, 5694, 5776, 5858, 5939, 6020, 6102, 6183, 6264, 6346, 6427]
    # hit = 1
    data2 = [0, 1071, 1179, 1289, 1397, 1506, 1614, 1723, 1831, 1941, 2049, 2158, 2266, 2375, 2483, 2594, 2700, 2811, 2919, 3028, 3136, 3245, 3354, 3463, 3571, 3680, 3788, 3897, 4005, 4115, 4223, 4333, 4441, 4550, 4658, 4768, 4876, 4985, 5093, 5202, 5310, 5420, 5528, 5637, 5745, 5855, 5962, 6073, 6181, 6290, 6398, 6507, 6615, 6724, 6833, 6942, 7050, 7159, 7267, 7376, 7484, 7595, 7703, 7812, 7920, 8029, 8137, 8247, 8355, 8464, 8572]
    # hit = 1
    data3 = [0, 481, 531, 580, 629, 677, 726, 775, 824, 873, 921, 970, 1019, 1068, 1117, 1165, 1215, 1264, 1313, 1362, 1411, 1459, 1508, 1557, 1606, 1655, 1703, 1753, 1802, 1851, 1901, 1950, 1999, 2047, 2096, 2145, 2194, 2243, 2291, 2340, 2389, 2438, 2487, 2535, 2585, 2634, 2683, 2732, 2781, 2829, 2878, 2927, 2976, 3025, 3073, 3122, 3171, 3220, 3271, 3320, 3369, 3417, 3466, 3515, 3564, 3613, 3661, 3710, 3759, 3808, 3857]
    # hit = 1
    收招倍率 = 1
    TP成长 = 0.1
    TP上限 = 5
    CD = 7.0
    演出时间 = 0.2

    def 等效百分比(self, 武器类型):
        return ((self.data[self.等级]+self.data1[self.等级]+self.data2[self.等级]) * self.攻击次数 + self.data3[self.等级] * self.收招倍率) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.187


class 技能5(主动技能):
    名称 = '绝杀斩'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    data = [0, 2202, 2425, 2648, 2872, 3096, 3320, 3543, 3765, 3989, 4213, 4437, 4660, 4884, 5107, 5330, 5554, 5778, 6001, 6224, 6448, 6671, 6895, 7118, 7341, 7565, 7789, 8012, 8236, 8458, 8682, 8906, 9130, 9354, 9575, 9799, 10023, 10247, 10471, 10695, 10916, 11140, 11364, 11588, 11812, 12033, 12257, 12481, 12705, 12929, 13153, 13374, 13598, 13822, 14046, 14270, 14492, 14715, 14939, 15163, 15387, 15611, 15833, 16056, 16280, 16504, 16728, 16950, 17174, 17397, 17621]
    data1 = [0, 67, 72, 78, 86, 92, 99, 106, 113, 118, 126, 132, 140, 146, 153, 160, 165, 172, 179, 186, 192, 200, 205, 214, 219, 227, 233, 240, 247, 254, 259, 266, 273, 279, 287, 293, 301, 307, 313, 320, 327, 333, 341, 347, 352, 360, 366, 374, 380, 387, 394, 401, 406, 414, 420, 428, 434, 442, 448, 453, 461, 467, 474, 481, 488, 494, 502, 507, 515, 521, 528]
    data2 = [0, 125, 137, 148, 162, 174, 188, 200, 214, 225, 239, 250, 263, 277, 288, 302, 313, 327, 340, 351, 365, 377, 390, 403, 416, 428, 440, 453, 465, 479, 491, 504, 517, 528, 542, 554, 567, 580, 594, 605, 619, 630, 643, 657, 668, 682, 693, 707, 720, 731, 745, 757, 770, 782, 796, 808, 820, 833, 845, 859, 871, 884, 897, 908, 922, 934, 947, 960, 974, 985, 999]
    收招倍率 = 1
    TP成长 = 0.1
    TP上限 = 5
    CD = 7.0
    演出时间 = 0.2

    def 等效百分比(self, 武器类型):
        return (self.data[self.等级] * self.攻击次数 + (self.data1[self.等级] + self.data2[self.等级] * 3) * self.收招倍率) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.187


class 技能6(主动技能):
    名称 = '旋舞斩'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    data = [0, 2086, 2299, 2510, 2722, 2933, 3145, 3357, 3568, 3781, 3992, 4204, 4416, 4627, 4839, 5050, 5262, 5475, 5686, 5898, 6109, 6321, 6533, 6744, 6957, 7168, 7380, 7592, 7803, 8015, 8226, 8438, 8651, 8862, 9074, 9285, 9497, 9709, 9920, 10133, 10344, 10556, 10768, 10979, 11191, 11405, 11616, 11828, 12040, 12251, 12463, 12674, 12887, 13099, 13310, 13522, 13733, 13945, 14157, 14368, 14581, 14792, 15004, 15216, 15427, 15639, 15850, 16063, 16275, 16486, 16698]
    data1 = [0, 418, 459, 501, 544, 586, 629, 671, 713, 756, 798, 841, 883, 926, 967, 1009, 1052, 1094, 1137, 1179, 1222, 1264, 1306, 1349, 1391, 1434, 1476, 1517, 1560, 1602, 1645, 1687, 1730, 1772, 1815, 1857, 1899, 1942, 1984, 2026, 2068, 2110, 2153, 2195, 2238, 2280, 2323, 2365, 2408, 2450, 2492, 2535, 2576, 2619, 2661, 2703, 2746, 2788, 2831, 2873, 2916, 2958, 3001, 3043, 3084, 3127, 3169, 3212, 3254, 3296, 3339]
    收招倍率2 = 1
    TP成长 = 0.1
    TP上限 = 5
    CD = 7.0
    演出时间 = 0.1

    def 等效百分比(self, 武器类型):
        return (self.data[self.等级] * self.攻击次数 + self.data1[self.等级] * self.收招倍率2) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.187


class 技能7(主动技能):
    名称 = '旋刃'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data = [0, 239, 265, 289, 313, 338, 361, 387, 411, 435, 461, 485, 509, 533, 557, 583, 607, 630, 655, 679, 705, 729, 753, 777, 802, 827, 851, 875, 899, 924, 949, 973, 997, 1023, 1046, 1070, 1095, 1120, 1145, 1169, 1192, 1217, 1242, 1267, 1291, 1314, 1339, 1364, 1389, 1413, 1437, 1462, 1486, 1510, 1535, 1560, 1584, 1608, 1632, 1657, 1682, 1707, 1730, 1754, 1779, 1804, 1829, 1853, 1876, 1902, 1926]
    data1 = [0, 331, 365, 398, 432, 464, 498, 533, 567, 600, 633, 666, 700, 735, 769, 802, 835, 868, 902, 936, 971, 1003, 1037, 1070, 1104, 1138, 1170, 1205, 1239, 1272, 1306, 1339, 1372, 1407, 1441, 1474, 1508, 1541, 1574, 1608, 1643, 1676, 1709, 1743, 1776, 1810, 1844, 1878, 1911, 1945, 1978, 2012, 2045, 2079, 2113, 2147, 2180, 2214, 2247, 2280, 2315, 2349, 2382, 2415, 2449, 2482, 2517, 2551, 2584, 2617, 2651]
    data2 = [0, 452, 497, 543, 589, 635, 679, 727, 773, 817, 864, 909, 956, 1001, 1047, 1093, 1139, 1185, 1231, 1277, 1321, 1368, 1413, 1459, 1506, 1551, 1598, 1643, 1689, 1735, 1781, 1826, 1873, 1919, 1963, 2010, 2055, 2101, 2147, 2193, 2240, 2285, 2331, 2377, 2423, 2467, 2514, 2559, 2605, 2652, 2697, 2743, 2789, 2835, 2880, 2927, 2972, 3019, 3065, 3109, 3156, 3201, 3247, 3293, 3339, 3385, 3431, 3477, 3522, 3569, 3613]
    data3 = [0, 204, 225, 246, 267, 288, 309, 330, 349, 370, 391, 412, 433, 454, 475, 496, 517, 536, 557, 578, 599, 620, 641, 662, 683, 704, 724, 744, 765, 786, 807, 828, 849, 870, 890, 911, 932, 953, 974, 995, 1015, 1036, 1057, 1077, 1098, 1119, 1140, 1161, 1181, 1202, 1223, 1243, 1264, 1285, 1306, 1327, 1348, 1368, 1389, 1409, 1430, 1451, 1472, 1493, 1514, 1534, 1555, 1575, 1596, 1617, 1638]
    收招倍率 = 1
    TP成长 = 0.1
    TP上限 = 5
    CD = 8.0
    演出时间 = 0.2

    def 等效百分比(self, 武器类型):
        return ((self.data[self.等级] * 3 + self.data1[self.等级] * 3 + self.data2[self.等级] * 3) * self.攻击次数 + self.data3[self.等级] * 3 * self.收招倍率) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.164


class 技能8(主动技能):
    名称 = '剑刃风暴'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    data = [0, 448, 495, 539, 585, 630, 676, 722, 768, 813, 858, 903, 950, 995, 1040, 1086, 1131, 1176, 1223, 1268, 1314, 1359, 1404, 1451, 1496, 1541, 1587, 1632, 1679, 1724, 1769, 1815, 1860, 1905, 1952, 1997, 2042, 2088, 2133, 2179, 2225, 2270, 2316, 2360, 2407, 2453, 2498, 2543, 2589, 2633, 2680, 2726, 2771, 2816, 2862, 2907, 2954, 2999, 3044, 3090, 3136, 3180, 3227, 3272, 3317, 3363, 3409, 3455, 3500, 3545, 3591]
    data1 = [0, 898, 987, 1079, 1171, 1260, 1352, 1444, 1536, 1625, 1717, 1809, 1898, 1990, 2082, 2172, 2263, 2354, 2447, 2536, 2627, 2720, 2810, 2900, 2993, 3083, 3174, 3266, 3357, 3447, 3540, 3630, 3720, 3813, 3903, 3993, 4086, 4177, 4268, 4359, 4450, 4542, 4632, 4723, 4814, 4905, 4996, 5087, 5180, 5269, 5360, 5453, 5542, 5633, 5726, 5815, 5906, 5999, 6090, 6179, 6272, 6363, 6452, 6545, 6636, 6726, 6818, 6909, 7001, 7092, 7182]
    旋转次数 = 8
    收招倍率 = 1
    CD = 12.0
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 0.5

    def 等效百分比(self, 武器类型):
        return (self.data[self.等级] * self.旋转次数 * self.攻击次数 + self.data1[self.等级] * self.收招倍率) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.163


class 技能9(主动技能):
    名称 = '螺旋穿刺'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data = [0, 657, 725, 792, 859, 925, 994, 1059, 1126, 1192, 1261, 1327, 1394, 1459, 1527, 1594, 1661, 1727, 1795, 1863, 1928, 1994, 2062, 2130, 2196, 2264, 2329, 2396, 2463, 2531, 2597, 2664, 2730, 2798, 2864, 2931, 3000, 3066, 3133, 3198, 3264, 3333, 3400, 3466, 3534, 3600, 3667, 3733, 3801, 3868, 3935, 4003, 4068, 4134, 4202, 4270, 4336, 4403, 4469, 4535, 4603, 4670, 4737, 4805, 4870, 4937, 5003, 5072, 5138, 5205, 5273]
    data1 = [0, 2306, 2541, 2774, 3007, 3242, 3475, 3709, 3944, 4178, 4412, 4645, 4880, 5114, 5348, 5583, 5817, 6051, 6285, 6519, 6752, 6987, 7220, 7453, 7687, 7922, 8156, 8390, 8625, 8859, 9091, 9327, 9560, 9794, 10028, 10263, 10497, 10731, 10965, 11199, 11433, 11668, 11899, 12133, 12367, 12602, 12836, 13070, 13305, 13539, 13772, 14007, 14241, 14475, 14710, 14944, 15178, 15410, 15645, 15879, 16113, 16348, 16580, 16814, 17049, 17283, 17517, 17752, 17986, 18218, 18452]
    data2 = [0, 1384, 1523, 1665, 1804, 1945, 2085, 2226, 2366, 2507, 2647, 2787, 2928, 3067, 3208, 3350, 3489, 3631, 3770, 3911, 4051, 4192, 4332, 4473, 4613, 4753, 4894, 5034, 5174, 5315, 5455, 5597, 5736, 5877, 6016, 6158, 6297, 6439, 6579, 6719, 6860, 7000, 7140, 7280, 7420, 7563, 7701, 7842, 7981, 8123, 8262, 8403, 8545, 8684, 8824, 8965, 9105, 9246, 9386, 9527, 9667, 9808, 9947, 10089, 10228, 10369, 10511, 10650, 10792, 10931, 11072]
    收招倍率 = 1
    旋转次数 = 1
    旋转倍率 = 1
    CD = 15.0
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 0.5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        # if x == 0:
        #     self.旋转倍率 = 2.25
        # elif x == 1:
        #     self.旋转倍率 = 2.91
        if x == 0:
            self.旋转倍率 = (1-0.5)*1.25*3
        elif x == 1:
            self.旋转倍率 = (1-0.5)*1.47*3

    def 等效百分比(self, 武器类型):
        return ((self.data[self.等级] * self.旋转次数 * self.旋转倍率 + self.data[self.等级]+ self.data1[self.等级]) * self.攻击次数 + self.data2[self.等级] * self.收招倍率) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.167


class 技能10(主动技能):
    名称 = '雷光刃影'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data = [0, 4565, 5030, 5493, 5955, 6418, 6883, 7346, 7809, 8272, 8736, 9199, 9662, 10125, 10589, 11052, 11515, 11978, 12442, 12905, 13368, 13831, 14295, 14758, 15221, 15684, 16148, 16611, 17074, 17537, 18001, 18464, 18927, 19390, 19855, 20318,
          20780, 21243, 21708, 22171, 22634, 23097, 23560, 24024, 24487, 24950, 25413, 25877, 26340, 26803, 27266, 27730, 28193, 28656, 29119, 29583, 30046, 30509, 30972, 31436, 31899, 32362, 32825, 33289, 33752, 34215, 34678, 35143, 35605, 36068, 36531]
    data1 = [0, 3044, 3353, 3661, 3970, 4279, 4588, 4897, 5206, 5514, 5823, 6132, 6442, 6750, 7059, 7367, 7676, 7985, 8295, 8603, 8912, 9221, 9529, 9838, 10148, 10456, 10765, 11074, 11382, 11691, 12001, 12310, 12618, 12927, 13236, 13544, 13854,
           14163, 14471, 14780, 15089, 15397, 15706, 16016, 16324, 16633, 16942, 17250, 17559, 17869, 18178, 18486, 18795, 19104, 19412, 19722, 20031, 20339, 20648, 20957, 21265, 21575, 21884, 22193, 22501, 22810, 23118, 23428, 23737, 24046, 24354]
    data2 = [0, 1521, 1676, 1830, 1984, 2139, 2294, 2449, 2603, 2757, 2912, 3066, 3220, 3374, 3529, 3683, 3837, 3992, 4147, 4302, 4456, 4610, 4765, 4919, 5073, 5228, 5382, 5536, 5691, 5845, 6000, 6155, 6309, 6463, 6618, 6772, 6926,
           7081, 7235, 7389, 7544, 7698, 7852, 8008, 8162, 8317, 8471, 8625, 8780, 8934, 9088, 9242, 9397, 9551, 9705, 9861, 10015, 10170, 10324, 10478, 10633, 10787, 10941, 11096, 11250, 11404, 11559, 11714, 11868, 12023, 12177]
    收招倍率 = 1
    CD = 15.0
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 0.3

    def 等效百分比(self, 武器类型):
        return ((self.data[self.等级] + self.data1[self.等级]) * self.攻击次数 + self.data2[self.等级] * self.收招倍率) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.058


class 技能11(主动技能):
    名称 = '疾风乱舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    data = [0, 687, 756, 826, 896, 965, 1035, 1106, 1175, 1244, 1315, 1384, 1453, 1524, 1593, 1663, 1733, 1803, 1872, 1941, 2011, 2081, 2150, 2221, 2291, 2360, 2430, 2499, 2569, 2639, 2708, 2778, 2849, 2918, 2987, 3058, 3127, 3196, 3266, 3337, 3406, 3476, 3546, 3615, 3684, 3754, 3825, 3894, 3964, 4033, 4103, 4173, 4242, 4313, 4383, 4452, 4521, 4592, 4661, 4730, 4800, 4871, 4940, 5010, 5080, 5149, 5219, 5288, 5359, 5429, 5498]
    data1 = [0, 684, 753, 823, 893, 962, 1031, 1100, 1170, 1239, 1308, 1378, 1447, 1516, 1586, 1655, 1725, 1794, 1864, 1933, 2002, 2073, 2142, 2211, 2281, 2350, 2420, 2490, 2559, 2628, 2697, 2767, 2836, 2905, 2975, 3044, 3113, 3183, 3253, 3322, 3392, 3461, 3530, 3599, 3669, 3738, 3807, 3877, 3946, 4015, 4085, 4156, 4225, 4295, 4364, 4433, 4502, 4572, 4641, 4710, 4780, 4850, 4919, 4989, 5058, 5127, 5196, 5266, 5335, 5404, 5474]
    data2 = [0, 1230, 1355, 1479, 1603, 1728, 1853, 1978, 2102, 2228, 2353, 2477, 2602, 2727, 2852, 2976, 3102, 3227, 3351, 3476, 3600, 3725, 3849, 3974, 4100, 4224, 4349, 4474, 4599, 4723, 4848, 4974, 5098, 5223, 5348, 5473, 5597, 5721, 5846, 5970, 6096, 6221, 6346, 6470, 6595, 6720, 6846, 6970, 7095, 7220, 7344, 7469, 7594, 7719, 7842, 7968, 8093, 8217, 8342, 8467, 8592, 8716, 8841, 8967, 9091, 9216, 9341, 9466, 9590, 9715, 9841]
    data3 = [0, 2305, 2539, 2772, 3006, 3240, 3473, 3708, 3942, 4176, 4408, 4642, 4876, 5111, 5343, 5578, 5812, 6045, 6279, 6513, 6747, 6980, 7215, 7449, 7683, 7916, 8150, 8384, 8617, 8852, 9086, 9320, 9553, 9787, 10021, 10255, 10488, 10723, 10957, 11190, 11424, 11658, 11892, 12124, 12360, 12594, 12828, 13060, 13294, 13528, 13761, 13995, 14230, 14464, 14697, 14931, 15165, 15399, 15632, 15867, 16101, 16335, 16568, 16802, 17036, 17269, 17504, 17738, 17972, 18205, 18439]
    收招倍率 = 1
    CD = 25.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    乱舞数 = 11
    分身乱舞数 = 4
    演出时间 = 0.6
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.分身乱舞数 *= 2.1
            self.收招倍率 *= 1.08
            self.CD *= 0.9
        elif x == 1:
            self.分身乱舞数 *= 2.88
            self.收招倍率 *= 1.08
            self.CD *= 0.9

    def 等效百分比(self, 武器类型):
        return ((self.data[self.等级]*self.乱舞数 + self.data1[self.等级] * self.分身乱舞数 + self.data2[self.等级]) * self.攻击次数 + self.data3[self.等级] * self.收招倍率) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.11


class 技能12(主动技能):
    名称 = '绝命瞬狱杀'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    data = [0, 1809, 1991, 2176, 2359, 2541, 2726, 2909, 3093, 3276, 3461, 3643, 3827, 4010, 4194, 4377, 4560, 4744, 4928, 5111, 5294, 5479, 5661, 5846, 6029, 6211, 6396, 6579, 6763, 6946, 7130, 7313, 7497, 7681, 7864, 8047, 8230, 8414, 8598, 8781, 8964, 9149, 9331, 9516, 9699, 9881, 10066, 10250, 10433, 10616, 10800, 10983, 11167, 11351, 11534, 11717, 11902, 12084, 12267, 12452, 12634, 12819, 13001, 13186, 13369, 13552, 13736, 13920, 14102, 14286, 14470]
    data1 = [0, 2712, 2988, 3262, 3539, 3814, 4089, 4364, 4640, 4914, 5190, 5465, 5739, 6015, 6291, 6567, 6841, 7117, 7391, 7667, 7942, 8218, 8492, 8768, 9044, 9319, 9594, 9870, 10144, 10420, 10695, 10970, 11245, 11521, 11795, 12072, 12347, 12621, 12897, 13172, 13447, 13722, 13998, 14272, 14548, 14824, 15100, 15374, 15650, 15925, 16200, 16475, 16751, 17025, 17301, 17577, 17852, 18127, 18403, 18677, 18952, 19228, 19502, 19778, 20053, 20328, 20604, 20880, 21154, 21430, 21705]
    data2 = [0, 3617, 3984, 4350, 4718, 5085, 5452, 5820, 6186, 6553, 6921, 7287, 7653, 8020, 8388, 8755, 9122, 9490, 9856, 10223, 10591, 10958, 11323, 11691, 12058, 12425, 12792, 13160, 13526, 13893, 14261, 14628, 14993, 15361, 15728, 16095, 16462, 16829, 17196, 17563, 17931, 18298, 18663, 19031, 19398, 19765, 20133, 20499, 20866, 21233, 21601, 21968, 22333, 22701, 23068, 23435, 23803, 24169, 24536, 24904, 25271, 25638, 26003, 26372, 26738, 27105, 27473, 27839, 28206, 28574, 28941]
    data3 = [0, 4521, 4981, 5439, 5898, 6356, 6815, 7274, 7733, 8191, 8651, 9109, 9568, 10026, 10485, 10944, 11403, 11861, 12321, 12779, 13238, 13696, 14155, 14614, 15073, 15532, 15991, 16449, 16908, 17366, 17826, 18284, 18743, 19202, 19661, 20119, 20577, 21036, 21496, 21954, 22414, 22872, 23331, 23789, 24247, 24706, 25165, 25624, 26084, 26542, 27000, 27459, 27917, 28377, 28835, 29294, 29753, 30212, 30670, 31129, 31587, 32047, 32505, 32965, 33423, 33882, 34340, 34799, 35257, 35717, 36175]
    data4 = [0, 2532, 2788, 3045, 3302, 3559, 3816, 4073, 4330, 4587, 4844, 5101, 5358, 5614, 5871, 6128, 6384, 6641, 6900, 7157, 7413, 7670, 7927, 8184, 8441, 8697, 8954, 9211, 9468, 9725, 9982, 10239, 10496, 10753, 11010, 11267, 11523, 11780, 12037, 12294, 12550, 12807, 13064, 13321, 13578, 13835, 14093, 14350, 14605, 14862, 15120, 15377, 15634, 15891, 16148, 16405, 16662, 16919, 17176, 17433, 17689, 17946, 18203, 18460, 18716, 18973, 19230, 19487, 19744, 20001, 20258]
    收招倍率 = 1
    CD = 45.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.6
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.收招倍率 *= 1.4805
        elif x == 1:
            self.收招倍率 *= 1.6356

    def 等效百分比(self, 武器类型):
        return ((self.data[self.等级] + self.data1[self.等级] + self.data2[self.等级] + self.data3[self.等级]) * self.攻击次数 + self.data4[self.等级] * self.收招倍率) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.166


class 技能13(主动技能):
    名称 = '月轮舞'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 40326
    成长 = 12177
    data = [0, 12381, 15252, 18124, 20994, 23866, 26739, 29609, 32479, 35350, 38223, 41094, 43965, 46837, 49709, 52579, 55450, 58322, 61192, 64065, 66937, 69807, 72677, 75548, 78421, 81292, 84163, 87035, 89907, 92777, 95648, 98520, 101390, 104263, 107135, 110005, 112875, 115746, 118619, 121490, 124361]
    攻击次数 = 5
    演出时间 = 0.6
    CD = 145

    def 等效百分比(self, 武器类型):
        return self.data[self.等级] * self.攻击次数 * self.倍率 * 1.205

    def 等效CD(self, 武器类型, 输出类型):
        if 武器类型 == '双剑':
            return round(self.CD / self.恢复, 1)
        else:
            return round(self.CD / self.恢复 * 武器冷却惩罚(武器类型, 输出类型, self.版本), 1)


class 技能14(主动技能):
    名称 = '旋刃冲击'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    data = [0, 479, 528, 576, 625, 673, 723, 772, 820, 869, 917, 966, 1014, 1064, 1112, 1161, 1209, 1258, 1306, 1355, 1404, 1453, 1502, 1550, 1599, 1647, 1696, 1745, 1794, 1842, 1891, 1939, 1988, 2036, 2085, 2134, 2183, 2231, 2280, 2328, 2377, 2426, 2475, 2524, 2572, 2621, 2669, 2718, 2766, 2816, 2864, 2913, 2961, 3010, 3058, 3107, 3157, 3205, 3254, 3302, 3351, 3399, 3448, 3497, 3546, 3594, 3643, 3691, 3740, 3788, 3838]
    data1 = [0, 537, 591, 646, 700, 754, 810, 864, 918, 973, 1027, 1081, 1135, 1192, 1246, 1301, 1355, 1409, 1463, 1518, 1573, 1627, 1682, 1736, 1790, 1845, 1899, 1954, 2009, 2063, 2117, 2171, 2227, 2281, 2335, 2391, 2445, 2499, 2554, 2608, 2662, 2717, 2772, 2826, 2881, 2935, 2989, 3043, 3098, 3154, 3209, 3263, 3317, 3371, 3426, 3480, 3535, 3590, 3644, 3698, 3753, 3807, 3861, 3917, 3971, 4025, 4079, 4135, 4189, 4243, 4299]
    攻击次数 = 29
    收招倍率 = 5
    收招倍率3 = 0
    CD = 30.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 35
            self.收招倍率 *= 0.2
            self.收招倍率3 = 30
            self.CD *= 0.89
        elif x == 1:
            self.攻击次数 = 37.45
            self.收招倍率 *= 0.214
            self.收招倍率3 = 32.1
            self.CD *= 0.89

    def 等效百分比(self, 武器类型):
        return (self.data[self.等级] * self.攻击次数 + self.data1[self.等级] * self.收招倍率 + self.data[self.等级] * self.收招倍率3) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.257


class 技能15(主动技能):
    名称 = '陨落螺旋刺'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    data = [0, 2273, 2504, 2734, 2965, 3194, 3426, 3657, 3886, 4118, 4349, 4578, 4810, 5040, 5270, 5501, 5732, 5962, 6193, 6424, 6654, 6884, 7116, 7346, 7576, 7808, 8039, 8268, 8499, 8731, 8960, 9191, 9423, 9652, 9883, 10115, 10344, 10575, 10804, 11036, 11267, 11497, 11728, 11959, 12189, 12420, 12651, 12881, 13112, 13343, 13573, 13803, 14035, 14265, 14495, 14726, 14957, 15187, 15418, 15649, 15880, 16109, 16341, 16570, 16801, 17033, 17262, 17493, 17725, 17955, 18185]
    data1 = [0, 15911, 17527, 19141, 20756, 22369, 23983, 25598, 27212, 28828, 30442, 32056, 33670, 35284, 36898, 38513, 40126, 41742, 43356, 44971, 46584, 48199, 49813, 51428, 53041, 54657, 56271, 57886, 59499, 61114, 62728, 64343, 65956, 67572, 69186, 70801, 72414, 74029, 75643, 77256, 78872, 80487, 82101, 83714, 85329, 86943, 88558, 90171, 91787, 93401, 95016, 96629, 98244, 99858, 101472, 103086, 104702, 106316, 107930, 109544, 111159, 112773, 114387, 116001, 117617, 119231, 120845, 122459, 124074, 125687, 127301]
    data2 = [0, 4546, 5008, 5468, 5930, 6391, 6852, 7313, 7775, 8236, 8696, 9158, 9620, 10080, 10542, 11002, 11465, 11926, 12386, 12849, 13309, 13770, 14233, 14693, 15154, 15617, 16077, 16538, 16999, 17461, 17923, 18383, 18844, 19306, 19767, 20228, 20688, 21151, 21611, 22073, 22535, 22995, 23457, 23917, 24379, 24841, 25301, 25764, 26225, 26685, 27148, 27608, 28069, 28531, 28992, 29453, 29914, 30375, 30837, 31298, 31759, 32219, 32682, 33143, 33603, 34066, 34526, 34987, 35450, 35910, 36372]
    倍率1 = 1
    倍率2 = 1
    收招倍率 = 1
    CD = 50.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = -0.6
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率1 = 0
            self.倍率2 = 2.04
        elif x == 1:
            self.倍率1 = 0
            self.倍率2 = 2.27

    def 等效百分比(self, 武器类型):
        return ((self.data[self.等级] * 3 * self.倍率1 + self.data1[self.等级] * self.倍率2) * self.攻击次数 + self.data2[self.等级] * self.收招倍率) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.166


class 技能16(主动技能):
    名称 = '乱空杀'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    data = [0, 2645, 3066, 3489, 3911, 4332, 4755, 5176, 5598, 6020, 6442, 6863, 7286, 7708, 8129, 8552, 8973, 9395, 9815, 10237, 10659, 11081, 11502, 11925, 12347, 12768, 13191, 13612, 14034, 14456, 14878, 15299, 15722, 16144, 16565, 16988, 17409, 17831, 18254, 18675, 19097]
    data1 = [0, 10583, 12270, 13959, 15646, 17333, 19019, 20706, 22395, 24082, 25769, 27457, 29142, 30831, 32518, 34205, 35893, 37581, 39267, 40954, 42642, 44329, 46017, 47705, 49392, 51078, 52765, 54453, 56141, 57828, 59515, 61201, 62889, 64577, 66264, 67951, 69640, 71325, 73013, 74700, 76389]
    data2 = [0, 5291, 6135, 6979, 7822, 8666, 9508, 10353, 11197, 12040, 12884, 13728, 14571, 15415, 16259, 17103, 17947, 18791, 19633, 20476, 21320, 22164, 23007, 23851, 24696, 25539, 26383, 27227, 28070, 28914, 29758, 30600, 31443, 32287, 33132, 33975, 34819, 35663, 36506, 37350, 38194]
    收招倍率 = 1
    CD = 30.0
    是否有护石 = 1
    演出时间 = 0.2
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.17
            self.收招倍率 *= 1.17
            self.CD *= 0.89

    def 等效百分比(self, 武器类型):
        return ((self.data[self.等级] * 6 + self.data1[self.等级]) * self.攻击次数 + self.data2[self.等级] * self.收招倍率) * self.倍率 * 1.187


class 技能17(主动技能):
    名称 = '月影突袭'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    data = [0, 3861, 4254, 4646, 5037, 5429, 5820, 6212, 6605, 6996, 7388, 7780, 8172, 8562, 8954, 9347, 9739, 10131, 10522, 10914, 11306, 11699, 12091, 12481, 12873, 13265, 13657, 14048, 14441, 14833, 15225, 15616, 16007, 16399, 16792, 17184, 17576, 17967, 18358, 18750, 19142]
    data1 = [0, 7723, 8508, 9291, 10075, 10858, 11642, 12425, 13210, 13993, 14776, 15560, 16344, 17127, 17910, 18695, 19479, 20261, 21046, 21829, 22613, 23397, 24180, 24964, 25746, 26531, 27314, 28098, 28883, 29665, 30449, 31233, 32017, 32799, 33584, 34368, 35150, 35935, 36718, 37502, 38284]
    收招倍率 = 1
    CD = 50.0
    演出时间 = 0.6
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.35
            self.收招倍率 *= 1.35

    def 等效百分比(self, 武器类型):
        return (self.data[self.等级] * 10 * self.攻击次数 + self.data1[self.等级] * self.收招倍率) * self.倍率 * 1.256


class 技能18(主动技能):
    名称 = '天渊星狱'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    data = [0, 346, 426, 506, 586, 667, 747, 828, 907, 988, 1068, 1149, 1229, 1309, 1390, 1471, 1550, 1631, 1711, 1792, 1872, 1951, 2032, 2114, 2193, 2273, 2353, 2434, 2515, 2594, 2675, 2755, 2836, 2915, 2996, 3076, 3157, 3237, 3318, 3397, 3479, 3558, 3638, 3719, 3798, 3880, 3959, 4040, 4120, 4201, 4281, 4362, 4441, 4523, 4602, 4683, 4763, 4843, 4924, 5004, 5084, 5163, 5245, 5326, 5405, 5485, 5566, 5646, 5727, 5806, 5887]
    data1 = [0, 80008, 98560, 117113, 135666, 154217, 172770, 191323, 209875, 228428, 246980, 265534, 284087, 302638, 321191, 339744, 358296, 376849, 395403, 413955, 432508, 451059, 469612, 488165, 506717, 525270, 543823, 562374, 580928, 599480, 618033, 636586, 655138, 673691, 692244, 710795, 729348, 747900, 766454, 785007, 803559, 822112, 840665, 859216, 877769, 896323, 914875, 933428, 951980, 970532, 989085, 1007637, 1026190, 1044743, 1063296, 1081849, 1100400, 1118953, 1137506, 1156058, 1174611, 1193164, 1211716, 1230270, 1248820, 1267374, 1285927, 1304479, 1323032, 1341585, 1360136]
    data2 = [0, 16624, 20480, 24335, 28189, 32045, 35899, 39754, 43610, 47465, 51320, 55176, 59030, 62885, 66741, 70596, 74451, 78307, 82162, 86016, 89870, 93726, 97581, 101435, 105291, 109146, 113001, 116857, 120712, 124567, 128422, 132277, 136132, 139988, 143843, 147696, 151551, 155407, 159262, 163118, 166973, 170827, 174683, 178538, 182393, 186249, 190104, 193959, 197814, 201669, 205524, 209378, 213233, 217088, 220943, 224799, 228654, 232509, 236365, 240219, 244074, 247930, 251785, 255640, 259496, 263350, 267205, 271060, 274915, 278770, 282624]
    收招倍率 = 1
    CD = 180
    演出时间 = 3

    def 等效百分比(self, 武器类型):
        return ((self.data[self.等级] * 8 + self.data1[self.等级]) * self.攻击次数 + self.data2[self.等级] * self.收招倍率) * self.倍率 * 1.187


class 技能19(被动技能):
    名称 = '死亡风暴'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 22
    关联技能 = ['无']
    data = [0, 419, 462, 505, 550, 592, 636, 679, 722, 767, 810, 854, 896, 940, 984, 1026, 1069, 1113, 1155, 1199, 1243, 1287, 1329, 1373, 1416, 1461, 1505, 1546, 1589, 1632, 1675, 1720, 1764, 1806, 1850, 1893, 1938, 1980, 2024, 2067, 2109, 2152, 2197, 2239, 2283, 2326, 2370, 2415, 2457, 2501, 2544, 2587, 2629, 2674, 2716, 2760, 2803, 2847, 2892, 2934, 2978, 3021, 3064, 3108, 3152, 3193, 3237, 3280, 3324, 3367, 3411]
    匕首数量 = 30
    倍率 = 1

    def 额外百分比(self):
        return self.data[self.等级] * self.匕首数量 * self.倍率 * 1.247


class 技能20(被动技能):
    名称 = '绝命时刻'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能21(主动技能):
    名称 = '幻灭瞬杀'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    data0 = [0, 13675, 15062, 16449, 17837, 19224, 20611, 21999, 23386, 24773, 26161, 27548, 28935, 30323, 31710, 33097, 34485, 35872, 37259, 38647, 40034, 41422, 42809, 44196, 45584, 46971, 48358, 49746, 51133, 52520, 53908, 55295, 56682, 58070, 59457, 60844, 62232, 63619, 65006, 66394, 67781]
    攻击次数 = 5
    data1 = [0, 13675, 15062, 16449, 17837, 19224, 20611, 21999, 23386, 24773, 26161, 27548, 28935, 30323, 31710, 33097, 34485, 35872, 37259, 38647, 40034, 41422, 42809, 44196, 45584, 46971, 48358, 49746, 51133, 52520, 53908, 55295, 56682, 58070, 59457, 60844, 62232, 63619, 65006, 66394, 67781]
    收招倍率 = 1
    CD = 60
    演出时间 = 0.5

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级] * self.攻击次数 + self.data1[self.等级]  * self.收招倍率) * self.倍率 * 1.167


class 技能22(主动技能):
    名称 = '影·万古星辰'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    data0 = [0, 16509, 20338, 24166, 27994, 31823, 35651, 39479, 43308, 47136, 50964, 54793, 58621, 62450, 66278, 70106, 73935, 77763, 81591, 85420, 89248, 93076, 96905, 100733, 104561, 108390, 112218, 116046, 119875, 123703, 127532, 131360, 135188, 139017, 142845, 146673, 150502, 154330, 158158, 161987, 165815]
    攻击次数 = 13
    data1 = [0, 42925, 52879, 62832, 72786, 82740, 92694, 102647, 112601, 122555, 132508, 142462, 152416, 162370, 172323, 182277, 192231, 202184, 212138, 222092, 232046, 241999, 251953, 261907, 271860, 281814, 291768, 301722, 311675, 321629, 331583, 341536, 351490, 361444, 371398, 381351, 391305, 401259, 411212, 421166, 431120]
    收招倍率 = 1
    CD = 290
    演出时间 = 6

    def 等效百分比(self, 武器类型):
        return (self.data0[self.等级]* self.攻击次数 + self.data1[self.等级] * self.收招倍率) * self.倍率 * 1.189

    关联技能 = ['无']

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

    实际名称 = '隐夜·刺客'
    角色 = '暗夜使者'
    职业 = '刺客'

    武器选项 = ['匕首', '双剑']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 1.77

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                i.收招倍率 *= self.技能栏[0].终结追击倍率()
                i.收招倍率2 *= self.技能栏[0].终结追击倍率()
        if self.武器类型 == '双剑':
            for i in self.技能栏:
                if i.是否有伤害 == 1:
                    i.收招倍率 *= self.技能栏[1].终结追击倍率() * 3.25
                    i.收招倍率2 *= self.技能栏[1].终结追击倍率()
                    if self.装备栏[11] == '血色舞会':
                        i.收招倍率 *= 1.4
                        i.收招倍率2 *= 1.4
            if self.装备栏[11] == '一叶障目':
                self.技能栏[self.技能序号['死亡风暴']].倍率 *= 1+0.32*self.技能伤害增加增幅
        if self.武器类型 == '匕首':
            for i in self.技能栏:
                if i.是否有伤害 == 1:
                    i.收招倍率 *= 4.25

    def 数据计算(self, x=0, y=-1):
        self.预处理()
        # 初步计算
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算(y)
        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        # 死亡风暴伤害
        if 技能总伤害[self.技能序号['剑刃风暴']] != 0:
            技能释放次数[self.技能序号['死亡风暴']] = 1
            技能总伤害[self.技能序号['死亡风暴']] = 技能总伤害[self.技能序号['剑刃风暴']] * \
                self.技能栏[self.技能序号['死亡风暴']].额外百分比(
            ) / self.技能栏[self.技能序号['剑刃风暴']].等效百分比(self.武器类型)

        # 返回结果
        return self.数据返回(x, 技能释放次数, 技能总伤害)


class 隐夜·刺客(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业属性()
        self.角色属性A = 职业属性()
        self.角色属性B = 职业属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)

    def 界面(self):
        super().界面()
        self.收招选择 = []
        count = 0
        for i in self.初始属性.技能栏:
            if i.是否有伤害 == 1:
                if i.收招倍率 != 0:
                    self.收招选择.append(QCheckBox(i.名称 + '-收招', self.main_frame2))
                    self.收招选择[count].resize(120, 20)
                    self.收招选择[count].move(
                        335 + 135 * int(count / 7), 440 + 26 * (count % 7))
                    self.收招选择[count].setStyleSheet(复选框样式)
                    self.收招选择[count].setChecked(True)
                    count += 1

        self.旋舞斩收招次数 = MyQComboBox(self.main_frame2)
        for i in range(8):
            self.旋舞斩收招次数.addItem('旋舞斩收招次数:'+str(i))
        self.旋舞斩收招次数.resize(170, 20)
        self.旋舞斩收招次数.move(600, 470)
        self.旋舞斩收招次数.setToolTip('匕首最高7次，双剑最高6次')

        self.剑刃风暴旋转次数 = MyQComboBox(self.main_frame2)
        for i in range(1, 11):
            self.剑刃风暴旋转次数.addItem('剑刃风暴旋转次数:'+str(i))
        self.剑刃风暴旋转次数.resize(170, 20)
        self.剑刃风暴旋转次数.move(600, 498)
        self.剑刃风暴旋转次数.setToolTip('旋转次数最高10次')
        self.剑刃风暴旋转次数.setCurrentIndex(8)

        self.螺旋穿刺旋转次数 = MyQComboBox(self.main_frame2)
        for i in range(7):
            self.螺旋穿刺旋转次数.addItem('螺旋穿刺旋转次数:'+str(i))
        self.螺旋穿刺旋转次数.resize(170, 20)
        self.螺旋穿刺旋转次数.move(600, 526)
        self.螺旋穿刺旋转次数.setToolTip('旋转次数最高6次，护石旋转次数为3倍')

        self.死亡风暴攻击次数 = MyQComboBox(self.main_frame2)
        for i in range(1, 31):
            self.死亡风暴攻击次数.addItem('死亡风暴攻击次数:'+str(i))
        self.死亡风暴攻击次数.resize(170, 20)
        self.死亡风暴攻击次数.move(600, 554)
        self.死亡风暴攻击次数.setToolTip('最高30次')
        self.死亡风暴攻击次数.setCurrentIndex(27)

        self.职业存档.append(('旋舞斩收招次数', self.旋舞斩收招次数, 1))
        self.职业存档.append(('剑刃风暴旋转次数', self.剑刃风暴旋转次数, 1))
        self.职业存档.append(('螺旋穿刺旋转次数', self.螺旋穿刺旋转次数, 1))
        self.职业存档.append(('死亡风暴攻击次数', self.死亡风暴攻击次数, 1))
        num = 0
        for item in self.收招选择:
            self.职业存档.append(('收招选择-{}'.format(num), item, 0))
            num += 1

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        count = 0
        for i in 属性.技能栏:
            if i.是否有伤害 == 1:
                if i.收招倍率 != 0:
                    if not self.收招选择[count].isChecked():
                        i.收招倍率 = 0
                        i.收招倍率3 = 0
                    count += 1

        属性.技能栏[属性.技能序号['旋舞斩']].收招倍率2 = self.旋舞斩收招次数.currentIndex()
        属性.技能栏[属性.技能序号['剑刃风暴']].旋转次数 = self.剑刃风暴旋转次数.currentIndex() + 1
        属性.技能栏[属性.技能序号['螺旋穿刺']].旋转次数 = self.螺旋穿刺旋转次数.currentIndex()
        属性.技能栏[属性.技能序号['死亡风暴']].匕首数量 = self.死亡风暴攻击次数.currentIndex() + 1
