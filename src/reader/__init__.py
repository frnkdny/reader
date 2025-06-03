"""Real Python feed reader.

Import the `feed` module to work with the Real Python feed:

    >>> from reader import feed
    >>> feed.get_titles()
    ['Logging in Python', 'The Best Python Books', ...]

See https://github.com/realpython/reader/ for more information.
"""
# Standard library imports
from importlib import resources

try:
    import tomllib
except ModuleNotFoundError:
    # Third party imports
    import tomli as tomllib


# Version of realpython-reader package
__version__ = "1.1.2"

# Read URL of the Real Python feed from config file
try:
    from importlib.resources import files
except ImportError:
    _cfg = tomllib.loads(resources.read_text("reader", "config.toml"))
else:
    _cfg = tomllib.loads((files("reader") / "config.toml").read_text())

URL = _cfg["feed"]["url"]
