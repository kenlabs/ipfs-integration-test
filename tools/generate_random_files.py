#!/usr/bin/env python3

import sys
import os
import random

LETTERS = [' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def usage():
    print("""
USAGE
  generate_random_files.py [target-dir] [file-size] [file-count] 
""")


def setup_dir(target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)


def generate_file(target_file, file_size):
    f = open(target_file, 'w')
    letters_len = len(LETTERS)
    for n in range(file_size):
        index = random.randint(0, letters_len - 1)
        f.write(LETTERS[index])
    f.close()


def generate_files(target_dir, file_size, file_count):
    setup_dir(target_dir)
    for n in range(file_count):
        target_file = os.path.join(target_dir, "random_file_%d.txt" % (n + 1))
        generate_file(target_file, file_size)


def main():
    if len(sys.argv) < 4:
        usage()
        return

    target_dir = sys.argv[1]
    file_size = int(sys.argv[2])
    file_count = int(sys.argv[3])

    generate_files(target_dir, file_size, file_count)


if __name__ == '__main__':
    main()
