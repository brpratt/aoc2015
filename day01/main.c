#include <stdio.h>
#include <stdlib.h>

#include "day01.h"

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("usage: day01 <input>\n");
        return -1;
    }

    FILE *fp = fopen(argv[1], "r");
    if (fp == NULL) {
        printf("usage: day01 <input>\n");
    }

    fseek(fp, 0, SEEK_END);
    long length = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    char *input = malloc(length);
    fread(input, 1, length, fp);
    fclose(fp);

    printf("%d\n", solve_part_1(input, length));
    printf("%d\n", solve_part_2(input, length));

    free(input);
}
