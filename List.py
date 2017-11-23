# list是一种有序的集合，可以随时添加和删除其中的元素。

workmates = ['jack', 'steve', 'boers']
print(workmates)
# 取元素
print('取出下标为1的元素', workmates[1])
# 取出最后一个元素还可以直接取-1  负号表示倒数 ,倒数第一(-1),倒数第二个(-2)
print('取出最后一个的元素', workmates[-1])
# 数组越界
"""
 print('取出下标为-1的元素', workmates[3])
 Traceback (most recent call last):
   File "/Users/cyhe/Desktop/py/list.py", line 7, in <module>
     print('取出下标为-1的元素', workmates[3])
IndexError: list index out of range
"""

# 数组操作
# list是可变的有序表 可以追加元素到末尾
workmates.append('lily')
print(workmates)
# 元素插入  插入到指定位置
workmates.insert(1, "mary")
print(workmates)

# 元素删除
# 1.删除末尾元素
workmates.pop()
# 2.删除指定位置
workmates.pop(2)

# 元素替换 某个元素替换为别的元素
workmates[1] = 'michel'

# list的元素类型可以不同
list = ['list', 123456, True]
print(list)

# list的元素可以是一个list 相当于二维数组
fruits = ['apple', 'orange', ['redPitaya', 'whitePitaya'], 'Grape']
print(fruits)
print(fruits[2])

# 数组长度len()
print(len(fruits))

# ---------------------------------  分割线---------------------------------

# tuple 另一种有序列表 元组   tuple一旦初始化就不能修改  不可变
# 定义空tuple
t = ()
# 定义有一个元素的tuple   (1, ) 消除与单纯()歧义
t1 = (1, )

# 问题? t = ('a', 'b', ['A', 'B'])
t2 = ('a', 'b', ['A', 'B'])
t2[2][0] = 'X'
t2[2][1] = 'Y'
print(t2)

"""
tuple说不能变,但是却变了, 但变的不是tuple的元素,而是list元素,tuple一开始指向list并没有改成别的list,tuple的每个元素,永远
# 指向不变,之所以变了,是指向的list没变,而指向的list本身是可变的
"""
