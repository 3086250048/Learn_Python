'''
利用http://httpbin.org/API 对发送的http请求进行观测

'''
str0='''
{
    "sites": [
    { "name":"菜鸟教程" , "url":"www.runoob.com" }, 
    { "name":"google" , "url":"www.google.com" }, 
    { "name":"微博" , "url":"www.weibo.com" }
    ]
}
'''
import json
#loads解析字符串中的json
str1=json.loads(str0)
print(str1)
print(str1['sites'])