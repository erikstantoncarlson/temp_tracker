#!/usr/bin/env python

import unittest

import temp_tracker


class TestTempTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = temp_tracker.TempTracker()

    def test_flatten(self):
        value = [[1,2,[3]],4]
        expected = [1, 2, 3, 4]
        result = temp_tracker.flatten_array(value)
        self.assertEqual(result, expected)

    def test_insert(self):
        self.tracker.insert(5)
        self.tracker.insert(10)
        self.assertEqual(self.tracker._temperatures, [5, 10])

    def test_insert_bad_values(self):
        with self.assertRaises(ValueError):
            self.tracker.insert(-10)
            self.tracker.insert(200)
            self.tracker.insert(1.2)

    def test_max(self):
        self.tracker.insert(3)
        self.tracker.insert(5)
        result = self.tracker.get_max()
        self.assertEqual(result, 5)

    def test_max_no_values(self):
        with self.assertRaises(ValueError):
            self.tracker.get_max()

    def test_min(self):
        self.tracker.insert(3)
        self.tracker.insert(5)
        result = self.tracker.get_min()
        self.assertEqual(result, 3)

    def test_min_no_values(self):
        with self.assertRaises(ValueError):
            self.tracker.get_min()

    def test_mean(self):
        self.tracker.insert(1)
        self.tracker.insert(2)
        result = self.tracker.get_mean()
        self.assertAlmostEqual(result, 1.5)

    def test_mean_no_values(self):
        with self.assertRaises(ValueError):
            self.tracker.get_mean()