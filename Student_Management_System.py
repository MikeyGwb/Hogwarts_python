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

def add_Student_Information(sid, name, age, gender):
    Student_Information_dict = {}
    Student_Information_dict["sid"] = sid
    Student_Information_dict["name"] = name
    Student_Information_dict["age"] = age
    Student_Information_dict["gender"] = gender
    # print(Student_Information_dict)
    Student_Information_value.append(Student_Information_dict)
    # print(Student_Information_value)
    return print("添加成功")

while (True):
    select_op = input("输入编号选择操作：")

    if select_op == "8":
        break

    if select_op == "1":
        sid_value = input("请输入学生编号：")
        name_value = input("请输入学生姓名：")
        age_value = input("请输入学生年龄：")
        gender_value = input("请输入学生性别：")
        add_Student_Information(sid_value, name_value, age_value, gender_value)

    if select_op == '7':
        print(Student_Information_value)
# - 编号（sid), 姓名（name), 年龄（age), 性别（gender) 四个信息

