from tested_system import HeroManagement
import pytest
import yaml

class Test_Add_Hero:
    def setup_class(self):
        self.hero_list = []
    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.parametrize("test_data", yaml.safe_load(open("./create_hero_data.yaml")))
    def test_add_hero(self, test_data):
        create_hero_result = HeroManagement.create_hero(self, hero_name = test_data["hero_name_value"], hero_volume = int(test_data["hero_volume_value"]), hero_power= int(test_data["hero_power_value"]))
        assert create_hero_result == test_data["expected_results"]