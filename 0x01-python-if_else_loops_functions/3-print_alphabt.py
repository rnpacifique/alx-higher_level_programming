#!/usr/bin/python3

for letter in range(97,223):
    if chr(letter) != 113 and letter != 101:
        print("{:c}".format(letter), end="")
