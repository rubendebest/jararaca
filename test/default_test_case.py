import unittest
import click
from lib.config_loader import ConfigLoader

class Config(object):
  def __init__(self):
    self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure = True)

class DefaultTestCase(unittest.TestCase):
  def setUp(self):
    self.loaded_config = ConfigLoader(Config(), 'test/source_for_tests.yml')

  def tearDown(self):
    pass

#if __name__ == '__main__':
#  unittest.main()
