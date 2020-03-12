# 导入随机模块 #
import random
# 接收用户输入并将数值赋值给 counts 变量 #
counts=int(input('请输入抛硬币的次数：'))
i = 0
j,k=0,0

print("开始抛硬币实验：")
while i < counts:
    # 生成一个随机数num #
    num=random.randint(0,99)
    if num % 2:
        # 打印结果 #
        print('正面',end=' ')
        j+=1
    else:
        # 打印结果 #
        print('反面',end=' ')
        k+=1

    i = i + 1

print('\n本次实验一共投掷硬币',i,'次！')
print('其中正面次数',j,'次,反面次数',k,'次！')
