#!/usr/bin/env python

import unittest

import temp_tracker


class TestTempTrackerFast(unittest.TestCase):
    def setUp(self):
        self.tracker = temp_tracker.TempTrackerFast()

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