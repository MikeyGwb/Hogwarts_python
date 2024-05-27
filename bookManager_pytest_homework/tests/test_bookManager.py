import pytest
from bookManager_homework.book_manager import BookManagement
from bookManager_pytest_homework.utils.utils import Utils

add_P0_data = Utils().get_datas('add', 'P0', "test_data")
add_P1_data = Utils().get_datas('add', 'P1', "test_data")
class TestBookManager():

    def setup_class(self):
        self.bm = BookManagement()

    @pytest.mark.parametrize("ID, Name, Price, Summary, expect", add_P0_data[0], ids=add_P0_data[1])
    def test_addBook_P0(self, ID, Name, Price, Summary, expect):
        result = self.bm.addBook(ID, Name, Price, Summary)
        assert result == expect

    @pytest.mark.parametrize("ID, Name, Price, Summary, expect", add_P1_data[0], ids=add_P1_data[1])
    def test_addBook_P1(self, ID, Name, Price, Summary, expect):
        result = self.bm.addBook(ID, Name, Price, Summary)
        assert result == expect

    # def test_modifyBookByID(self):
    #     result = self.bm.modifyBookByID("01", "tom", 100, "test")
    #     assert result == "修改成功"
    #
    # def test_deleteBookByID(self):
    #     result = self.bm.deleteBookByID("01")
    #     assert result == "删除成功"
    #
    # def test_deleteBookByName(self):
    #     self.bm.addBook("01", "jack", 100, "test")
    #     result = self.bm.deleteBookByName("jack")
    #     assert result == "删除成功"
    #
    # def test_queryBookByID(self):
    #     self.bm.addBook("01", "jack", 100, "test")
    #     result = self.bm.queryBookByID("01")
    #     assert result == "查询成功"
    #
    # def test_queryBookByName(self):
    #     result = self.bm.queryBookByName("jack")
    #     assert result == "查询成功"