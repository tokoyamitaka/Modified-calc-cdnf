##称号属性部分

称号列表 = [None] * 27


class 称号26():
    名称 = '(21)至尊·穿越星空的祈愿'

    def 城镇属性(self, 属性):
        属性.力量 += 100
        属性.智力 += 100
        属性.物理攻击力 += 65
        属性.魔法攻击力 += 65
        属性.独立攻击力 += 65
        属性.所有属性强化加成(22)
        属性.百分比三攻加成(0.12)
        属性.附加伤害加成(0.10)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +100<br>'
        temp += '智力 +100<br>'
        temp += '物理攻击力 +65<br>'
        temp += '魔法攻击力 +65<br>'
        temp += '独立攻击力 +65<br>'
        temp += '所有属性强化 +22<br>'
        temp += '百分比三攻 +12%<br>'
        temp += '附加伤害 +10%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号25():
    名称 = '(21)普通·永恒追猎'

    def 城镇属性(self, 属性):
        属性.力量 += 80
        属性.智力 += 80
        属性.物理攻击力 += 60
        属性.魔法攻击力 += 60
        属性.独立攻击力 += 60
        属性.所有属性强化加成(15)
        属性.伤害增加加成(0.15)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +80<br>'
        temp += '智力 +80<br>'
        temp += '物理攻击力 +60<br>'
        temp += '魔法攻击力 +60<br>'
        temp += '独立攻击力 +60<br>'
        temp += '所有属性强化 +15<br>'
        temp += '伤害增加 +15%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号24():
    名称 = '(21)普通·永恒判罪'

    def 城镇属性(self, 属性):
        属性.力量 += 80
        属性.智力 += 80
        属性.物理攻击力 += 60
        属性.魔法攻击力 += 60
        属性.独立攻击力 += 60
        属性.所有属性强化加成(15)
        属性.暴击伤害加成(0.15)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +80<br>'
        temp += '智力 +80<br>'
        temp += '物理攻击力 +60<br>'
        temp += '魔法攻击力 +60<br>'
        temp += '独立攻击力 +60<br>'
        temp += '所有属性强化 +15<br>'
        temp += '暴击伤害 +15%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号23():
    名称 = '(21)普通·永恒战吼'

    def 城镇属性(self, 属性):
        属性.力量 += 80
        属性.智力 += 80
        属性.物理攻击力 += 60
        属性.魔法攻击力 += 60
        属性.独立攻击力 += 60
        属性.所有属性强化加成(15)
        属性.百分比力智加成(0.15)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +80<br>'
        temp += '智力 +80<br>'
        temp += '物理攻击力 +60<br>'
        temp += '魔法攻击力 +60<br>'
        temp += '独立攻击力 +60<br>'
        temp += '所有属性强化 +15<br>'
        temp += '百分比力智 +15%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号22():
    名称 = '(20)至尊·伟大的意志'

    def 城镇属性(self, 属性):
        属性.力量 += 90
        属性.智力 += 90
        属性.物理攻击力 += 65
        属性.魔法攻击力 += 65
        属性.独立攻击力 += 65
        属性.所有属性强化加成(20)
        属性.暴击伤害加成(0.18)
        属性.百分比力智加成(0.04)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +90<br>'
        temp += '智力 +90<br>'
        temp += '物理攻击力 +65<br>'
        temp += '魔法攻击力 +65<br>'
        temp += '独立攻击力 +65<br>'
        temp += '所有属性强化 +20<br>'
        temp += '暴击伤害 +18%<br>'
        temp += '百分比力智 +4%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号21():
    名称 = '(20)普通·使徒降临'

    def 城镇属性(self, 属性):
        属性.力量 += 80
        属性.智力 += 80
        属性.物理攻击力 += 60
        属性.魔法攻击力 += 60
        属性.独立攻击力 += 60
        属性.所有属性强化加成(15)
        属性.附加伤害加成(0.12)
        属性.百分比力智加成(0.03)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +80<br>'
        temp += '智力 +80<br>'
        temp += '物理攻击力 +60<br>'
        temp += '魔法攻击力 +60<br>'
        temp += '独立攻击力 +60<br>'
        temp += '所有属性强化 +15<br>'
        temp += '附加伤害 +12%<br>'
        temp += '百分比力智 +3%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号20():
    名称 = '(20)国庆·安徒恩的烈焰'

    def 城镇属性(self, 属性):
        属性.力量 += 60
        属性.智力 += 60
        属性.所有属性强化加成(15)
        属性.黄字 = max(属性.黄字, 0.15)

    def 触发属性(self, 属性):
        属性.进图属强 += 10

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +60<br>'
        temp += '智力 +60<br>'
        temp += '所有属性强化 +15<br>'
        temp += '黄字 +15%（取最高值）<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '所有属强 +10<br>'
        return temp


