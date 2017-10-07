from default_test_case import DefaultTestCase

class TestSqsDefaults(DefaultTestCase):
  def test_sqs_defaults(self):
    sqs_defaults = self.loaded_config.sqs_defaults
    self.assertEqual(sqs_defaults.deadletter, False)
    self.assertEqual(sqs_defaults.env, 'default_sqs_env')
    self.assertEqual(sqs_defaults.max_receive_count, 7)
    self.assertEqual(sqs_defaults.message_retention_period, 1209600)
    self.assertEqual(sqs_defaults.region, 'default_sqs_region')
    self.assertEqual(sqs_defaults.visibility_timeout, 60)

if __name__ == '__main__':
  unittest.main()
