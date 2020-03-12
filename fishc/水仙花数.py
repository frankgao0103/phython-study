#如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
#例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。

for i in range(1,9):
    for j in range(10):
        for k in range(10):
            if 100*i+10*j+k == i**3+j**3+k**3:
                print(100*i+10*j+k,'是水仙花数')
    
