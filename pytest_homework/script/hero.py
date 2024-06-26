'''
项目简介
       英雄管理系统的主要功能为增删查改，用户通过输入不同的信息，选择不同的操作。
1、增加英雄：输入英雄姓名、血量、和攻击力，名称为字符串，血量、攻击力为正整数，其中血量的最大值为 99，最小值为 1。
2、删除英雄：输入英雄姓名，如果删除成功，返回英雄列表，如果英雄不存在返回 False。
3、修改英雄血量：输入英雄姓名、血量，如果更新成功，返回更新后的英雄信息，如果英雄不存在或更新失败返回 False。
4、查找英雄：输入英雄信息，在英雄列表中存在则返回成功，不存在则返回失败。

知识点
Pytest 测试框架基本用法
参数化
结合 Allure 生成测试报告与项目总结
数据驱动
pytest fixture 实现测试装置及参数化
pytest conftest.py 的用法

受众
高级测试工程师

作业内容
1、针对英雄管理系统的增加功能，完成等价类与边界值的测试。要求测试数据使用单独的文件维护。
2、使用参数化减少代码量，提高代码的可维护性。
3、原有需求发生变化，边界值都增加1（变为最大值100，最小值2）。如何在不改变原始测试数据情况下，还能依然完成对修改需求后的测试（使用fixture）。
4、编写自动化测试用例，结合 Allure 与截图技术等自动生成带截图与操作步骤的测试报告。
5、将有效等价类和无效等价类的场景分别用标签进行分类。

'''

class HeroManagement:
    def __init__(self):
        self.hero_list = []

    def update_hero(self, hero_name, hero_volume):

        for i in self.hero_list:
            if i.get("name") == hero_name:
                i["volume"] = hero_volume
                return i
        return False

    def delete_hero(self, hero_name):
        """
        :param hero_list:  英雄列表信息
        :param hero_name:  英雄的名字
        :return:
        """
        for i in self.hero_list:
            if hero_name == i["name"]:
                self.hero_list.remove(i)
                return self.hero_list
        return False

    def create_hero(self, hero_name, hero_volume, hero_power):
        if hero_volume<=0 or hero_volume >= 100:
            return False
        if hero_power <=0:
            return False
        hero_info = {"name": hero_name, "volume": hero_volume, "power": hero_power}
        self.hero_list.append(hero_info)
        return True

    def find_hero(self, res):
        """
        如果查询到英雄，则返回英雄信息。
        如果没有查询到英雄，则返回False
        :param res:
        :return:
        """
        # 遍历所有的英雄信息，
        for i in self.hero_list:
            if res == i["name"]:
                return i
        return False