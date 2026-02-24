#!/usr/bin/env python3
"""Utilities for redacting sensitive fields from log messages."""

import logging
import os
import re
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Return a log message with the specified field values redacted."""
    pattern = (rf"({'|'.join(map(re.escape, fields))})="
               rf"[^{re.escape(separator)}]*")
    return re.sub(pattern, rf"\1={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """Format log records while redacting configured sensitive fields."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields that must be redacted."""
        super().__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """Return the formatted record with sensitive values redacted."""
        message = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR
        )


def get_logger() -> logging.Logger:
    """Create and return the application logger for user data."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.handlers = [handler]
    return logger


def get_db() -> object:
    """Return a MySQL connection using credentials from the environment."""
    import mysql.connector

    return mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME"),
    )


try:
    get_db.__annotations__["return"] = __import__(
        "mysql.connector.connection", fromlist=["MySQLConnection"]
    ).MySQLConnection
except ModuleNotFoundError:
    pass
