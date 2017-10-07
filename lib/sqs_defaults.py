from lib.color_printer import ColorPrinter
class SqsDefaults:
  def __init__(self, config, config_data):
    self.config = config
    try:
      self.deadletter = config_data['deadletter']
      self.env = config_data['env']
      self.max_receive_count = config_data['max_receive_count']
      self.message_retention_period = config_data['message_retention_period']
      self.region = config_data['region']
      self.visibility_timeout = config_data['visibility_timeout']
    except KeyError as e:
      print(f"Required key {e} not found in sqs_config.")
    if config.verbose:
      print("Success loading SqsDefaults.")


  def dump(self):
    cp = ColorPrinter(self.config.verbose)
    print("SqsDefaults are:")
    cp.puts(f"  deadletter:               {self.deadletter}")
    cp.puts(f"  env:                      {self.env}")
    cp.puts(f"  region:                   {self.region}")
    cp.puts(f"  max_receive_count:        {self.max_receive_count}")
    cp.puts(f"  message_retention_period: {self.message_retention_period}")
    cp.puts(f"  visibility_timeout:       {self.visibility_timeout}")

