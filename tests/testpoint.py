import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import unittest

from app.point import Point
from app.rectangle import Rectangle


class PointTesting(unittest.TestCase):
    def setUp(self):
        self.pointInside = Point(100, 200)
        self.pointOutside = Point(1, 2)

    def test_print(self):
        self.assertEqual('Point(100,200)', self.pointInside.__str__())

    def test_IsInsideTrue(self):
        rectangle = Rectangle(50, 50, 300, 300)

        self.assertTrue(self.pointInside.isInside(rectangle))

    def test_IsInsideFalse(self):
        rectangle = Rectangle(50, 50, 300, 300)

        self.assertFalse(self.pointOutside.isInside(rectangle))
