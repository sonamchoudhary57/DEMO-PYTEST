import pytest

class TestClass:
    @pytest.fixture()   # decorator
    def setup(self):
        print("Launching browser...")
        print("Open application..")
        yield # print after every test method
        print("Closing browser")

    def test_Login(self,setup):
        print("This is login test")

    def test_Search(self,setup):
        print("this is search test")

    def test_Advancedsearch(self, setup):
        print("this is advanced search test")