#include <stdlib.h>
#include <stdio.h>

unsigned long get_sp(void) {
  __asm__("movl %esp,%eax");
}

void main(int argc, char **argv) {
  printf("Stack Address: 0x%x\n", get_sp());
}

