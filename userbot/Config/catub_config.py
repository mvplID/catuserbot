# config values will be loaded from here

from os import environ

ENV = bool(environ.get("ENV", False))

# fmt: off
if ENV:
    from sample_config import Config
else:
    if os.path.exists("config.py"):
        from config import Development as Config
# fmt: on
