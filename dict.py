# ---------------------------------dictionary---------------------------------
# dictionary:字典,其他语言中的map,存放键值对(key-value)
d = {'michael': 98, 'bob': 90, 'tracy': 99}
print(d['bob'])  # >>> 90
# print(d['jack'])  key不存在,报错
'''
Traceback (most recent call last):
  File "/Users/esirnus/Desktop/py/py/dict.py", line 5, in <module>
    print(d['jack'])
KeyError: 'jack'
'''

# 避免key不存在的错误,有两种方法
# 1.听过in判断key是否存在:
'jack' in d
# >>> False
# 2.通过dict的get()方法,如果key存在,可以返回None,或者自己指定的value
d.get('jack')
# None
d.get('jack', -1)
# -1

'''
和list比较,dict有2个特点:
1.查找和插入的速度极快,不会随着key的增加而变慢
2.需要占用大量的内存,内存浪费多
而list相反:
1.查找和插入的时间随着元素的增加而增加;
2.占用空间少,浪费内存很少,
dict,空间换时间
'''
# 注意:dict的key必须为不可变对象,dict根据key来计算value的存储位置,通过这个key计算位置的算法称为Hash算法


# ---------------------------------set---------------------------------
# set 和 dict类似,也是key的集合,但不存储value,由于key不能重复,在set中,没有重复的key
# 要创建一个set,需要提供一个list作为输入集合
s = set([1, 2, 3])
print(s)  # >>> {1, 2, 3}
s1 = set([1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6])
print(s1)  # >>> {1, 2, 3, 4, 5, 6}  重复元素在set中自动被过滤

# add(key) 添加元素到set中
s2 = {1, 2, 3}
s2.add(4)
print(s2) # >>> {1, 2, 3, 4}
s2.remove(1)
print(s2) # >>> {2, 3, 4}

# set可以看成数学意义上的无序和无重复元素的集合,so,两个set可以做数学意义上的交集、并集等操作

s3 = set([1, 2, 3])
s4 = set([2, 4, 5])
print(s3 & s4)  # >>> {2}
print(s3 | s4)  # >>> {1, 2, 3, 4, 5}

# set和dict的唯一区别仅在于没有存储对应的value,但是两者的原理一样,so,同样不可放入可变对象,因为无法判断两个可变对象是否相等,也就无法
# 保证set内部"不会有重复元素"