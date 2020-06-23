# Functional programming utilities
Some nifty tools in Python.

- `decorator` a function to help writing decorators
- `auto_shelve.cache` a decorator to cache function results to disk

## Decorator
Facilitates arbitrary keyword arguments to functions decorators. You may define a decorator:

```python
from decorator import decorator
from functools import wraps

@decorator
def my_decorator(f, extra_arg=None):
    @wraps(f)
    def g(x):
        ...
    return g
```

And then use your decorator with or without extra arguments:

```python
@my_decorator
def a(x):
    pass

@my_decorator(extra_arg=42)
def b(x):
    pass
```

## Cache
Auto-shelve, assumes you have a function that takes formatable arguments, and serialisable output. You decorate an expensive function `auto_shelve.cache`, and presto:

```python
from auto_shelve import cache

@cache(path="cache.db")
def expensive_func(x):
    ...
```

The arguments to the function are combined into a string (via `inspect.signature`, so it is smart about default arguments). This string is used as a key into a `shelve` database. The default `path` argument is `"cache.db"` in the current work dir.
