'''
    递归的是一种解决问题的方式，它和循环很像
    它的整体思想是将一个大问题分解为一个个小的问题，直到问题无法分解，再去解决问题

    递归函数的两个要件
    1.基线条件
        -问题被分解为最小的问题，当满足基线条件时，递归就不再执行了
    2.递归条件
        -将问题分解的条件
'''
def factorial(n):
    '''
        该函数用于求任意数的阶乘

    '''
    #基线条件
    if n==1:
        return 1
    #递归条件
    return n*factorial(n-1)

# print(factorial(900))
    
'''
求任意数n的i次幂
'''
def power(n,i):
    if i==1:return n 
    return n * power(n,i-1)
print(power(2,999))

'''
判断一个字符串是否是回文字符串,如果是则返回true，否则返回false
'''

def hui_wen(s):
    #基线条件
    if len(s)<=1:return True
    #递归条件，如果第一个和最后一个字符相等则and找false进行递归
    return s[0] == s[-1]  and  hui_wen(s[1:-1])


print(hui_wen('a11a1a'))