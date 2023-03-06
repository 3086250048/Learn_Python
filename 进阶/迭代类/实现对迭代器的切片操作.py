from os import getcwd,chdir
from itertools import islice
import re
chdir(r'C:\Users\30862\Desktop\Python\进阶\迭代类')
print(getcwd())
with open('test.txt','r',encoding='utf-8') as file_obj:
    for i in islice(file_obj,0,21,2):
        print(i)
l=list(range(10))
print(l)
#等价于l[3]
print(l.__getitem__(3))
#等价于1[0:4:2]
print(l.__getitem__(slice(0,4,2)))
'''
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
'''
def my_slice(iterable,start,end,step):
    tmp=0
    for i,x in enumerate(iterable):
        if i >=end:break
        if i>=start:
            if tmp==0:
                tmp=step
                yield x
            tmp-=1
print(list(my_slice(range(100,150),10,140,2)))
