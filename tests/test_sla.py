import unittest
from sla import is_overdue

class SLATests(unittest.TestCase):
    # Тесты для приоритета normal (лимит 120)
    def test_normal_before_limit(self):
        self.assertFalse(is_overdue(119, "normal"))

    def test_normal_at_limit(self):
        self.assertFalse(is_overdue(120, "normal"))  # Граница! Должно быть False

    def test_normal_after_limit(self):
        self.assertTrue(is_overdue(121, "normal"))

    # Тесты для приоритета high (лимит 30)
    def test_high_before_limit(self):
        self.assertFalse(is_overdue(29, "high"))

    def test_high_at_limit(self):
        self.assertFalse(is_overdue(30, "high"))

    def test_high_after_limit(self):
        self.assertTrue(is_overdue(31, "high"))
    
    def test_negative_elapsed(self):
     with self.assertRaises(ValueError):
         is_overdue(-1)

    def test_unknown_priority(self):
     with self.assertRaises(ValueError):
         is_overdue(10, "urgent")

    

     
