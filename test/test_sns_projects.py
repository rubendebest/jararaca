from default_test_case import DefaultTestCase
from sns_project import SnsProject

class TestSnsProjects(DefaultTestCase):
  def test_project_with_defaults(self):
    project = SnsProject.find(self.loaded_config.sns_projects, 'project_with_defaults')
    self.assertEqual(project.raw_message, False)
    self.assertEqual(project.env, 'default_sns_env')
    self.assertEqual(project.region, 'default_sns_region')

  def test_project_with_custom_env(self):
    project = SnsProject.find(self.loaded_config.sns_projects, 'project_with_custom_env')
    self.assertEqual(project.raw_message, False)
    self.assertEqual(project.env, 'custom_sns_env')
    self.assertEqual(project.region, 'default_sns_region')

  def test_project_with_custom_raw_message(self):
    project = SnsProject.find(self.loaded_config.sns_projects, 'project_with_custom_raw_message')
    self.assertEqual(project.raw_message, True)
    self.assertEqual(project.env, 'default_sns_env')
    self.assertEqual(project.region, 'default_sns_region')

  def test_project_with_custom_region(self):
    project = SnsProject.find(self.loaded_config.sns_projects, 'project_with_custom_region')
    self.assertEqual(project.raw_message, False)
    self.assertEqual(project.env, 'default_sns_env')
    self.assertEqual(project.region, 'custom_sns_region')

if __name__ == '__main__':
  unittest.main()
