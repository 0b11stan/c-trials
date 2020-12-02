#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void display(int length, char* words[]) {
    for (int i = 0; i < length; i++) {
        printf("%s", words[i]);
        if (i == length - 1)
            printf("\n");
        else
            printf(" ");
    }
}

void merge(int length, char* words[], int len_left, char* left[], int len_right, char* right[]) {
    int mi = 0;
    int li = 0;
    int ri = 0;
    while (mi < length) {
        if (ri == len_right) {
            words[mi] = left[li];
            li++;
        } else if (li == len_left) {
            words[mi] = right[ri];
            ri++;
        } else if (strlen(right[ri]) > strlen(left[li])) {
            words[mi] = left[li];
            li++;
        } else {
            words[mi] = right[ri];
            ri++;
        }
        mi++;
    }
}

void split(int length, char* words[], char* left[], char* right[]) {
    int left_min = 0;
    int left_max = length / 2 - 1;
    int right_min = left_max + 1;
    int right_max = length - 1;

    for (int i = left_min; i <= left_max; i++) left[i] = words[i];

    for (int i = right_min; i <= right_max; i++)
        right[i - right_min] = words[i];
}

void sort(int length, char* words[]) {
    if (length < 2) return;

    int len_left = length / 2;
    int len_right = length - length / 2;
    char* left[len_left];
    char* right[len_right];

    split(length, words, left, right);

    sort(len_left, left);
    sort(len_right, right);

    merge(length, words, len_left, left, len_right, right);
}

int main(int argc, char* argv[]) {
    // remove executable name from arguments list
    int length = argc - 1;
    char* words[length];
    for (int i = 1; i < argc; i++) words[i - 1] = argv[i];

    sort(length, words);

    display(length, words);

    return EXIT_SUCCESS;
}
