score=input('请输入你的分数：')
while score !='e':
    score =int(score)
    if score <60:
        print('D')
    elif 60 <= score < 80:
        print('C')
    elif 80 <= score < 90:
        print('B')
    elif 90 <= score < 100:
        print('A')
    elif score == 100:
        print('S')
    score=input('请输入你的分数：')
