from math import *
from PublicReference.carry.base import *
# 2021.4.7 韩测


class 职业主动技能(主动技能):
    锁定护石 = 0
    歼灭次数 = 0


class 技能0(职业主动技能):
    名称 = '连续射击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    data0 = [int(x*1.0*932/888) for x in [0, 888, 979, 1069, 1159, 1250, 1340, 1430, 1520, 1611, 1701, 1790, 1881, 1971, 2061, 2151, 2242, 2332, 2422, 2513, 2603, 2693, 2784, 2873, 2963, 3053, 3144, 3234, 3324, 3415, 3505, 3595, 3686,
                                          3776, 3865, 3955, 4046, 4136, 4226, 4317, 4407, 4497, 4587, 4678, 4768, 4857, 4948, 5038, 5128, 5219, 5309, 5399, 5489, 5580, 5670, 5760, 5851, 5940, 6030, 6120, 6211, 6301, 6391, 6482, 6572, 6662, 6753, 6843, 6932, 7022, 7113]]
    攻击次数1 = 2
    data1 = [int(x*1.0*1244/1185) for x in [0, 1185, 1305, 1426, 1546, 1666, 1786, 1907, 2027, 2147, 2268, 2388, 2508, 2628, 2749, 2869, 2989, 3109, 3230, 3351, 3470, 3591, 3711, 3831, 3951, 4072, 4192, 4312, 4432, 4553, 4674, 4793, 4914,
                                            5034, 5154, 5274, 5395, 5515, 5635, 5756, 5876, 5997, 6116, 6237, 6357, 6477, 6597, 6718, 6838, 6958, 7079, 7199, 7320, 7439, 7560, 7680, 7800, 7920, 8041, 8161, 8281, 8402, 8522, 8643, 8762, 8883, 9003, 9123, 9243, 9364, 9485]]
    攻击次数2 = 1
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return ((self.data0[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.data1[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率


class 技能1(被动技能):
    名称 = '特工秘技'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + 0.02 * self.等级, 5)


class 技能2(职业主动技能):
    名称 = '双弦斩'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    data0 = [int(x*1.0*1246/1187) for x in [0, 1187, 1307, 1427, 1548, 1668, 1788, 1909, 2030, 2149, 2270, 2391, 2512, 2631, 2752, 2873, 2993, 3113, 3234, 3354, 3474, 3595, 3715, 3836, 3956, 4077, 4197, 4318, 4438, 4558, 4679, 4800, 4919,
                                            5040, 5161, 5280, 5401, 5522, 5642, 5762, 5883, 6004, 6124, 6244, 6365, 6485, 6606, 6726, 6846, 6967, 7088, 7207, 7328, 7449, 7568, 7689, 7810, 7931, 8050, 8171, 8292, 8412, 8532, 8653, 8773, 8894, 9014, 9134, 9255, 9375, 9495]]
    攻击次数1 = 1
    data1 = [int(x*1.0*1869/1780) for x in [0, 1780, 1960, 2141, 2322, 2502, 2683, 2863, 3044, 3225, 3406, 3587, 3767, 3948, 4129, 4309, 4490, 4670, 4851, 5032, 5212, 5393, 5573, 5754, 5935, 6115, 6296, 6476, 6657, 6838, 7018, 7199, 7379, 7560, 7741,
                                            7921, 8102, 8282, 8463, 8644, 8824, 9006, 9186, 9367, 9548, 9728, 9909, 10089, 10270, 10451, 10631, 10812, 10992, 11173, 11354, 11534, 11715, 11895, 12076, 12257, 12437, 12618, 12798, 12979, 13160, 13340, 13521, 13701, 13882, 14063, 14243]]
    攻击次数2 = 1
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return ((self.data0[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.data1[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率


class 技能3(职业主动技能):
    名称 = '月光挥斩'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据 = [int(x*1.0*2143/2029) for x in [0, 2029, 2234, 2441, 2647, 2853, 3059, 3264, 3470, 3676, 3882, 4088, 4293, 4499, 4705, 4912, 5118, 5324, 5529, 5735, 5941, 6147, 6353, 6558, 6764, 6970, 7177, 7383, 7588, 7794, 8000, 8206, 8412, 8617, 8823, 9029,
                                         9235, 9441, 9647, 9853, 10059, 10265, 10471, 10676, 10882, 11088, 11294, 11500, 11705, 11912, 12118, 12324, 12530, 12735, 12941, 13147, 13353, 13559, 13764, 13970, 14176, 14383, 14589, 14795, 15000, 15206, 15412, 15618, 15824, 16029, 16235]]
    攻击次数 = 2
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能4(被动技能):
    名称 = '小太刀精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.040 + 0.01 * self.等级, 5)
        if self.等级 > 10:
            return round(1.150 + 0.02 * (self.等级 - 10), 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.040 + 0.01 * self.等级, 5)
        if self.等级 > 10:
            return round(1.150 + 0.02 * (self.等级 - 10), 5)


class 技能5(职业主动技能):
    名称 = '满月斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data0 = [int(x*1.0*1332/1217) for x in [0, 1217, 1341, 1465, 1588, 1712, 1835, 1958, 2082, 2205, 2329, 2453, 2576, 2700, 2823, 2946, 3070, 3194, 3317, 3441, 3565, 3688, 3812, 3935, 4058, 4182, 4306, 4429, 4553, 4677, 4800, 4923, 5047,
                                            5170, 5294, 5418, 5541, 5665, 5788, 5912, 6035, 6158, 6282, 6406, 6529, 6653, 6777, 6900, 7023, 7147, 7270, 7394, 7518, 7641, 7765, 7889, 8012, 8135, 8259, 8382, 8506, 8630, 8753, 8877, 9001, 9123, 9247, 9370, 9494, 9618, 9741]]
    攻击次数1 = 3
    data1 = [int(x*1.0*4884/4465) for x in [0, 4465, 4917, 5371, 5823, 6277, 6729, 7182, 7636, 8088, 8542, 8994, 9447, 9900, 10353, 10807, 11259, 11712, 12165, 12618, 13071, 13524, 13977, 14430, 14883, 15336, 15789, 16241, 16695, 17148, 17601, 18054, 18506, 18960,
                                            19412, 19866, 20319, 20771, 21225, 21677, 22131, 22583, 23036, 23490, 23942, 24396, 24848, 25301, 25754, 26207, 26661, 27113, 27566, 28019, 28472, 28925, 29378, 29831, 30284, 30737, 31190, 31643, 32095, 32549, 33002, 33455, 33908, 34360, 34814, 35266, 35720]]
    攻击次数2 = 1
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.8

    def 等效百分比(self, 武器类型):
        return ((self.data0[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.data1[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率


class 技能6(职业主动技能):
    名称 = '迅步突袭'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据 = [int(x*1.0*2952/2695) for x in [0, 2695, 2968, 3241, 3515, 3788, 4062, 4335, 4608, 4883, 5157, 5429, 5703, 5977, 6250, 6523, 6797, 7070, 7344, 7617, 7890, 8164, 8438, 8711, 8984, 9258, 9532, 9804, 10078, 10352, 10624, 10898, 11172, 11445, 11719,
                                         11992, 12265, 12539, 12813, 13085, 13359, 13633, 13905, 14179, 14453, 14726, 14999, 15273, 15546, 15820, 16093, 16366, 16640, 16914, 17187, 17460, 17735, 18009, 18281, 18555, 18829, 19102, 19375, 19649, 19922, 20196, 20469, 20742, 21016, 21290, 21562]]
    攻击次数 = 1
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 5
    ###
    # 倍率 = 1/1.072*1.103
    # 韩测加强

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能7(职业主动技能):
    名称 = '月影秘步'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据 = [int(x*1.0) for x in [0, 837, 922, 1007, 1091, 1176, 1261, 1346, 1431, 1516, 1601, 1686, 1771, 1856, 1941, 2026, 2111, 2196, 2281, 2365, 2450, 2535, 2620, 2705, 2790, 2875, 2960, 3045, 3130, 3215, 3300, 3385, 3470, 3554,
                               3639, 3724, 3809, 3894, 3979, 4064, 4149, 4234, 4319, 4404, 4489, 4574, 4659, 4744, 4828, 4913, 4998, 5083, 5168, 5253, 5338, 5423, 5508, 5593, 5678, 5763, 5848, 5933, 6017, 6102, 6187, 6272, 6357, 6442, 6527, 6612, 6697]]
    攻击次数 = 6
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 2
    护石选项 = ['魔界', '圣痕']

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.18
            self.CD *= 0.85
        elif x == 1:
            self.倍率 *= 1.27
            self.CD *= 0.85


class 技能8(职业主动技能):
    名称 = '锁定射击'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据 = [int(x*1.0*1300/1210*1.1) for x in [0, 1210, 1332, 1455, 1578, 1701, 1823, 1946, 2069, 2191, 2314, 2437, 2560, 2683, 2806, 2928, 3051, 3174, 3296, 3419, 3542, 3665, 3787, 3910, 4033, 4156, 4279, 4402, 4524, 4646, 4769, 4892, 5015,
                                             5138, 5261, 5383, 5506, 5629, 5752, 5875, 5997, 6119, 6242, 6365, 6488, 6611, 6734, 6857, 6979, 7102, 7225, 7347, 7470, 7593, 7715, 7838, 7961, 8084, 8207, 8330, 8453, 8575, 8698, 8820, 8943, 9066, 9189, 9311, 9434, 9557, 9680]]
    攻击次数 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.6 - 4.2
    锁定护石 = 0
    护石选项 = ['魔界', '圣痕']

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.05
            self.锁定护石 = 1
        elif x == 1:
            self.倍率 *= 1.14
            self.锁定护石 = 1


class 技能9(职业主动技能):
    名称 = '枪刃旋杀'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    data0 = [int(x*1.0*1218/1160*1.102) for x in [0, 1160, 1278, 1395, 1514, 1632, 1749, 1867, 1985, 2102, 2221, 2338, 2456, 2574, 2691, 2809, 2926, 3045, 3163, 3280, 3398, 3515, 3633, 3752, 3869, 3987, 4104, 4222, 4340, 4458, 4576, 4694,
                                                  4811, 4929, 5046, 5164, 5283, 5400, 5518, 5635, 5753, 5871, 5989, 6107, 6224, 6342, 6460, 6577, 6696, 6813, 6931, 7049, 7166, 7284, 7403, 7520, 7638, 7755, 7873, 7991, 8108, 8227, 8344, 8462, 8580, 8697, 8815, 8933, 9051, 9169, 9286]]
    攻击次数1 = 1
    data1 = [int(x*1.0*1044/994*1.102) for x in [0, 994, 1095, 1196, 1298, 1399, 1499, 1600, 1701, 1802, 1903, 2003, 2105, 2206, 2307, 2408, 2508, 2609, 2710, 2812, 2913, 3014, 3114, 3215, 3316, 3417, 3519, 3619, 3720, 3821, 3922, 4023,
                                                 4123, 4225, 4326, 4427, 4528, 4628, 4729, 4830, 4931, 5033, 5133, 5234, 5335, 5436, 5537, 5637, 5739, 5840, 5941, 6042, 6143, 6243, 6344, 6446, 6547, 6648, 6748, 6849, 6950, 7051, 7152, 7253, 7354, 7455, 7556, 7657, 7757, 7858, 7960]]
    攻击次数2 = 17
    数据3 = [int(x*1.0*5375/5119*1.102) for x in [0, 5119, 5639, 6157, 6677, 7197, 7715, 8235, 8755, 9274, 9793, 10313, 10832, 11352, 11870, 12390, 12910, 13428, 13948, 14468, 14987, 15506, 16026, 16545, 17065, 17583, 18103, 18623, 19142, 19661, 20181, 20700, 21219, 21739,
                                                22258, 22778, 23296, 23816, 24336, 24855, 25374, 25894, 26413, 26933, 27452, 27971, 28491, 29009, 29529, 30049, 30568, 31087, 31607, 32126, 32646, 33165, 33684, 34204, 34722, 35242, 35762, 36281, 36800, 37320, 37839, 38359, 38878, 39397, 39917, 40436, 40955]]
    攻击次数3 = 2
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4.5
    护石选项 = ['魔界', '圣痕']

    def 等效百分比(self, 武器类型):
        return ((self.data0[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.data1[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))+(self.数据3[self.等级] * self.攻击次数3 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 *= 1.92
            self.攻击次数3 *= 0
        elif x == 1:
            self.攻击次数2 *= 2.07
            self.攻击次数3 *= 0


class 技能10(职业主动技能):
    名称 = '终极锁定'
    所在等级 = 60
    等级上限 = 60
    基础等级 = 23
    数据 = [int(x*1.0*5564/5288*1.10) for x in [0, 5288, 5824, 6361, 6897, 7434, 7971, 8507, 9044, 9580, 10117, 10653, 11190, 11725, 12262, 12798, 13335, 13872, 14408,
                                              14945, 15481, 16018, 16554, 17091, 17627, 18164, 18701, 19237, 19774, 20310, 20847, 21383, 21920, 22456, 22992, 23528, 24065, 24602, 25138, 25675, 26211]]
    攻击次数 = 4
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.2
    护石选项 = ['魔界', '圣痕']

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.07
            self.CD *= 0.90
            self.攻击次数 += 0.6
        elif x == 1:
            self.倍率 *= 1.16
            self.CD *= 0.90
            self.攻击次数 += 0.6


class 技能11(被动技能):
    名称 = '使命觉悟'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class 技能12(职业主动技能):
    名称 = '噬血绝杀'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据 = [int(x*1.0*95112/90161) for x in [0, 29207, 35979, 42753, 49525, 56298, 63070, 69843, 76616, 83389, 90161, 96934, 103706, 110480, 117252, 124025, 130797, 137571, 144344,
                                           151116, 157889, 164661, 171435, 178207, 184980, 191752, 198526, 205298, 212071, 218843, 225616, 232389, 239162, 245934, 252707, 259480, 266253, 273025, 279798, 286570, 293344]]
    攻击次数 = 2
    一觉减CD = 0
    冷却关联技能 = ['所有']
    暗杀目标加成 = 1.1
    CD = 145.0

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.暗杀目标加成 * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

    def CD缩减倍率(self, 武器类型):
        return round(1 - self.一觉减CD, 3)


class 技能13(职业主动技能):
    名称 = '月相轮舞'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    data0 = [int(x*1.0*5100/4682*1.105) for x in [0, 4682, 5158, 5632, 6108, 6582, 7058, 7533, 8007, 8483, 8958, 9433, 9908, 10383, 10858, 11334, 11808, 12284, 12759, 13233, 13709, 14183, 14659, 15134, 15609, 16084, 16560, 17034, 17509, 17984, 18459, 18935, 19409, 19885,
                                                  20360, 20835, 21310, 21784, 22260, 22735, 23210, 23685, 24161, 24635, 25111, 25585, 26061, 26536, 27010, 27486, 27960, 28436, 28911, 29386, 29861, 30337, 30811, 31286, 31761, 32236, 32712, 33186, 33662, 34137, 34612, 35087, 35561, 36037, 36512, 36987, 37462]]
    攻击次数1 = 2
    data1 = [int(x*1.0*5767/5294*1.105) for x in [0, 5294, 5832, 6368, 6906, 7442, 7980, 8517, 9054, 9591, 10128, 10666, 11202, 11740, 12277, 12814, 13351, 13888, 14425, 14963, 15500, 16037, 16574, 17111, 17648, 18185, 18723, 19259, 19797, 20334, 20871, 21408, 21945,
                                                  22483, 23019, 23557, 24093, 24631, 25169, 25705, 26243, 26779, 27317, 27853, 28391, 28928, 29465, 30003, 30539, 31077, 31613, 32151, 32688, 33225, 33762, 34299, 34837, 35373, 35911, 36448, 36985, 37522, 38059, 38596, 39134, 39670, 40208, 40745, 41282, 41819, 42356]]
    攻击次数2 = 2
    数据3 = [int(x*1.0*7210/6618*1.105) for x in [0, 6618, 7289, 7960, 8632, 9303, 9975, 10646, 11318, 11989, 12661, 13332, 14003, 14675, 15346, 16018, 16689, 17361, 18032, 18704, 19375, 20046, 20718, 21389, 22061, 22731, 23403, 24074, 24746, 25417, 26088, 26760, 27431,
                                                28103, 28774, 29446, 30117, 30789, 31460, 32131, 32803, 33474, 34146, 34817, 35489, 36160, 36832, 37503, 38174, 38846, 39517, 40189, 40860, 41532, 42203, 42875, 43546, 44217, 44889, 45560, 46232, 46902, 47574, 48245, 48917, 49588, 50259, 50931, 51602, 52274, 52945]]
    攻击次数3 = 2
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.0
    护石选项 = ['魔界', '圣痕']

    def 等效百分比(self, 武器类型):
        return ((self.data0[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.data1[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))+(self.数据3[self.等级] * self.攻击次数3 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
            self.CD *= 0.90
        elif x == 1:
            self.倍率 *= 1.28
            self.CD *= 0.90


class 技能14(职业主动技能):
    名称 = '月光镇魂曲'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    data0 = [int(x*1.0*4834/4604*1.051) for x in [0, 4604, 5070, 5538, 6005, 6472, 6939, 7407, 7874, 8340, 8807, 9275, 9742, 10209, 10676, 11144, 11611, 12077, 12544,
                                                  13012, 13479, 13946, 14413, 14881, 15347, 15814, 16281, 16749, 17216, 17683, 18150, 18617, 19084, 19551, 20018, 20486, 20953, 21420, 21887, 22353, 22821]]
    攻击次数1 = 9
    data1 = [int(x*1.0*18647/17759*1.051) for x in [0, 17759, 19560, 21362, 23164, 24966, 26768, 28569, 30371, 32173, 33975, 35776, 37577, 39379, 41181, 42983, 44785, 46586,
                                                    48388, 50190, 51992, 53793, 55594, 57396, 59198, 61000, 62802, 64603, 66405, 68207, 70009, 71810, 73611, 75413, 77215, 79017, 80819, 82620, 84422, 86224, 88026]]
    攻击次数2 = 1
    CD = 40.0
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return ((self.data0[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.data1[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.攻击次数1 = 1.64*(9 - 3)
        self.攻击次数2 *= 1.75


class 技能15(被动技能):
    名称 = '冷酷杀意'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 技能16(职业主动技能):
    名称 = '毁灭狂欢'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    data0 = [int(x*1.0*4993/4521*1.104) for x in [0, 4521, 4980, 5439, 5898, 6357, 6816, 7273, 7732, 8191, 8650, 9109, 9568, 10026, 10485, 10944, 11403, 11861, 12320, 12779, 13237, 13696, 14155, 14614, 15073, 15532, 15989, 16448, 16907, 17366, 17825, 18284, 18743, 19201,
                                                  19660, 20119, 20577, 21036, 21495, 21953, 22412, 22871, 23330, 23789, 24248, 24707, 25164, 25623, 26082, 26541, 27000, 27459, 27917, 28376, 28835, 29294, 29752, 30211, 30669, 31128, 31587, 32046, 32505, 32964, 33423, 33880, 34339, 34798, 35257, 35716, 36175]]
    攻击次数1 = 9
    暗杀目标追加攻击次数1 = 2
    data1 = [int(x*1.0*9693/8777*1.104) for x in [0, 8777, 9667, 10558, 11449, 12340, 13230, 14120, 15011, 15901, 16792, 17682, 18572, 19463, 20354, 21245, 22135, 23025, 23916, 24806, 25697, 26587, 27477, 28368, 29258, 30150, 31040, 31931, 32821, 33711, 34602, 35492, 36383,
                                                  37273, 38163, 39055, 39945, 40836, 41726, 42616, 43507, 44397, 45288, 46178, 47068, 47959, 48850, 49741, 50631, 51521, 52412, 53302, 54193, 55083, 55973, 56864, 57755, 58646, 59536, 60426, 61317, 62207, 63098, 63988, 64878, 65769, 66659, 67551, 68441, 69332, 70222]]
    攻击次数2 = 1
    CD = 45.0
    演出时间 = 1.5
    歼灭次数 = 0
    是否有护石 = 1
    ###
    # 倍率 = 1 / 1.115 * 1.12
    # 韩测加强

    def 等效百分比(self, 武器类型):
        return ((self.data0[self.等级] * (self.攻击次数1 + self.暗杀目标追加攻击次数1) * (1 + self.TP成长 * self.TP等级))+(self.data1[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.33


class 技能17(职业主动技能):
    名称 = '精准射击'
    技能图标顺序 = 5
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据 = [int(x*1.0*5652/5211*1.1) for x in [0, 5211, 5740, 6270, 6798, 7327, 7855, 8384, 8912, 9442, 9971, 10499, 11028, 11556, 12086, 12615, 13143, 13672, 14200, 14729, 15258, 15787, 16316, 16844, 17373, 17901, 18431, 18960, 19488, 20017, 20545, 21075, 21603, 22132,
                                             22661, 23189, 23718, 24247, 24776, 25305, 25833, 26362, 26891, 27420, 27948, 28477, 29006, 29534, 30064, 30592, 31121, 31650, 32178, 32708, 33236, 33765, 34293, 34822, 35351, 35880, 36409, 36937, 37466, 37994, 38523, 39053, 39581, 40110, 40638, 41167, 41697]]
    攻击次数 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能18(职业主动技能):
    名称 = '月相天陨'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    data0 = [int(x*1.0*4402/4174) for x in [0, 4174, 5142, 6110, 7078, 8046, 9014, 9982, 10950, 11918, 12886, 13854, 14822, 15790, 16758, 17726, 18694, 19662, 20630, 21597, 22566, 23534, 24502, 25470, 26438, 27406, 28374, 29342, 30310, 31277, 32246, 33214, 34182, 35150,
                                            36118, 37086, 38054, 39022, 39990, 40957, 41925, 42894, 43862, 44830, 45798, 46766, 47734, 48702, 49670, 50637, 51605, 52574, 53542, 54510, 55478, 56446, 57414, 58382, 59350, 60317, 61285, 62253, 63222, 64190, 65158, 66126, 67094, 68062, 69030, 69997, 70965]]
    攻击次数1 = 21
    data1 = [int(x*1.0*49783/47203) for x in [0, 47203, 58149, 69095, 80040, 90987, 101932, 112878, 123824, 134770, 145716, 156661, 167607, 178553, 189499, 200445, 211390, 222336, 233282, 244228, 255173, 266119, 277066, 288011, 298957, 309902, 320849, 331795, 342740, 353686, 364631, 375578, 386523, 397469,
                                              408415, 419361, 430307, 441252, 452198, 463143, 474090, 485036, 495981, 506927, 517873, 528819, 539765, 550710, 561657, 572602, 583548, 594493, 605439, 616386, 627331, 638277, 649222, 660169, 671114, 682060, 693006, 703952, 714898, 725843, 736789, 747734, 758681, 769627, 780572, 791518, 802464]]
    攻击次数2 = 1
    CD = 180.0

    def 等效百分比(self, 武器类型):
        return ((self.data0[self.等级] * self.攻击次数1)+(self.data1[self.等级] * self.攻击次数2)) * self.倍率


class 技能19(被动技能):
    名称 = '无暇'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能20(职业主动技能):
    名称 = '夜影迷踪'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 6
    data0 = [int(x*1.0*54754/49942) for x in [0, 33135, 36496, 39858, 43219, 46581, 49942, 53304, 56665, 60027, 63389, 66751, 70112, 73474, 76835, 80197, 83558, 86919, 90281, 93643, 97004, 100365, 103727, 107090, 110451, 113812, 117173, 120536, 123897, 127258, 130619, 133982, 137343, 140704, 144065,
                                              147428, 150789, 154151, 157512, 160874, 164236, 167597, 170958, 174319, 177682, 181043, 184404, 187765, 191128, 194489, 197850, 201212, 204574, 207936, 211297, 214658, 218020, 221382, 224743, 228104, 231466, 234828, 238189, 241550, 244913, 248274, 251636, 254997, 258359, 261720, 265082]]
    攻击次数1 = 1
    data1 = [int(x*1.0*58404/53273) for x in [0, 35343, 38930, 42515, 46101, 49686, 53273, 56858, 60443, 64029, 67615, 71201, 74786, 78372, 81957, 85544, 89128, 92714, 96300, 99885, 103471, 107057, 110643, 114228, 117814, 121400, 124985, 128570, 132156, 135742, 139328, 142913, 146499, 150085, 153671,
                                              157255, 160842, 164427, 168014, 171598, 175184, 178770, 182356, 185941, 189526, 193113, 196698, 200284, 203869, 207456, 211041, 214627, 218212, 221797, 225384, 228968, 232555, 236140, 239727, 243311, 246898, 250483, 254069, 257654, 261240, 264826, 268412, 271997, 275582, 279168, 282753]]
    攻击次数2 = 1
    数据3 = [int(x*1.0*69355/63260) for x in [0, 41971, 46228, 50486, 54745, 59003, 63260, 67518, 71777, 76035, 80292, 84550, 88808, 93067, 97325, 101582, 105840, 110098, 114356, 118614, 122872, 127131, 131389, 135646, 139904, 144162, 148420, 152677, 156935, 161193, 165453, 169710, 173968, 178226,
                                            182484, 186741, 190999, 195257, 199515, 203774, 208031, 212290, 216548, 220806, 225063, 229321, 233579, 237837, 242095, 246353, 250611, 254869, 259127, 263385, 267643, 271901, 276158, 280417, 284675, 288933, 293190, 297448, 301706, 305965, 310223, 314480, 318739, 322997, 327255, 331512, 335770]]
    攻击次数3 = 1
    CD = 60

    def 等效百分比(self, 武器类型):
        return ((self.data0[self.等级] * self.攻击次数1)+(self.data1[self.等级] * self.攻击次数2)+(self.数据3[self.等级] * self.攻击次数3)) * self.倍率


class 技能21(职业主动技能):
    名称 = '月夜：终极行动'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    data0 = [int(x*1.0*32437/29533) for x in [0, 23975, 29533, 35093, 40653, 46213, 51771, 57331, 62891, 68450, 74009, 79568, 85128, 90687, 96247, 101806, 107366, 112924, 118485, 124044, 129603, 135162, 140722, 146282, 151841, 157400, 162959, 168520, 174078, 179638, 185197, 190757, 196316, 201875,
                                              207435, 212994, 218554, 224113, 229673, 235232, 240791, 246351, 251911, 257469, 263029, 268588, 274148, 279707, 285266, 290826, 296386, 301945, 307504, 313064, 318623, 324183, 329742, 335302, 340860, 346419, 351980, 357539, 363098, 368657, 374218, 379777, 385336, 390895, 396455, 402015, 407574]]
    攻击次数1 = 11
    data1 = [int(x*1.0*152919/139233) for x in [0, 113024, 139233, 165441, 191650, 217858, 244067, 270276, 296484, 322693, 348901, 375110, 401319, 427527, 453737, 479945, 506154, 532363, 558571, 584780, 610988, 637197, 663406, 689614, 715823, 742031, 768240, 794449, 820657, 846866, 873074, 899283, 925492, 951700, 977909, 1004117,
                                                1030326, 1056536, 1082744, 1108953, 1135161, 1161370, 1187579, 1213787, 1239996, 1266204, 1292414, 1318623, 1344831, 1371040, 1397248, 1423457, 1449666, 1475874, 1502083, 1528291, 1554500, 1580709, 1606917, 1633126, 1659334, 1685543, 1711752, 1737960, 1764169, 1790377, 1816586, 1842795, 1869003, 1895212, 1921421]]
    攻击次数2 = 1
    CD = 290

    def 等效百分比(self, 武器类型):
        return ((self.data0[self.等级] * self.攻击次数1)+(self.data1[self.等级] * self.攻击次数2)) * self.倍率

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

苍暮·特工一觉序号 = 0
苍暮·特工二觉序号 = 0
苍暮·特工三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        苍暮·特工一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        苍暮·特工二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        苍暮·特工三觉序号 = 技能序号[i.名称]

苍暮·特工护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        苍暮·特工护石选项.append(i.名称)

苍暮·特工符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        苍暮·特工符文选项.append(i.名称)


class 苍暮·特工角色属性(角色属性):

    实际名称 = '苍暮·特工'
    角色 = '枪剑士'
    职业 = '特工'

    武器选项 = ['小太刀']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 2.00

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 技能释放次数计算(self):
        技能释放次数 = []
        for i in self.技能栏:
            if i.名称 == '毁灭狂欢':
                if '/CD' in self.次数输入[self.技能序号[i.名称]]:
                    i.歼灭次数 += (int((self.时间输入 - i.演出时间) /
                                   i.等效CD(self.武器类型, self.类型) + 1 + i.基础释放次数))
                else:
                    i.歼灭次数 += (eval(self.次数输入[self.技能序号[i.名称]])+i.基础释放次数)
        for i in self.技能栏:
            if i.是否有伤害 == 1 and i.名称 != '月影秘步' and i.名称 != '锁定射击':
                if '/CD' in self.次数输入[self.技能序号[i.名称]]:
                    技能释放次数.append(int((self.时间输入 - i.演出时间) /
                                      i.等效CD(self.武器类型, self.类型) + 1 + i.基础释放次数))
                else:
                    技能释放次数.append(eval(self.次数输入[self.技能序号[i.名称]]))
            elif i.名称 == '月影秘步':
                if '/CD' in self.次数输入[self.技能序号[i.名称]]:
                    # 计算CD时间为技能释放完毕后
                    技能释放次数.append(int((self.时间输入 - i.演出时间) /
                                      (i.等效CD(self.武器类型, self.类型)+1) + 1 + i.基础释放次数)*3)
                else:
                    技能释放次数.append(eval(self.次数输入[self.技能序号[i.名称]]))
            elif i.名称 == '锁定射击':
                if '/CD' in self.次数输入[self.技能序号[i.名称]] and self.技能栏[self.技能序号['锁定射击']].锁定护石 == 1:
                    技能释放次数.append(int(int((self.时间输入 - i.演出时间)/i.等效CD(self.武器类型, self.类型) +
                                          1 + i.基础释放次数) * 12)+(int(self.技能栏[self.技能序号['毁灭狂欢']].歼灭次数 * 6)))
                elif '/CD' in self.次数输入[self.技能序号[i.名称]] and self.技能栏[self.技能序号['锁定射击']].锁定护石 == 0:
                    技能释放次数.append(
                        int((self.时间输入 - i.演出时间)/i.等效CD(self.武器类型, self.类型) + 1 + i.基础释放次数) * 12)
                else:
                    技能释放次数.append(eval(self.次数输入[self.技能序号[i.名称]]))
            else:
                技能释放次数.append(0)

        return self.技能释放次数解析(技能释放次数)


class 苍暮·特工(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 苍暮·特工角色属性()
        self.角色属性A = 苍暮·特工角色属性()
        self.角色属性B = 苍暮·特工角色属性()
        self.一觉序号 = 苍暮·特工一觉序号
        self.二觉序号 = 苍暮·特工二觉序号
        self.三觉序号 = 苍暮·特工三觉序号
        self.护石选项 = deepcopy(苍暮·特工护石选项)
        self.符文选项 = deepcopy(苍暮·特工符文选项)

    def 界面(self):
        super().界面()
        self.一觉减CD开关 = QCheckBox('一觉减CD Buff', self.main_frame2)
        self.一觉减CD开关.setChecked(False)
        self.一觉减CD开关.resize(120, 20)
        self.一觉减CD开关.move(325, 400)
        self.一觉减CD开关.setStyleSheet(复选框样式)
        self.职业存档.append(('一觉减CD开关', self.一觉减CD开关, 0))

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        if self.一觉减CD开关.isChecked():
            属性.技能栏[属性.技能序号['噬血绝杀']].一觉减CD = 0.1
