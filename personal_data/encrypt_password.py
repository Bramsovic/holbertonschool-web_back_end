#!/usr/bin/env python3
"""Utilities for securely hashing user passwords."""


def hash_password(password: str) -> bytes:
    """Return a salted bcrypt hash of the provided plain-text password."""
    import bcrypt

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Return whether the plain-text password matches the bcrypt hash."""
    import bcrypt

    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
