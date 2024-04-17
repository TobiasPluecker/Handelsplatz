# Import magic
try:
  import stockmarket
except ImportError as e:
  print(f"Importing the shared library 'stockmarket' did not work.")
  print(f"Is (a link to) the shared library 'stockmarket.____.so' in the same directory as this python script?")
  print(f"The import caused the following exception '{e}'")
  print(f"Exiting")
  exit(1)
else:
  print(f"Importing the shared library 'stockmarket' did work.")


import pydoc


def main():
  print(f"Module name: '{stockmarket.__doc__}'")


if __name__ == '__main__':
  main()
