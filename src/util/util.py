import argparse
from config import config


def validate_env_name(env_name):
    if env_name not in config:
        raise argparse.ArgumentTypeError("Invalid environment value: {environment_name}".
                                         format(environment_name=env_name))
    return env_name
