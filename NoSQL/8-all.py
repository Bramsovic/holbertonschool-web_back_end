#!/usr/bin/env python3
"""List all documents in MongoDB collection."""


def list_all(mongo_collection):
    """Return all documents from given collection."""
    return list(mongo_collection.find())
