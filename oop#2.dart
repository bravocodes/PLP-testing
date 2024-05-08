# Define an interface
class Drawable:
  def draw(self):
    pass

# Define a base class
class Shape(Drawable):
  def __init__(self, color):
    self.color = color

  def get_info(self):
    return f"Shape: color - {self.color}"

# Define a child class that inherits from Shape and overrides the draw method
class Circle(Shape):
  def __init__(self, color, radius):
    super().__init__(color)
    self.radius = radius

  def draw(self):
    print(f"Drawing a {self.color} circle with radius {self.radius}")

# Define a function to read data from a file and create a circle object
def create_circle_from_file(filename):
  try:
    with open(filename, 'r') as file:
      data = file.readline().split(',')
      color = data[0].strip()
      radius = float(data[1].strip())
      return Circle(color, radius)
  except FileNotFoundError:
    print(f"Error: File {filename} not found.")
    return None

# Create an instance of Circle from a file
circle = create_circle_from_file("circle_data.txt")

# Check if circle was created successfully
if circle:
  # Demonstrate the use of a loop by drawing the circle multiple times
  for i in range(3):
    circle.draw()
  # Print circle information using the inherited method
  print(circle.get_info())
