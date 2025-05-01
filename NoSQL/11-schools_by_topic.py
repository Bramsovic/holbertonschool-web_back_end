#!/usr/bin/env python3
"""
Module 11-schools_by_topic
Finds and returns all documents where
'topic' is in the 'topics' list.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools with a specific topic

    Args:
        mongo_collection: PyMongo collection object
        topic (str): topic to search for in the 'topics' array field

    Returns:
        List of documents (dicts) that match the query
    """
    return list(mongo_collection.find({"topics": topic}))
