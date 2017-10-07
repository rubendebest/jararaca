from lib.color_printer import ColorPrinter

class SnsProject:
  def __init__(self, config, sns_defaults, project):
    self.config = config
    self.sns_defaults = sns_defaults
    self.project = project.get('project')
    self.env = project.get('env') or sns_defaults.env
    self.region = project.get('region') or sns_defaults.region
    if project.get('raw_message') is None:
      self.raw_message = sns_defaults.raw_message
    else:
      self.raw_message = project.get('raw_message')
    if config.verbose:
      print(f"Success loading sns_project {self.project}.")

  def dump(self):
    cp = ColorPrinter(self.config.verbose)
    print(f"  {self.project}")
    cp.puts(f"    env:         {self.env}", self.env, self.sns_defaults.env)
    cp.puts(f"    region:      {self.region}", self.region, self.sns_defaults.region)
    cp.puts(f"    raw_message: {self.raw_message}", self.raw_message, self.sns_defaults.raw_message)

  def __hash__(self):
    return(hash((self.project, self.env, self.region)))

  def __eq__(self, other):
    return(self.project, self.env, self.region == other.project, other.env, other.region)

  @staticmethod
  def find(projects, name):
    project = [p for p in projects if p.project == name]
    if(len(project)) == 0:
      raise Exception(f"Unable to find project with {name}")
    elif(len(project)) > 1:
      raise Exception(f"More than one project with {name} found.")
    return project[0]
