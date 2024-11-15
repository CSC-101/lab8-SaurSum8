import unittest
import group

class TestCase(unittest.TestCase):

    def test_group_1(self):
        self.assertEqual(group.groups_of_3([1,2,3,4,5,6,7,8,9]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_group_2(self):
        self.assertEqual(group.groups_of_3([1, 2, 3, 4, 5, 6, 7, 8]), [[1, 2, 3], [4, 5, 6], [7, 8]])

    def test_group_3(self):
        self.assertEqual(group.groups_of_3([]), [])

    if __name__ == '__main__':
        unittest.main()