import allure
import pytest
from bookManager_homework.book_manager import BookManagement
from bookManager_pytest_homework.utils.utils import Utils

add_P0_data = Utils().get_datas('add', 'P0', "test_data")
add_P1_data = Utils().get_datas('add', 'P1', "test_data")
add_P2_data = Utils().get_datas('add', 'P2', "test_data")

modify_P0_data = Utils().get_datas('modify', 'P0', "test_data")
modify_P1_data = Utils().get_datas('modify', 'P1', "test_data")
modify_P2_data = Utils().get_datas('modify', 'P2', "test_data")

@allure.feature('图书馆管理功能测试')
class TestBookManager():

    def setup_class(self):
        self.bm = BookManagement()

    @allure.story('创建书本 P0 级别用例')
    @pytest.mark.P0
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("ID, Name, Price, Summary, expect", add_P0_data[0], ids=add_P0_data[1])
    def test_addBook_P0(self, ID, Name, Price, Summary, expect):
        with allure.step("调用创建方法"):
            result = self.bm.addBook(ID, Name, Price, Summary)
        with allure.step(f'断言 {result} == {expect}'):
            assert result == expect

    @allure.story('创建书本 P1 级别用例')
    @pytest.mark.P1
    @pytest.mark.run(order=7)
    @pytest.mark.parametrize("ID, Name, Price, Summary, expect", add_P1_data[0], ids=add_P1_data[1])
    def test_addBook_P1(self, ID, Name, Price, Summary, expect):
        with allure.step("调用创建方法"):
            result = self.bm.addBook(ID, Name, Price, Summary)
        with allure.step(f'断言 {result} == {expect}'):
            assert result == expect

    @allure.story('创建书本 P2 级别用例')
    @pytest.mark.P2
    @pytest.mark.run(order=9)
    @pytest.mark.parametrize("ID, Name, Price, Summary, expect", add_P2_data[0], ids=add_P2_data[1])
    def test_addBook_P2(self, ID, Name, Price, Summary, expect):
        with allure.step("调用创建方法"):
            result = self.bm.addBook(ID, Name, Price, Summary)
        with allure.step(f'断言 {result} == {expect}'):
            assert result == expect

    @allure.story('修改书本 P0 级别用例')
    @pytest.mark.P0
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("ID, Name, Price, Summary, expect", modify_P0_data[0], ids=modify_P0_data[1])
    def test_modifyBookByID_P0(self, ID, Name, Price, Summary, expect):
        with allure.step("调用修改方法"):
            result = self.bm.modifyBookByID(ID, Name, Price, Summary)
        with allure.step(f'断言 {result} == {expect}'):
            assert result == expect

    @allure.story('修改书本 P1 级别用例')
    @pytest.mark.P1
    @pytest.mark.run(order=8)
    @pytest.mark.parametrize("ID, Name, Price, Summary, expect", modify_P1_data[0], ids=modify_P1_data[1])
    def test_modifyBookByID_P1(self, ID, Name, Price, Summary, expect):
        with allure.step("调用修改方法"):
            result = self.bm.modifyBookByID(ID, Name, Price, Summary)
        with allure.step(f'断言 {result} == {expect}'):
            assert result == expect

    @allure.story('修改书本 P2 级别用例')
    @pytest.mark.P2
    @pytest.mark.run(order=10)
    @pytest.mark.parametrize("ID, Name, Price, Summary, expect", modify_P2_data[0], ids=modify_P2_data[1])
    def test_modifyBookByID_P2(self, ID, Name, Price, Summary, expect):
        with allure.step("调用修改方法"):
            result = self.bm.modifyBookByID(ID, Name, Price, Summary)
        with allure.step(f'断言 {result} == {expect}'):
            assert result == expect

    @allure.story('根据ID删除书本 P0 级别用例')
    @pytest.mark.P0
    @pytest.mark.run(order=5)
    def test_deleteBookByID(self):
        self.bm.addBook("01", "jack", 100, "test")
        with allure.step("调用根据ID删除方法"):
            result = self.bm.deleteBookByID("01")
        with allure.step(f'断言 {result} == "删除成功"'):
            assert result == "删除成功"

    @allure.story('根据书名删除书本 P0 级别用例')
    @pytest.mark.P0
    @pytest.mark.run(order=6)
    def test_deleteBookByName(self):
        self.bm.addBook("01", "jack", 100, "test")
        with allure.step("调用根据名称删除方法"):
            result = self.bm.deleteBookByName("jack")
        with allure.step(f'断言 {result} == "删除成功"'):
            assert result == "删除成功"

    @allure.story('根据ID查询书本 P0 级别用例')
    @pytest.mark.P0
    @pytest.mark.run(order=3)
    def test_queryBookByID(self):
        with allure.step("调用根据ID查询方法"):
            result = self.bm.queryBookByID("s01")
        with allure.step(f'断言 {result} == "查询成功"'):
            assert result == "查询成功"

    @allure.story('根据书名查询书本 P0 级别用例')
    @pytest.mark.P0
    @pytest.mark.run(order=4)
    def test_queryBookByName(self):
        with allure.step("调用根据名称查询方法"):
            result = self.bm.queryBookByName("jack_book")
        with allure.step(f'断言 {result} == "查询成功"'):
            assert result == "查询成功"