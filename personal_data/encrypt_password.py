#!/usr/bin/env python3
"""Utilities for securely hashing user passwords."""


def hash_password(password: str) -> bytes:
    """Return a salted bcrypt hash of the provided plain-text password."""
    import bcrypt

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
