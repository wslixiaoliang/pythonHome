import random

print('\033[1;32;48m')
print('*' * 50)
compuer = random.randint(1, 3)


print()
player = int(input('请输入你所出的拳：【1 石头，2 剪刀，3 布】：'))
print()

print('玩家出的拳头是：%d ,电脑出的拳头是：%d' % (player, compuer))
print()

if (player == 1 and compuer == 2) or (player == 2 and compuer == 3) or (player == 3 and compuer == 1):
    print('玩家胜，电脑太菜了')
    print()

elif(player == compuer):
    print('哈哈！太默契了，你和电脑平局了！')
    print()

else:
    print('电脑胜，玩家继续加油！')
    print('*' * 50)
    print('\033[0m')


