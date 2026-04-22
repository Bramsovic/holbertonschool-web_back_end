#!/usr/bin/env python3
"""Unit tests for the utility helpers defined in utils.py."""

import unittest
from typing import Any, Mapping, Tuple

from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping[str, Any],
        path: Tuple[str, ...],
        expected: Any,
    ) -> None:
        """Check that access_nested_map returns the expected value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
