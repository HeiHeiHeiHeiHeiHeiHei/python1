# coding=utf-8
import os
from io import StringIO, BytesIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

f = StringIO('hello!\nHi!\nWorld!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f = BytesIO()
f.write('中文'.encode('UTF-8'))
print(f.getvalue())


print(os.name)
print(os.environ)
