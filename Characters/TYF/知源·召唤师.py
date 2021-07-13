from PublicReference.base import *


class 知源·召唤师主动技能(主动技能):
    秒伤基础 = 0
    秒伤成长 = 0
    秒伤倍率 = 1
    # def 等效CD(self, 武器类型):
    #     if 武器类型 == '法杖':
    #         return round(self.CD / self.恢复 * 1.10, 1)
    #     if 武器类型 == '魔杖':
    #         return round(self.CD / self.恢复 * 1.00, 1)

    def 秒伤百分比(self):
        if self.等级 == 0:
            return 0
        else:
            return int((self.秒伤基础 + self.秒伤成长 * self.等级) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.秒伤倍率)


class 知源·召唤师技能0(被动技能):
    名称 = '召唤兽强化'
    所在等级 = 15
    等级上限 = 30
    基础等级 = 20
    关联技能 = ['契约召唤：桑德尔', '契约召唤：袄索', '精灵召唤：亡魂默克尔', '精灵召唤：极光格雷林', '精灵召唤：火焰赫瑞克', '精灵召唤：冰影阿奎利斯', '契约召唤：路易斯', '精灵召唤：伊伽贝拉',
            '契约召唤：牛头王库鲁塔', '契约召唤：征服者卡西利亚斯', '咒令：愤怒咆哮', '传说召唤：逆月者拉莫斯', '咒令：逆月之蚀', '必杀剑千鬼杀', '至高精灵王', '传说召唤：月蚀之影', '黑月之噬', '魔月·德拉里昂']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00+0.02*self.等级, 3)


class 知源·召唤师技能1(被动技能):
    名称 = '心灵感应'
    所在等级 = 15
    等级上限 = 16
    基础等级 = 6

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03+0.02*self.等级, 3)


class 知源·召唤师技能2(知源·召唤师主动技能):
    名称 = '精灵献祭'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1903.9803*1.05 + 380.9019*8*1.05 + 1921.9019*1.05 + 1903.9803*1.05
    成长 = 215.0196*1.05 + 43.0980*8*1.05 + 215.0196*1.05 + 215.0196*1.05
    CD = 20.0
    演出时间 = 2
    TP成长 = 0.05
    TP上限 = 5


class 知源·召唤师技能3(知源·召唤师主动技能):
    名称 = '契约召唤：桑德尔'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 1880.6458*1.0646
    成长 = 212.3541*1.0646
    秒伤基础 = 238.125 *1.0646+ 332.4583/1.5*1.0646
    秒伤成长 = 26.875*1.0646 + 37.5416/1.5*1.0646
    秒伤倍率 = (20 - 3.501361 * 2) / (20 - 1.65 * 2)
    CD = 12
    演出时间 = 1.65
    TP成长 = 0.10
    TP上限 = 5


class 知源·召唤师技能4(知源·召唤师主动技能):
    名称 = '契约召唤：袄索'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 3099.189189*1.0646
    成长 = 349.81081*1.0646
    秒伤基础 = 83.56756*1.0646 + 211.1351*6/4*1.0646
    秒伤成长 = 9.4324*1.0646 + 23.8648*6/4*1.0646
    秒伤倍率 = 0.932241021
    CD = 15
    演出时间 = 1.53
    TP成长 = 0.10
    TP上限 = 5


class 知源·召唤师技能5(知源·召唤师主动技能):
    名称 = '精灵召唤：亡魂默克尔'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 360.3555*6*1.0646
    成长 = 40.6444*6*1.0646
    秒伤基础 = 107.8222*1.0646 + 163.5111/1.5 *1.0646+ 102.4222*4/7*1.0646
    秒伤成长 = 12.1778 *1.0646+ 18.4888/1.5*1.0646 + 11.5778*4/7*1.0646
    秒伤倍率 = (20 - 1.5013323 * 2) / (20 - 0.67 * 2)
    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.67


class 知源·召唤师技能6(知源·召唤师主动技能):
    名称 = '精灵召唤：极光格雷林'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2160.1778*1.0646
    成长 = 243.8222*1.0646
    秒伤基础 = 23.333*3*1.0646 + 102.3777/2*5*1.0646
    秒伤成长 = 2.666*3 *1.0646+ 11.6222/2*5*1.0646
    秒伤倍率 = (20 - 2.09 * 2) / (20 - 1 * 0.7)
    CD = 15
    演出时间 = 0.7
    TP成长 = 0.10
    TP上限 = 5


