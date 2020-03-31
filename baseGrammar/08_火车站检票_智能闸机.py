
have_ticket = True
knif_length = 10
ticket_number = 'G6987'
ticket_time = '2020-03-30 12:30:00'
GATE_NUMBER = 'G6987'
TIMER = '2020-03-30 12:30:00'

if have_ticket:
    print('欢迎进站，即将开始安检……')
    if knif_length >=20:
        print('抱歉，您携带的刀具已超过 20 厘米，安检不通过，不允许进站！')
    else:
        print('您好，安检通过，欢迎进如候车室……')
        if ticket_number == GATE_NUMBER and ticket_time == TIMER:
            print('欢迎乘车，请到16站台排队候车！')
        else:
            print('你的车票有误，无法通行')
else:
    print('您好，请先购买车票，谢谢！')