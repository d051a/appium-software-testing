class MainClass:
    __number = 20
    @staticmethod
    def get_class_number():
        return __class__.__number


class TestMainClass:
    def test_get_class_number(self, test_number=45):
        class_number = MainClass.get_class_number()
        assert class_number > test_number, f"Number {class_number} is not more than {test_number}"
