class Human:
  def __init__(self, name):
    self.name = name
    print(f'Hello, {self.name}! Welcome to existence \U0001f609')

  @classmethod
  def species(cls):
    return 'Human is Homosapiens'

  @staticmethod
  def advice():
    return 'Use your brain and opposable thumb responsibly'
  