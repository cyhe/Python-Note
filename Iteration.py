# for interating_var in sequence:
#     statements(s)

for letter in 'Python':
    print('当前字母:', letter)

fuilts = ['banana', 'apple', 'mango']
for fruit in fuilts:
    print('当前水果:', fruit)

print('-------end---------')

# 通过序列索引迭代
fruits1 = ['banana', 'apple', 'mango']
for index in range(len(fruits1)):
    print('当前水果:', fruits1[index])
# 函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数。
print('-------end---------')

# 输出2~200之间的素数
i = 2
while (i < 100):
    j = 2
    while(j <= (i / j)):
        if not(i % j): break
        j = j+1
    if (j > i / j): print(i, "是素数")
    i = i + 1

print('-------end---------')

# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句，
a = 2
if a > 1:
    pass
    #如果没有内容，可以先写pass，但是如果不写pass，就会语法错误
    # SyntaxError: unexpected EOF while parsing