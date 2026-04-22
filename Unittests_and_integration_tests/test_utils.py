#!/usr/bin/env python3
"""Unit tests for the utility helpers defined in utils.py."""

import unittest
from typing import Any, Mapping, Tuple
from unittest.mock import Mock, patch

from parameterized import parameterized

from utils import access_nested_map, get_json


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

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping[str, Any],
        path: Tuple[str, ...],
        expected_message: str,
    ) -> None:
        """Check that access_nested_map raises the expected KeyError."""
        with self.assertRaises(KeyError) as exc:
            access_nested_map(nested_map, path)

        self.assertEqual(str(exc.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
        self,
        test_url: str,
        test_payload: Mapping[str, bool],
    ) -> None:
        """Check that get_json returns the expected JSON payload."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch(
            "utils.requests.get", return_value=mock_response
        ) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
