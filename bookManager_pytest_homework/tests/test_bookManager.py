from bookManager_homework.book_manager import BookManagement


class TestBookManager():

    def setup_class(self):
        self.bm = BookManagement()

    def test_addBook(self):
        result = self.bm.addBook("01", "jack", 100, "test")
        assert result == "添加成功"

    def test_modifyBookByID(self):
        result = self.bm.modifyBookByID("01", "tom", 100, "test")
        assert result == "修改成功"

    def test_deleteBookByID(self):
        result = self.bm.deleteBookByID("01")
        assert result == "删除成功"

    def test_deleteBookByName(self):
        result = self.bm.deleteBookByName("jack")
        assert result == "添加成功"

    def test_queryBookByID(self):
        result = self.bm.queryBookByID("01")
        assert result == "添加成功"

    def test_queryBookByName(self):
        result = self.bm.queryBookByName("jack")
        assert result == "添加成功"