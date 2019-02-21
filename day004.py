# a=2.0
# b=1.0
# s=0
# for n in range(1,21):
#     s=s+a/b
#     t=a
#     a=a+b
#     b=t
# print(s)

# a=2.0
# b=1.0
# s=0
# for i in range(1,21):
#     s = s + a / b
#     t=a
#     a=a+b
#     b=t
# print(s)

#二 输入一个数求1！+2！+3！+4！+n！=？
# import math
# num=int(input("请输入一个数字"))
# sum=0
# f=1
# for i in range(1,num+1):
#     f=f*i
#     sum+=f
# print("阶乘之和为",sum)

# import math
# num=int(input("请随机输入一个数"))
# sum=0
# f=1
# for i in range(1,num+1):
#     f*=i
#     sum+=f
# print("阶乘之和为",sum)

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i!=j)and(i!=k)and(j!=k):
#                 print(i,k,j)

#编写一个八维月考成绩转换函数,输入的成绩是同学在月考中获得的标准成绩,成绩范围0~100。输出的成绩是ABCDE五档
# num=int(input("请输入同学的成绩"))
# # 100——90输出A
# if num>90 and num<100:
#     print("A")
# # 89——80输出B
# elif num>80 and num<89:
#     print("B")
# # 79——70输出C
# elif num>70 and num<79:
#     print("C")
# # 69——60输出D
# elif num>60 and num<69:
#     print("D")
# # 60分以下的输出E
# elif num>0 and num<60:
#     print("E")
# elif num>100 or num<0 :
#     print("输入的成绩有误，请重新输入")

# a=[]
# for i in range(100,201):
#     b=0
#     for x in range(100,201):
#         if i%x==0:
#             b+=1
#         if b==0:
#             a.append(i)
# print(a)
# print(len(a))

# a=[]
# for i in range(100,201):
#     b=0
#     for x in range(100,201):
#         if i%x==0:
#             b+=1
#         if b==0:
#             a.append(i)
# print(a)
# print(len(a))

# a=2.0
# b=1.0
# s=0
# for i in range(1,21):
#     s=s+a/b
#     t=a
#     a=a+b
#     b=t
# print(s)

# sum=0
# num=int(input("请随机输入一个数"))
# f=1
# for i in range(1,num+1):
#         f*=i
#         sum+=f
# print(sum)

# for i in range(1,5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i!=j)and(i!=k)and(k!=j):
#                 print(i,j,k)

# a=[]
# for i in range(100,201):
#     b=0
#     for x in range(100, 201):
#         if i%x==0:
#             b=b+1
#         if b ==0:
#             a.append(i)
# print(a)
# print(len(a))

#生成一个包含50个随机整数的列表
# 随机整数的范围是从-10到10
# 然后将列表中所有的正数存为一个新的子列表
# 负数存为另一个新的子列表

import random
i=0
j=0
list=[]
list1=[]
list2=[]
for i in range(0,51):
    b = random.randint(-10, 10)
    list.append(b)
print("list",list)
for i in list:
    if i > 0 :
        list1.append(i)
print("list1",list1)


