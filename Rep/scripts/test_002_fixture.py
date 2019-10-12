import pytest

@pytest.fixture(scope="class")
def bcd001():
    print(">>>>bcd001")
@pytest.fixture(scope="class")
def cde001():
    print(">>>>>cde001")

class Test_bcd:
    def setup_class(self):
        pass
    def teardown_class(self):
        pass

    @pytest.mark.usefixtures("bcd001", "cde001")
    def test_002(self):
        print(">>>>test_002")
        assert True

