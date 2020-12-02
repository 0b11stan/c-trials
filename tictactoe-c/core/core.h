#ifndef TICTACTOE_CORE
#define TICTACTOE_CORE

#define Player core_player
#define won core_won
#define init core_init

typedef struct Player {
    char *name;
    char symbol;
} Player;

typedef struct Game {
    Player x;
    Player o;
    Player *current;
    char grid[3][3];
} Game;

char is_over(const char grid[3][3]);
char won(const Player *player, const char grid[3][3]);
void init(Game *game);
char step(Game *game, const int coordinates[2]);

#endif  // TICTACTOE_CORE
