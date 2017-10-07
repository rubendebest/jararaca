from lib.color_printer import ColorPrinter
import boto3
import json

class SqsQueue:
  def __init__(self, config, project, queue):
    self.config = config
    # Configs inherited from project
    self.project = project
    self.project_name = project.project
    self.env = self.project.env
    self.region = project.region
    # Configs specific to queue
    if queue.get('deadletter') is None:
      self.deadletter = self.project.deadletter
    else:
      self.deadletter = queue.get('deadletter')
    self.max_receive_count = queue.get('max_receive_count') or self.project.max_receive_count
    self.message_retention_period = queue.get('message_retention_period') or self.project.message_retention_period
    self.visibility_timeout = queue.get('visibility_timeout') or self.project.visibility_timeout
    self.name = queue['name']
    self.__set_complete_name()
    if self.region.find('default') != -1 or self.region.find('custom') != -1:
      pass
    else:
      self.resource = boto3.client('sqs', region_name = self.region)

  def dump(self):
    cp = ColorPrinter(self.config.verbose)
    print(f"  {self.complete_name}")
    cp.puts(f"    name:                     {self.name}", self.name, self.name)
    cp.puts(f"    deadletter:               {self.deadletter}", self.deadletter, self.project.deadletter)
    cp.puts(f"    max_receive_count:        {self.max_receive_count}", self.max_receive_count, self.project.max_receive_count)
    cp.puts(f"    message_retention_period: {self.message_retention_period}", self.message_retention_period, self.project.message_retention_period)
    cp.puts(f"    visibility_timeout:       {self.visibility_timeout}", self.visibility_timeout, self.project.visibility_timeout)
    cp.puts(f"    env:                      {self.env}", self.env, self.project.env)
    cp.puts(f"    region:                   {self.region}", self.region, self.project.region)
    cp.puts(f"    project:                  {self.project_name}", self.project_name, self.project.project)

  def __set_complete_name(self):
    self.complete_name= (f"{self.project_name}_{self.env}_{self.name}")

  def create_queue(self):
    if self.deadletter:
      # Deadletter queue creation
      print(f"Started creating queue  {self.deadletter_name()}")
      self.resource.create_queue(QueueName = self.deadletter_name())
      print(f"Setting attributes for {self.deadletter_name()}")
      self.resource.set_queue_attributes(
       QueueUrl = self.get_queue_url(self.deadletter_name()),
       Attributes = {
         'MessageRetentionPeriod': '1209600'
       }
      )
    print(f"Started creating queue  {self.complete_name}")
    self.resource.create_queue(
      QueueName=self.complete_name
    )
    print(f"Setting attributes for {self.complete_name}")
    self.resource.set_queue_attributes(
      QueueUrl = self.get_queue_url(self.complete_name),
      Attributes = {
        'MessageRetentionPeriod': str(self.message_retention_period),
        'VisibilityTimeout': str(self.visibility_timeout),
        'RedrivePolicy': self.build_redrive_policy()
      }
    )
    print('')

  def build_redrive_policy(self):
    policy = {
       'maxReceiveCount': self.max_receive_count,
       'deadLetterTargetArn': self.get_queue_arn(self.complete_name)
    }
    return(json.dumps(policy))

  def get_queue_policy(self):
    return(self.resource.get_queue_attributes(
      QueueUrl = self.get_queue_url(self.complete_name),
      AttributeNames = ['All']
    ))['Attributes']

  def get_queue_arn(self, queue_name):
    return(self.resource.get_queue_attributes(
      QueueUrl = self.get_queue_url(queue_name),
      AttributeNames = ['QueueArn']
    ))['Attributes']['QueueArn']

  def get_queue_url(self, queue_name):
    return(self.resource.get_queue_url(QueueName = queue_name))['QueueUrl']

  def deadletter_name(self):
    return(f"{self.complete_name}_failures")

  def add_publication_permission(self, topic_arn):
    current_policy = self.get_queue_policy().get('Policy')
    queue_arn = self.get_queue_arn(self.complete_name)
    policy = json.dumps(self.build_policy(topic_arn, queue_arn, current_policy))
    self.resource.set_queue_attributes(
     QueueUrl = self.get_queue_url(self.complete_name),
     Attributes = {
       'Policy': policy
       }
    )
  def build_policy(self, topic_arn, queue_arn, current_policy):
    if current_policy:
      statement = json.loads(current_policy)['Statement']
    else:
      statement = []
    statement.append(self.build_statement(topic_arn, queue_arn))
    return {
      "Version": "2012-10-17",
      "Id": f"{queue_arn}/SQSDefaultPolicy",
      "Statement": statement
    }

  def build_statement(self, topic_arn, queue_arn):
    return {
      "Sid": f"{topic_arn}_send_{queue_arn}",
      "Effect": "Allow",
      "Principal": { "AWS": "*" },
      "Action": "SQS:SendMessage",
      "Resource": queue_arn,
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": topic_arn
        }
      }
    }

  @staticmethod
  def find(queues, project_name, queue_name):
    queue = [q for q in queues if q.project_name == project_name and q.name == queue_name]
    if(len(queue)) == 0:
      raise Exception(f"Unable to find queue with {project_name} and {queue_name}.")
    elif(len(queue)) > 1:
      raise Exception(f"More than one queues with {project_name} and {queue_name} found.")
    return queue[0]

  @staticmethod
  def create_queues(queues):
    for queue in queues:
      queue.create_queue()