class 称号19():
    名称 = '(20)国庆·卢克的创造'

    def 城镇属性(self, 属性):
        属性.力量 += 60
        属性.智力 += 60
        属性.所有属性强化加成(15)
        属性.爆伤 = max(属性.爆伤, 0.15)

    def 触发属性(self, 属性):
        属性.进图属强 += 10

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +60<br>'
        temp += '智力 +60<br>'
        temp += '所有属性强化 +15<br>'
        temp += '爆伤 +15%（取最高值）<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '所有属强 +10<br>'
        return temp


class 称号18():
    名称 = '(20)国庆·伊希斯的天空'

    def 城镇属性(self, 属性):
        属性.力量 += 60
        属性.智力 += 60
        属性.所有属性强化加成(15)
        属性.百分比三攻加成(0.15)

    def 触发属性(self, 属性):
        属性.进图属强 += 10

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +60<br>'
        temp += '智力 +60<br>'
        temp += '所有属性强化 +15<br>'
        temp += '百分比三攻 +15%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '所有属强 +10<br>'
        return temp


class 称号17():
    名称 = '(20)国庆·希洛克的悲鸣'

    def 城镇属性(self, 属性):
        属性.力量 += 60
        属性.智力 += 60
        属性.所有属性强化加成(15)
        属性.最终伤害加成(0.15)

    def 触发属性(self, 属性):
        属性.进图属强 += 10

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +60<br>'
        temp += '智力 +60<br>'
        temp += '所有属性强化 +15<br>'
        temp += '最终伤害 +15%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '所有属强 +10<br>'
        return temp


class 称号16():
    名称 = '(19)至尊·神选之英杰'

    def 城镇属性(self, 属性):
        属性.力量 += 75
        属性.智力 += 75
        属性.物理攻击力 += 45
        属性.魔法攻击力 += 45
        属性.独立攻击力 += 65
        属性.所有属性强化加成(20)
        属性.暴击伤害加成(0.18)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +75<br>'
        temp += '智力 +75<br>'
        temp += '物理攻击力 +45<br>'
        temp += '魔法攻击力 +45<br>'
        temp += '独立攻击力 +65<br>'
        temp += '所有属性强化 +20<br>'
        temp += '暴击伤害 +18%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号15():
    名称 = '(19)普通·秘境迷踪'

    def 城镇属性(self, 属性):
        属性.力量 += 70
        属性.智力 += 70
        属性.物理攻击力 += 40
        属性.魔法攻击力 += 40
        属性.独立攻击力 += 60
        属性.所有属性强化加成(15)
        属性.附加伤害加成(0.10)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +70<br>'
        temp += '智力 +70<br>'
        temp += '物理攻击力 +40<br>'
        temp += '魔法攻击力 +40<br>'
        temp += '独立攻击力 +60<br>'
        temp += '所有属性强化 +15<br>'
        temp += '附加伤害 +10%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号14():
    名称 = '(19)国庆·超越极限者'

    def 城镇属性(self, 属性):
        属性.力量 += 60
        属性.智力 += 60
        属性.所有属性强化加成(15)
        属性.爆伤 = max(属性.爆伤, 0.15)

    def 触发属性(self, 属性):
        属性.进图属强 += 10

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +60<br>'
        temp += '智力 +60<br>'
        temp += '所有属性强化 +15<br>'
        temp += '爆伤 +15%（取最高值）<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '所有属强 +10<br>'
        return temp


