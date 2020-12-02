#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]) {
    int len_word = 0;

    for (int i = 1; i < argc; i++) {
        if (strlen(argv[i]) < len_word) return EXIT_FAILURE;
        len_word = strlen(argv[i]);
    }

    return EXIT_SUCCESS;
}
