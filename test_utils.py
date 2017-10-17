#!/usr/bin/env python
# encoding: utf-8
"""
Unit tests for utils.py
"""
from __future__ import print_function, unicode_literals
import unittest

import utils


class TestIt(unittest.TestCase):

    def test_supports_has_support(self):
        # Arrange
        classifiers = [
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
        ]

        # Act
        has_support = utils.supports(classifiers, "2.6")

        # Assert
        self.assertEqual(has_support, "yes")

    def test_supports_no_support_but_others_are(self):
        # Arrange
        classifiers = [
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
        ]

        # Act
        has_support = utils.supports(classifiers, "2.6")

        # Assert
        self.assertEqual(has_support, "no")

    def test_supports_no_support_but_other_2x_are(self):
        # Arrange
        classifiers = [
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
        ]

        # Act
        has_support = utils.supports(classifiers, "2.6")

        # Assert
        self.assertEqual(has_support, "no")

    def test_supports_no_support_but_other_3x_are(self):
        # Arrange
        classifiers = [
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
        ]

        # Act
        has_support = utils.supports(classifiers, "2.6")

        # Assert
        self.assertEqual(has_support, "no")

    def test_supports_no_support_or_any_major_minor(self):
        # Arrange
        # No major.minor classifiers
        classifiers = [
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
        ]

        # Act
        # Classifiers are not explicit: we want to assume support
        has_support = utils.supports(classifiers, "2.6")

        # Assert
        self.assertEqual(has_support, "maybe")

    def test_supports_no_support_for_empty(self):
        # Arrange
        # No classifiers
        classifiers = []

        # Act
        # Classifiers are not explicit: we want to assume support
        has_support = utils.supports(classifiers, "2.6")

        # Assert
        self.assertEqual(has_support, "maybe")

    def test_supports_2_only_only(self):
        # Arrange
        classifiers = [
            "Programming Language :: Python :: 2 :: Only",
        ]

        # Act
        has_support_26 = utils.supports(classifiers, "2.6")
        has_support_34 = utils.supports(classifiers, "3.4")

        # Assert
        self.assertEqual(has_support_26, "maybe")
        self.assertEqual(has_support_34, "no")

    def test_supports_2_only_plus_others(self):
        # Arrange
        classifiers = [
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 2 :: Only",
        ]

        # Act
        has_support_26 = utils.supports(classifiers, "2.6")
        has_support_27 = utils.supports(classifiers, "2.7")
        has_support_34 = utils.supports(classifiers, "3.4")

        # Assert
        self.assertEqual(has_support_26, "no")
        self.assertEqual(has_support_27, "yes")
        self.assertEqual(has_support_34, "no")

    def test_supports_3_only_only(self):
        # Arrange
        classifiers = [
            "Programming Language :: Python :: 3 :: Only",
        ]

        # Act
        has_support_26 = utils.supports(classifiers, "2.6")
        has_support_34 = utils.supports(classifiers, "3.4")

        # Assert
        self.assertEqual(has_support_26, "no")
        self.assertEqual(has_support_34, "maybe")

    def test_supports_3_only_plus_others(self):
        # Arrange
        classifiers = [
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3 :: Only",
        ]

        # Act
        has_support_26 = utils.supports(classifiers, "2.6")
        has_support_32 = utils.supports(classifiers, "3.2")
        has_support_34 = utils.supports(classifiers, "3.4")

        # Assert
        self.assertEqual(has_support_26, "no")
        self.assertEqual(has_support_32, "no")
        self.assertEqual(has_support_34, "yes")


if __name__ == '__main__':
    unittest.main()

# End of file
