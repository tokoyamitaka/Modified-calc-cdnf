# 武器融合属性部分


class 武器属性():
    固定属性描述 = ''
    随机属性描述 = ''
    当前值 = 0
    间隔 = 1

    def 融合属性(self, 属性):
        pass


class 武器属性A0(武器属性):
    固定属性描述 = '无'
    随机属性描述 = '无'
    最小值 = 0
    最大值 = 0


class 武器属性A1(武器属性):
    固定属性描述 = '黄字'
    随机属性描述 = 'BUFF力智+3%,一觉力智+'
    最小值 = 40
    最大值 = 60
    间隔 = 10

    def 融合属性(self, 属性):
        属性.BUFF力量per *= 1.03
        属性.BUFF智力per *= 1.03
        属性.一觉力智 += self.当前值


class 武器属性A2(武器属性):
    固定属性描述 = '爆伤'
    随机属性描述 = '一觉力智+3%,BUFF力智+'
    最小值 = 2
    最大值 = 4

    def 融合属性(self, 属性):
        属性.BUFF力量per *= 1 + self.当前值 / 100
        属性.BUFF智力per *= 1 + self.当前值 / 100
        属性.一觉力智per *= 1.03


class 武器属性A3(武器属性):
    固定属性描述 = '白字'
    随机属性描述 = '一觉力智+25,BUFF三攻+'
    最小值 = 2
    最大值 = 4

    def 融合属性(self, 属性):
        属性.BUFF物攻per *= 1 + self.当前值 / 100
        属性.BUFF魔攻per *= 1 + self.当前值 / 100
        属性.BUFF独立per *= 1 + self.当前值 / 100
        属性.一觉力智 += 25


class 武器属性A4(武器属性):
    固定属性描述 = '终伤'
    随机属性描述 = 'BUFF三攻+3%,一觉力智+'
    最小值 = 1
    最大值 = 3

    def 融合属性(self, 属性):
        属性.BUFF物攻per *= 1.03
        属性.BUFF魔攻per *= 1.03
        属性.BUFF独立per *= 1.03
        属性.一觉力智per *= 1 + self.当前值 / 100


class 武器属性A5(武器属性):
    固定属性描述 = '力智'
    随机属性描述 = '面板+'
    最小值 = 125
    最大值 = 185
    间隔 = 30

    def 融合属性(self, 属性):
        属性.守护恩赐体精 += self.当前值
        属性.转职被动智力 += self.当前值


class 武器属性A6(武器属性):
    固定属性描述 = '三攻'
    随机属性描述 = '一觉Lv+1,BUFF力智+'
    最小值 = 1
    最大值 = 3

    def 融合属性(self, 属性):
        属性.一觉Lv += 1
        属性.BUFF力量per *= 1 + self.当前值 / 100
        属性.BUFF智力per *= 1 + self.当前值 / 100


class 武器属性B0(武器属性):
    固定属性描述 = '无'
    随机属性描述 = '无'
    最小值 = 0
    最大值 = 0


class 武器属性B1(武器属性):
    固定属性描述 = '黄字'
    随机属性描述 = 'BUFF力智+3%,一觉力智 +'
    最小值 = 20
    最大值 = 40
    间隔 = 10

    def 融合属性(self, 属性):
        属性.BUFF力量per *= 1.03
        属性.BUFF智力per *= 1.03
        属性.一觉力智 += self.当前值


class 武器属性B2(武器属性):
    固定属性描述 = '爆伤'
    随机属性描述 = '一觉力智+2%,BUFF力智 +'
    最小值 = 2
    最大值 = 4

    def 融合属性(self, 属性):
        属性.BUFF力量per *= 1 + self.当前值 / 100
        属性.BUFF智力per *= 1 + self.当前值 / 100
        属性.一觉力智per *= 1.02


class 武器属性B3(武器属性):
    固定属性描述 = '白字'
    随机属性描述 = '一觉力智+25,BUFF三攻+'
    最小值 = 1
    最大值 = 3

    def 融合属性(self, 属性):
        属性.BUFF物攻per *= 1 + self.当前值 / 100
        属性.BUFF魔攻per *= 1 + self.当前值 / 100
        属性.BUFF独立per *= 1 + self.当前值 / 100
        属性.一觉力智 += 25


class 武器属性B4(武器属性):
    固定属性描述 = '终伤'
    随机属性描述 = 'BUFF三攻+2%,一觉力智+'
    最小值 = 1
    最大值 = 3

    def 融合属性(self, 属性):
        属性.BUFF物攻per *= 1.02
        属性.BUFF魔攻per *= 1.02
        属性.BUFF独立per *= 1.02
        属性.一觉力智per *= 1 + self.当前值 / 100


class 武器属性B5(武器属性):
    固定属性描述 = '力智'
    随机属性描述 = '面板+'
    最小值 = 85
    最大值 = 145
    间隔 = 30

    def 融合属性(self, 属性):
        属性.被动进图加成 += self.当前值


class 武器属性B6(武器属性):
    固定属性描述 = '三攻'
    随机属性描述 = 'BUFFLv+1,一觉力智+'
    最小值 = 10
    最大值 = 30
    间隔 = 10

    def 融合属性(self, 属性):
        属性.BUFFLv += 1
        属性.一觉力智 += self.当前值


武器属性A列表 = ()
武器属性B列表 = ()
for i in range(7):
    exec('武器属性A列表 += (武器属性A' + str(i) + '(),)')
    exec('武器属性B列表 += (武器属性B' + str(i) + '(),)')

武器属性A序号 = dict()
武器属性B序号 = dict()
for i in range(len(武器属性A列表)):
    武器属性A序号[武器属性A列表[i].固定属性描述] = i
for i in range(len(武器属性B列表)):
    武器属性B序号[武器属性B列表[i].固定属性描述] = i

武器属性组合 = ()
for i in range(1, 7):
    for j in range(1, 7):
        武器属性组合 += ([武器属性A序号[武器属性A列表[i].固定属性描述], 武器属性B序号[武器属性B列表[j].固定属性描述]], )
