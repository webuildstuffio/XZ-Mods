"""Pilot probe for the qodo-review v3.9.0 wiring test.

Exists only to give the reviewer something concrete to
suggest on; not for merge.
"""


def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags


def collect_names(records):
    names = []
    for record in records:
        if record.get("name"):
            names.append(record["name"].strip().lower())
    return names
