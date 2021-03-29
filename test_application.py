import unittest
from application import clean_data, _convert_height, _convert_experience


class TestCleanData1(unittest.TestCase):
    def setUp(self):
        self.player = {
            'name': 'Chloe Alaska',
            'guardians': 'David Alaska and Jamie Alaska',
            'experience': 'NO',
            'height': '47 inches'
        }

        self.expected = {
            'name': 'Chloe Alaska',
            'guardians': 'David Alaska and Jamie Alaska',
            'experience': False,
            'height': 47
        }

    def test_it_cleans_data(self):
        cleaned_player = clean_data(self.player)
        self.assertEqual(self.expected, cleaned_player)

    def test_it_does_not_change_original_data(self):
        expected = self.player.copy()
        clean_data(self.player)
        self.assertEqual(expected, self.player)


class TestCleanData2(unittest.TestCase):
    def setUp(self):
        self.player = {
            'name': 'Les Clay',
            'guardians': 'Wynonna Brown',
            'experience': 'YES',
            'height': '42 inches'
        }

        self.expected = {
            'name': 'Les Clay',
            'guardians': 'Wynonna Brown',
            'experience': True,
            'height': 42
        }

    def test_it_cleans_data(self):
        cleaned_player = clean_data(self.player)
        self.assertEqual(self.expected, cleaned_player)

    def test_it_does_not_change_original_data(self):
        expected = self.player.copy()
        clean_data(self.player)
        self.assertEqual(expected, self.player)


class TestHelperFunctions(unittest.TestCase):
    def test_it_converts_yes_to_true(self):
        self.assertEqual(True, _convert_experience('YES'))

    def test_it_converts_no_to_false(self):
        self.assertEqual(False, _convert_experience('NO'))

    def test_it_converts_height_to_int(self):
        self.assertEqual(39, _convert_height('39 inches'))
        self.assertEqual(42, _convert_height('42 inches'))
        self.assertEqual(100, _convert_height('100 inches'))


if __name__ == '__main__':
    unittest.main()
