from lib.color_printer import ColorPrinter
import boto3

class SnsTopic:
  def __init__(self, config, project, topic):
    self.config = config
    # Configs inherited from project
    self.project = project
    self.project_name = project.project
    self.env = project.env
    self.region = project.region
    # Configs specific to topic
    if topic.get('raw_message') is None:
      self.raw_message = self.project.raw_message
    else:
      self.raw_message = topic.get('raw_message')
    self.name = topic.get('name')
    self.__set_complete_name()
    if self.region.find('default') != -1 or self.region.find('custom') != -1:
      pass
    else:
      self.resource = boto3.client('sns', region_name = self.region)

  def dump(self):
    cp = ColorPrinter(self.config.verbose)
    print(f"  {self.complete_name}")
    cp.puts(f"    topic name:  {self.name}", self.name, self.name)
    cp.puts(f"    env:         {self.env}", self.env, self.project.env)
    cp.puts(f"    region:      {self.region}", self.region, self.project.region)
    cp.puts(f"    project:     {self.project_name}", self.project_name, self.project.project)
    cp.puts(f"    raw_message: {self.raw_message}", self.raw_message, self.project.raw_message)

  def __set_complete_name(self):
    self.complete_name= (f"{self.project_name}_{self.env}_{self.name}")

  def create_topic(self):
    print(f"Started creating topic {self.complete_name}")
    response = self.resource.create_topic(
      Name = self.complete_name
    )
    return(response['TopicArn'])

  @staticmethod
  def find(topics, project_name, topic_name):
    topic = [t for t in topics if t.project_name == project_name and t.name == topic_name]
    if(len(topic)) == 0:
      raise Exception(f"Unable to find queue with {project_name} and {queue_name}.")
    elif(len(topic)) > 1:
      raise Exception(f"More than one queues with {project_name} and {queue_name} found.")
    return topic[0]

  def __set_url(self):
    self.url = (f"{self.project_name}_{self.env}_{self.name}")

  @staticmethod
  def create_topics(topics):
    for topic in topics:
      topic.create_topic()
