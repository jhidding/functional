import shelve
import functools
from decorator import decorator
from pathlib import Path
from inspect import signature
from itertools import chain


@decorator
def cache(f, path=Path("cache.db")):
    """Wraps a function so that results are cached in a shelve."""
    db = shelve.open(str(path))

    @functools.wraps(f)
    def g(*args, **kwargs):
        bound_args = signature(f).bind(*args, **kwargs)
        bound_args.apply_defaults()
        argstrs = chain(
            (f"{a}" for a in bound_args.args),
            (f"{k}={v}" for k, v in bound_args.kwargs.items()))
        call_sig = f"{f.__name__}(" + ",".join(argstrs) + ")"
        if call_sig not in db:
            db[call_sig] = f(*bound_args.args, **bound_args.kwargs)
        return db[call_sig]

    return g


def test_cache(tmpdir):
    tmpdir = Path(tmpdir)
    log = []

    @cache(path=tmpdir/"cache.db")
    def f1(x=3):
        log.append(f"computing f({x})")
        return x*x

    assert f1() == 9
    assert f1(x=3) == 9
    assert len(log) == 1

    assert f1(4) == 16
    assert len(log) == 2
    assert log[-1] == "computing f(4)"

    assert f1(x=4) == 16
    assert len(log) == 2

    assert f1(5) == 25
    assert log[-1] == "computing f(5)"
