for i in range(4):
    for j in range (4):
        if i+j<2:
            continue
        print('本次红球：',i,'个；黄球：',j,'个；绿球',8-i-j,'个。')
