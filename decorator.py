import functools


def decorator(f):
    """Creates a paramatric decorator from a function. The resulting decorator
    will optionally take keyword arguments."""
    @functools.wraps(f)
    def decoratored_function(*args, **kwargs):
        if args and len(args) == 1 and callable(args[0]):
            return f(*args, **kwargs)

        if args:
            raise TypeError(
                "This decorator only accepts extra keyword arguments.")

        return lambda g: f(g, **kwargs)

    return decoratored_function


def test_decorator():
    import pytest

    @decorator
    def dec1(f, a=1, b=2):
        def g(*args, **kwargs):
            return (a, b, args, dict(kwargs), f())
        return g

    @dec1
    def f1():
        pass

    assert f1() == (1, 2, (), {}, None)
    assert f1(3, 4, foo="bar") == (1, 2, (3, 4), {"foo": "bar"}, None)

    @dec1(a="a", b="b")
    def f2():
        pass

    assert f2() == ("a", "b", (), {}, None)

    with pytest.raises(TypeError):
        @dec1(2)
        def f3():    # pragma: no cover
            pass

    with pytest.raises(TypeError):
        @dec1(print, 5)
        def f4():    # pragma: no cover
            pass
