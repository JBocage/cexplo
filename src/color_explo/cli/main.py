"""This file implements a command line interface"""

import os

import click

from color_explo import __VERSION__
from color_explo.utils.paths import PackagePaths


class Config(object):
    """An object designed to conatin and pass the config"""

    def __init__(self) -> None:
        self.config = {}

    def set_config(self, key, value):
        """Sets a key-value pair into the config"""
        self.config[key] = value


@click.command()
@click.version_option(version=__VERSION__)
@click.pass_context
def cli(ctx, *args, **kwargs):
    """Loads all high level kwargs into the config"""
    ctx.obj = Config()
    for key, value in kwargs.items():
        ctx.obj.set_config(key, value)

    args = ctx.obj.config

    # Do something with the args
    print(args)

    os.system(f"streamlit run {PackagePaths.APP_START.as_posix()}")
