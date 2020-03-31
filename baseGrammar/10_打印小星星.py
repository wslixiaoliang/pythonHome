

# while 循环的使用案例
# 需求：根据行号 打印相同数量的小星星
print('\033[1;32;48m')
row = 1

while row < 100:
    print('*' * row)
    row  = row + 1
print('\033[0m')