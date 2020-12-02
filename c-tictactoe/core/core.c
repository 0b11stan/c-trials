#include <stdlib.h>

#include "core.h"

static char is_winning(const Player *player, const char set[3]) {
    for (int x = 0; x < 3; x++)
        if (set[x] != player->symbol) return 0;
    return 1;
}

char is_over(const char grid[3][3]) {
    for (int y = 0; y < 3; y++)
        for (int x = 0; x < 3; x++)
            if (grid[y][x] == ' ') return 0;
    return 1;
}

char won(const Player *player, const char grid[3][3]) {
    char result = 0;
    for (int x = 0; x < 3; x++) {
        char col[3] = {grid[0][x], grid[1][x], grid[2][x]};
        result += is_winning(player, col);
        result += is_winning(player, grid[x]);
    }
    char diag1[3] = {grid[0][0], grid[1][1], grid[2][2]};
    result += is_winning(player, diag1);
    char diag2[3] = {grid[0][2], grid[1][1], grid[2][0]};
    result += is_winning(player, diag2);
    return result;
}

void init(Game *game) {
    for (int x = 0; x < 3; x++) {
        for (int y = 0; y < 3; y++) {
            game->grid[x][y] = ' ';
        }
    }
    game->x.name = malloc(sizeof(char));
    game->x.symbol = 'X';
    game->o.name = malloc(sizeof(char));
    game->o.symbol = 'O';
    game->current = &game->x;
}

char step(Game *game, const int coordinates[2]) {
    game->grid[coordinates[1] - 1][coordinates[0] - 1] = game->current->symbol;
    if (won(game->current, game->grid) || is_over(game->grid))
        return 0;
    else {
        if (game->current == &game->x)
            game->current = &game->o;
        else
            game->current = &game->x;
    }
    return 1;
}
