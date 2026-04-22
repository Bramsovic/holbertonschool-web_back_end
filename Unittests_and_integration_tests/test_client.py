#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class defined in client.py."""

import unittest
from unittest.mock import PropertyMock, patch

from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json) -> None:
        """Check that GithubOrgClient.org returns the expected payload."""
        expected_payload = {"login": org_name}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)

        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )

    def test_public_repos_url(self) -> None:
        """Check that _public_repos_url returns the repos URL from org."""
        expected_url = "https://api.github.com/orgs/google/repos"
        payload = {"repos_url": expected_url}

        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")

            self.assertEqual(client._public_repos_url, expected_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json) -> None:
        """Check that public_repos returns the expected repository names."""
        expected_url = "https://api.github.com/orgs/google/repos"
        payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = payload

        with patch.object(
            GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = expected_url
            client = GithubOrgClient("google")

            self.assertEqual(
                client.public_repos(), ["repo1", "repo2", "repo3"]
            )
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(expected_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
        self, repo: dict, license_key: str, expected: bool
    ) -> None:
        """Check that has_license returns the expected boolean."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected
        )


if __name__ == "__main__":
    unittest.main()
