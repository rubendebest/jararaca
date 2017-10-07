from termcolor import colored
class ColorPrinter:
  def __init__(self, verbose = False):
    self.verbose = verbose

  def puts(self, text, to_print = None, to_compare = None):
    if to_print == to_compare:
      if self.verbose or (to_print is None and to_compare is None):
        print(colored(text, 'green'))
    else:
      print(colored(text, 'yellow'))
