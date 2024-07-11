#!/usr/bin/env python3
# Author ID: sshrestha83

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return content



def read_file_list(file_name):
    # Takes a file_name as string for a file name
    f = open(file_name, 'r')
    # return its entire contents as a list of lines without new-line characters
    read_data = f.read()
    f.close()
    list_of_lines = read_data.splitlines()
    return list_of_lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))