#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "ihm.h"

static void print_grid(const char grid[3][3]) {
    char ASCII_ONE = 49;
    printf("   1   2   3  \n");
    for (unsigned char x = 0; x < 3; x++)
        printf("%c  %c | %c | %c |\n", ASCII_ONE + x, grid[x][0], grid[x][1],
               grid[x][2]);
}

void print_turn(const Game* game) {
    printf("Your turn %s\n", game->current->name);
    print_grid(game->grid);
}

void print_victory(const Game* game) {
    printf("BRAVO %s, you won !\n", game->current->name);
    print_grid(game->grid);
}

void print_equality(const Game* game) {
    printf("ARGH, this is an equality !\n");
    print_grid(game->grid);
}

void read(const char* message, char* input) {
    printf("%s", message);
    char current_char = 0;
    do {
        strncat(input, &current_char, sizeof(char));
        current_char = getchar();
    } while (current_char != 10);
}

void readi(const char* message, int* input) {
    char* tmp_input = malloc(sizeof(char));
    read(message, tmp_input);
    *input = atoi(tmp_input);
    free(tmp_input);
}
