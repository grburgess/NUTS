"""
This package implements the No-U-Turn Sampler (NUTS) algorithm 6 from the NUTS
paper (Hoffman & Gelman, 2011).

Content
-------

The package mainly contains:
  nuts6                     return samples using the NUTS
  numerical_grad            return numerical estimate of the local gradient
  emcee                     emcee NUTS sampler
"""

from .nuts import nuts6, numerical_grad
try:
    from .emcee_nuts import NUTSSampler
except ImportError:
    pass
