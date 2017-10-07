from default_test_case import DefaultTestCase
from sns_topic import SnsTopic

class TestSnsTopics(DefaultTestCase):
  def test_topic_with_defaults(self):
    topic = SnsTopic.find(self.loaded_config.sns_topics, 'project_with_defaults', 'topic_with_defaults')
    self.assertEqual(topic.project_name, 'project_with_defaults')
    self.assertEqual(topic.env, 'default_sns_env')
    self.assertEqual(topic.region, 'default_sns_region')
    self.assertEqual(topic.raw_message, False)

  def test_topic_with_project_env(self):
    topic = SnsTopic.find(self.loaded_config.sns_topics, 'project_with_custom_env', 'topic_with_project_env')
    self.assertEqual(topic.project_name, 'project_with_custom_env')
    self.assertEqual(topic.env, 'custom_sns_env')
    self.assertEqual(topic.region, 'default_sns_region')
    self.assertEqual(topic.raw_message, False)

  def test_topic_with_project_region(self):
    topic = SnsTopic.find(self.loaded_config.sns_topics, 'project_with_custom_region', 'topic_with_project_region')
    self.assertEqual(topic.project_name, 'project_with_custom_region')
    self.assertEqual(topic.env, 'default_sns_env')
    self.assertEqual(topic.region, 'custom_sns_region')
    self.assertEqual(topic.raw_message, False)

  def test_topic_with_project_raw_message(self):
    topic = SnsTopic.find(self.loaded_config.sns_topics, 'project_with_custom_raw_message', 'topic_with_project_raw_message')
    self.assertEqual(topic.project_name, 'project_with_custom_raw_message')
    self.assertEqual(topic.env, 'default_sns_env')
    self.assertEqual(topic.region, 'default_sns_region')
    self.assertEqual(topic.raw_message, True)

  def test_topic_with_custom_raw_message(self):
    topic = SnsTopic.find(self.loaded_config.sns_topics, 'project_with_custom_raw_message', 'topic_with_custom_raw_message')
    self.assertEqual(topic.project_name, 'project_with_custom_raw_message')
    self.assertEqual(topic.env, 'default_sns_env')
    self.assertEqual(topic.region, 'default_sns_region')
    self.assertEqual(topic.raw_message, False)

if __name__ == '__main__':
  unittest.main()