class 知源·召唤师技能7(知源·召唤师主动技能):
    名称 = '精灵召唤：火焰赫瑞克'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 432.2444*1.0646 + 647.8444*1.0646 + 863.4444*1.0646 + 70.9333*3*1.0646
    成长 = 48.7555*1.0646 + 73.1555*1.0646 + 97.5666*1.0646 + 8.0666*3*1.0646
    秒伤基础 = 179.6666*1.0646 + 204.9111/1.5*1.0646 + 50.2/1.5*1.0646
    秒伤成长 = 20.3333*1.0646 + 23.0888/1.5*1.0646 + 5.8/1.5*1.0646
    秒伤倍率 = (20 - 1.65899 * 2) / (20 - 1 * 1.1)
    CD = 15
    演出时间 = 1.1
    TP成长 = 0.10
    TP上限 = 5


class 知源·召唤师技能8(知源·召唤师主动技能):
    名称 = '精灵召唤：冰影阿奎利斯'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 304.888*7*1.0646
    成长 = 32.5111*7*1.0646
    秒伤基础 = 22.3777*3 *1.0646+ 208.4888/2*1.0646 + 231.8888/5*3*1.0646
    秒伤成长 = 2.622*3*1.0646 + 23.5111/2 *1.0646+ 26.1111/5*3*1.0646
    秒伤倍率 = (20 - 1.98 * 2) / (20 - 1 * 0.817)
    CD = 15
    演出时间 = 0.817
    TP成长 = 0.10
    TP上限 = 5


class 知源·召唤师技能9(知源·召唤师主动技能):
    名称 = '契约召唤：路易斯'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 661.4047*1.0646 + 2647.6904*1.0646
    成长 = 74.5952*1.0646 + 298.3095*1.0646
    秒伤基础 = 165.3571*1.0646 + 109.5714/5*10*1.0646 + 174.2380/1.5*1.0646 + 228.1666/1.5*1.0646
    秒伤成长 = 18.6428 *1.0646+ 12.4285/5*10 *1.0646+ 19.7619/1.5*1.0646 + 25.8333/1.5*1.0646
    秒伤倍率 = (20 - 9.22) / (20 - 0.6)
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.6
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.2779
            self.成长 *= 1.2779

        elif x == 1:
            self.基础 *= 1.3123
            self.成长 *= 1.3123


class 知源·召唤师技能10(知源·召唤师主动技能):
    名称 = '精灵召唤：伊伽贝拉'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 555.2820*1.3*8*1.0646
    成长 = 62.7179*1.3*8*1.0646
    秒伤基础 = 82.5641*1.3/0.6*1.0646 + 190.3846*1.3/3.1*3*1.0646 + 415.9230*1.3/5*3*1.0646 + 646.1025*1.3*4/9.3*1.0646
    秒伤成长 = 9.4358*1.3/0.6 *1.0646+ 21.6153*1.3/3.1*3*1.0646 + 26.0769*1.3/5*3*1.0646 + 72.8974*1.3*4/9.3*1.0646
    秒伤倍率 = (20 - 7.7) / (20 - 1.7)
    CD = 31
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 1.7+1.0
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.秒伤基础 *= 0.5618*1.15*2
            self.秒伤成长 *= 0.5618*1.15*2
            self.基础 *= 1.15
            self.成长 *= 1.15

        elif x == 1:
            self.秒伤基础 *= 0.6069*1.15*2
            self.秒伤成长 *= 0.6069*1.15*2
            self.基础 *= 1.15
            self.成长 *= 1.15


class 知源·召唤师技能11(知源·召唤师主动技能):
    名称 = '束缚印记'
    所在等级 = 45
    等级上限 = 11
    基础等级 = 1
    基础 = 14368.5714*1.052
    成长 = 1622.4285*1.052
    CD = 25


class 知源·召唤师技能12(知源·召唤师主动技能):
    名称 = '契约召唤：牛头王库鲁塔'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 1568.918*1.06469 + 2195.0540*1.06469 + 2823.2432*1.06469
    成长 = 177.0810*1.06469 + 247.9459*1.06469 + 318.7567*1.06469
    秒伤基础 = 403.4594 *1.0646+ 651.4594/2 *1.0646+ 1283.1351/3*1.0646
    秒伤成长 = 45.5404 *1.0646+ 73.5405/2 *1.0646+ 144.8648/3*1.0646
    秒伤倍率 = (20 - 6.8505) / (20 - 1.83)
    CD = 40
    演出时间 = 1.83
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.秒伤基础 *= 1.23
            self.秒伤成长 *= 1.23
            self.基础 *= 1.23
            self.成长 *= 1.23

        elif x == 1:
            self.秒伤基础 *= 1.31
            self.秒伤成长 *= 1.31
            self.基础 *= 1.31
            self.成长 *= 1.31


