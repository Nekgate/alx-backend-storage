#!/usr/bin/env python3
"""0. Create a Cache class. In the __init__ method, store an instance of
the Redis client as a private variable named _redis (using redis.Redis())
and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the
input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str,
bytes, int or float.
"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        if isinstance(data, (int, float)):
            data = str(data)
        self._redis.set(key, data)
        return key
