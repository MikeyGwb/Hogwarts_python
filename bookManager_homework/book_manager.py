import json
import os

manager_value = []


def menu():
    print("*****************************")
    print("*      图书管理系统           *")
    print("* 1. 添加新图书信息           *")
    print("* 2. 通过图书ID修改图书信息      *")
    print("* 3. 通过图书ID删除图书信息      *")
    print("* 4. 通过书名删除图书信息      *")
    print("* 5. 通过图书ID查询图书信息      *")
    print("* 6. 通过书名查询图书信息      *")
    print("* 7. 显示所有图书信息         *")
    print("* 8. 退出系统                *")
    print("*****************************")
    select_no = input("请输入编码操作系统：")
    return select_no


def getID():
    ID = input("请输入编码：")
    return ID


def getName():
    Name = input("请输入书名：")
    return Name


def getPrice():
    Price = input("请输入价格：")
    if Price.isdigit():
        return int(Price)
    else:
        print("输入价格不合法，请输入数字")


def getSummary():
    Summary = input("请输入简介：")
    return Summary


def addBook(ID, Name, Price, Summary):
    for i in manager_value:
        if i["sid"] == ID:
            print("书本编号已存在，添加失败")
            return "添加失败"

    else:
        book_detail_value = {"sid": ID, "name": Name, "price": Price, "summary": Summary}
        manager_value.append(book_detail_value)
        print("添加成功")
        return "添加成功"


def modifyBookByID(ID):
    for i in manager_value:
        if i["sid"] == ID:
            i["name"] = getName()
            i["price"] = getPrice()
            i["summary"] = getSummary()
            print("修改成功")
            return "修改成功"
    print(f"没有{ID}对应的书本信息")
    return "修改失败"


def deleteBookByID(ID):
    for i in manager_value:
        if i["sid"] == ID:
            manager_value.remove(i)
            print("删除成功")
            return "删除成功"
    print(f"没有{ID}对应的书本信息")
    return "删除失败"


def deleteBookByName(Name):
    Staging = []
    for i in manager_value:
        if i["name"] == Name:
            Staging.append(i)

    if len(Staging) > 0:
        for s in Staging:
            manager_value.remove(s)

        print(f"成功删除{len(Staging)}本书")
        del Staging
        return "删除成功"
    print(f"没有{Name}对应的书本信息")
    return "删除失败"


def queryBookByID(ID):
    for i in manager_value:
        if i["sid"] == ID:
            print(f"编码{ID}的书本信息如下：")
            print(i)
            return "查询成功"
    print(f"没有{ID}对应的书本信息")
    return "查询失败"


def queryBookByName(Name):
    for i in manager_value:
        if i["name"] == Name:
            print(f"名字{Name}的书本信息如下：")
            print(i)
            return "查询成功"
    print(f"没有{Name}对应的书本信息")
    return "查询失败"


def showAllInfo():
    for i in manager_value:
        print(i)
    return "查询成功"


#   因写法有问题导致读写后系统的功能实现不了，需要换为模板上的写法（上课时需询问为啥不能直接存直接读）
# def save_data():
#     with open("db.txt", 'w') as f:
#         for i in manager_value:
#             print(i)
#             f.write(f'{i}\n')
#
# def load_data():
#     if os.path.exists('db.txt'):
#         with open('db.txt', 'r') as f:
#             content = f.read()
#             content = content.split('\n')
#             content.remove("")
#             for i in content:
#                 manager_value.append(json.loads(i))

def load_data():
    if os.path.exists("db.txt"):
        with open("db.txt", "r") as f:
            content = f.read()
            content = content.split("\n")
            content.remove("")
            for item in content:
                book = {}
                print(item)
                item = item.split("-")
                book["sid"] = item[0]
                book["name"] = item[1]
                book["price"] = item[2]
                book["summary"] = item[3]
                manager_value.append(book)


# 保存文件
def save_data():
    with open("db.txt", 'w') as f:
        for item in manager_value:
            bookStr = ""
            print(item)
            for v in item.values():
                bookStr += str(v) + "-"
            f.write(bookStr[:-1] + '\n')


def bookManager():
    load_data()
    while True:

        select_no = menu()

        if len(select_no) == 1 and select_no in "12345678":
            if select_no == "1":
                ID = getID()
                Name = getName()
                Price = getPrice()
                Summary = getSummary()
                addBook(ID, Name, Price, Summary)
            elif select_no == '2':
                ID = getID()
                modifyBookByID(ID)
            elif select_no == '3':
                ID = getID()
                deleteBookByID(ID)
            elif select_no == '4':
                Name = getName()
                deleteBookByName(Name)
            elif select_no == '5':
                ID = getID()
                queryBookByID(ID)
            elif select_no == '6':
                Name = getName()
                queryBookByName(Name)
            elif select_no == '7':
                showAllInfo()
            else:
                save_data()
                break
        else:
            print("输入的数据不合法，请输入在合法范围内的操作编号！！！")


if __name__ == '__main__':
    bookManager()
