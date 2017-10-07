from default_test_case import DefaultTestCase
from sqs_queue import SqsQueue

class TestSqsQueues(DefaultTestCase):
  def test_queue_with_defaults(self):
    queue = SqsQueue.find(self.loaded_config.sqs_queues, 'project_with_defaults', 'queue_with_defaults')
    self.assertEqual(queue.project_name, 'project_with_defaults')
    self.assertEqual(queue.deadletter, False)
    self.assertEqual(queue.env, 'default_sqs_env')
    self.assertEqual(queue.max_receive_count, 7)
    self.assertEqual(queue.message_retention_period, 1209600)
    self.assertEqual(queue.region, 'default_sqs_region')
    self.assertEqual(queue.visibility_timeout, 60)

  def test_queue_with_project_env(self):
    queue = SqsQueue.find(self.loaded_config.sqs_queues, 'project_with_custom_env', 'queue_with_project_env')
    self.assertEqual(queue.project_name, 'project_with_custom_env')
    self.assertEqual(queue.deadletter, False)
    self.assertEqual(queue.env, 'custom_sqs_env')
    self.assertEqual(queue.max_receive_count, 7)
    self.assertEqual(queue.message_retention_period, 1209600)
    self.assertEqual(queue.region, 'default_sqs_region')
    self.assertEqual(queue.visibility_timeout, 60)

# Max receive count tests
  def test_queue_with_project_max_receive_count(self):
    queue = SqsQueue.find(self.loaded_config.sqs_queues, 'project_with_custom_max_receive_count', 'queue_with_project_max_receive_count')
    self.assertEqual(queue.project_name, 'project_with_custom_max_receive_count')
    self.assertEqual(queue.deadletter, False)
    self.assertEqual(queue.env, 'default_sqs_env')
    self.assertEqual(queue.max_receive_count, 1000)
    self.assertEqual(queue.message_retention_period, 1209600)
    self.assertEqual(queue.region, 'default_sqs_region')
    self.assertEqual(queue.visibility_timeout, 60)

  def test_queue_with_custom_max_receive_count(self):
    queue = SqsQueue.find(self.loaded_config.sqs_queues, 'project_with_custom_max_receive_count', 'queue_with_custom_max_receive_count')
    self.assertEqual(queue.project_name, 'project_with_custom_max_receive_count')
    self.assertEqual(queue.deadletter, False)
    self.assertEqual(queue.env, 'default_sqs_env')
    self.assertEqual(queue.max_receive_count, 500)
    self.assertEqual(queue.message_retention_period, 1209600)
    self.assertEqual(queue.region, 'default_sqs_region')
    self.assertEqual(queue.visibility_timeout, 60)

# Message retention period tests
  def test_queue_with_project_message_retention_period(self):
    queue = SqsQueue.find(self.loaded_config.sqs_queues, 'project_with_custom_message_retention_period', 'queue_with_project_message_retention_period')
    self.assertEqual(queue.project_name, 'project_with_custom_message_retention_period')
    self.assertEqual(queue.deadletter, False)
    self.assertEqual(queue.env, 'default_sqs_env')
    self.assertEqual(queue.max_receive_count, 7)
    self.assertEqual(queue.message_retention_period, 1234)
    self.assertEqual(queue.region, 'default_sqs_region')
    self.assertEqual(queue.visibility_timeout, 60)

  def test_queue_with_custom_message_retention_period(self):
    queue = SqsQueue.find(self.loaded_config.sqs_queues, 'project_with_custom_message_retention_period', 'queue_with_custom_message_retention_period')
    self.assertEqual(queue.project_name, 'project_with_custom_message_retention_period')
    self.assertEqual(queue.deadletter, False)
    self.assertEqual(queue.env, 'default_sqs_env')
    self.assertEqual(queue.max_receive_count, 7)
    self.assertEqual(queue.message_retention_period, 2345)
    self.assertEqual(queue.region, 'default_sqs_region')
    self.assertEqual(queue.visibility_timeout, 60)

# Visibility timeout tests
  def test_queue_with_project_visibility_timeout(self):
    queue = SqsQueue.find(self.loaded_config.sqs_queues, 'project_with_custom_visibility_timeout', 'queue_with_project_visibility_timeout')
    self.assertEqual(queue.project_name, 'project_with_custom_visibility_timeout')
    self.assertEqual(queue.deadletter, False)
    self.assertEqual(queue.env, 'default_sqs_env')
    self.assertEqual(queue.max_receive_count, 7)
    self.assertEqual(queue.message_retention_period, 1209600)
    self.assertEqual(queue.region, 'default_sqs_region')
    self.assertEqual(queue.visibility_timeout, 120)

  def test_queue_with_custom_visibility_timeout(self):
    queue = SqsQueue.find(self.loaded_config.sqs_queues, 'project_with_custom_visibility_timeout', 'queue_with_custom_visibility_timeout')
    self.assertEqual(queue.project_name, 'project_with_custom_visibility_timeout')
    self.assertEqual(queue.deadletter, False)
    self.assertEqual(queue.env, 'default_sqs_env')
    self.assertEqual(queue.max_receive_count, 7)
    self.assertEqual(queue.message_retention_period, 1209600)
    self.assertEqual(queue.region, 'default_sqs_region')
    self.assertEqual(queue.visibility_timeout, 600)

if __name__ == '__main__':
  unittest.main()
