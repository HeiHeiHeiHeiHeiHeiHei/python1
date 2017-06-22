# coding=utf-8
# try:
#     f = open('E:\\PYTHON\\python1\\baike\\spider\\output.txt', 'r',encoding='UTF-8')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# from io import open
#
# with open('E:\\PYTHON\\python1\\baike\\spider\\output.txt','r',encoding='UTF-8') as f:
#     for line in f.readlines():
#         print(line.strip())

# try:
#     f = open('E:\\PYTHON\\python1\\baike\\spider\\output.txt', 'rb')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#
# try:
#     f=open('E:\\1.txt','w')
#     f.write('hello world')
# finally:
#     if f:
#         f.close()

with open('E:\\1.txt','w') as f:
    f.write('中国')

