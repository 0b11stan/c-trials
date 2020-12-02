#include "stdbool.h"
#include "stdint.h"
#include "stdio.h"
#include "stdlib.h"

bool isroot(size_t value) { return value == SIZE_MAX; }

void Display(size_t* set, size_t size) {
  for (int x = 0; x < size; x++) {
    if (isroot(set[x]))
      printf("P ");
    else
      printf("%zu ", set[x]);
  }
  printf("\n");
}

void MakeSet(size_t* set, size_t size) {
  for (int x = 0; x < size; x++) set[x] = SIZE_MAX;
}

bool Union(size_t* set, size_t parent, size_t children) {
  if (!isroot(set[children])) return false;
  set[children] = parent;
  return true;
}

size_t FindRoot(size_t* set, size_t element) {
  if (isroot(set[element]))
    return element;
  else
    FindRoot(set, set[element]);
}

void _RecurseReplace(size_t* set, size_t element, size_t new_parent) {
  if (set[element] != new_parent && !isroot(set[element]))
    _RecurseReplace(set, set[element], new_parent);
  set[element] = new_parent;
}

void FindReplace(size_t* set, size_t element, size_t new_parent) {
  _RecurseReplace(set, set[element], new_parent);
  set[element] = SIZE_MAX;
}

void FindCompress(size_t* set, size_t element) {
  size_t root = FindRoot(set, element);
  _RecurseReplace(set, set[element], root);
  set[element] = root;
}

int main() {
  size_t SET_SIZE = 10;
  size_t set[SET_SIZE];
  size_t root;
  bool success;

  // test successful union of 2 parents
  MakeSet(set, SET_SIZE);
  success = Union(set, 0, 1);
  if (!success || set[1] != 0) return EXIT_FAILURE;

  // test union of an already united children
  MakeSet(set, SET_SIZE);
  Union(set, 0, 1);
  success = Union(set, 2, 1);
  if (success) return EXIT_FAILURE;

  // test find on a root element
  MakeSet(set, SET_SIZE);
  root = FindRoot(set, 0);
  if (root != 0) return EXIT_FAILURE;

  // test find with one level deepness
  MakeSet(set, SET_SIZE);
  Union(set, 0, 1);
  root = FindRoot(set, 1);
  if (root != 0) return EXIT_FAILURE;

  // test find with two level deepness
  MakeSet(set, SET_SIZE);
  Union(set, 0, 1);
  Union(set, 1, 2);
  root = FindRoot(set, 2);
  if (root != 0) return EXIT_FAILURE;

  // test find with five level deepness
  MakeSet(set, SET_SIZE);
  Union(set, 0, 1);
  Union(set, 1, 2);
  Union(set, 2, 3);
  Union(set, 3, 4);
  Union(set, 4, 5);
  root = FindRoot(set, 2);
  if (root != 0) return EXIT_FAILURE;

  // test find replace
  MakeSet(set, SET_SIZE);
  Union(set, 0, 1);
  Union(set, 1, 2);
  Union(set, 2, 3);
  Union(set, 3, 4);
  Union(set, 4, 5);
  FindReplace(set, 3, 5);
  if (!(FindRoot(set, 0) == 3 && FindRoot(set, 1) == 3 &&
	FindRoot(set, 2) == 3 && FindRoot(set, 4) == 3 &&
	FindRoot(set, 5) == 3))
    return EXIT_FAILURE;

  // test find compress
  MakeSet(set, SET_SIZE);
  Union(set, 0, 1);
  Union(set, 1, 2);
  Union(set, 2, 3);
  Union(set, 3, 4);
  Union(set, 4, 5);
  FindCompress(set, 4);
  if (!(set[0] == SIZE_MAX && set[1] == 0 && set[2] == 0 && set[4] == 0 &&
	set[5] != 3))
    return EXIT_FAILURE;

  return 0;
}
