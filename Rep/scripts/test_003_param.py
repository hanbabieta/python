import pytest

class Test_bcd:
    def setup_class(self):
        pass
    def teardown_class(self):
        pass

    @pytest.mark.parametrize("param1,param2,param3", [(1,2,3)])
    def test_002(self, param1, param2, param3):
        print(">>>>:", param1)
        print(">>>>:", param2)
        print(">>>>:", param3)
        assert True
