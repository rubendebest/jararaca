from lib.color_printer import ColorPrinter
import boto3

class Subscription:
  def __init__(self, config, topic, queue):
    self.config = config
    self.topic = topic
    self.queue = queue
    if self.topic.region.find('default') != -1 or self.topic.region.find('custom') != -1:
      pass
    else:
      self.resource = boto3.client('sns', region_name = self.topic.region)

  @staticmethod
  def dump(subscriptions):
    all_topics = set([s.topic for s in subscriptions])
    for topic in all_topics:
      print('')
      print(f"  {topic.complete_name}")
      for subscription in subscriptions:
        if subscription.topic == topic:
          print(f"    {subscription.queue.complete_name}")

  def create_subscription(self):
    print(f"Started subscribing {self.queue.complete_name} to {self.topic.complete_name}")
    topic_arn = self.topic.create_topic()
    queue_arn = self.queue.get_queue_arn(self.queue.complete_name)
    response = self.resource.subscribe(
      TopicArn = topic_arn,
      Protocol = 'sqs',
      Endpoint = queue_arn
    )
    subscription_arn = response['SubscriptionArn']
    print(f"Subscription created with arn {subscription_arn}")
    print("Configuring subscription.")
    self.resource.set_subscription_attributes(
      SubscriptionArn = subscription_arn,
      AttributeName = "RawMessageDelivery",
      AttributeValue = str(self.topic.raw_message)
    )
    print("Setting sqs permissions.")
    self.queue.add_publication_permission(topic_arn)
    print("")

  @staticmethod
  def find(subscriptions, topic, queue):
    subscription = [s for s in subscriptions if s.topic == topic and s.queue == queue]
    if(len(subscription)) == 0:
      raise Exception(f"Unable to find subscription")
    elif(len(subscription)) > 1:
      raise Exception(f"More than one subscription found")
    return subscription[0]

  @staticmethod
  def create_subscriptions(subscriptions):
    for subscription in subscriptions:
      subscription.create_subscription()
