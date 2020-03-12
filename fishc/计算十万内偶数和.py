i = 0
s = 0
j = 1000000
while i <= j:
    if i % 2 == 0:
        s=s+i
    i = i + 1
print(j,'以内所有偶数的和是',s)
