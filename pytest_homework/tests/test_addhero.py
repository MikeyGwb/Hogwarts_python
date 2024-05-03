import pytest
import yaml
from pytest_homework.script.hero import HeroManagement
from pytest_homework.utils.log_util import logger


class Test_Add_Hero:
    def setup_class(self):
        self.heromanage = HeroManagement()
    def setup(self):
        logger.info("开始添加")

    def teardown(self):
        logger.info("添加结束")

    def teardown_class(self):
        logger.info("=======结束测试=======")

    def test_add_hero(self):
        create_hero_result = self.heromanage.create_hero('hero01', 90, 100)
        assert create_hero_result == True