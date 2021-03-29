import unittest
from application import clean_data


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

    def test_it_does_not_mutate_the_original_data(self):
        expected = self.player.copy()
        clean_data(self.player)
        self.assertEqual(expected, self.player)

    def test_it_changes_height_to_integer(self):
        cleaned_player = clean_data(self.player)
        self.assertEqual(self.expected['height'], cleaned_player['height'])

    def test_it_changes_no_experience_to_false(self):
        cleaned_player = clean_data(self.player)
        self.assertEqual(self.expected['experience'],
                         cleaned_player['experience'])


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

    def test_it_does_not_mutate_the_original_data(self):
        expected = self.player.copy()
        clean_data(self.player)
        self.assertEqual(expected, self.player)

    def test_it_changes_height_to_integer(self):
        cleaned_player = clean_data(self.player)
        self.assertEqual(self.expected['height'], cleaned_player['height'])

    def test_it_changes_yes_experience_to_true(self):
        cleaned_player = clean_data(self.player)
        self.assertEqual(self.expected['experience'],
                         cleaned_player['experience'])


if __name__ == '__main__':
    unittest.main()