class 知源·召唤师技能13(被动技能):
    名称 = '强击光环'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['精灵召唤：亡魂默克尔', '精灵召唤：极光格雷林', '精灵召唤：火焰赫瑞克', '精灵召唤：冰影阿奎利斯']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.15


class 知源·召唤师技能14(被动技能):
    名称 = '灵魂支配'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105+0.015*self.等级, 3)


class 知源·召唤师技能15(知源·召唤师主动技能):
    名称 = '契约召唤：征服者卡西利亚斯'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    秒伤基础 = 229.8*1.1426*1.06467 + 516.2666*1.1426/2*1.06467 + 1100.6666*1.1426/2*1.06467
    秒伤成长 = 69.2*1.1426*1.06467 + 155.7333*1.1426/1.9 *1.06467+ 332.3333*1.1426/2*1.06467
    秒伤倍率 = 0.77
    演出时间 = 0
    CD = 145


class 知源·召唤师技能16(知源·召唤师主动技能):
    名称 = '必杀剑千鬼杀'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 6190.6875*1.1426*1.06467 + 3714.4375*1.1426*5*1.06467
    成长 = 1869.3125*1.1426*1.06467+ 1121.5625*1.1426*5*1.06467
    CD = 145
    演出时间 = 3.47  # 9.1


class 知源·召唤师技能17(知源·召唤师主动技能):
    名称 = '精灵召唤：融合精灵海伊轮'
    所在等级 = 60
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    自定义描述 = 1

    def 技能描述(self, 武器类型):
        return '所有属性强化+' + str(self.属强加成())

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        else:
            return (2 + 2*self.等级)


class 知源·召唤师技能18(知源·召唤师主动技能):
    名称 = '咒令：愤怒咆哮'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 3945.5*4*1.051 + 10522*1.051
    成长 = 445.5*4*1.051 + 1188*1.051
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 2.3
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.124

        elif x == 1:
            self.倍率 *= 1.204


class 知源·召唤师技能19(被动技能):
    名称 = '蚀月附灵'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22+0.02*self.等级, 3)


class 知源·召唤师技能20(知源·召唤师主动技能):
    名称 = '黑月之噬'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 32819.33333*1.054
    成长 = 3705.66667*1.054
    CD = 35.3
    是否有护石 = 1
    是否带护石 = 0
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.18
        self.CD *= 0.90
        self.是否带护石 = 1


class 知源·召唤师技能21(知源·召唤师主动技能):
    名称 = '传说召唤：月蚀之影'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 3828.583333*1.05
    成长 = 432.416667*1.05
    攻击次数 = 15.0
    演出时间 = 3
    CD = 43
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.32
        self.演出时间 = 1.3


class 知源·召唤师技能22(知源·召唤师主动技能):
    名称 = '传说召唤：逆月者拉莫斯'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 1992.4*1.15*3*1.0646
    成长 = 601.6*1.15*3*1.0646
    秒伤基础 = 717.6*1.15/3*2*1.0646 + 192.4*1.15/3*1.0646 + 335*1.15 /3*1.0646 + 430*1.15/3*1.0646 + 238.8*1.15/6 *1.0646+ 837.4*1.15/6*1.0646
    秒伤成长 = 216.4*1.15/3*2*1.0646 + 57.6*1.15/3 *1.0646+ 101*1.15 /3*1.0646 + 130*1.15/3*1.0646 + 72.2*1.15/6*1.0646 + 252.6*1.15/6*1.0646
    演出时间 = 1.55
    额外演出时间 = 0
    秒伤倍率 = (20 - 4.500625 * 2) / (20 - 1.55 * 2)
    CD = 10


class 知源·召唤师技能23(知源·召唤师主动技能):
    名称 = '咒令：逆月之蚀'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 4782.4*1.15*1.0646 + 1912.5*1.15*5*1.0646 + 2733.2*1.15*8*1.0646 + 14346*1.15*1.0646
    成长 = 1443.7*1.15*1.0646 + 577.7*1.15*5 *1.0646+ 824.9*1.15*8*1.0646 + 4332*1.15*1.0646
    演出时间 = 5.25
    CD = 180


