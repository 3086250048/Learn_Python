'''
使用zip函数将序列合并
'''
lis0=[x for x in range(100) if x %2==0]
lis1=[x for x in range(100) if x%2!=0]
# print(list(zip(lis0,lis1)))
# for i,j in zip(lis0,lis1):
#     print(i,j)
'''
使用itertools 中的chain
'''
from itertools import chain
print(list(chain(lis0,lis1)))
for i in chain(lis0,lis1):
    print(i)

s=r'adas;dasdad|dasdad;asdiuwd\edawdawdawd'
lis3=list(map(lambda ss:ss.split('|'),s.split(';')))
print(lis3)
new_lis3=list(chain(*lis3))
print(new_lis3)