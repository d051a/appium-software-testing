class MainClass:
    @staticmethod
    def get_local_number():
        return 14


class TestMainClass:
    def test_get_local_number(self, test_number=14):
        local_number = MainClass.get_local_number()
        assert local_number == test_number, f"Number {local_number} is not equal to {test_number}"
