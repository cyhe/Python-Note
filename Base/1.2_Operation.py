# 赋值
a = 2
b = 4

# 四则运算
a + b
a - b
a * b
a / b

# 取整
b // a
# 取余
9 % 2

# 乘方
2 ** 3

c = 3.7
d = 3.2
c + d

(c + d) == 6.9

print((c + d) == 6.9)

# Decimal模块:十进制浮点运算
# 注意:
# 1.可以传递给Decimal整型或者字符串参数,但不能是浮点数据，因为浮点数据本身就不准确。
# 2.要从浮点数据转换为Decimal类型
from decimal import Decimal
x = Decimal('7.2')
y = Decimal('2.5')
x + y
print(x + y)

print(x + y == Decimal('9.7'))