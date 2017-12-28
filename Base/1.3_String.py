# 字符串用(' ')(" ")
a = 'this is a string'
b = "this is also a string"

# 转义字符( \ )
c = 'No, she doesn\'t'
print(c)

# 反斜杠可以作为续行符,表示下一行是上一行的延续
# 还可以使用"""......""" 或 '''......'''跨越多行

d = '123456\
789'
print(d)
e = '''
321
654
987
'''
print(e)
f = """
123
456
789
"""
print(f)

# 字符串拼接 +拼接   * 重复
print('user'+'Name', 'biu~' * 3)

# 字符串索引
# 1.从左往右 从0递增
# 2.从右往左 从-1递减
# 一个字符就是长度为1的字符串
hi = 'helloworld'
print(hi[0], hi[5])
print(hi[-1], hi[-6])
# string index out of range  取hi[-20]

# 对字符串切片,获取一段字符串
# 用冒号分割两个索引, 表达式 [头下标:尾下标]
# 截取的范围是前闭后开,并且两个索引都可以省略

summary = 'handsome'
# ands
print(summary[1:5])
# handsome
print(summary[:])
# some
print(summary[4:])
# some
print(summary[-4:])
# so
print(summary[-4:-2])

# summary[1] = 'a'  报错 TypeError: 'str' object does not support item assignment

# 检测开头和结尾
filename = 'splider.py'
filename.endswith('.py')
filename.startswith('file:')

url = 'https://www.sina.com'
url.startswith('https:')

choices = ('http:', 'https')
url = 'https//www.sina.com'
url.startswith(choices)

# 查找某个字符串
string = "who am I"
string.find("am")
string.find("who")

# 忽略大小写的搜索
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)

# 搜索和替换
text = 'yeah, only no, only yeah, onlyyeah, biubiu'
replaceText = text.replace('yeah', 'yep')
print(text)
print(replaceText)

# 忽略大小写替换
text = 'UPPER PYTHON, lower python, Mixed Python'
replaceText = re.sub('python', 'Java', text, flags=re.IGNORECASE)
print(replaceText)

# 合并字符串
parts = ['Yes,', 'you', 'are', 'right', '!']
str1 = ' '.join(parts)
print(str1)

str2 = '🙂'.join(parts)
print(str2)

str3 = '哈'.join(parts)
print(str3)

