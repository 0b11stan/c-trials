#include "test.h"
#include <stdio.h>
#include "../minunit.h"
#include "core.h"

static char *init_fill_the_game_grid_with_spaces() {
    printf("init_fill_the_game_grid_with_spaces\n");
    Game game;
    init(&game);
    mu_assert("- error, grid is not filled with 3x3 spaces.",
              sizeof(game.grid) == 9 && game.grid[0][0] == ' ');
    return 0;
}

static char *init_fill_the_game_players_symbols() {
    printf("init_fill_the_game_players_symbols\n");
    Game game;
    init(&game);
    mu_assert("- error, game's players symbol are wrong.",
              game.x.symbol == 'X' && game.o.symbol == 'O');
    return 0;
}

static char *init_fill_the_game_current_player() {
    printf("init_fill_the_game_current_player\n");
    Game game;
    init(&game);
    mu_assert("- error, game's current player is unset.",
              game.current == &game.x);
    return 0;
}

static char *step_switch_players() {
    printf("step_switch_players\n");
    Game game;
    init(&game);
    game.x.name = "testx";
    game.o.name = "testo";
    int coo[2] = {1, 1};
    step(&game, coo);
    mu_assert("- error, current player is not changing.",
              game.current == &game.o);
    return 0;
}

static char *won_return_true_when_player_win_vertically() {
    printf("won_return_true_when_player_win_vertically\n");

    char v0[3][3] = {{'X', ' ', ' '}, {'X', ' ', ' '}, {'X', ' ', ' '}};
    char v1[3][3] = {{' ', 'X', ' '}, {' ', 'X', ' '}, {' ', 'X', ' '}};
    char v2[3][3] = {{' ', ' ', 'X'}, {' ', ' ', 'X'}, {' ', ' ', 'X'}};
    Game game;
    init(&game);

    mu_assert("- error, v0 not winning.", won(&game.x, v0));
    mu_assert("- error, v1 not winning.", won(&game.x, v1));
    mu_assert("- error, v2 not winning.", won(&game.x, v2));

    return 0;
}

static char *won_return_true_when_player_win_horizontally() {
    printf("won_return_true_when_player_win_horizontally\n");

    char v0[3][3] = {{'O', 'O', 'O'}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    char v1[3][3] = {{' ', ' ', ' '}, {'O', 'O', 'O'}, {' ', ' ', ' '}};
    char v2[3][3] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {'O', 'O', 'O'}};
    Game game;
    init(&game);

    mu_assert("- error, v0 not winning.", won(&game.o, v0));
    mu_assert("- error, v1 not winning.", won(&game.o, v1));
    mu_assert("- error, v2 not winning.", won(&game.o, v2));

    return 0;
}

static char *won_return_true_when_player_win_diagonally() {
    printf("won_return_true_when_player_win_diagonally\n");

    char v0[3][3] = {{'X', ' ', ' '}, {' ', 'X', ' '}, {' ', ' ', 'X'}};
    char v1[3][3] = {{' ', ' ', 'X'}, {' ', 'X', ' '}, {'X', ' ', ' '}};
    Game game;
    init(&game);

    mu_assert("- error, v0 not winning.", won(&game.x, v0));
    mu_assert("- error, v1 not winning.", won(&game.x, v1));

    return 0;
}

static char *won_return_false_when_wrong_win_vertically() {
    printf("won_return_false_when_wrong_win_vertically\n");

    char v0[3][3] = {{'X', 'O', ' '}, {'X', ' ', ' '}, {'X', ' ', 'O'}};
    Game game;
    init(&game);

    mu_assert("- error, o player should not win.", !won(&game.o, v0));

    return 0;
}

static char *is_over_return_true_when_grid_is_full() {
    printf("is_over_return_true_when_grid_is_full\n");
    char grid[3][3] = {{'X', 'O', 'X'}, {'O', 'X', 'X'}, {'X', 'O', 'O'}};
    mu_assert("- error, is_over do not detecte a full grid.\n", is_over(grid));
    return 0;
}

static char *all_tests() {
    mu_run_test(init_fill_the_game_grid_with_spaces);
    mu_run_test(init_fill_the_game_players_symbols);
    mu_run_test(init_fill_the_game_current_player);
    mu_run_test(step_switch_players);
    mu_run_test(won_return_true_when_player_win_vertically);
    mu_run_test(won_return_false_when_wrong_win_vertically);
    mu_run_test(won_return_true_when_player_win_horizontally);
    mu_run_test(won_return_true_when_player_win_diagonally);
    mu_run_test(is_over_return_true_when_grid_is_full);
    return 0;
}

int core_tests() {
    printf("\n# CORE TESTS #\n");

    char *result = all_tests();
    if (result != 0) {
        printf("%s\n", result);
    } else {
        printf("CORE TESTS PASSED\n\n");
    }

    return result != 0;
}
