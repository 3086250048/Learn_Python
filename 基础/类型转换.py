#类型转换不是改变对象本身的类型，而是根据当前对象的值转换为新的对象
#int()\float()\str()\bool(),将对象转化为指定的类型，并将其作为返回值返回

#---------int()----------
#   布尔值:true=1,false=0
#   浮点数:直接取整省略小数点
#   字符串:合法的整数字符串直接转换为对应的数字，如果不是一个合法的整数字符串则报错 
#   ValueError: invalid literal for int() with base 10: 'd123'
#   对于其他不可以转换为整型的对象，则直接抛出ValueError异常
# i0='d123'
# print(type(i0))
# str0=int(i0)
# print(type(i0))

#---------------float()-------------------------
#      布尔值:true=1.0,false=1.0
#      字符串:合法的小数字符串直接转换为对应的数字，如果不是一个合法的小数字符串则报错 
#      对于其他不可以转换为小数的对象，则直接抛出ValueError异常
# f0='1'
# f0=float(f0)
# print(f0)


#----------------str()-----------------------------
# str0=123
# str0=str(str0)
# print(type(str0))
# str1=None
# str1=str(str1)
# print(type(str1)) #结果为none字符

#----------------------bool()--------------------
#规则:所有表示为空性质的对象都会转换为false，其余的转换为true
# b0=0\''\none
# b0=bool(b0)
# print(b0)#以上表示空的对象转换为布尔值后都为false
