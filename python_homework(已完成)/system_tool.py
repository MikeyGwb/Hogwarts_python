def add_Student_Information(Student_Information_value, sid, name, age, gender):
    Student_Information_dict = {}
    Student_Information_dict["sid"] = sid
    Student_Information_dict["name"] = name
    Student_Information_dict["age"] = age
    Student_Information_dict["gender"] = gender
    if not Student_Information_value:
        # print(Student_Information_dict)
        Student_Information_value.append(Student_Information_dict)
        # print(Student_Information_value)
        return print("*****添加成功*****")
    else:
        if any(sid == i.get("sid") for i in Student_Information_value):
            return print("添加失败，学生的编号已存在")

        Student_Information_value.append(Student_Information_dict)
        return print("*****添加成功*****")


def edit_Student_Information(Student_Information_value, sid):
    if not Student_Information_value:
        return print("系统中没有数据不可进行修改")
    else:
        if any(sid == i.get("sid") for i in Student_Information_value):
            for dict in Student_Information_value:
                for key, value in dict.items():
                    if key == 'sid' and value == sid:
                        print("对应学生编号中原有的数据为：", dict)
                        new_name_value = input("请输入学生的新名字：")
                        dict['name'] = new_name_value
                        new_age_value = input("请输入学生的新年龄：")
                        while (is_number(new_age_value)):
                            new_age_value = input("输入的学生年龄有误，请重新输入学生年龄：")
                        dict['age'] = new_age_value
                        new_gender_value = input("请输入学生的新性别：")
                        while (is_gender(new_gender_value)):
                            new_gender_value = input("输入的学生性别有误，请重新输入学生性别：")
                        dict['gender'] = new_gender_value
            return print("*****修改成功*****")

        return print("想要修改的学生编码不存在，无法进行修改")


def delete_Student_Information(Student_Information_value, key, value):
    if not Student_Information_value:
        return print("系统中没有数据不可进行删除")
    else:
        if any(value == i.get(key) for i in Student_Information_value):
            for i in Student_Information_value:
                for dict in Student_Information_value:
                    for dict_key, dict_value in dict.items():
                        if dict_key == key and dict_value == value:
                            print("删除学生的数据为：", dict)
                            Student_Information_value.remove(dict)
            return print("*****删除成功*****")

        return print("想要删除的学生编码&学生名字不存在")


def select_Student_Information(Student_Information_value, key, value):
    if not Student_Information_value:
        return print("系统暂时没有数据")
    else:
        if any(value == i.get(key) for i in Student_Information_value):
            for dict in Student_Information_value:
                for dict_key, dict_value in dict.items():
                    if dict_key == key and dict_value == value:
                        print("查询学生的数据为：", dict)
            return print("*****查询成功*****")

        return print("想要查询的学生编码&学生名字不存在")

def is_number(a):
    try:
        int(a)
        return False
    except ValueError:
        return True

def is_gender(b):
    if b != '男' and b != '女':
        return True
    else:
        return False
