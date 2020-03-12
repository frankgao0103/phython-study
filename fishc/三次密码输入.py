x=3
j='FishC.com'
i=input('请输入密码：')
while x>0:
    if '*' in i:
        print('密码中不能含有“*”号！您还有',x,'次机会！',end=' ')
        i=input('请输入密码：')
        continue
    elif i == j:
        print('密码正确，进入程序……')
        break
    else:
        x -= 1
        print('密码输入错误！您还有',x,'次机会！',end=' ')
        i=input('请输入密码：')
    
