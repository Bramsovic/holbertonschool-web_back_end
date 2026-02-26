#!/usr/bin/env python3
"""Define the BasicAuth authentication class."""
import base64
from api.v1.auth.auth import Auth
from models.user import User


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Return the UTF-8 decoded value of a Base64 authorization part."""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Return the email and password from a decoded Basic header."""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> User:
        """Return the user matching the given email and password."""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            User.load_from_file()
            users = User.search({"email": user_email})
        except Exception:
            return None

        if len(users) == 0:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> User:
        """Return the current user from a request using Basic auth."""
        authorization_header = self.authorization_header(request)
        base64_authorization_header = (
            self.extract_base64_authorization_header(authorization_header)
        )
        decoded_base64_authorization_header = (
            self.decode_base64_authorization_header(
                base64_authorization_header
            )
        )
        user_email, user_pwd = self.extract_user_credentials(
            decoded_base64_authorization_header
        )
        return self.user_object_from_credentials(user_email, user_pwd)