class 称号13():
    名称 = '(18)至尊·天选之人'

    def 城镇属性(self, 属性):
        属性.力量 += 75
        属性.智力 += 75
        属性.物理攻击力 += 35
        属性.魔法攻击力 += 35
        属性.独立攻击力 += 55
        属性.所有属性强化加成(20)
        属性.最终伤害加成(0.12)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +75<br>'
        temp += '智力 +75<br>'
        temp += '物理攻击力 +35<br>'
        temp += '魔法攻击力 +35<br>'
        temp += '独立攻击力 +55<br>'
        temp += '所有属性强化 +20<br>'
        temp += '最终伤害 +12%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号12():
    名称 = '(18)普通·兽人守护神'

    def 城镇属性(self, 属性):
        属性.力量 += 70
        属性.智力 += 70
        属性.物理攻击力 += 30
        属性.魔法攻击力 += 30
        属性.独立攻击力 += 50
        属性.所有属性强化加成(15)
        属性.附加伤害加成(0.10)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +70<br>'
        temp += '智力 +70<br>'
        temp += '物理攻击力 +30<br>'
        temp += '魔法攻击力 +30<br>'
        temp += '独立攻击力 +50<br>'
        temp += '所有属性强化 +15<br>'
        temp += '附加伤害 +10%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号11():
    名称 = '(18)国庆·神之试炼'

    def 城镇属性(self, 属性):
        属性.力量 += 55
        属性.智力 += 55
        属性.所有属性强化加成(15)
        属性.爆伤 = max(属性.爆伤, 0.15)

    def 触发属性(self, 属性):
        属性.进图属强 += 10

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +55<br>'
        temp += '智力 +55<br>'
        temp += '所有属性强化 +15<br>'
        temp += '爆伤 +15%（取最高值）<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '所有属强 +10<br>'
        return temp


class 称号10():
    名称 = '(17)至尊·龙之威仪'

    def 城镇属性(self, 属性):
        属性.力量 += 65
        属性.智力 += 65
        属性.物理攻击力 += 35
        属性.魔法攻击力 += 35
        属性.独立攻击力 += 55
        属性.所有属性强化加成(15)
        属性.附加伤害加成(0.12)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +65<br>'
        temp += '智力 +65<br>'
        temp += '物理攻击力 +35<br>'
        temp += '魔法攻击力 +35<br>'
        temp += '独立攻击力 +55<br>'
        temp += '所有属性强化 +15<br>'
        temp += '附加伤害 +12%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号9():
    名称 = '(17)普通·龙之挑战'

    def 城镇属性(self, 属性):
        属性.力量 += 60
        属性.智力 += 60
        属性.物理攻击力 += 30
        属性.魔法攻击力 += 30
        属性.独立攻击力 += 50
        属性.所有属性强化加成(15)
        属性.附加伤害加成(0.10)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +60<br>'
        temp += '智力 +60<br>'
        temp += '物理攻击力 +30<br>'
        temp += '魔法攻击力 +30<br>'
        temp += '独立攻击力 +50<br>'
        temp += '所有属性强化 +15<br>'
        temp += '附加伤害 +10%<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号8():
    名称 = '(17)国庆·海洋霸主'

    def 城镇属性(self, 属性):
        属性.力量 += 55
        属性.智力 += 55
        属性.所有属性强化加成(15)
        属性.黄字 = max(属性.黄字, 0.10)

    def 触发属性(self, 属性):
        属性.进图属强 += 10

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +55<br>'
        temp += '智力 +55<br>'
        temp += '所有属性强化 +15<br>'
        temp += '黄字 +10%（取最高值）<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '所有属强 +10<br>'
        return temp


class 称号7():
    名称 = '(16)至尊·桃园结义[义]'

    def 城镇属性(self, 属性):
        属性.力量 += 60
        属性.智力 += 60
        属性.物理攻击力 += 30
        属性.魔法攻击力 += 30
        属性.独立攻击力 += 50
        属性.所有属性强化加成(15)
        属性.黄字 = max(属性.黄字, 0.15)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +60<br>'
        temp += '智力 +60<br>'
        temp += '物理攻击力 +30<br>'
        temp += '魔法攻击力 +30<br>'
        temp += '独立攻击力 +50<br>'
        temp += '所有属性强化 +15<br>'
        temp += '黄字 +15%（取最高值）<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号6():
    名称 = '(16)普通·三英雄[义]'

    def 城镇属性(self, 属性):
        属性.力量 += 55
        属性.智力 += 55
        属性.物理攻击力 += 30
        属性.魔法攻击力 += 30
        属性.独立攻击力 += 50
        属性.所有属性强化加成(15)
        属性.黄字 = max(属性.黄字, 0.12)

    def 触发属性(self, 属性):
        属性.进图力量 += 35
        属性.进图智力 += 35

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +55<br>'
        temp += '智力 +55<br>'
        temp += '物理攻击力 +30<br>'
        temp += '魔法攻击力 +30<br>'
        temp += '独立攻击力 +50<br>'
        temp += '所有属性强化 +15<br>'
        temp += '黄字 +12%（取最高值）<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        return temp


