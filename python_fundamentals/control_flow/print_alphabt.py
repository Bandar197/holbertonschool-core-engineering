#!/usr/bin/env python3
"""Print the lowercase alphabet except q and e."""

for letter in range(ord('a'), ord('z') + 1):
    if letter != ord('q') and letter != ord('e'):
        print("{}".format(chr(letter)),
              end="\n" if letter == ord('z') else "")
