#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  if(argc != 2) {
    fprintf(stderr, "Usage: %s <ENV NAME>\n", argv[0]);
    exit(1);
  }
  printf("%s: %p\n", argv[1], getenv(argv[1]));
  return 0;
}

