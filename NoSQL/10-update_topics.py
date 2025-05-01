#!/usr/bin/env python3
"""Update school topics in MongoDB collection."""


def update_topics(mongo_collection, name, topics):
    """Update topics of a school document by name."""
    update_result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return update_result.modified_count
