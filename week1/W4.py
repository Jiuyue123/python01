# import random
# str='abcde'
# str1=''
# #随机生成一个包含1000个字母的字符串
# for i in range(1000):
#     str1+=random.choice(str)
#print("字符串长度",len(str1))
#
# dict={}
# for i in str1:
#     key = dict.get(i)
#     if(key==None):
#         dict[i]=1
#     else:
#         dict[i]+=1
# print(dict)

# import random
# str='abcde'
# str1=''
# for i in range(1000):
#     str1+=random.choice(str)
#     print("字符串长度",len(str1))
#
# dict={}
# for i in str1:
#     key = dict.get(i)
#     if(key==None):
#         dict[i]=1
#     else:
#         dict[i]+=1
# print(dict)

import random
str='abcde'
str1=''
for i in range(1000):
    str1+=random.choice(str)
    print("字符串长度",len(str1))
dict={}
for i in str1:
    key = dict.get(i)
    if(key==None):
        dict[i]=1
    else:
        dict[i]+=1
print(dict)