#include <assert.h>
#include <stdbool.h>
#include <stdio.h>

bool vequals(size_t size, int vector1[], int vector2[]);
bool mequals(size_t size[], unsigned m1[][size[0]], unsigned m2[][size[0]]);
void display_vector(size_t size, int* vector);
void display_matrix(size_t size[], unsigned matrix[][size[0]]);
void vector_product(unsigned* output_vector, size_t size, unsigned* vector1,
		    unsigned* vector2);
unsigned vector_sum(size_t size, unsigned vector[]);
void matrix_product(size_t matrix1_size[], unsigned matrix1[][matrix1_size[0]],
		    size_t matrix2_size[], unsigned matrix2[][matrix2_size[0]],
		    unsigned output_matrix[][matrix2_size[1]]);
void extract_column(size_t col_index, unsigned column[], size_t matrix_size[],
		    unsigned matrix[][matrix_size[0]]);
void extract_line(size_t line_index, unsigned line[], size_t matrix_size[],
		  unsigned matrix[][matrix_size[0]]);

void test_simple_vector_product();
void test_matrix_product();

int main() {
  test_simple_vector_product();
  test_matrix_product();
}

bool vequals(size_t size, int* vector1, int* vector2) {
  for (int x = 0; x < size; x++)
    if (vector1[x] != vector2[x]) return false;
  return true;
}

bool mequals(size_t size[], unsigned m1[][size[0]], unsigned m2[][size[0]]) {
  for (int y = 0; y < size[1]; y++)
    for (int x = 0; x < size[0]; x++)
      if (m1[y][x] != m2[y][x]) return false;
  return true;
}

void extract_column(size_t col_index, unsigned column[], size_t matrix_size[],
		    unsigned matrix[][matrix_size[0]]) {
  for (int y = 0; y < matrix_size[1]; y++) column[y] = matrix[y][col_index];
}

void extract_line(size_t line_index, unsigned line[], size_t matrix_size[],
		  unsigned matrix[][matrix_size[0]]) {
  for (int x = 0; x < matrix_size[0]; x++) line[x] = matrix[line_index][x];
}

unsigned vector_sum(size_t size, unsigned vector[]) {
  unsigned sum = 0;
  for (int x = 0; x < size; x++) sum += vector[x];
  return sum;
}

void vector_product(unsigned* output_vector, size_t size, unsigned* vector1,
		    unsigned* vector2) {
  for (int x = 0; x < size; x++) output_vector[x] = vector1[x] * vector2[x];
}

void matrix_product(size_t matrix1_size[], unsigned matrix1[][matrix1_size[0]],
		    size_t matrix2_size[], unsigned matrix2[][matrix2_size[0]],
		    unsigned output_matrix[][matrix2_size[1]]) {
  size_t vlength = matrix1_size[1];
  unsigned column[vlength];
  unsigned line[vlength];
  unsigned product[vlength];
  for (int m1col = 0; m1col < matrix1_size[0]; m1col++) {
    for (int m2line = 0; m2line < matrix2_size[1]; m2line++) {
      extract_column(m1col, column, matrix1_size, matrix1);
      extract_line(m2line, line, matrix2_size, matrix2);
      vector_product(product, vlength, line, column);
      output_matrix[m2line][m1col] = vector_sum(vlength, product);
    }
  }
}

void display_vector(size_t size, int* vector) {
  printf("[");
  for (int x = 0; x < size; x++) {
    char* suffix = (size - 1) == x ? "]\n" : ", ";
    printf("%d%s", vector[x], suffix);
  }
}

void display_matrix(size_t size[], unsigned matrix[][size[0]]) {
  for (int y = 0; y < size[1]; y++) {
    unsigned line[size[0]];
    extract_line(y, line, size, matrix);
    display_vector(size[0], line);
  }
}

void test_simple_vector_product() {
  // arrange
  unsigned v1[] = {1, 2, 3};
  unsigned v2[] = {2, 3, 4};
  size_t length = sizeof v1 / sizeof v1[0];
  unsigned result[3];
  // act
  vector_product(result, length, v1, v2);
  // assert
  unsigned expect[] = {2, 6, 12};
  assert(vequals(length, result, expect));
}

void test_matrix_product() {
  // arrange
  unsigned m1[3][2] = {{1, 2}, {8, 6}, {3, 5}};
  unsigned m2[2][3] = {{1, 2, 4}, {2, 3, 6}};
  size_t sm1[] = {
      [0] = sizeof m1[0] / sizeof m1[0][0], [1] = sizeof m1 / sizeof m1[0]};
  size_t sm2[] = {
      [0] = sizeof m2[0] / sizeof m2[0][0], [1] = sizeof m2 / sizeof m2[0]};
  // act
  unsigned result[sm1[0]][sm2[1]];
  matrix_product(sm1, m1, sm2, m2, result);
  // assert
  unsigned expect[2][2] = {{29, 34}, {44, 52}};
  size_t len[] = {2, 2};
  assert(mequals(len, result, expect));
}
