import random
import sys
import time
print("+---------------------------------------------------------------------+")
print("|                                                                     |")
print("|                         花有重开日, 人无再少年                          |")
print("|                                                                     |")
print("|                         欢迎来到, 人生重开模拟器                         |")
print("|                                                                     |")
print("+---------------------------------------------------------------------+")

# 设置初始属性
while True:
    print("请设定初始属性(可用总点数 20)")
    face = int(input("设定 颜值(1-10):"))
    strong = int(input("设定 体质(1-10):"))
    iq = int(input("设定 智力(1-10):"))
    home = int(input("设定 家境(1-10):"))
    if face < 1 or face > 10:
        print("颜值设置有误!")
        continue
    if strong < 1 or strong > 10:
        print("体质设置有误!")
        continue
    if iq < 1 or iq > 10:
        print("智力设置有误!")
        continue
    if home < 1 or home > 10:
        print("家境设置有误!")
        continue
    if face + strong + iq + home > 20:
        print("总点数超过了 20!")
        continue
    print("初始属性设定完成!")
    break

# 设置性别
point = random.randint(1, 6) # 掷色子
if point % 2 == 1:
    gender = 'boy'
    print("你是个男孩")
else:
    gender = 'girl'
    print("你是个女孩")

# 设置出生点
point = random.randint(1, 3) # 掷色子
if home == 10:
    print('你出生在帝都, 你的父母是高官政要')
    home += 1
    iq += 1
    face += 1
elif 7 <= home <= 9:
    if point == 1:
        print('你出生在大城市, 你的父母是公务员')
        face += 2
    elif point == 2:
        print('你出生在大城市, 你的父母是大企业高管')
        home += 2
    else:
        print('你出生在大城市, 你的父母是大学教授')
        iq += 2
elif 4 <= home <= 6:
    if point == 1:
        print('你出生在三线城市, 你的父母是教师')
        iq += 1
    elif point == 2:
        print('你出生在镇上, 你的父母是医生')
        strong += 1
    else:
        print("你出生在镇上, 你的父母是个体户")
        home += 1
else:
    if 1 <= point <= 2:
        print('你出生在村里, 你的父母是辛苦劳作的农民')
        strong += 1
        face -= 2
    elif 3 <= point <= 4:
        print('你出生在穷乡僻壤, 你的父母是无业游民')
        home -= 1
    else:
        print('你出生在镇上, 你父母感情不和')
        strong -= 1

# 针对每一岁, 生成人生经历
for age in range(1, 60):
    info = f'你今年 {age} 岁, '
    point = random.randint(1, 3)
    # 性别触发事件
    if gender == 'girl' and home <= 3 and point == 1:
        info += '你家里人重男轻女思想非常严重, 你被遗弃了!'
        print(info)
        print("游戏结束!")
        sys.exit(0)
    # 体质触发的事件
    elif strong < 6 and point != 3:
        info += '你生了一场病, '
        if home >= 5:
            info += '在父母的精心照料下恢复了健康'
            strong += 1
            home -= 1
        else:
            info += '你的父母没精力管你, 你的身体状况更糟糕了'
            strong -= 1
    # 颜值触发的事件
    elif face < 4 and age >= 7 and age <= 12:
        info += '你因为长的太丑, 别的小朋友不喜欢你, '
        if iq > 5:
            info += '你决定用学习填充自己'
            iq += 1
        else:
            if gender == 'boy':
                info += '你和别的小朋友经常打架'
                iq -= 1
                strong += 1
            else:
                info += '你经常被别的小朋友欺负'
                strong -= 1
    # 智商触发的事件
    elif iq < 5:
        info += '你看起来傻傻的, '
        if home >= 8 and age >= 6:
            info += '你的父母给你送到更好的学校学习'
        elif 4 <= home <= 7:
            if gender == 'boy':
                info += '你的父母鼓励你多运动, 加强身体素质'
                strong += 1
            else:
                info += '你的父母鼓励你多打扮自己'
                face += 1
        else:
            info += '你的父母为此经常吵架'
            if point == 1:
                strong -= 1
            elif point == 2:
                iq -= 1
    elif 18 <= age <= 35:  # 壮年时期的逻辑
        # 壮年时期的事件处理
        if point == 1:
            info += '你在事业上取得了巨大的成功, '
            if home >= 7:
                info += '你成为了公司的高级管理人员'
                iq += 2
                face += 1
            else:
                info += '你成功创业，成为了企业家'
                strong += 2
                home += 1
        elif point == 2:
            info += '你家庭生活幸福美满, '
            if gender == 'boy':
                info += '你有了一个可爱的儿子'
            else:
                info += '你有了一个漂亮的女儿'
            home += 2
        else:
            info += '你陷入了感情困扰, '
            if gender == 'boy':
                info += '你和妻子产生了矛盾，但最终化解了'
                iq -= 1
                strong -= 1
            else:
                info += '你和丈夫因为事业压力产生了分歧，但最终调解了'
                iq -= 1
                face -= 1

    elif age > 35:  # 老年时期的逻辑
        # 老年时期的事件处理
        if point == 1:
            info += '你健康状况良好, '
            if home >= 8:
                info += '你在退休后继续过上了充实的生活'
                iq += 1
                face += 1
            else:
                info += '你在退休后仍然坚持工作，为社会贡献力量'
                strong += 1
                iq += 1
        elif point == 2:
            info += '你的身体健康状况一般, '
            if home >= 6:
                info += '你享受着悠闲的退休生活'
                face += 1
            else:
                info += '你因为生活压力，偶有身体不适'
                strong -= 1
                iq -= 1
        else:
            info += '你的身体状况较差, '
            if home >= 5:
                info += '你在子女的陪伴下渡过了晚年'
                face += 1
            else:
                info += '你因为孤独感加剧，身体状况更加恶化'
                strong -= 25
    print('-------------------------------------------')
    print(info)
    print(f'strong={strong}, face={face}, iq={iq}, home={home}')
    time.sleep(1)