class 知源·召唤师技能24(被动技能):
    名称 = '魔法秀'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    是否主动 = 1
    关联技能 = ['无']
    冷却关联技能 = ['咒令：愤怒咆哮', '精灵献祭', '咒令：逆月之蚀']

    魔法秀数值 = [0, 22, 43, 65, 86, 108, 130, 151, 173, 194, 216,
             238, 259, 281, 302, 324, 324, 324, 324, 324, 324]

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 - 0.001*self.魔法秀数值[self.等级], 3)


class 知源·召唤师技能25(知源·召唤师主动技能):
    名称 = '鞭挞'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 32
    基础 = 30.5612*1.05 + 46.8388*1.05
    成长 = 113.7419*1.05 + 170.5806*1.05
    CD = 3
    TP成长 = 0.05
    TP上限 = 5


class 知源·召唤师技能26(知源·召唤师主动技能):
    名称 = '魔力印记'
    备注 = '(秒伤)'
    所在等级 = 25
    等级上限 = 11
    基础等级 = 1
    基础 = 322*1.0522
    成长 = 61*1.0522
    攻击次数 = 2
    演出时间 = 1

    def 等效CD(self, 武器类型, 输出类型):
        return 1


class 知源·召唤师技能27(知源·召唤师主动技能):
    名称 = '驱散魔法'
    所在等级 = 10
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    数据 = [0, 11, 15, 20, 25, 30, 35, 41, 47, 53, 60,
          67, 74, 82, 90, 98, 106, 115, 124, 133, 143]
    自定义描述 = 1

    def 技能描述(self, 武器类型):
        return '智力+' + str(self.智力加成())

    def 智力加成(self):
        return self.数据[self.等级] * 4


class 知源·召唤师技能28(知源·召唤师主动技能):
    名称 = '至高精灵王'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 2162*1.3*1.1844
    成长 = 244*1.3*1.1844
    攻击次数 = 9.0
    基础2 = 29185.8*1.3*1.1844
    成长2 = 3295.2*1.3*1.1844
    攻击次数2 = 1.0
    CD = 58
    演出时间 = 2.3


class 知源·召唤师技能29(被动技能):
    名称 = '逆月'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18+0.02*self.等级, 3)


class 知源·召唤师技能30(知源·召唤师主动技能):
    名称 = '魔月·德拉里昂'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 28837*1.1823 + 67288*1.1823 + 96125*1.1823
    成长 = 8706*1.1823 + 20313 *1.1823+ 29019*1.1823
    CD = 290
    演出时间 = 5.7
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0


class 知源·召唤师技能31(被动技能):
    名称 = '绝对支配'
    所在等级 = 10
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['契约召唤：桑德尔', '契约召唤：袄索', '精灵召唤：亡魂默克尔', '精灵召唤：极光格雷林', '精灵召唤：火焰赫瑞克', '精灵召唤：冰影阿奎利斯', '契约召唤：路易斯',
            '精灵召唤：伊伽贝拉', '契约召唤：牛头王库鲁塔', '契约召唤：征服者卡西利亚斯', '咒令：愤怒咆哮', '传说召唤：逆月者拉莫斯', '咒令：逆月之蚀', '必杀剑千鬼杀', '至高精灵王']

    def 加成倍率(self, 武器类型):
        return 1.045 if self.等级 > 0 else 1.0


知源·召唤师技能列表 = []
i = 0
while i >= 0:
    try:
        exec('知源·召唤师技能列表.append(知源·召唤师技能'+str(i)+'())')
        i += 1
    except:
        i = -1

知源·召唤师技能序号 = dict()
for i in range(len(知源·召唤师技能列表)):
    知源·召唤师技能序号[知源·召唤师技能列表[i].名称] = i

知源·召唤师一觉序号 = 0
知源·召唤师二觉序号 = 0
知源·召唤师三觉序号 = 0
for i in 知源·召唤师技能列表:
    if i.所在等级 == 50:
        知源·召唤师一觉序号 = 知源·召唤师技能序号[i.名称]
    if i.所在等级 == 85:
        知源·召唤师二觉序号 = 知源·召唤师技能序号[i.名称]
    if i.所在等级 == 100:
        知源·召唤师三觉序号 = 知源·召唤师技能序号[i.名称]

