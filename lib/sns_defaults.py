from lib.color_printer import ColorPrinter

class SnsDefaults:
  def __init__(self, config, config_data):
    self.config = config
    try:
      self.env = config_data['env']
      self.region = config_data['region']
      self.raw_message = config_data['raw_message']
    except KeyError as e:
      print(f"Required key {e} not found in sns_config.")
      quit()
    if config.verbose:
      print("Success loading SnsDefaults.")

  def dump(self):
    cp = ColorPrinter(self.config.verbose)
    print("SnsDefauls are:")
    cp.puts(f"  env:         {self.env}")
    cp.puts(f"  raw_message: {self.raw_message}")
    cp.puts(f"  region:      {self.region}")


