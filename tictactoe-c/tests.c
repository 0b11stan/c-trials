#include <stdio.h>

#include "core/test.h"
#include "ihm/test.h"
#include "minunit.h"

int tests_run = 0;

int main(int argc, char **argv) {
    char result = 0;

    result += core_tests();
    result += ihm_tests();

    printf("Tests run: %d\n", tests_run);

    return result != 0;
}

