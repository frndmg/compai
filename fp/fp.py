from functools import partial, reduce, wraps
from operator import itemgetter


def compose(*F):
    return reduce(lambda f, g: lambda x: f(g(x)), F)


def fmap(f):
    return partial(map, f)


def ffilter(f):
    return partial(filter, f)


def none_map(func, if_none=None):
    """Returns a function that will call func if the argument is not none, and return if_none otherwise.
    >>> f = none_map(str, if_none=const(1))
    >>> f(1)
    '1'
    >>> f(None)
    1
    """

    @wraps(func)
    def _func(x):
        if x is not None:
            return func(x)

        return if_none()

    return _func


def tupled(func):
    """Returns a tupled version of the function.
    >>> tupled(lambda a, b: a + b)((2, 3))
    5
    """

    @wraps(func)
    def _func(x):
        return func(*x)

    return _func


def tuple_map(*fs):
    """Returns a function that will apply every f_i for evey element of the tuple argument.
    >>> inc = lambda x: x + 1
    >>> tuple_map(None, inc)((1, 2))
    (1, 3)
    >>> tuple_map(inc)((1, 2))
    (2, 2)
    """

    return compose(
        tuple,
        fmap(
            tupled(lambda i, v: fs[i](v) if i < len(fs) and fs[i] else v),
        ),
        enumerate,
    )


def identity(x):
    return x


def apply(f, *args):
    return f(*args)


def const(x):
    """Returns a function that will always return `x`.
    >>> f = const('foo')
    >>> f()
    'foo'
    >>> f(1, a='brr')
    'foo'
    """

    return lambda *_, **__: x


def length(xs):
    """Returns the length of xs.
    >>> length([1, 2, 3])
    3
    >>> length(range(10))
    10
    >>> length(None for _ in range(10))
    10
    """

    len_ = getattr(xs, '__len__', None)

    def default_len():
        return sum(1 for _ in xs)

    return compose(
        apply,
        none_map(identity, if_none=const(default_len))
    )(len_)


def swap(x):
    return itemgetter(1, 0)(x)
