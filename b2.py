list1 = [128, 2, 4, 16, 2, 128, 64, 4, 8, 7, 32, 16, 64]
a = 0
list2 = []
print("Có các cặp số phân biệt sau có tích là 256:")
for i in list1:
    a += 1
    for j in range(a,len(list1)):
        b = list1[j]
        if i * b == 256:
            if i not in list2:
                if b not in list2:              
                    print(i,"và",b,"tại vị trí",a,"và",j+1)
                    list2.append(i)
                    list2.append(b)
