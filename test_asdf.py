#!/usr/bin/env python3
"""
Tests for the asdf utility.
"""

import unittest
from asdf import asdf_pattern, asdf_reverse, asdf_keyboard_row


class TestAsdfUtility(unittest.TestCase):
    """Test cases for asdf utility functions."""
    
    def test_asdf_pattern_default(self):
        """Test default pattern generation."""
        self.assertEqual(asdf_pattern(), "asdfasdfasdfasdf")
    
    def test_asdf_pattern_custom_length(self):
        """Test pattern generation with custom length."""
        self.assertEqual(asdf_pattern(2), "asdfasdf")
        self.assertEqual(asdf_pattern(1), "asdf")
    
    def test_asdf_reverse(self):
        """Test reverse pattern."""
        self.assertEqual(asdf_reverse(), "fdsa")
    
    def test_asdf_keyboard_row(self):
        """Test keyboard home row."""
        self.assertEqual(asdf_keyboard_row(), "asdfghjkl")


if __name__ == "__main__":
    unittest.main()
