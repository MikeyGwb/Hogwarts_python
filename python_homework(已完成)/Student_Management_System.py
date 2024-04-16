'''
作业：
实现学生管理系统：

学生信息包含：
    - 编号（sid), 姓名（name), 年龄（age), 性别（gender) 四个信息
    - 每个学生信息使用字典形式保存
    - 使用列表保存所有学生的信息
[{sid: , name: , age: , gender: }]
1. 实现菜单函数，输出下列信息，返回用户输入的编号，并进行输入校验。

    print("****************************************")
    print("*                                学生管理系统                         *")
    print("*              1. 添加新学生信息              *")
    print("*             2. 通过学号修改学生信息                 *")
    print("*                3. 通过学号删除学生信息                 *")
    print("*                4. 通过姓名删除学生信息                 *")
    print("*             5. 通过学号查询学生信息          *")
    print("*                6. 通过姓名查询学生信息          *")
    print("*                7. 显示所有学生信息             *")
    print("*                8. 退出系统                                           *")
    print("****************************************")
    select_op = input("输入编号选择操作：")

2. 实现控制函数，用来控制菜单的输出与功能的选择，直到用户选择8，结束程序运行。
3. 实现添加学生函数，函数参数为编号，姓名，年龄，性别四个参数，返回是否添加成功的结果，要求编号不可重复。
4. 实现修改函数，参数为学号，如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功
5. 实现删除函数，参数为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
6. 实现删除函数，参数为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功
7. 实现查询函数，参数为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
8. 实现查询函数，参数为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否删除成功
9. 实现函数，输出所有学生信息
'''

from system_tool import add_Student_Information, edit_Student_Information, delete_Student_Information, \
    select_Student_Information, is_number, is_gender

Student_Information_value = []

print("****************************************")
print("*                                学生管理系统                         *")
print("*              1. 添加新学生信息                                      *")
print("*             2. 通过学号修改学生信息                                  *")
print("*                3. 通过学号删除学生信息                               *")
print("*                4. 通过姓名删除学生信息                               *")
print("*             5. 通过学号查询学生信息                                  *")
print("*                6. 通过姓名查询学生信息                               *")
print("*                7. 显示所有学生信息                                  *")
print("*                8. 退出系统                                         *")
print("****************************************")


while (True):
    select_op = input("输入编号选择操作：")

    if select_op == "8":
        break

    if select_op == "1":
        age_try = True
        sid_value = input("请输入学生编号：")
        while (is_number(sid_value)):
            sid_value = input("输入的学生编码有误，请重新输入学生编码：")
        name_value = input("请输入学生姓名：")
        age_value = input("请输入学生年龄：")
        while(is_number(age_value)):
            age_value = input("输入的学生年龄有误，请重新输入学生年龄：")
        gender_value = input("请输入学生性别：")
        while(is_gender(gender_value)):
            gender_value = input("输入的学生性别有误，请重新输入学生性别：")
        add_Student_Information(Student_Information_value, sid_value, name_value, age_value, gender_value)

    if select_op == '7':
        print(Student_Information_value)

    if select_op == '2':
        sid_value = input("请输入想要修改的学生编号：")
        while (is_number(sid_value)):
            sid_value = input("输入的学生编码有误，请重新输入学生编码：")
        edit_Student_Information(Student_Information_value, sid_value)

    if select_op == '3':
        sid_value = input("请输入想要删除的学生编号：")
        while (is_number(sid_value)):
            sid_value = input("输入的学生编码有误，请重新输入学生编码：")
        delete_Student_Information(Student_Information_value, "sid", sid_value)

    if select_op == '4':
        name_value = input("请输入想要删除的学生名称：")
        delete_Student_Information(Student_Information_value, "name", name_value)

    if select_op == '5':
        sid_value = input("请输入想要查询的学生编号：")
        while (is_number(sid_value)):
            sid_value = input("输入的学生编码有误，请重新输入学生编码：")
        select_Student_Information(Student_Information_value, "sid", sid_value)

    if select_op == '6':
        name_value = input("请输入想要查询的学生名称：")
        select_Student_Information(Student_Information_value, "name", name_value)

