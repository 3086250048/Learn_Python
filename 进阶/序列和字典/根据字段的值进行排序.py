'''
如何根据字段的值进行排序
解决方案：
    -将字典转换为元组
        -使用列表解析
        -使用zip
    -元组比较大小时，根据索引依次比较
    -将字典的的key和value位置对调，使比较时先比较value

'''

from random import randint
dir0={'student%d'%i:randint(50,100) for i in range(0,21)}

#方式1.使用列表解析
lis_tuple=[(v,k) for k,v in dir0.items()]
#sorted不会改变原有列表，而是返回一个新的列表
new_list_tuple=sorted(lis_tuple,reverse=True)
print(new_list_tuple)


#方式2.使用zip
#zip会将每个序列的内的相对于索引的数值组合成元组，最终返回一个生成器对象
print(list(zip([1,2,3],[4,5,6])))
new_list_tuple=sorted(list(zip(dir0.values(),dir0.keys())),reverse=True)
print(new_list_tuple)

#方式3:使用sorted()中的key关键字
new_list_tuple=sorted(dir0.items(),key=lambda item:item[1],reverse=True)
print(new_list_tuple)



'''
使用enumerate()函数生成位次索引,返回一个生成器对象
    参数
        -序列
        -起始值
'''                    
lis0=list(enumerate(new_list_tuple,1))
print(lis0)
#替换原始列表中的items,新item以key=姓名,value=(排名,分数)的方式显示
#方式1
for i,(k,v) in lis0:
    dir0[k]=(i,v)
print(dir0)
#方式2
new_dir0={k:(i,v) for i,(k,v) in lis0}
print(new_dir0)

