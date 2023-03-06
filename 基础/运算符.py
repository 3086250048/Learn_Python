'''
+|+=(两个字符串进行加法则会进行拼串操作)  
-|-=   
*|*=(如果将字符串和数字相乘，则将字符串重复指定次数) 
 /|/=(除数不能为0)
 //|//=(整除只会保留整数位)
 ** | **= (幂次，**0.5就是开方) 
 % | %= (取余数)
''' 
# num0=8
# num0 /=2
# print(num0)
# num1=9
# num1 //= 4
# print(num1)
# num2=9
# num2%=8
# print(num2)
# num3=9
# num3**=0.5
# print(num3)

'''
关系运算符
> >= <= == !=
1.>|>=|<= 比较符不支持整数和字符串的比较   
2.在python中对两个字符串进行> | >= | <= 的比较，实际上比较的是unicode编码
3.字符串比较会逐位进行比较，例如'2'>'12'由于2的unicode编码已经大于'1'
所以不再和之后的'2'比较。
4.==和!= 比较的是对象的 value(值)，而不是id
5.is is not 比较的是对象的id
'''
# result= 10>20
# print(result)
# i0=100
# i1='100'
# result=i0>=i1#TypeError: '>=' not supported between instances of 'int' and 'str'
# print(result)
# r1=1
# r2=True
# print(r1 is r2)

'''
逻辑运算符
not and or ^(异或)
1.not 对于非布尔值，非运算会先将其转换为布尔值，然后取反
2.python中and是短路的，如果第一个值为false则不看第二个值。
3.python中or是短路的，如果第一个值为true则不看第二个值。
4.当我们对非布尔值进行运算的时候，python会当成布尔值运算，并返回原值
    当进行and运算时，找的是false
        1.第一个值是false则直接返回第一个值
        2.第一个值是true则直接返回第二个值
    当进行or运算时，找的是true
        1.第一个值是true，则直接返回第一个值
        2.第一个值是false，则返回第二个值。
    
'''
# print(0b110011 ^ 0b110010 )
True and print('你好')
res1=1 or 0
print(res1)