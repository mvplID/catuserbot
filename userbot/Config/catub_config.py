from os import environ

# config values will be loaded from here

ENV = bool(environ.get("ENV", False))

if ENV:
    from sample_config import Config
else:
    if os.path.exists("config.py"):
        from config import Development as Config
