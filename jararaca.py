#!/usr/bin/env python3
import click
from lib.main import Main


class Config(object):
    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True, help="verbose mode")
@pass_config
def cli(config, verbose):
    """ Complete setup for SQS and SNS based on config files."""
    config.verbose = verbose


@cli.command()
@click.argument('source_file')
@pass_config
def describe(config, source_file):
    """Shows what queues and topics will be created."""
    Main(config).describe(source_file)


@cli.command()
@click.argument('source_file')
@pass_config
def create_queues(config, source_file):
    """Create all aws queues"""
    Main(config).create_queues(source_file)


@cli.command()
@click.argument('source_file')
@pass_config
def create_topics(config, source_file):
    """Create all aws topics"""
    Main(config).create_topics(source_file)


@cli.command()
@click.argument('source_file')
@pass_config
def create_subscriptions(config, source_file):
    """Create all subscriptions"""
    Main(config).create_subscriptions(source_file)


@cli.command()
@click.argument('source_file')
@pass_config
def create_all(config, source_file):
    """Creates topics, queues and subscriptions."""
    Main(config).create_all(source_file)


if __name__ == '__main__':
    cli()
