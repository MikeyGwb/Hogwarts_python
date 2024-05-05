import os.path

import pytest
import yaml
from pytest_homework.script.hero import HeroManagement
from pytest_homework.utils.log_util import logger
from pytest_homework.utils.utils import Utils


def get_datas(name, level):
    root_path = os.path.dirname(os.path.abspath(__file__))
    system = Utils.get_windos_or_mac()
    if system == "Windows":
        yaml_path = os.sep.join([root_path, '..', 'datas\create_hero_data.yaml'])
    else:
        yaml_path = os.sep.join([root_path, '..', 'datas/create_hero_data.yaml'])
    yaml_datas = Utils.get_yaml_data(yaml_path)
    datas = yaml_datas.get(name).get(level).get("datas")
    ids = yaml_datas.get(name).get(level).get("ids")
    return [datas, ids]

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
        "hero_name,hero_volume,hero_power,expected_results", get_datas('create', 'P0')[0], ids=get_datas('create', 'P0')[1]
    )
    def test_add_hero(self, hero_name, hero_volume, hero_power, expected_results):
        logger.info(f'创建英雄的名字为：{hero_name}，血量为：{hero_volume}，力量为：{hero_power}，预期结果为：{expected_results}')
        create_hero_result = self.heromanage.create_hero(hero_name, hero_volume, hero_power)
        logger.info(f'实际结果为：{create_hero_result}')
        assert create_hero_result == expected_results

