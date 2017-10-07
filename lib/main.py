from lib.config_loader import ConfigLoader

class Main:
  def __init__(self, config):
    self.config = config

  def describe(self, config_file):
    ConfigLoader(self.config, config_file).describe()

  def create_queues(self, config_file):
    ConfigLoader(self.config, config_file).create_queues()

  def create_topics(self, config_file):
    ConfigLoader(self.config, config_file).create_topics()

  def create_subscriptions(self, config_file):
    ConfigLoader(self.config, config_file).create_subscriptions()

  def create_all(self, config_file):
    ConfigLoader(self.config, config_file).create_all()
