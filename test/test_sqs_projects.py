from default_test_case import DefaultTestCase
from sqs_project import SqsProject

class TestSqsProjects(DefaultTestCase):
  def test_project_with_defaults(self):
    project = SqsProject.find(self.loaded_config.sqs_projects, 'project_with_defaults')
    self.assertEqual(project.deadletter, False)
    self.assertEqual(project.env, 'default_sqs_env')
    self.assertEqual(project.max_receive_count, 7)
    self.assertEqual(project.message_retention_period, 1209600)
    self.assertEqual(project.region, 'default_sqs_region')
    self.assertEqual(project.visibility_timeout, 60)

  def test_project_with_custom_deadletter(self):
    project = SqsProject.find(self.loaded_config.sqs_projects, 'project_with_custom_deadletter')
    self.assertEqual(project.deadletter, True)
    self.assertEqual(project.env, 'default_sqs_env')
    self.assertEqual(project.max_receive_count, 7)
    self.assertEqual(project.message_retention_period, 1209600)
    self.assertEqual(project.region, 'default_sqs_region')
    self.assertEqual(project.visibility_timeout, 60)

  def test_project_with_custom_env(self):
    project = SqsProject.find(self.loaded_config.sqs_projects, 'project_with_custom_env')
    self.assertEqual(project.deadletter, False)
    self.assertEqual(project.env, 'custom_sqs_env')
    self.assertEqual(project.max_receive_count, 7)
    self.assertEqual(project.message_retention_period, 1209600)
    self.assertEqual(project.region, 'default_sqs_region')
    self.assertEqual(project.visibility_timeout, 60)

  def test_project_with_custom_max_receive_count(self):
    project = SqsProject.find(self.loaded_config.sqs_projects, 'project_with_custom_max_receive_count')
    self.assertEqual(project.deadletter, False)
    self.assertEqual(project.env, 'default_sqs_env')
    self.assertEqual(project.max_receive_count, 1000)
    self.assertEqual(project.message_retention_period, 1209600)
    self.assertEqual(project.region, 'default_sqs_region')
    self.assertEqual(project.visibility_timeout, 60)

  def test_project_with_custom_message_retention_period(self):
    project = SqsProject.find(self.loaded_config.sqs_projects, 'project_with_custom_message_retention_period')
    self.assertEqual(project.deadletter, False)
    self.assertEqual(project.env, 'default_sqs_env')
    self.assertEqual(project.max_receive_count, 7)
    self.assertEqual(project.message_retention_period, 1234)
    self.assertEqual(project.region, 'default_sqs_region')
    self.assertEqual(project.visibility_timeout, 60)

  def test_project_with_custom_region(self):
    project = SqsProject.find(self.loaded_config.sqs_projects, 'project_with_custom_region')
    self.assertEqual(project.deadletter, False)
    self.assertEqual(project.env, 'default_sqs_env')
    self.assertEqual(project.max_receive_count, 7)
    self.assertEqual(project.message_retention_period, 1209600)
    self.assertEqual(project.region, 'custom_sqs_region')
    self.assertEqual(project.visibility_timeout, 60)

  def test_project_with_custom_visibility_timeout(self):
    project = SqsProject.find(self.loaded_config.sqs_projects, 'project_with_custom_visibility_timeout')
    self.assertEqual(project.deadletter, False)
    self.assertEqual(project.env, 'default_sqs_env')
    self.assertEqual(project.max_receive_count, 7)
    self.assertEqual(project.message_retention_period, 1209600)
    self.assertEqual(project.region, 'default_sqs_region')
    self.assertEqual(project.visibility_timeout, 120)

if __name__ == '__main__':
  unittest.main()
