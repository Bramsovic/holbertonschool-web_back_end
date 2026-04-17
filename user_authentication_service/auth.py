#!/usr/bin/env python3
"""Auth module."""

import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a new UUID and return its string representation."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize Auth."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Validate a user's login credentials."""
        try:
            user = self._db.find_user_by(email=email)
            hashed_password = user.hashed_password
            if isinstance(hashed_password, str):
                hashed_password = hashed_password.encode("utf-8")
            return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session ID for an existing user."""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
