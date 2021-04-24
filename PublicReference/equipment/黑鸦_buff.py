# 黑鸦变换属性部分


class 变换属性():
    固定属性描述 = ''
    随机属性描述 = ''
    索引 = ["伤害词条", "黄字", "爆伤", "白字", "终伤", "力智", "三攻"]
    当前值 = 0
    间隔 = 1

    def 变换属性(self, 属性):
        pass


class 武器变换属性0(变换属性):
    固定属性描述 = '无'
    随机属性描述 = '无'
    最小值 = 0
    最大值 = 0


class 武器变换属性1(变换属性):
    固定属性描述 = '黄字'
    随机属性描述 = 'BUFF力智+3%,一觉力智+'
    最小值 = 30
    最大值 = 60
    间隔 = 10

    def 变换属性(self, 属性):
        属性.BUFF力量per *= 1.03
        属性.BUFF智力per *= 1.03
        属性.一觉力智 += self.当前值


class 武器变换属性2(变换属性):
    固定属性描述 = '爆伤'
    随机属性描述 = '一觉力智+3%,BUFF力智+'
    最小值 = 2
    最大值 = 5

    def 变换属性(self, 属性):
        属性.BUFF力量per *= 1 + self.当前值 / 100
        属性.BUFF智力per *= 1 + self.当前值 / 100
        属性.一觉力智per *= 1.03


class 武器变换属性3(变换属性):
    固定属性描述 = '白字'
    随机属性描述 = '一觉力智+30,BUFF三攻+'
    最小值 = 1
    最大值 = 4

    def 变换属性(self, 属性):
        属性.BUFF物攻per *= 1 + self.当前值 / 100
        属性.BUFF魔攻per *= 1 + self.当前值 / 100
        属性.BUFF独立per *= 1 + self.当前值 / 100
        属性.一觉力智 += 30


class 武器变换属性4(变换属性):
    固定属性描述 = '终伤'
    随机属性描述 = 'BUFF三攻+2%,一觉力智+'
    最小值 = 2
    最大值 = 5

    def 变换属性(self, 属性):
        属性.BUFF物攻per *= 1.02
        属性.BUFF魔攻per *= 1.02
        属性.BUFF独立per *= 1.02
        属性.一觉力智per *= 1 + self.当前值 / 100


class 武器变换属性5(变换属性):
    固定属性描述 = '力智'
    随机属性描述 = '面板+'
    最小值 = 120
    最大值 = 180
    间隔 = 20

    def 变换属性(self, 属性):
        # 属性.被动进图加成 += self.当前值
        属性.守护恩赐体精 += self.当前值
        属性.转职被动智力 += self.当前值


class 武器变换属性6(变换属性):
    固定属性描述 = '三攻'
    随机属性描述 = '一觉Lv+1,BUFF力智+'
    最小值 = 1
    最大值 = 4

    def 变换属性(self, 属性):
        属性.一觉Lv += 1
        属性.BUFF力量per *= 1 + self.当前值 / 100
        属性.BUFF智力per *= 1 + self.当前值 / 100


class 装备变换属性0(变换属性):
    固定属性描述 = '无'
    随机属性描述 = '无'
    最小值 = 0
    最大值 = 0


class 装备变换属性1(变换属性):
    固定属性描述 = '黄字'
    随机属性描述 = 'BUFF力智+4%,一觉力智+'
    最小值 = 10
    最大值 = 40
    间隔 = 10

    def 变换属性(self, 属性):
        属性.BUFF力量per *= 1.04
        属性.BUFF智力per *= 1.04
        属性.一觉力智 += self.当前值


class 装备变换属性2(变换属性):
    固定属性描述 = '爆伤'
    随机属性描述 = '一觉力智+2%,BUFF力智+'
    最小值 = 2
    最大值 = 5

    def 变换属性(self, 属性):
        属性.BUFF力量per *= 1 + self.当前值 / 100
        属性.BUFF智力per *= 1 + self.当前值 / 100
        属性.一觉力智per *= 1.02


class 装备变换属性3(变换属性):
    固定属性描述 = '白字'
    随机属性描述 = '一觉力智+25,BUFF三攻+'
    最小值 = 1
    最大值 = 4

    def 变换属性(self, 属性):
        属性.BUFF物攻per *= 1 + self.当前值 / 100
        属性.BUFF魔攻per *= 1 + self.当前值 / 100
        属性.BUFF独立per *= 1 + self.当前值 / 100
        属性.一觉力智 += 25


class 装备变换属性4(变换属性):
    固定属性描述 = '终伤'
    随机属性描述 = 'BUFF三攻 +2%,一觉力智+'
    最小值 = 1
    最大值 = 4

    def 变换属性(self, 属性):
        属性.BUFF物攻per *= 1.02
        属性.BUFF魔攻per *= 1.02
        属性.BUFF独立per *= 1.02
        属性.一觉力智per *= 1 + self.当前值 / 100


class 装备变换属性5(变换属性):
    固定属性描述 = '力智'
    随机属性描述 = '面板+'
    最小值 = 100
    最大值 = 160
    间隔 = 20

    def 变换属性(self, 属性):
        # 属性.被动进图加成 += self.当前值
        属性.守护恩赐体精 += self.当前值
        属性.转职被动智力 += self.当前值


class 装备变换属性6(变换属性):
    固定属性描述 = '三攻'
    随机属性描述 = 'BUFFLv+1,一觉力智+'
    最小值 = 10
    最大值 = 40
    间隔 = 10

    def 变换属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉力智 += self.当前值


武器变换属性列表 = []
装备变换属性列表 = []
for i in range(7):
    exec('武器变换属性列表.append(武器变换属性' + str(i) + '())')
    exec('装备变换属性列表.append(装备变换属性' + str(i) + '())')

武器变换属性序号 = dict()
装备变换属性序号 = dict()
for i in range(len(武器变换属性列表)):
    武器变换属性序号[武器变换属性列表[i].固定属性描述] = i
for i in range(len(装备变换属性列表)):
    装备变换属性序号[装备变换属性列表[i].固定属性描述] = i

防具变换属性组合 = []
# for i in range(7):
for j in range(1, 7):
    for k in range(1, 7):
        for l in range(1, 7):
            防具变换属性组合.append([j, k, l])
