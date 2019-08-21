import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise08
        self.exercises = Exercise08

    def test(self):
        self.assertEqual(self.exercises.my_diary.show_birthday(), '14-May-20')

        
if __name__ == '__main__':
    unittest.main()
   