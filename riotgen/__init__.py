"""RIOT generator is a helper library for bootstraping RIOT code.

It can be used to generate:
- a new board support with the default structure
- a new driver support
- a new application
- a new test
"""

__version__ = '0.1.0-dev0'

from .generator import cli
