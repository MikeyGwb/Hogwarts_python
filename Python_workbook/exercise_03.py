
while(1):
    year_value = int(input("请输入年份："))

    calculate_01 = year_value % 4

    calculate_02 = year_value % 100

    calculate_03 = year_value % 400

    if (calculate_01 == 0 and calculate_02 != 0) or calculate_03 == 0:
        print("是闰年")
    else:
        print("不是闰年")
