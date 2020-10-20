# test_class.py - This is a simple example of writing a basic class and some code to test this class
class Test_Class:
  def __init__(self, id = "", name = "", value = 0.0, number = 0):
    self.id = id
    self.name = name
    self.value = value
    self.number = number
  def get_value(self):
    return self.value * self.number
  def display(self):
    print("{}: {} x {} @ {} = {}".format(self.id, self.name, self.number, self.value, self.get_value()))

def main():
    pencil = Test_Class(12345, "Pencil", 1.29, 7)
    print("Get value:", pencil.get_value())
    pencil.display()
if __name__ == "__main__":
    main()