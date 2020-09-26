#include <stdio.h>

void display_vector(int* vector) {
  size_t vlength = sizeof(vector) / sizeof(vector[0]);
  printf("[");
  for (int x = 0; x <= vlength; x++) {
    char* suffix = vlength == x ? "]\n" : ", ";
    printf("%d%s", vector[x], suffix);
  }
}

void scalar_product(unsigned* r, size_t len, unsigned* v1, unsigned* v2) {
  for (int x = 0; x < len; x++) r[x] = v1[x] * v2[x];
}

int main() {
  unsigned v1[] = {1, 2, 3};
  unsigned v2[] = {2, 3, 4};
  unsigned r[3];
	size_t length = sizeof v1 / sizeof v1[0];
  scalar_product(r, length, v1, v2);
  display_vector(r);
}
