'''
元组 tuple
元组是一个不可变的序列
它的操作方式和列表基本一致，唯一的区别就是元组的元素不可变
'''
tup0=()
print(type(tup0))
tup1=(1,2,3,4)
print(tup1[0])
#使用元组快速赋值
a,b,c,d=tup1
print(f'{a}{b}{c}{d}')
#当元组不是空元组则括号可以省略
tup2=10,20,30
print(tup2)
#python中可以利用上面这个特性，交换数值的值
a0=100
a1=200
a0,a1=a1,a0#后面的这个a1,a0 等同于(a1,a0)
#如果元组中的值个数多于变量的个数则会报错，此时可以用*x将多余的数值都已列表的方式赋值给某一个变量
#一个赋值表达式中只能出现一个*x的变量,且以下用法可以对所有序列使用
a0,*b0=100,200,300
*a1,b1=1,2,3
a3,*b3,c3=100,'你好','世界',200
print('b0=',b0)
print('a1=',a1)
print('b3=',b3)
print(f'a0={a0},a1={a1}')
#当元组中只有一个元素可以写成以下两种方式
tup3=100,
tup4=(100,)
print(f'{type(tup3)}     {type(tup4)}')