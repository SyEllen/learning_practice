import random
player_score=0
competitor_score=0
print('''
*********石头剪刀布**********
*****************************
''')
player_name=input('请输入用户名：')
print('请选择对弈角色：1. 布丁😻； 2．糖糖🍬；３.毛球🐶')
yourChose = input('您的选择是：')

if yourChose == '' :
    competitor_name='绝世高手🎅'
    print('系统自动为您匹配绝世高手')
else:
    choice=eval(yourChose)
    if choice==1:
        competitor_name='布丁😻'
    elif choice==2:
        competitor_name='糖糖🍬'
    elif choice==3:
        competitor_name='毛球🐶'
    else:
        competitor_name='绝世高手🎅'
        print('系统自动为您匹配绝世高手')
    
print(player_name,'VS',competitor_name,'对战开始')

# 三局两胜
i=0
while i<3 and player_score < 2 and competitor_score < 2:
    #玩家出拳
    player_choice=eval(input('-----------玩家请出拳：1.石头；2.剪刀；3.布-------------'))
    if player_choice==1:
        player_hand='石头👊'
    elif player_choice==2:
        player_hand='剪刀✌'
    elif player_choice==3:
        player_hand='布🖐'
    else:
        print('别墨迹，快点出拳👻')
        continue

# 电脑出拳：
    computer_choice=random.randint(1,3)
    if computer_choice==1:
        computer_hand='石头👊'
    elif computer_choice==2:
        computer_hand='剪刀✌'
    else: 
        computer_hand='布🖐'
    print(player_name,'出',player_hand)
    print(competitor_name,'出',computer_hand)

# 计算对弈结果 
    if player_choice==computer_choice:
        print('平局')
    else:
        i+=1
        if(player_choice==1 and computer_choice==2) or (player_choice==2 and computer_choice==3) or (player_choice==3 and computer_choice==1):
            print(player_name,'胜')
            player_score+=1
        else:
            print(competitor_name,'胜')
            competitor_score+=1
    print('-------------------当前得分--------------------')
    print(player_name,player_score)
    print(competitor_name,competitor_score)
    

# 战局汇总
print('**************战局**************')
if player_score==competitor_score:
    print('平局👬')
elif player_score>competitor_score:
    print('哦哦，赢啦！🎉')
else:
    print('不服再战🤸️')
    

    