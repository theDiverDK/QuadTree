import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import unittest

from app.point import Point
from app.rectangle import Rectangle


class RectangleTesting(unittest.TestCase):
    def setUp(self):
        self.rectangle1 = Rectangle(100, 100, 200, 200)
        self.rectangle2 = Rectangle(150, 150, 250, 250)
        self.rectangle3 = Rectangle(0, 0, 50, 50)
        self.point = Point(150,150)

    def test_print(self):
        self.assertEqual('Rectangle(100,100,200,200)',
                         self.rectangle1.__str__())
        self.assertEqual('Rectangle(150,150,250,250)',
                         self.rectangle2.__str__())
        self.assertEqual('Rectangle(0,0,50,50)',
                         self.rectangle3.__str__())

    def test_doOverlap_is_true(self):
        self.assertTrue(self.rectangle1.doOverlap(self.rectangle2))
        self.assertTrue(self.rectangle2.doOverlap(self.rectangle1))

    def test_doOverlap_is_false(self):
        self.assertFalse(self.rectangle1.doOverlap(self.rectangle3))
        self.assertFalse(self.rectangle3.doOverlap(self.rectangle1))

    def test_contains_is_true(self):
        self.assertTrue(self.rectangle1.contains(self.point))
        self.assertTrue(self.rectangle2.contains(self.point))

    def test_contains_is_false(self):
        self.assertFalse(self.rectangle3.contains(self.point))

