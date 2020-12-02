#include <stdio.h>

#define BUFFER_SIZE 5
#define FALSE 0
#define TRUE 1

struct circular_buffer {
    int buffer[BUFFER_SIZE];
    int r_index;
    int w_index;
    int is_empty;
};

typedef struct circular_buffer cbuff;

void move_forward(int* index) { *index = (*index + 1) % BUFFER_SIZE; }

void w_buffer(cbuff* buff, int value) {
    buff->buffer[buff->w_index] = value;
    if (buff->r_index == buff->w_index && !buff->is_empty)
        move_forward(&buff->r_index);
    move_forward(&buff->w_index);
    buff->is_empty = FALSE;
}

int* r_buffer(cbuff* buff) {
    int* tmp = NULL;
    if (buff->is_empty == FALSE) {
        tmp = &buff->buffer[buff->r_index];
        move_forward(&buff->r_index);
    }
    if (buff->r_index == buff->w_index) buff->is_empty = TRUE;
    return tmp;
}

void print_r_buffer(int* value) {
    if (value != NULL) printf("%i\n", *value);
}

void display_buffer(cbuff* buff) {
    int i;
    printf("### BUFFER ###\n");
    for (i = 0; i < BUFFER_SIZE; i++) printf("%i ", buff->buffer[i]);
    printf("\n");
    printf("read index: %i\n", buff->r_index);
    printf("write index: %i\n", buff->w_index);
    printf("is empty: %i\n", buff->is_empty);
    printf("##############\n");
}

int main() {
    cbuff buff = {.r_index = 0, .w_index = 0, .is_empty = 1};
    w_buffer(&buff, 1);
    w_buffer(&buff, 2);
    w_buffer(&buff, 3);
    print_r_buffer(r_buffer(&buff));
    print_r_buffer(r_buffer(&buff));
    return 0;
}
