# import random
# list=[]
# for i in range(20):
#     n=random.choice(range(10))
#     list.append(n)
# print(len(list))
# print(list)
# list[::2]=sorted(list[::2],reverse=True)
# print("排序list",list)

# import random
# list=[]
# for i in range(20):
#     n=random.choice(range(10))
#     list.append(n)
# print(list)
# list[::2]=sorted(list[::2],reverse=True)
# print("排序list",list)

import random
list=[]
for i in  range(20):
    n=random.choice(range(10))
    list.append(n)
print(list)
list[::2]=sorted(list[::2],reverse=True)
print(list)