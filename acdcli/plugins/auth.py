"""
This is a template that you can use for adding custom plugins.
"""

import json
from . import *
from ..api import oauth
import acd_cli


class AuthPlugin(Plugin):
    MIN_VERSION = '0.3.1'

    @classmethod
    def attach(cls, subparsers: argparse.ArgumentParser, log: list, **kwargs):
        """ Attaches this plugin to the top-level argparse subparser group
        :param subparsers the action subparser group
        :param log a list to put initialization log messages in
         """
        p = subparsers.add_parser('get-auth', add_help=False)
        p.set_defaults(func=cls.action)

        log.append(str(cls) + ' attached.')

    @classmethod
    def action(cls, args: argparse.Namespace) -> int:
        handler = oauth.create_handler(acd_cli.CACHE_PATH)
        print(json.dumps(handler.oauth_data))
        return 0
