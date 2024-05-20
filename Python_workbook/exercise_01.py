
while(True):
    number = int(input("请输入分数："))
    if 100 >= number >= 90:
        print("A等级")
    elif 90 > number >= 60:
        print("B等级")
    else:
        print("C等级")