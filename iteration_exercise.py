#coding:utf-8

rows = int(input('输入列数: '))
# 声明变量, i用于控制外层循环(图形行数),j用于控制空格的个数,k用于控制*的个数
i = j = k = 1

# 等腰直角三角形
for i in range(0, rows):
    for k in range(0, rows - i):
        # print('*',)
        print(' * ', end='')
        k += 1
    i += 1
    print('\n')
# * * * * * *
#
# * * * * *
#
# * * * *
#
# * * *
#
# * *
#
# *

# 等边三角形
for i in range(0, rows + 1):
    for j in range(0, rows - i):
        print(' ', end='')
        j += 1
    for k in range(0, 2 * i - 1):
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
                if k % 2 == 0:
                    print('*', end='')
                else:
                    print(' ', end='')
            else:
                print('*', end='')
        else:
            print(' ', end='')
        k += 1
    print('\n')
    i += 1

#     *
#
#    * *
#
#   *   *
#
#  *     *
#
# * * * * *