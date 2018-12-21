a = input("Nhập vào một dãy số, cách nhau bởi dấu ' ':")
b = ""
list1 = []
# Lọc và bỏ từng số vào list1
for i in a:
    if i != " ":
        b += i
    else:
        list1.append(int(b))
        b = ""
list1.append(int(b)) # Lấy số cuối cùng vào list
# In dãy số:
for i in range(len(list1)):
    print(list1[len(list1)-1-i])
