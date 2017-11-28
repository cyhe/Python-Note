
# if 语句的完成形式  注意冒号 :
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

inputNumber = input('请输入年份:')
year = int(inputNumber)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, '是闰年')
else:
    print(year, '不是闰年')


# height = 1.75
# width = 80.5

height = float(input('请输入身高:'))
width = float(input('请输入体重:'))

if height > 0 and width > 0:
    BMI = width / (height * height)
    if 0 < BMI < 18.5:
        print('太轻了')
    elif 18.5 < BMI <= 25:
        print('正常')
    elif 25 < BMI <= 28:
        print('肥胖')
    elif BMI > 32:
        print('严重诽谤')
    else:
        print('无法计算')
else:
    print('请输入大于合法的身高体重')

