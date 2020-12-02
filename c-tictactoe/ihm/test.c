#include <stdio.h>
#include "../minunit.h"

static char *all_tests() { return 0; }

int ihm_tests() {
    printf("\n# IHM TESTS #\n");

    char *result = all_tests();
    if (result != 0) {
        printf("%s\n", result);
    } else {
        printf("IHM TESTS PASSED\n\n");
    }

    return result != 0;
}
