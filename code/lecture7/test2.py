# while循环
i = 0
while i < 5:
    print(i)
    i = i + 1

# break
j = 0
while True:
    if(j > 10):break
    print(j)
    j = j + 1

# continue
k = 0
while k < 10:
    if (k % 2 == 1):
        k = k + 1
        continue
    print(k)
    k = k + 1