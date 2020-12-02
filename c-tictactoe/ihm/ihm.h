#ifndef TICTACTOE_IHM
#define TICTACTOE_IHM

#define read ihm_read
#define readi ihm_readi
#define print_turn ihm_print_turn
#define print_victory ihm_print_victory

#include "../core/core.h"

void read(const char* message, char* input);
void readi(const char* message, int* input);
void print_turn(const Game* game);
void print_victory(const Game* game);
void print_equality(const Game* game);

#endif  // TICTACTOE_IHM
