class MainClass:
    __class_sting = "Hello, world"

    @staticmethod
    def get_class_string():
        return __class__.__class_sting


class TestMainClass:
    def test_get_class_string(self):
        class_string = MainClass.get_class_string()
        substring_one = 'Hello'
        substring_two = 'hello'

        assert substring_one in class_string or substring_two in class_string,\
            f"In string '{class_string}' substrings "\
            f"'{substring_one}' or '{substring_two}' not found"



