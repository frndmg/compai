from importlib.metadata import version

from .compai import (apply, compose, const, ffilter, fmap, identity, length,
                     none_map, swap, tuple_map, tupled)

__version__ = version('fp-py')

__all__ = [
    'compose',
    'fmap',
    'none_map',
    'tupled',
    'const',
    'swap',
    'tuple_map',
    'length',
    'identity',
    'apply',
    'ffilter',
]