class 称号5():
    名称 = '(16)国庆·骑士王荣耀'

    def 城镇属性(self, 属性):
        属性.力量 += 55
        属性.智力 += 55
        属性.所有属性强化加成(15)
        属性.黄字 = max(属性.黄字, 0.10)

    def 触发属性(self, 属性):
        属性.进图属强 += 10

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +55<br>'
        temp += '智力 +55<br>'
        temp += '所有属性强化 +15<br>'
        temp += '黄字 +10%（取最高值）<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '所有属强 +10<br>'
        return temp


class 称号4():
    名称 = '(16)五一·荣耀贵族'

    def 城镇属性(self, 属性):
        属性.力量 += 30
        属性.智力 += 30
        属性.物理攻击力 += 70
        属性.魔法攻击力 += 70
        属性.独立攻击力 += 90
        属性.加算冷却缩减 += 0.10

    def 触发属性(self, 属性):
        pass

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +30<br>'
        temp += '智力 +30<br>'
        temp += '物理攻击力 +70<br>'
        temp += '魔法攻击力 +70<br>'
        temp += '独立攻击力 +90<br>'
        temp += '技能冷却 -10%(加算)<br>'
        return temp


class 称号3():
    名称 = '(15)国庆·圣殿之巅'

    def 城镇属性(self, 属性):
        属性.物理攻击力 += 30
        属性.魔法攻击力 += 30
        属性.独立攻击力 += 50
        属性.所有属性强化加成(15)
        属性.爆伤 = max(属性.爆伤, 0.10)

    def 触发属性(self, 属性):
        pass

    def 装备描述(self, 属性):
        temp = ''
        temp += '物理攻击力 +30<br>'
        temp += '魔法攻击力 +30<br>'
        temp += '独立攻击力 +50<br>'
        temp += '所有属性强化 +15<br>'
        temp += '爆伤 +10%（取最高值）<br>'
        return temp


class 称号2():
    名称 = '(14)五一·明日-春华'

    def 城镇属性(self, 属性):
        属性.力量 += 35
        属性.智力 += 35
        属性.物理攻击力 += 10
        属性.魔法攻击力 += 10
        属性.独立攻击力 += 18
        属性.所有属性强化加成(12)

    def 触发属性(self, 属性):
        属性.加算冷却缩减 += 0.30
        pass

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +35<br>'
        temp += '智力 +35<br>'
        temp += '物理攻击力 +10<br>'
        temp += '魔法攻击力 +10<br>'
        temp += '独立攻击力 +18<br>'
        temp += '所有属性强化 +12<br>'
        temp += '<font color="#00A2E8">进图触发属性：</font><br>'
        temp += '技能冷却 -30%(加算)<br>'
        return temp


class 称号1():
    名称 = '(20)DPL专属称号·输出'

    def 城镇属性(self, 属性):
        属性.力量 += 1251
        属性.智力 += 1251
        属性.物理攻击力 += 377
        属性.魔法攻击力 += 377
        属性.独立攻击力 += 380
        属性.所有属性强化加成(166)
        属性.技能等级加成('主动', 1, 30, 2)
        属性.技能等级加成('主动', 1, 50, 2)
        属性.技能等级加成('所有', 1, 50, 2)

    def 触发属性(self, 属性):
        pass

    def 装备描述(self, 属性):
        temp = ''
        temp += '力量 +1251<br>'
        temp += '智力 +1251<br>'
        temp += '物理攻击力 +377<br>'
        temp += '魔法攻击力 +377<br>'
        temp += '独立攻击力 +380<br>'
        temp += '所有属性强化 +166<br>'
        temp += 'Lv1-30 (主动)技能等级+2<br>'
        temp += 'Lv1-50 (主动)技能等级+2<br>'
        temp += 'Lv1-50 (所有)技能等级+2<br>'
        return temp


class 称号0():
    名称 = '无'

    def 城镇属性(self, 属性):
        pass

    def 触发属性(self, 属性):
        pass

    def 装备描述(self, 属性):
        temp = ''
        return temp


for i in range(len(称号列表)):
    exec('称号列表[{}] = 称号{}()'.format(len(称号列表) - i - 1, i))

称号序号 = dict()
for i in range(len(称号列表)):
    称号序号[称号列表[i].名称] = i
