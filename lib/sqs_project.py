from lib.color_printer import ColorPrinter

class SqsProject:
  def __init__(self, config, sqs_defaults, project):
    self.config = config
    self.sqs_defaults = sqs_defaults
    self.project = project.get('project')
    if project.get('deadletter') is None:
      self.deadletter = sqs_defaults.deadletter
    else:
      self.deadletter = project.get('deadletter')
    self.env = project.get('env') or sqs_defaults.env
    self.max_receive_count = project.get('max_receive_count')\
                             or sqs_defaults.max_receive_count
    self.message_retention_period = project.get('message_retention_period') or sqs_defaults.message_retention_period
    self.region = project.get('region') or sqs_defaults.region
    self.visibility_timeout = project.get('visibility_timeout') or sqs_defaults.visibility_timeout
    if config.verbose:
      print(f"Success loading sqs_project {self.project}.")

  def dump(self):
    print(f"  {self.project}")
    cp = ColorPrinter(self.config.verbose)
    cp.puts(f"    deadletter:               {self.deadletter}", self.deadletter, self.sqs_defaults.deadletter)
    cp.puts(f"    env:                      {self.env}", self.env, self.sqs_defaults.env)
    cp.puts(f"    region:                   {self.region}", self.region, self.sqs_defaults.region)
    cp.puts(f"    max_receive_count:        {self.max_receive_count}", self.max_receive_count, self.sqs_defaults.max_receive_count)
    cp.puts(f"    message_retention_period: {self.message_retention_period}", self.message_retention_period, self.sqs_defaults.message_retention_period)
    cp.puts(f"    visibility_timeout:       {self.visibility_timeout}", self.visibility_timeout, self.sqs_defaults.visibility_timeout)

  @staticmethod
  def find(projects, name):
    project = [p for p in projects if p.project == name]
    if(len(project)) == 0:
      raise Exception(f"Unable to find project with {name}")
    elif(len(project)) > 1:
      raise Exception(f"More than one project with {name} found.")
    return project[0]

  def __hash__(self):
    return(hash((self.project, self.env, self.region)))

  def __eq__(self, other):
    return(self.project, self.env, self.region == other.project, other.env, other.region)
