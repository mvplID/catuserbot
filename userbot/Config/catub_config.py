# config values will be loaded from here

from os import environ

ENV = bool(environ.get("ENV", False))

# fmt: off
if ENV:
    pass
else:
    if os.path.exists("config.py"):
        pass
# fmt: on
