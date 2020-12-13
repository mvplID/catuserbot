from os import environ

# config values will be loaded from here

ENV = bool(environ.get("ENV", False))

if ENV:
    pass
else:
    if os.path.exists("config.py"):
        pass
