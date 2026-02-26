#!/usr/bin/env python3
"""Define the base authentication class used by the API."""
from typing import List, TypeVar
from flask import request


class Auth:
    """Represent a template authentication class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return whether authentication is required for a path."""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path is None:
                continue
            if not excluded_path.endswith('/'):
                excluded_path += '/'
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Return the authorization header from a Flask request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user resolved from a Flask request."""
        return None
