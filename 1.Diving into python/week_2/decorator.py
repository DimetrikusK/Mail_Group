import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.JSONEncoder().encode(result)
    return wrapped
