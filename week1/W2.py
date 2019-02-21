# import random
# list=[]
# list1=[]
# list2=[]
# #生成一个包含50个随机数的整数列表 随机整数范围-10到10
# for i in range(50):
#     n=random.randint(-10,11)
#     list.append(n)
# print(list)
# for j in list:
#     if j>0 :
#         list1.append(j)
#     elif j<0:
#         list2.append(j)
# print(list1)
# print(list2)

#第二遍
# import random
# list=[]
# list1=[]
# list2=[]
# for i in range(50):
#     n=random.randint(-10,11)
#     list.append(n)
# print(list)
# for j in list:
#     if j > 0:
#         list1.append(j)
#     elif j<0:
#         list2.append(j)
# print(list1)
# print(list2)

import random
list=[]
list1=[]
list2=[]
for i in range(50):
    n=random.randint(-10,11)
    list.append(n)
print(list)
for j in list:
    if j > 0:
        list1.append(j)
    elif j < 0:
        list2.append(j)
print(list1)
print(list2)