'''
水仙花数练习
'''
# num=100
# while num<1000:
#     num0=num%10
#     num1=num//100
#     num2=num%100//10
#     if num0**3+num1**3+num2**3 == num:
#         print(num)
#     num+=1

'''
质数练习
'''
# num=int(input('输入一个大于1的整数'))
# i=2
# flag=True
# while i<num:
#     if num % i == 0:
#         flag=False
#     i+=1

# if flag:
#     print('是质数')
# else:
#     print('不是质数')

'''
求100以内的质数
'''
# star_num=1234567
# end_num=12345678
# while star_num<=end_num:
#     flag=True
#     inner_start=2
#     while inner_start < star_num:
#         if star_num % inner_start == 0:
#             flag=False
#             break #break用来终止循环立即退出,包括else语句
#         inner_start+=1
#     if flag:
#         print('%d是质数'%star_num)
#     else:
#         print('%d不是质数'%star_num)
#         flag = True
#     star_num+=1
'''
break和continue只对离它最近的循环起作用，continue用于跳过它之后的语句，break用于跳出循环
'''
'''
引入time模块来计算程序运算时间,time()函数用于获取当前时间，返回的单位是秒
计算程序用时，并对程序进行优化
'''

from time import *
star_num=2
end_num=100000
st=time()
while star_num<=end_num:
    flag=True
    inner_start=2
    while inner_start <= star_num**0.5:
        if star_num % inner_start == 0:
            flag=False
            break #break用来终止循环立即退出,包括else语句
        inner_start+=1
    if flag:
        print('%d是质数'%star_num)
    flag = True
    star_num+=1
et=time()
print('执行花费%f'%(et-st))

