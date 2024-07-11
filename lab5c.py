#!/usr/bin/env python3
# Author ID: sshrestha83@myseneca.ca

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
  try:
      output = int(number1) + int(number2)
      return output
  except ValueError:
        return 'error: could not add numbers'
def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        return 'error: could not read file'
if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
