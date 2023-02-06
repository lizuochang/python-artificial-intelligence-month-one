"""
    str 编码
    练习:exercise01.py
"""

name = "悟空"
name = "孙悟空"
print(name) # 不是将字符串"悟空" 改变为"孙悟空"
#而是创建了新字符串对象"孙悟空",替换变量name中存储的地址.

# 字符 -->  编码值
# print("天的Unicode码是："+str(ord("天"))
print("天的Unicode码是："+str(ord("天")))

# 编码值 --> 字符
print("22825的字符是:"+chr(22825))















