def write_to_file():
  """
  Creates a new text file named "my_file.txt" and writes content to it.
  """
  try:
    with open("my_file.txt", "w") as file:
      file.write("This is the first line.\n")
      file.write("Here's some data: 42\n")
      file.write("And a string to mix things up.\n")
  except PermissionError:
    print("Error: Insufficient permissions to write to the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def read_from_file():
  """
  Reads the contents of "my_file.txt" and displays them on the console.
  """
  try:
    with open("my_file.txt", "r") as file:
      contents = file.read()
      print(contents)
  except FileNotFoundError:
    print("Error: File 'my_file.txt' not found.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def append_to_file():
  """
  Opens "my_file.txt" in append mode and writes additional content.
  """
  try:
    with open("my_file.txt", "a") as file:
      file.write("Appending some more lines...\n")
      file.write("Numbers don't hurt: 3.14\n")
      file.write("The end.\n")
  except PermissionError:
    print("Error: Insufficient permissions to write to the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
  write_to_file()
  read_from_file()
  append_to_file()
  read_from_file()  # Read again to show appended content
