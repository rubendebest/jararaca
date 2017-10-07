from default_test_case import DefaultTestCase

class TestSnsDefaults(DefaultTestCase):
  def test_sns_defaults(self):
    sns_defaults = self.loaded_config.sns_defaults
    self.assertEqual(sns_defaults.env, 'default_sns_env')
    self.assertEqual(sns_defaults.raw_message, False)
    self.assertEqual(sns_defaults.region, 'default_sns_region')

if __name__ == '__main__':
  unittest.main()
