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
        return print("添加成功")
    else:
        if any(sid == i.get("sid") for i in Student_Information_value):
            return print("添加失败，学生的编号已存在")

        Student_Information_value.append(Student_Information_dict)
        return print("添加成功")

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
                        dict['age'] = new_age_value
                        new_gender_value = input("请输入学生的新性别：")
                        dict['gender'] = new_gender_value
            return print("修改成功")

        return print("想要修改的学生编码不存在，无法进行修改")