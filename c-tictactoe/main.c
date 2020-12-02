#include <stdlib.h>

#include "core/core.h"
#include "ihm/ihm.h"

int main() {
    Game game;
    init(&game);

    int coordinates[2] = {0, 0};

    read("X : ", game.x.name);
    read("O : ", game.o.name);

    do {
        print_turn(&game);
        readi("COL : ", &coordinates[0]);
        readi("ROW : ", &coordinates[1]);
    } while (step(&game, coordinates));

    if (won(game.current, game.grid)) print_victory(&game);
    else print_equality(&game);

    free(game.x.name);
    free(game.o.name);
    return 0;
}
