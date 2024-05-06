import os.path

import allure
import pytest
import yaml
from pytest_homework.script.hero import HeroManagement
from pytest_homework.utils.log_util import logger
from pytest_homework.utils.utils import Utils

@allure.feature("创建英雄功能")
class Test_Add_Hero:
    def setup_class(self):
        self.heromanage = HeroManagement()
    def setup(self):
        logger.info("开始添加")

    def teardown(self):
        logger.info("添加结束")

    def teardown_class(self):
        logger.info("=======结束测试=======")

    @pytest.mark.parametrize(
        "hero_name,hero_volume,hero_power,expected_results", Utils.get_datas('create', 'P0', "create_hero_data")[0], ids=Utils.get_datas('create', 'P0', "create_hero_data")[1]
    )
    @allure.story("创建功能 P0 级别用例")
    def test_add_hero(self, hero_name, hero_volume, hero_power, expected_results):
        logger.info(f'创建英雄的名字为：{hero_name}，血量为：{hero_volume}，力量为：{hero_power}，预期结果为：{expected_results}')
        with allure.step("调用创建方法"):
            create_hero_result = self.heromanage.create_hero(hero_name, hero_volume, hero_power)
            logger.info(f'实际结果为：{create_hero_result}')
        with allure.step(f"断言 {create_hero_result} == {expected_results}"):
            assert create_hero_result == expected_results

