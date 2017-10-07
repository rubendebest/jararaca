import yaml

from lib.sqs_queue import SqsQueue
from lib.sns_topic import SnsTopic
from lib.sqs_defaults import SqsDefaults
from lib.sns_defaults import SnsDefaults
from lib.sqs_project import SqsProject
from lib.sns_project import SnsProject
from lib.subscription import Subscription

class ConfigLoader:
  def __init__(self, config, config_file):
    self.config = config
    self.config_file = config_file
    with open(config_file) as source:
      self.config_data = yaml.load(source)
    self.__set_sqs_defaults()
    self.__set_sns_defaults()
    self.__set_sqs_projects()
    self.__set_sns_projects()
    self.__set_sqs_queues()
    self.__set_sns_topics()
    self.__set_subscriptions()

  def describe(self):
    print("")
    self.sns_defaults.dump()

    print("")
    self.sqs_defaults.dump()

    print("")
    print("SnsProjects are:")
    for sns_project in self.sns_projects:
      sns_project.dump()
      print("")

    print("SnsTopics are:")
    for sns_topic in self.sns_topics:
      sns_topic.dump()
      print("")

    print("SqsProjects are:")
    for sqs_project in self.sqs_projects:
      sqs_project.dump()
      print("")

    print("SqsQueues are:")
    for sqs_queue in self.sqs_queues:
      sqs_queue.dump()
      print("")

    print("Subscriptions are:")
    Subscription.dump(self.subscriptions)

  def __print_item(self, item):
    print(f"    {item}")

  def __set_sqs_defaults(self):
    self.sqs_defaults = SqsDefaults(self.config, self.config_data['default']['queues'])

  def __set_sns_defaults(self):
    self.sns_defaults = SnsDefaults(self.config, self.config_data['default']['topics'])

  def __set_sqs_projects(self):
    projects = []
    for project in self.config_data['queue_configs']:
      projects.append(SqsProject(self.config, self.sqs_defaults, project))
    self.sqs_projects = set(projects)

  def __set_sns_projects(self):
    projects = []
    for project in self.config_data['topic_configs']:
      projects.append(SnsProject(self.config, self.sns_defaults, project))
    self.sns_projects = set(projects)

  def __set_sqs_queues(self):
    queues = []
    for node in self.config_data['all_queues']:
      for queue in node['queues']:
        project = SqsProject.find(self.sqs_projects, node['project'])
        queues.append(SqsQueue(self.config, project, queue))
    self.sqs_queues = set(queues)

  def __set_sns_topics(self):
    topics = []
    for node in self.config_data['all_topics']:
      for topic in node['topics']:
        project = SnsProject.find(self.sns_projects, node['project'])
        topics.append(SnsTopic(self.config, project, topic))
    self.sns_topics = set(topics)

  def __set_subscriptions(self):
    subscriptions = []
    for node in self.config_data['all_subscriptions']:
      for topic in node['topics']:
        topic_project = node['topic_project']
        topic_name = topic['name']
        for subscription in topic['subscriptions']:
          queue_project = subscription['queue_project']
          for queue_name in subscription['queues']:
            sns_topic = SnsTopic.find(self.sns_topics, topic_project, topic_name)
            sqs_queue = SqsQueue.find(self.sqs_queues, queue_project, queue_name)
            subscriptions.append(Subscription(self.config, sns_topic, sqs_queue))
    self.subscriptions = set(subscriptions)

  def create_queues(self):
    SqsQueue.create_queues(self.sqs_queues)

  def create_topics(self):
    SnsTopic.create_topics(self.sns_topics)

  def create_subscriptions(self):
    Subscription.create_subscriptions(self.subscriptions)

  def create_all(self):
    self.create_queues()
    self.create_topics()
    self.create_subscriptions()
