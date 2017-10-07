from termcolor import colored
class ColorPrinter:
  def __init__(self, verbose = False):
    self.verbose = verbose

  def puts(text, printed_text, compared_text, wtf):
    if printed_text == compared_text:
      if self.verbose:
        print(printed_text)
    else:
      print(colored(printed_text, 'yellow'))
