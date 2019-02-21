# phone = input("请输入手机号：")
# list=[183,159,152,139,138,135]
# try:
#     int (phone)
#     if len(phone==11):
#         head = phone[0:3]
#         bool=False
#         for i in list:
#             if(int(head)==(i)):
#                 bool=True
#                 break
#             if(bool):
#                 print("有效的手机号")
#             else:
#                 print("无效的手机号")
#     else:
#         print("输入的手机号无效")
# except ValueErroy:
#     print("输入的手机号不是有效的")


#第二遍
# phone=input("请输入手机号")
# list=[135,136,137,139,152,183]
# try:
#     int(phone)
#     if (len(phone)==11):
#         head=phone[0:3]
#         bool=False
#         for i in list:
#             if (int(head)==(i)):
#                 bool=True
#                 break
#         if (bool):
#             print("手机号有效")
#         else:
#             print("手机号无效")
#     else:
#         print("输入的手机号有效")
# except ValueError :
#     print("输入的不是有效的手机号")


#第三遍
p=input("请输入手机号：")
list=[135,138,139,183,152,188]
try:
    int(p)
    if (len(p)==11):
        h=p[0:3]
        b=False
        for i in list:
            if (int(h)==(i)):
                b=True
                break
        if (b):
            print("手机号有效")
        else:
            print("手机号无效")
except ValueError:
    print("输入手机号有误 请重新操作")

