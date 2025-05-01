#!/usr/bin/env python3
"""Insert school documents into MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert new school document and return its ObjectId."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
