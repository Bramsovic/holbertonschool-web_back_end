#!/usr/bin/env python3
"""Define the BasicAuth authentication class."""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Represent the basic authentication mechanism."""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Return the Base64 part from a Basic authorization header."""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
