
# break 跳出整个循环体，停止循环；
i = 0
while i <= 10:
    i = i + 1
    if i == 6:
        break
    print('变量 i 的值是： %d' % i)
    print('=========== i game over ==============')

# continue 跳出当前循环，继续执行后面的循环；
print('\033[1;32;48m')
j = 0

while j <= 10:
    j = j+1
    if j == 5:
        continue
    print('变量 i 的值是： %d' % j)
    print('=========== j game over ==============')
print('\033[0m')

