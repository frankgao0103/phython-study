
i=1
sum=0

while i <= 64:
    sum = sum + 2 ** (i-1)
    i = i + 1

print("舍罕王应该给达依尔", sum, "粒麦子！")
