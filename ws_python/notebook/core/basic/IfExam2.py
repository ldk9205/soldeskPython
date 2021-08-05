#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

fname = sys.argv[0]   # Python 파일명
su = int(sys.argv[1]) # 전달되는 데이터, 인수, 정수형으로 변환

if su % 60:
    print(su,'은(는) 2, 3, 4, 5의 배수가 아님')
else:
    print(su,'은(는) 2, 3, 4, 5의 배수가 맞음')
    
print()

for x in range(2,6):
    if su % x:
        print(x, '의 배수가 아님')
    else:
        print(x, '의 배수가 맞음')