知源·召唤师护石选项 = ['无']
for i in 知源·召唤师技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        知源·召唤师护石选项.append(i.名称)

知源·召唤师符文选项 = ['无']
for i in 知源·召唤师技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        知源·召唤师符文选项.append(i.名称)


class 知源·召唤师角色属性(角色属性):

    实际名称 = '知源·召唤师'
    角色 = '魔法师(女)'
    职业 = '召唤师'

    武器选项 = ['法杖', '魔杖']

    类型选择 = ['魔法百分比']

    类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.790

    远古记忆 = 0
    秒伤比率 = 1
    觉醒选择状态 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(知源·召唤师技能列表)
        self.技能序号 = deepcopy(知源·召唤师技能序号)

    def 数据计算(self, x=0, y=-1):
        if self.技能栏[self.技能序号['黑月之噬']].是否带护石 == 0:
            self.技能栏[self.技能序号['黑月之噬']].基础 = 0
            self.技能栏[self.技能序号['黑月之噬']].成长 = 0

        self.预处理()
        # 初步计算
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算(y)
        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        # 召唤物秒伤
        for i in self.技能栏:
            if self.技能切装[self.技能序号[i.名称]] != y:
                if i.是否有伤害 == 1 and i.是否主动 == 1:
                    if i.名称 == '传说召唤：逆月者拉莫斯':
                        技能总伤害[self.技能序号[i.名称]] += self.秒伤比率 * i.秒伤百分比() * (self.时间输入 + i.额外演出时间 - i.演出时间 * 技能释放次数[self.技能序号[i.名称]]) * \
                            self.伤害指数 * i.被动倍率 * \
                            (1 + self.白兔子技能 * 0.20 + self.年宠技能 * 0.10 *
                             (10 / (self.时间输入 % 50)) + self.斗神之吼秘药 * 0.12)
                    else:
                        技能总伤害[self.技能序号[i.名称]] += self.秒伤比率 * i.秒伤百分比() * (self.时间输入 - i.演出时间 * 技能释放次数[self.技能序号[i.名称]]) * \
                            self.伤害指数 * i.被动倍率 * \
                            (1+self.白兔子技能*0.20+self.年宠技能*0.10 *
                             (10 / (self.时间输入 % 50))+self.斗神之吼秘药*0.12)

        # 返回结果
        return self.数据返回(x, 技能释放次数, 技能总伤害)

    def 伤害指数计算(self):
        self.所有属性强化(self.技能栏[self.技能序号['精灵召唤：融合精灵海伊轮']].属强加成())
        self.进图智力 += self.技能栏[self.技能序号['驱散魔法']].智力加成()
        if self.觉醒选择状态 == 2:
            self.技能栏[self.技能序号['传说召唤：逆月者拉莫斯']].额外演出时间 += 2.25
            self.技能栏[self.技能序号['契约召唤：征服者卡西利亚斯']].演出时间 += 2.97
        elif self.觉醒选择状态 == 1:
            self.技能栏[self.技能序号['契约召唤：征服者卡西利亚斯']].演出时间 -= 0
        super().伤害指数计算()


class 知源·召唤师(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 知源·召唤师角色属性()
        self.角色属性A = 知源·召唤师角色属性()
        self.角色属性B = 知源·召唤师角色属性()
        self.一觉序号 = 知源·召唤师一觉序号
        self.二觉序号 = 知源·召唤师二觉序号
        self.三觉序号 = 知源·召唤师三觉序号
        self.护石选项 = deepcopy(知源·召唤师护石选项)
        self.符文选项 = deepcopy(知源·召唤师符文选项)

    def 界面(self):
        super().界面()

        self.秒伤比率 = MyQComboBox(self.main_frame2)
        for i in range(9):
            self.秒伤比率.addItem('AI期望：' + str(80 + i * 5) + '%')
        self.秒伤比率.setCurrentIndex(4)
        self.秒伤比率.resize(120, 20)
        self.秒伤比率.move(325, 480)
        self.秒伤比率.setToolTip(
            'AI期望为各召唤兽各技能百分比/CD总和\n\n各召唤兽AI输出时间单独计算\n\n时间输入 - 附灵演出时间 * 附灵次数')

        self.职业存档.append(('秒伤比率', self.秒伤比率, 1))

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        属性.秒伤比率 = 0.8 + self.秒伤比率.currentIndex() * 0.05
        属性.觉醒选择状态 = self.觉醒选择状态
