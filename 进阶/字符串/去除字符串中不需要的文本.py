'去除左右两边的字符串:strip()、lstrip()、rstrip(),都会返回一个新的字符串'
str0='== =======czz@qq.com======-**  ===='
#去除字符串两边的 空串、*、-、= 
str00=str0.strip('= -*')
print(str00)

str1='    a  b  c   '
#将字符串中的空格替换为空串
str10=str1.replace(' ','')
print(str10)
#
import re
str2=' \n \t *a && b () c0--9-3'
#将列表中出现的字符都替换为''
str20=re.sub('[\n\t*&()-093 ]+','',str2)
print(str20)
