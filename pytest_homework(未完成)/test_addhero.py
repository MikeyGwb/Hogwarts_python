from tested_system import HeroManagement

class Test_Add_Hero:
    def setup_class(self):
        self.hero_list = []
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_add_hero(self, expected_results=True):
        create_hero_result = HeroManagement.create_hero(self, hero_name='hero01', hero_volume=99, hero_power=50)
        assert create_hero_result == expected_results